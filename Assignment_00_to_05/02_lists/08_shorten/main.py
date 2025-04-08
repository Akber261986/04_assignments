MAX_LENGTH: int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()
        print(removed)
    print(f"Shorten list = {lst}")

def get_list():
    lst: list = []
    elem = input("Input the element to add or press Enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Input the element to add or press Enter to stop: ")
    return lst

def main():
    lst = get_list()
    shorten(lst)

if __name__ == "__main__":
    main()