from datetime import datetime 
import re


def write_template(path: str, out: str) -> None:
    today = datetime.today()
    repl = today.strftime("%d.%m.%Y")

    text = ""
    with open(path, "r") as f:
        text = f.read()

    with open(out, "w") as f:
        text = re.sub(r"__\.__\.____", repl, text)
        f.write(text)


def test():
    path = "test_t21_4.txt"
    out = "out_t21_4.txt"
    write_template(path, out)


if __name__ == "__main__":
    # test()
    # exit()
    path = input("Input path to file: ")
    out = input("Input out file: ")
    write_template(path, out)


