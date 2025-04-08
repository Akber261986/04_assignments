_list: list = []
print(f"list Before: {_list}")

def main():
    user_input = input("Enter a message to copy: ")
    for i in range(3):
        _list.append(user_input)
    print(f"list After: {_list}")

if __name__ == '__main__':
    main()