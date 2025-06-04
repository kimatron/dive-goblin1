# check_collectstatic_config.py - Check Django settings for collectstatic
import os
import django
from pathlib import Path

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'divegob.settings')

# Add current directory to Python path
import sys
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    django.setup()
    from django.conf import settings
    
    print("🔍 Checking Django collectstatic configuration...")
    print()
    
    # Check environment variables
    print("🌍 Environment Variables:")
    print(f"   USE_AWS: {os.environ.get('USE_AWS', 'Not set')}")
    print(f"   DEVELOPMENT: {os.environ.get('DEVELOPMENT', 'Not set')}")
    print(f"   DEBUG: {getattr(settings, 'DEBUG', 'Not set')}")
    print()
    
    # Check static files settings
    print("📁 Static Files Settings:")
    print(f"   STATIC_URL: {getattr(settings, 'STATIC_URL', 'Not set')}")
    print(f"   STATIC_ROOT: {getattr(settings, 'STATIC_ROOT', 'Not set')}")
    print(f"   STATICFILES_STORAGE: {getattr(settings, 'STATICFILES_STORAGE', 'Not set')}")
    print()
    
    # Check AWS settings
    print("☁️ AWS Settings:")
    aws_settings = [
        'AWS_STORAGE_BUCKET_NAME',
        'AWS_S3_REGION_NAME', 
        'AWS_ACCESS_KEY_ID',
        'AWS_SECRET_ACCESS_KEY',
        'AWS_S3_CUSTOM_DOMAIN',
        'STATICFILES_LOCATION'
    ]
    
    for setting in aws_settings:
        value = getattr(settings, setting, 'Not set')
        if 'KEY' in setting and value != 'Not set':
            # Hide sensitive keys
            value = f"{value[:8]}...{value[-4:]}" if len(value) > 12 else "***"
        print(f"   {setting}: {value}")
    
    print()
    
    # Check if USE_AWS condition is working
    use_aws = 'USE_AWS' in os.environ
    print(f"🔧 Configuration Analysis:")
    print(f"   USE_AWS in environment: {use_aws}")
    print(f"   Should use AWS: {use_aws}")
    
    if use_aws:
        print("   ✅ AWS should be active")
        if hasattr(settings, 'AWS_STORAGE_BUCKET_NAME'):
            print(f"   ✅ AWS settings loaded")
        else:
            print(f"   ❌ AWS settings NOT loaded!")
    else:
        print("   ❌ AWS not active - using local storage")
    
    # Check staticfiles directories
    print()
    print("📂 Static Files Directories:")
    for static_dir in getattr(settings, 'STATICFILES_DIRS', []):
        static_path = Path(static_dir)
        exists = static_path.exists()
        print(f"   {static_dir}: {'✅ Exists' if exists else '❌ Missing'}")
        
        if exists:
            css_files = list(static_path.rglob('*.css'))
            js_files = list(static_path.rglob('*.js'))
            print(f"     CSS files: {len(css_files)}")
            print(f"     JS files: {len(js_files)}")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()