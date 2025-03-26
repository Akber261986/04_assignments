numbers: list[int] = [1, 2, 3, 4, 5, 6]

def main():
    new_list = []
    for num in numbers:
        result = num * 2
        new_list.append(result)
    return new_list
res = main()
print(f"Numbers = {res}")

if __name__ == "__main__":
    main()