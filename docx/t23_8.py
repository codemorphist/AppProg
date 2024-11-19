import os
import re
from docx import Document

def replace_docx(path: str, ptr: str, repl: str):
    doc = Document(path)
    regex = re.compile(ptr)

    for paragraph in doc.paragraphs:
        if regex.search(paragraph.text):
            paragraph.text = regex.sub(repl, paragraph.text)

    file_path, filename = os.path.split(path)
    print(file_path, filename)
    file_path = os.path.join(file_path, "replaced_" + filename)
    print(file_path)
    doc.save(file_path)


def process_directory(path: str, ptr: str, repl: str):
    for root, dirs, files in os.walk(path):
        for file in filter(lambda f: f.endswith(".docx"), files):
            file_path = os.path.join(root, file)
            print(file_path)
            replace_docx(file_path, ptr, repl)
            input()


if __name__ == "__main__":
    # dir = input()
    # ptr = input()
    # repl= input()
    dir = "."
    ptr = "___"
    repl = "123"

    process_directory(dir, ptr, repl)
