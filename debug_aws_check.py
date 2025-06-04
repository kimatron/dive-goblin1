# debug_aws_check.py - Debug version with more output
import os
import boto3
from datetime import datetime, timezone

def debug_aws_check():
    print("🔍 Starting AWS debug check...")
    
    # Set AWS credentials
    os.environ["AWS_ACCESS_KEY_ID"] = "AKIAUY6KWBGGFOWPKFI"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "sYSsQllIFWRrHhbztNhvjyrhmCo6tq1y3l/VeZKD"
    
    print("🔑 AWS credentials set")
    
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name='eu-north-1'
        )
        print("📡 S3 client created")
        
        bucket_name = 'dive-goblin'
        print(f"🪣 Checking bucket: {bucket_name}")
        
        # Get all static files
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='static/')
        print(f"📊 API response received")
        
        if 'Contents' not in response:
            print("❌ No static files found in AWS!")
            return
        
        total_files = len(response['Contents'])
        print(f"📁 Found {total_files} files in static/ folder")
        
        # Show first 10 files to verify we're getting data
        print("\n📄 First 10 static files:")
        for i, obj in enumerate(response['Contents'][:10]):
            print(f"   {i+1}. {obj['Key']} - {obj['LastModified']}")
        
        # Look for custom files (not admin)
        custom_files = []
        all_css_js = []
        
        for obj in response['Contents']:
            key = obj['Key']
            modified = obj['LastModified']
            
            # Collect all CSS/JS files
            if key.endswith('.css') or key.endswith('.js'):
                all_css_js.append((key, modified))
                
                # Check if it's a custom file (not admin)
                if '/admin/' not in key:
                    custom_files.append((key, modified))
        
        print(f"\n📊 File analysis:")
        print(f"   Total CSS/JS files: {len(all_css_js)}")
        print(f"   Custom CSS/JS files: {len(custom_files)}")
        
        if custom_files:
            print(f"\n🎯 Custom CSS/JS files found:")
            for key, modified in sorted(custom_files):
                print(f"   {key} - Modified: {modified}")
        else:
            print(f"\n❌ No custom CSS/JS files found!")
            print(f"🔍 All CSS/JS files (first 10):")
            for key, modified in sorted(all_css_js)[:10]:
                print(f"   {key} - Modified: {modified}")
        
        # Check for recent uploads (last 24 hours)
        now = datetime.now(timezone.utc)
        recent_files = []
        
        for obj in response['Contents']:
            time_diff = now - obj['LastModified']
            if time_diff.total_seconds() < 86400:  # 24 hours
                recent_files.append((obj['Key'], obj['LastModified']))
        
        print(f"\n🕐 Files uploaded in last 24 hours: {len(recent_files)}")
        if recent_files:
            for key, modified in sorted(recent_files, key=lambda x: x[1], reverse=True)[:10]:
                print(f"   {key} - Modified: {modified}")
        
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_aws_check()