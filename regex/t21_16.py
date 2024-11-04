import re

P_NAME = r"\b[А-ЯҐЄІЇ][А-ЯҐЄІЇа-яґєії]*\b"
P_PHONE = r"\b(тел\.|телефон)\s*\+?(380\d{7,12})\b"
P_DEBT = r"(\d+(.\d+)?)\s*грн.?"


def get_top100_debtors(path: str, out: str):
    debtors = []
    with open(path, "r") as f:
        for line in f.readlines():
            name = " ".join(re.findall(P_NAME, line))
            phone = re.findall(P_PHONE, line)[0][1]
            debt = float(re.findall(P_DEBT, line)[0][0])
            debtors.append((name, phone, debt))

    debtors = sorted(debtors, key=lambda d: d[2], reverse=True)
    with open(out, "w") as f:
        f.write("\n".join([":".join([str(a) for a in d]) for d in debtors[:100]]))


if __name__ == "__main__":
    path = "./debtors_list_1.txt"
    out = "top_100_debtors.txt"
    get_top100_debtors(path, out)

