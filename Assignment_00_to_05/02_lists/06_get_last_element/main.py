def get_last_element(lst):
    print(lst[-1])

def get_list():
    lst:list = []
    ele = input("Please input an element or press Enter to stop: ")
    while ele != "":
        lst.append(ele)
        ele = input("Please input an element or press Enter to stop: ")
    return lst

def main():
    lst = get_list()
    get_last_element(lst)

if __name__ == "__main__":
    main()