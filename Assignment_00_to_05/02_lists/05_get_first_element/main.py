def get_first_element(lst):
    print(lst[0])

def get_lsit():
    lst:list = []
    user_input = input("Please enter an element of the list or press enter to stop: ")
    while user_input != "":
        lst.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lsit()
    get_first_element(lst)

if __name__ == "__main__":
    main()