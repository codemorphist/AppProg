import os


def compare_files(dir1: str, dir2: str, out str):
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    
    common_files = files1 & files2
    
    with open(out, "w") as f:
        for filename in common_files:
            path1 = os.path.join(dir1, filename)
            path2 = os.path.join(dir2, filename)
            
            size1 = os.path.getsize(path1)
            size2 = os.path.getsize(path2)
            
            if size1 != size2:
                diff = abs(size1 - size2)
                f.write(
                    f"File: {filename}, Size difference: {diff} bytes\n"
                    f"Path: {path1} | {path2}\n\n"
                )


if __name__ == "__main__":
    dir1 = "./dir1"
    dir2 = "./dir2"
    output_file = "t22_3_result.txt"
    compare_files(dir1, dir2, output_file)

