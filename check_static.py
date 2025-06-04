# check_static.py - Check what static files we have locally
import os
from pathlib import Path
from datetime import datetime

def check_local_static():
    print("🔍 Checking local static files...")
    
    # Check main static directory
    static_dir = Path('static')
    if not static_dir.exists():
        print("❌ No 'static' directory found!")
        return
    
    print(f"📁 Static directory exists: {static_dir.absolute()}")
    
    # Look for your custom CSS/JS files
    custom_files = []
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            if file.endswith(('.css', '.js')):
                file_path = Path(root) / file
                stat = file_path.stat()
                modified_time = datetime.fromtimestamp(stat.st_mtime)
                custom_files.append((file_path, modified_time))
    
    if custom_files:
        print(f"\n📄 Found {len(custom_files)} CSS/JS files:")
        for file_path, modified_time in sorted(custom_files):
            print(f"   {file_path} - Modified: {modified_time}")
    else:
        print("❌ No CSS/JS files found in static directory!")
    
    # Check staticfiles directory (collected files)
    staticfiles_dir = Path('staticfiles')
    if staticfiles_dir.exists():
        print(f"\n📁 Staticfiles directory exists: {staticfiles_dir.absolute()}")
        
        collected_files = []
        for root, dirs, files in os.walk(staticfiles_dir):
            for file in files:
                if file.endswith(('.css', '.js')) and not file.startswith('admin'):
                    file_path = Path(root) / file
                    stat = file_path.stat()
                    modified_time = datetime.fromtimestamp(stat.st_mtime)
                    collected_files.append((file_path, modified_time))
        
        if collected_files:
            print(f"📄 Found {len(collected_files)} custom CSS/JS files in staticfiles:")
            for file_path, modified_time in sorted(collected_files):
                print(f"   {file_path} - Modified: {modified_time}")
        else:
            print("❌ No custom CSS/JS files found in staticfiles directory!")
    else:
        print("❌ No 'staticfiles' directory found!")

if __name__ == "__main__":
    check_local_static()