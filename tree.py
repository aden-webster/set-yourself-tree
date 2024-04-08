import subprocess
import datetime

def run_tree_command():

    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y_%m_%d")

### DOn't forget to change these back to correct filename
    for i in range(3):
        for j in ['Movies', 'TV', 'Docs']:
                # Create a filename using the timestamp
                filename = f"/mnt/disks/dlcache/{j}_TREE_{timestamp}.txt"
                with open(filename, 'w') as file:
                    subprocess.run(['tree', ''], stdout=file) 

#def run_tree_command():
#    # Run the tree command and store the output in text file files for each dir
#    with open('{i}_tree_{timestamp}.txt', 'w') as file:
#        subprocess.run(['tree', '/'], stdout=file)

def main():
    run_tree_command()

if __name__ == "__main__":
    main()