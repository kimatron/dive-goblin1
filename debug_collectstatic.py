# debug_collectstatic.py - Debug why collectstatic isn't uploading to AWS
import os
import django
from pathlib import Path

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'divegob.settings')
os.environ["USE_AWS"] = "True"  # Make sure this is set

# Add current directory to Python path
import sys
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    django.setup()
    from django.conf import settings
    from django.core.management import call_command
    from django.contrib.staticfiles.storage import staticfiles_storage
    
    print("🔍 Debugging Django collectstatic process...")
    print()
    
    # Check what storage backend is being used
    print("📦 Storage Backend Analysis:")
    print(f"   Storage class: {staticfiles_storage.__class__}")
    print(f"   Storage module: {staticfiles_storage.__class__.__module__}")
    print(f"   Storage string: {settings.STATICFILES_STORAGE}")
    print()
    
    # Check if it's the right AWS storage
    expected_storage = 'custom_storages.StaticStorage'
    actual_storage = settings.STATICFILES_STORAGE
    
    if actual_storage == expected_storage:
        print("✅ Correct AWS storage configured")
    else:
        print(f"❌ Wrong storage! Expected: {expected_storage}, Got: {actual_storage}")
    
    # Check storage attributes
    print("🔧 Storage Attributes:")
    storage_attrs = [
        'bucket_name', 'location', 'custom_domain', 
        'access_key', 'secret_key', 'region_name'
    ]
    
    for attr in storage_attrs:
        if hasattr(staticfiles_storage, attr):
            value = getattr(staticfiles_storage, attr)
            if 'key' in attr.lower() and value:
                value = f"{value[:8]}...{value[-4:]}" if len(str(value)) > 12 else "***"
            print(f"   {attr}: {value}")
        else:
            print(f"   {attr}: Not found")
    
    # Check AWS connection from storage
    print()
    print("🌐 Testing Storage Connection:")
    try:
        # Try to get the bucket
        if hasattr(staticfiles_storage, 'bucket'):
            bucket = staticfiles_storage.bucket
            print(f"   ✅ Bucket accessible: {bucket.name}")
        elif hasattr(staticfiles_storage, 'bucket_name'):
            print(f"   📦 Bucket name: {staticfiles_storage.bucket_name}")
        
        # Try a simple operation
        test_key = 'test-collectstatic-debug.txt'
        test_content = 'Test from collectstatic debug'
        
        # Save a test file
        saved_name = staticfiles_storage.save(test_key, 
            type('MockFile', (), {
                'read': lambda: test_content.encode(),
                'chunks': lambda: [test_content.encode()],
                'size': len(test_content)
            })()
        )
        print(f"   ✅ Test file saved: {saved_name}")
        
        # Clean up
        if staticfiles_storage.exists(saved_name):
            staticfiles_storage.delete(saved_name)
            print(f"   ✅ Test file deleted")
            
    except Exception as e:
        print(f"   ❌ Storage test failed: {str(e)}")
    
    # Check environment variables during Django startup
    print()
    print("🌍 Environment Check During Django:")
    env_vars = ['USE_AWS', 'DEVELOPMENT', 'DEBUG']
    for var in env_vars:
        value = os.environ.get(var, 'Not set')
        django_debug = getattr(settings, 'DEBUG', 'Not set')
        print(f"   {var}: {value}")
    
    print(f"   Django DEBUG: {django_debug}")
    
    # Check if the issue is in settings logic
    print()
    print("🔧 Settings Logic Check:")
    use_aws_in_env = 'USE_AWS' in os.environ
    development_in_env = 'DEVELOPMENT' in os.environ
    
    print(f"   USE_AWS in environment: {use_aws_in_env}")
    print(f"   DEVELOPMENT in environment: {development_in_env}")
    print(f"   Should use AWS: {use_aws_in_env}")
    
    if use_aws_in_env and development_in_env:
        print("   ⚠️  Both USE_AWS and DEVELOPMENT are set!")
        print("   This might cause conflicts in your settings.py")
    
    # Test file operations
    print()
    print("📁 Testing File Operations:")
    static_dir = Path(settings.STATICFILES_DIRS[0]) if settings.STATICFILES_DIRS else None
    if static_dir and static_dir.exists():
        css_files = list(static_dir.glob('**/*.css'))
        js_files = list(static_dir.glob('**/*.js'))
        print(f"   CSS files found: {len(css_files)}")
        print(f"   JS files found: {len(js_files)}")
        
        if css_files:
            test_css = css_files[0]
            relative_path = test_css.relative_to(static_dir)
            print(f"   Test CSS: {relative_path}")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()