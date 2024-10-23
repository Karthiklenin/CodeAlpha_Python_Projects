import os
import shutil
import platform
import subprocess

def clean_temp_files():
    temp_dir = '/tmp' if platform.system() != 'Windows' else os.getenv('TEMP')
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        print("Temporary files cleaned.")
        
        
def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {total // (2**30)} GB, Used: {used // (2**30)} GB, Free: {free // (2**30)} GB")
    
def update_system():
    if platform.system() == 'Windows':
        print("System updates are not automated through thius script on Windows. ")
    else:
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "upgrade", "-y"])
        print("System updated successfully.")
        
clean_temp_files()
check_disk_usage()
update_system()
