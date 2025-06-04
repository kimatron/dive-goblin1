# compare_local_aws.py - Compare local files with AWS files
import os
import boto3
from pathlib import Path
from datetime import datetime

def compare_files():
    print("🔍 Comparing local static files with AWS...")
    
    # Check local static files
    static_dir = Path('static')
    local_files = {}
    
    if static_dir.exists():
        print(f"📁 Local static directory: {static_dir.absolute()}")
        for file_path in static_dir.rglob('*'):
            if file_path.is_file() and (file_path.suffix in ['.css', '.js']):
                relative_path = file_path.relative_to(Path('.'))
                key = str(relative_path).replace('\\', '/')
                
                stat = file_path.stat()
                modified_time = datetime.fromtimestamp(stat.st_mtime)
                local_files[key] = {
                    'path': file_path,
                    'modified': modified_time,
                    'size': stat.st_size
                }
        
        print(f"📄 Found {len(local_files)} local CSS/JS files:")
        for key, info in sorted(local_files.items()):
            print(f"   {key} - Modified: {info['modified']} - Size: {info['size']} bytes")
    else:
        print("❌ No local static directory found!")
        return
    
    # Get AWS files
    print(f"\n☁️ Getting AWS files...")
    os.environ["AWS_ACCESS_KEY_ID"] = "AKIAUY6KWBGGFOWPKFIM"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "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"
    
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        region_name='eu-north-1'
    )
    
    bucket_name = 'dive-goblin'
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='static/')
    
    aws_files = {}
    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            if key.endswith('.css') or key.endswith('.js'):
                if '/admin/' not in key:  # Only custom files
                    aws_files[key] = {
                        'modified': obj['LastModified'].replace(tzinfo=None),
                        'size': obj['Size']
                    }
    
    print(f"📄 Found {len(aws_files)} AWS CSS/JS files")
    
    # Compare files
    print(f"\n🔍 Comparison Results:")
    
    # Files that need updating (local is newer)
    needs_update = []
    # Files only in local
    only_local = []
    # Files only in AWS
    only_aws = []
    
    for local_key, local_info in local_files.items():
        if local_key in aws_files:
            aws_info = aws_files[local_key]
            # Compare modification times
            if local_info['modified'] > aws_info['modified']:
                needs_update.append((local_key, local_info, aws_info))
        else:
            only_local.append((local_key, local_info))
    
    for aws_key in aws_files:
        if aws_key not in local_files:
            only_aws.append(aws_key)
    
    if needs_update:
        print(f"\n🔄 Files that need updating ({len(needs_update)}):")
        for key, local_info, aws_info in needs_update:
            print(f"   {key}")
            print(f"     Local:  {local_info['modified']} ({local_info['size']} bytes)")
            print(f"     AWS:    {aws_info['modified']} ({aws_info['size']} bytes)")
    
    if only_local:
        print(f"\n📤 Files only in local ({len(only_local)}):")
        for key, local_info in only_local:
            print(f"   {key} - {local_info['modified']}")
    
    if only_aws:
        print(f"\n☁️ Files only in AWS ({len(only_aws)}):")
        for key in only_aws:
            print(f"   {key}")
    
    if not needs_update and not only_local:
        print(f"\n✅ All files are up to date!")
    else:
        total_to_update = len(needs_update) + len(only_local)
        print(f"\n📊 Summary: {total_to_update} files need to be uploaded to AWS")

if __name__ == "__main__":
    compare_files()