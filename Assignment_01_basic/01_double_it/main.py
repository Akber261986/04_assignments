user_input = int(input("Enter a value: "))
curr_value = user_input

def main():
    while curr_value < 100:
        curr_value = curr_value*2
        print(curr_value, end=" ")
        
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()