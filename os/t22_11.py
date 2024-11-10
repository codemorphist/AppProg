import os
import zipfile

def create_multivolume_archive(directory_path, max_size):
    temp_archive_path = "temp_archive.zip"
    with zipfile.ZipFile(temp_archive_path, "w") as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory_path))
    
    part_number = 1
    part_size = max_size
    archive_base_name = os.path.splitext(temp_archive_path)[0]

    with open(temp_archive_path, "rb") as f:
        while True:
            part_data = f.read(part_size)
            if not part_data:
                break
            part_file_name = f"{archive_base_name}_{part_number:04d}.zip"
            with open(part_file_name, "wb") as part_file:
                part_file.write(part_data)
            part_number += 1

    os.remove(temp_archive_path)


if __name__ == "__main__":
    dir_to_archive = "./dir4"
    create_multivolume_archive(dir_to_archive, max_size=1024 * 1024) 

