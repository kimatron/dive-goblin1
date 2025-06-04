import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import mimetypes
from pathlib import Path

# Import your environment variables from env.py
try:
    import env  # This loads your env.py file
    print("✅ Loaded env.py")
except ImportError:
    print("❌ Could not import env.py")

def force_upload_static():
    """Force upload all static files to S3"""
    try:
        # Get credentials from environment
        access_key = os.environ.get('AWS_ACCESS_KEY_ID')
        secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')
        
        print(f"Credentials check:")
        print(f"AWS_ACCESS_KEY_ID: {'✅' if access_key else '❌'}")
        print(f"AWS_SECRET_ACCESS_KEY: {'✅' if secret_key else '❌'}")
        print(f"AWS_STORAGE_BUCKET_NAME: {'✅' if bucket_name else '❌'}")
        
        if not all([access_key, secret_key, bucket_name]):
            return
        
        # Create S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        
        # Static files directory
        static_root = Path('staticfiles')
        
        if not static_root.exists():
            print("Running collectstatic first...")
            os.system('python manage.py collectstatic --noinput')
        
        print(f"Force uploading static files to {bucket_name}...")
        
        uploaded_count = 0
        
        # Walk through all static files
        for file_path in static_root.rglob('*'):
            if file_path.is_file():
                relative_path = file_path.relative_to(static_root)
                s3_key = f"static/{relative_path.as_posix()}"
                
                content_type, _ = mimetypes.guess_type(str(file_path))
                if content_type is None:
                    content_type = 'binary/octet-stream'
                
                try:
                    s3_client.upload_file(
                        str(file_path),
                        bucket_name,
                        s3_key,
                        ExtraArgs={
                            'ContentType': content_type,
                            'ACL': 'public-read'
                        }
                    )
                    uploaded_count += 1
                    print(f"✅ Uploaded: {s3_key}")
                    
                except ClientError as e:
                    print(f"❌ Failed to upload {s3_key}: {e}")
        
        print(f"\n🎉 Force upload complete! {uploaded_count} files uploaded.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    force_upload_static()