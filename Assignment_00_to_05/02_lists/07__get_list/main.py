def get_list(lst):
    print(lst)

def make_list():
    lst:list = []
    elem = input("Please input an element to add or press Enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please input an element to add or press Enter to stop: ")
    return lst

def main():
    lst = make_list()
    get_list(lst)
    
if __name__ == '__main__':
    main()