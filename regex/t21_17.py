import re


RESTRICTED = {
    "neflix.com",
    "vk.com",
    "vk.ru",
    "ok.ru",
    "onlyfans.com",
    "rezka.hd",
    "kinogo.biz",
    "youtube.com",
    "telegram.com"
}

P_COMP = r"((\d{1,3}\.){3}\d{1,3})"
P_ADDR = r"https?:\/\/([a-zA-Z0-9.-]+)"
P_TIME = r"((\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2}))"

p_com = re.compile(P_COMP)
p_addr = re.compile(P_ADDR)
p_time = re.compile(P_TIME)


def sanitize_url(url: str) -> str:
    return url.replace("www.", "")


def process_line(line: str) -> tuple:
    comp = re.search(p_com, line).groups()[0]
    addr = re.search(p_addr, line).groups()[0]
    time = re.search(p_time, line).groups()[0]

    addr = sanitize_url(addr)

    return (comp, addr, time)


def process_file(path: str, out: str):
    file = ""
    res_records = []
    with open(path, "r") as f:
        for line in f.readlines():
            rec = process_line(line)

            if rec[1] in RESTRICTED:
                res_records.append(rec)

    with open(out, "w") as f:
        f.write(
            "\n".join([
                " ".join(rec) for rec in res_records
            ])
        )


if __name__ == "__main__":
    process_file("./provider_data.txt", "porushniki.txt")
