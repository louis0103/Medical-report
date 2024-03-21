# Original report files copy to .txt 
import os
import shutil

# search for source folder
source_folder = './p18'

# save to destination folder
destination_folder = 'collection'

# Check for "destination_folder"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# search for ALL in "source_folder" folder
for folder_name in os.listdir(source_folder):
    folder_path = os.path.join(source_folder, folder_name)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            # If find .txt, copy to "destination_folder"
            if file_name.endswith('.txt'):
                source_file_path = os.path.join(folder_path, file_name)
                destination_file_path = os.path.join(destination_folder, file_name)
                shutil.copy(source_file_path, destination_file_path)

print("File copy complete in {}.".format(destination_folder))

