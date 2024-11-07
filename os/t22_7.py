from datetime import datetime
import os


def find_oldest_file(dir: str) -> tuple[str, int]:
    old_file = None
    old_time = float("inf")

    for dir, _, files in os.walk(dir):
        for file in files:
            path = os.path.join(dir, file)

            time = os.path.getctime(path)

            if time < old_time:
                old_time = time
                old_file = path

    return old_file, old_time


if __name__ == "__main__":
    dir = "./dir3/"

    old_file, old_time = find_oldest_file(dir)

    if old_file:
        time = datetime.fromtimestamp(old_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f"The oldest file is: {old_file}")
        print(f"Creation time: {time}")
    else:
        print("No files found.")

    
