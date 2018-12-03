def set_value(key: str, value: str) -> None:
    with open("test1.db", "r") as file:
        for line in file:
            if key + ":" in line:
                print("Error, this user already exists")
                return
    with open("test1.db", "a") as file:
        file.write(key + ":" + value + "\n")


def get_value(key: str) -> str:
    with open("test1.db", "r") as file:
        for line in file:
            if key + ":" in line:
                return line.split(":")[1].replace("\n", "")


def modify_value(key: str, value: str) -> None:
    new_lines = []
    with open("test1.db", "r") as file:
        for line in file:
            if key + ":" in line:
                new_line = line.replace(line.split(":")[1], value + "\n")
                new_lines.append(new_line)
            else:
                new_lines.append(line)
    with open("test1.db", "w") as file:
        for i in new_lines:
            file.write(i)


def remove_value(key: str) -> None:
    not_remove = []
    with open("test1.db", "r") as file:
        for line in file:
            if key + ":" in line:
                pass
            else:
                not_remove.append(line)
    with open("test1.db", "w") as file:
        for i in not_remove:
            file.write(i)


def backup_db() -> None:
    with open("test1.db", "r") as file:
        with open("test1.backup", "w") as new_file:
            for line in file:
                new_file.write(line)

#set_value("loot", "ACAB")
#modify_value("loot", "ACAB")
#print(get_value("loot"))
#remove_value("loot")
#backup_db()