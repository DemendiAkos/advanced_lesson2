
def count_char(text):
    result = set(item for item in text)
    return len(result)

def most_common_char(text):
    char = [item for item in text]
    my_dict  = {}
    for i in char:
        if i not in my_dict.keys():
            my_dict[i] = 1
        else:
            my_dict[i] += 1

    return max(my_dict, key=my_dict.get)

if __name__ == "__main__":
    user_input = input("Input text: ")
    print(count_char(user_input))
    print(most_common_char(user_input))