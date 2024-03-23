#   Using "multiprocessing"
#   when using bash in the previous problem, 
#   it takes about 8 to 10 seconds per file.
import os
import subprocess
import multiprocessing

def process_file(file):    
    # Execute label.py with reports_path argument
    try:
        subprocess.run(["python", "label.py", "--reports_path", file + ".csv"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing label.py for file {file}: {e}")

def process_files(files):
    with multiprocessing.Pool() as pool:
        pool.map(process_file, files)

if __name__ == "__main__":
    # Read file names from ".txt"
    with open("both_impression_list.txt", "r") as f:
        file_names = f.read().splitlines()

    # Find corresponding files in the directory
    files = [os.path.join("both_impression", file) for file in file_names]

    # Process the files in parallel
    process_files(files)