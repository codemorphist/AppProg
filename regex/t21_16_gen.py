import random

FEM_NAMES = "Анна,Вікторія,Єва,Злата,Катерина,Мирослава,Марія,Мілана,Софія,Соломія"
MAL_NAMES = "Андрій,Артем,Богдан,Давид,Данило,Дмитро,Максим,Матвій,Марк,Микола,Олександр,Сергій"

LASTNAMES = "Мельник,Шевченко,Коваленко,Бондаренко,Бойко,Ткаченко,Кравченко,Ковальчук,Олійник"

FEM_NAMES = FEM_NAMES.split(",")
MAL_NAMES = MAL_NAMES.split(",")
LASTNAMES = LASTNAMES.split(",")


def get_patronymic(pat: str, is_male: bool) -> str:
    if is_male:
        return pat + ("вич" if pat[-1] == "о" else "ович")
    else:
        if pat[-1] == "о":
            return pat[:-1] + "івна"
        elif pat[-1] in "aйя":
            return pat[:-1] + "ївна"
        else:
            return pat + "івна"


def get_name() -> str:
    firstname = random.choice(FEM_NAMES + MAL_NAMES)
    lastname = random.choice(LASTNAMES)
    pat = random.choice(MAL_NAMES)
    patronymic = get_patronymic(pat, firstname in MAL_NAMES) 

    if random.randint(0, 1):
        return " ".join([lastname, firstname, patronymic])
    else:
        return " ".join([lastname, firstname[0] + ".", patronymic[0] + "."])


def get_phone() -> str:
    return " ".join([
        random.choice(["тел.", "телефон"]),
        ("+" if random.randint(0,1) else "") +  
        "380" + str(random.randint(1000000000, 9999999999))
    ])


def get_debt() -> str:
    return f"{random.uniform(1, 1000):.2f} грн."


def get_debtor() -> str:
    debtor = [
        get_name(),
        get_phone(),
        get_debt(),
    ]
    random.shuffle(debtor)
    return " ".join(debtor)


def get_list(count: int, out: str):
    with open(out, "w") as f:
        for _ in range(count):
            f.write(get_debtor() + "\n")


if __name__ == "__main__":
    get_list(1000, "debtors_list_1.txt")


