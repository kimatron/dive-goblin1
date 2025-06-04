# test_aws.py - Run this to test your AWS connection
import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Set your AWS credentials (same as in your env.py)
os.environ["AWS_ACCESS_KEY_ID"] = "AKIAUY6KWBGGFOWPKFIM"
os.environ["AWS_SECRET_ACCESS_KEY"] = "sYSsQllIFWRrHhbztNhvjyrhmCo6tq1y3l/VeZKD"

def test_aws_connection():
    try:
        # Create S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name='eu-north-1'
        )
        
        # Test bucket access
        bucket_name = 'dive-goblin'
        print(f"Testing access to bucket: {bucket_name}")
        
        # List bucket contents
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        print("✅ AWS credentials are working!")
        print(f"Bucket contains {response.get('KeyCount', 0)} objects")
        
        # Check if we can write to the bucket
        test_key = 'test-write-permission.txt'
        s3_client.put_object(
            Bucket=bucket_name,
            Key=test_key,
            Body=b'Test file to check write permissions',
            ContentType='text/plain'
        )
        print("✅ Write permissions are working!")
        
        # Clean up test file
        s3_client.delete_object(Bucket=bucket_name, Key=test_key)
        print("✅ Delete permissions are working!")
        
        # List static folder contents
        print("\n📁 Current static folder contents:")
        static_objects = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='static/')
        if 'Contents' in static_objects:
            for obj in static_objects['Contents'][:10]:  # Show first 10 files
                print(f"   {obj['Key']} - Modified: {obj['LastModified']}")
        else:
            print("   No files found in static/ folder")
            
        return True
        
    except NoCredentialsError:
        print("❌ AWS credentials not found or invalid")
        return False
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'AccessDenied':
            print("❌ Access denied - check your AWS permissions")
        elif error_code == 'NoSuchBucket':
            print("❌ Bucket 'dive-goblin' does not exist")
        else:
            print(f"❌ AWS Error: {error_code} - {e.response['Error']['Message']}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🔍 Testing AWS S3 connection...")
    test_aws_connection()