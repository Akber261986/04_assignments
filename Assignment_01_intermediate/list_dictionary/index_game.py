elements: list = [1, 2, 3, "mango", "juice", "akber", True, False, ]

def access_elemnts():
    try:
        index = int(input("Enter the index number: "))
        value = elements[index]
        return value
    except IndexError:
        return "index is out of range"

def modifying_elements():
    try:
        index = int(input("Enter the index number: "))
        value = input("Enter the new Item: ")
        elements.insert(index, value)
        return elements
    except IndexError:
        return "Index is out of range"
    


def slice_elements():
    try:
        start_index = int(input("Enter the first index: "))
        end_index = int(input("Enter the second index: "))
        sliced_list = elements[start_index:end_index]
        return sliced_list
    except IndexError:
        return "Index is out of range"
    

def main():
    operation = input(f"Select an operation (access, modify, slice): ")
    if operation == "access":
        result = access_elemnts()
        print(result)
    elif operation == "modify":
        result = modifying_elements()
        print(result)
    elif operation == "slice":
        result = slice_elements()
        print(result)

main()