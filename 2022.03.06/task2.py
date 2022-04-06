

class User:

    def __init__(self,name,mail,permission):
        self.name = name
        self.mail = mail
        self.permission = permission

    def __str__(self):
        return (f"{self.name} {self.mail} {self.permission}")

def open_file():
    with open ("users.csv","r",encoding="UTF-8") as raw:
        raw = raw.read().splitlines()
        result = []
        for line in raw:
            item = line.split(";")
            dataappend = User(item[0],item[1],item[2])
            result.append(dataappend)
    return result

def read_user(data):
    result = [text.name for text in data]
    return result

def user_with_input_permission(data, user_i):
    result = [text.name for text in data if user_i == text.permission]
    return result

def return_if_name_duplicate(data):
    name_set = set([text.name for text in data])
    if len(name_set) < len([text.name for text in data]):
        return False
    return True

def return_names_by_permissions(data):
    permissions = {}
    for permission in data:
        

if __name__ == "__main__":
    data = open_file()
    #1
    print(read_user(data))
    #2
    user_permission = input("Input a permission type: ")
    print(user_with_input_permission(data,user_permission))
    #3
    print(return_if_name_duplicate(data))
    #4
    print(return_names_by_permissions(data))