minimum_height = 50

def main():
    while True:
        user_input = int(input("How Tall are you? "))
        if user_input >= minimum_height:
            print("You're tall enough to ride!")
            break
        else:
            print("You're not tall enough to ride, but maybe next year!")
if __name__ == '__main__':
    main()