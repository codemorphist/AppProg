from datetime import datetime, timedelta
import random


def get_comp_addr() -> str:
    return ".".join([str(random.randint(0, 255)) for _ in range(4)]) 


SITES = ["google.com", "netflix.com", "vk.com", "vk.ru", "ok.ru",
         "onlyfans.com", "rezka.hd", "kinogo.biz", "math.ru",
         "duckduckgo.com", "github.com", "youtube.com", "reddit.com",
         "diia.gov.ua", "wikipedia.com", "telegram.com", "dou.ua",
         "pentagon.com", "mil.ua", "privat24.ua"]

def get_site() -> str:
    site = random.choice(SITES) 
    protocol = random.choice(["https://", "http://"])

    return f"{protocol}www.{site}{random.choice(['/', ''])}"


def get_time() -> str:
    startdate = datetime(2022, 1, 1)
    delta = timedelta(days = random.randint(0, 365 * 2), 
                      hours = random.randint(0, 24), 
                      minutes = random.randint(0, 60), 
                      seconds = random.randint(0, 60))
    gen_date = startdate + delta
    return gen_date.strftime("%d.%m.%Y %H:%M:%S")


def get_record() -> str:
    return " ".join([
        get_comp_addr(),
        get_site(),
        get_time()
    ])


def gen_records_list(count: int, out: str):
    with open(out, "w") as f:
        f.write(
            "\n".join([get_record() for _ in range(count)])
        )
        

if __name__ == "__main__":
    gen_records_list(10000, "provider_data.txt")

