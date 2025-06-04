# force_upload_static.py - Manually upload static files to AWS
import os
import boto3
from pathlib import Path
import mimetypes

def force_upload_static():
    print("🚀 Force uploading static files to AWS S3...")
    
    # AWS credentials
    os.environ["AWS_ACCESS_KEY_ID"] = "AKIAUY6KWBGGFOWPKFIM"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "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"
    
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name='eu-north-1'
        )
        
        bucket_name = 'dive-goblin'
        
        # Find all static files to upload
        static_dir = Path('static')
        if not static_dir.exists():
            print("❌ Static directory not found!")
            return
        
        print(f"📁 Scanning {static_dir.absolute()}")
        uploaded_files = []
        failed_files = []
        
        for file_path in static_dir.rglob('*'):
            if file_path.is_file():
                # Calculate relative path for S3 key
                relative_path = file_path.relative_to(Path('.'))
                s3_key = str(relative_path).replace('\\', '/')  # Windows path fix
                
                # Get content type
                content_type, _ = mimetypes.guess_type(str(file_path))
                if content_type is None:
                    if file_path.suffix == '.css':
                        content_type = 'text/css'
                    elif file_path.suffix == '.js':
                        content_type = 'application/javascript'
                    else:
                        content_type = 'binary/octet-stream'
                
                try:
                    # Upload file
                    print(f"📤 Uploading: {s3_key}")
                    with open(file_path, 'rb') as file_data:
                        s3_client.put_object(
                            Bucket=bucket_name,
                            Key=s3_key,
                            Body=file_data,
                            ContentType=content_type,
                            CacheControl='max-age=86400',  # 24 hours cache
                            ACL='public-read'  # Make sure files are publicly accessible
                        )
                    uploaded_files.append(s3_key)
                    print(f"   ✅ SUCCESS")
                    
                except Exception as e:
                    print(f"   ❌ FAILED: {str(e)}")
                    failed_files.append((s3_key, str(e)))
        
        print(f"\n🎉 Upload Results:")
        print(f"   ✅ Successfully uploaded: {len(uploaded_files)} files")
        print(f"   ❌ Failed uploads: {len(failed_files)} files")
        
        if uploaded_files:
            print(f"\n📄 Successfully uploaded files:")
            for file_key in uploaded_files:
                print(f"   {file_key}")
        
        if failed_files:
            print(f"\n❌ Failed uploads:")
            for file_key, error in failed_files:
                print(f"   {file_key}: {error}")
        
        # Verify upload of key files
        key_files = ['static/css/base.css', 'static/js/main.js']
        print(f"\n🔍 Verifying key files:")
        for key_file in key_files:
            if key_file in uploaded_files:
                print(f"   ✅ {key_file} - UPLOADED")
            else:
                print(f"   ❌ {key_file} - NOT UPLOADED")
                
    except Exception as e:
        print(f"❌ Critical error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    force_upload_static()