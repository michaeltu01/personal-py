def user_input():
    list = []
    while True:
        item = input("Enter an item into the list (enter 'q' to quit): ")
        if(item == "q" or item == "Q"):
            break
        list.append(item)
    return list


def comma_code(list):
    print("\nHere is your list: ")
    for i in range(0, len(list)):
        if(len(list) == 1):
            print(list[i])
        elif(i == (len(list) - 1)):
            print("and", list[i])
        else:
            print(list[i] + ',', end = ' ')

comma_code(user_input())