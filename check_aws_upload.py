# check_aws_upload.py - Check what was actually uploaded to AWS
import os
import boto3
from datetime import datetime, timezone

def check_aws_static_files():
    # AWS credentials
    os.environ["AWS_ACCESS_KEY_ID"] = "AKIAUY6KWBGGFOWPKFIM"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "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"
    
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        region_name='eu-north-1'
    )
    
    bucket_name = 'dive-goblin'
    
    # Get all static files
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='static/')
    
    if 'Contents' not in response:
        print("❌ No static files found in AWS!")
        return
    
    # Filter for custom files (not admin)
    custom_files = []
    recent_files = []
    now = datetime.now(timezone.utc)
    
    for obj in response['Contents']:
        key = obj['Key']
        modified = obj['LastModified']
        
        # Check if it's a custom file (not admin)
        if not '/admin/' in key and (key.endswith('.css') or key.endswith('.js')):
            custom_files.append((key, modified))
        
        # Check if it's recently modified (within last hour)
        time_diff = now - modified
        if time_diff.total_seconds() < 3600:  # 1 hour
            recent_files.append((key, modified))
    
    print(f"📄 Custom CSS/JS files in AWS S3:")
    if custom_files:
        for key, modified in sorted(custom_files):
            print(f"   {key} - Modified: {modified}")
    else:
        print("   ❌ No custom CSS/JS files found!")
    
    print(f"\n🕐 Recently uploaded files (last hour):")
    if recent_files:
        for key, modified in sorted(recent_files, key=lambda x: x[1], reverse=True)[:10]:
            print(f"   {key} - Modified: {modified}")
    else:
        print("   ❌ No files uploaded in the last hour!")
    
    # Look specifically for your main CSS files
    main_css_files = [
        'static/css/base.css',
        'static/css/main.css',
        'static/js/main.js'
    ]
    
    print(f"\n🎯 Looking for main CSS/JS files:")
    for file_key in main_css_files:
        found = False
        for obj in response['Contents']:
            if obj['Key'] == file_key:
                print(f"   ✅ {file_key} - Modified: {obj['LastModified']}")
                found = True
                break
        if not found:
            print(f"   ❌ {file_key} - NOT FOUND")

if __name__ == "__main__":
    print("🔍 Checking AWS S3 static files...")
    check_aws_static_files()