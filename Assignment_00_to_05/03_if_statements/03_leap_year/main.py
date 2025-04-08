def main():
    user_input = int(input("Please enter a year to check is it leap year or not: "))

    if user_input % 4 == 0:
        if user_input % 100 == 0:
            if user_input % 400 == 0:
                print("It's a leap year.")
            else:
                print("It's not a leap year.")
        else:
            print("It's a leap year.")
    else:
        print("It's not a leap year.")
if __name__ == '__main__':
    main()