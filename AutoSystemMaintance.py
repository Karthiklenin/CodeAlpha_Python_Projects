import os
import shutil
import platform
import time
import psutil

# Configuration
temp_dir = '/path/to/temp'  # Replace with the path to the temporary directory
directory_to_clean = '/path/to/old_files'  # Replace with the path of the directory to clean
disk_usage_threshold = 80  # Disk usage threshold in percentage
days_old = 30  # Number of days to consider a file as "old"

def clear_temp_files(temp_dir_path):
    """Clear files in the specified temporary directory."""
    try:
        for filename in os.listdir(temp_dir_path):
            file_path = os.path.join(temp_dir_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
        print(f'Temporary files in {temp_dir_path} cleared successfully.')
    except Exception as e:
        print(f'Failed to access {temp_dir_path}. Reason: {e}')

def monitor_disk_space(threshold):
    """Monitor the disk space and alert if usage exceeds the specified threshold."""
    usage = psutil.disk_usage('/')
    percent_used = usage.percent
    if percent_used > threshold:
        print(f"Warning: Disk usage is at {percent_used}% which is above the {threshold}% threshold!")
    else:
        print(f"Disk usage is at {percent_used}%, within the safe limit.")

def delete_old_files(directory, days):
    """Delete files older than a specified number of days in the given directory."""
    now = time.time()
    cutoff = now - (days * 86400)  # Convert days to seconds

    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_age = os.stat(file_path).st_mtime
                if file_age < cutoff:
                    os.remove(file_path)
                    print(f"Deleted old file: {file_path}")
        print(f"Old files in {directory} deleted successfully.")
    except Exception as e:
        print(f"Failed to access {directory}. Reason: {e}")

def perform_system_maintenance():
    """Main function to perform system maintenance tasks."""
    # Clear temporary files
    clear_temp_files(temp_dir)

    # Monitor disk space
    monitor_disk_space(disk_usage_threshold)

    # Delete old files
    delete_old_files(directory_to_clean, days_old)

    print("System maintenance completed.")

if __name__ == "__main__":
    perform_system_maintenance()
