import subprocess
import datetime
import os

def run_tree_command():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y_%m_%d")

    # Get the mountpoints from environment variables
    # You are welcome to change the names, they are just labels.
    movies_mountpoint = os.getenv('MOUNT_MOVIES', '/mnt/user/Movies')
    tv_mountpoint = os.getenv('MOUNT_TV', '/mnt/user/TV')
    docs_mountpoint = os.getenv('MOUNT_DOCS', '/mnt/user/Docs')

    mountpoints = {
        'Movies': movies_mountpoint,
        'TV': tv_mountpoint,
        'Docs': docs_mountpoint
    }

    for i in range(3):
        for category, mountpoint in mountpoints.items():
                # Create a filename using the timestamp
                filename = f"{mountpoint}_TREE_{timestamp}.txt"
                with open(filename, 'w') as file:
                    subprocess.run(['tree', mountpoint], stdout=file) 

def main():
    run_tree_command()

if __name__ == "__main__":
    main()