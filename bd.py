def set_value(key: str, value: str) -> None:
    with open("test1.db", "r") as file:
        for line in file:
            if key in line:
                print("Error, this user already exists")
                return
    with open("test1.db", "a") as file:
        file.write(key + ":" + value + "\n")


def get_value(key: str) -> str:
    with open("test1.db", "r") as file:
        for line in file:
            if key in line:
                return line.split(":")[1].replace("\n", "")



def modify_value(key: str, value: str):
    with open("test1.db", "r") as file:
        for line in file:
            if key not in line:
                print("Error, user does not exist")
                return

#set_value("looser", "drowssap")
#set_value("loot", "password1")
modify_value("loot", "password123")
#print(get_value("looser"))