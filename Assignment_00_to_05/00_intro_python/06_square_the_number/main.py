def main():
    user_input: float = float(input("Type a number to see its square: "))
    result: float = user_input **2
    print(f"{user_input} squared is {result}")

if __name__ == '__main__':
    main()