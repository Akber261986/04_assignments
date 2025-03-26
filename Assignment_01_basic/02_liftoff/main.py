import time

# Count down with for loop
def main():
    count = 10
    for i in range(10):
        print(count)
        count -= 1
        time.sleep(1)
    print("Lift Off")

# count down with while loop
# def main():
    # count = 10
    # while count > 0:
    #     print(count)
    #     count -= 1
    #     time.sleep(1)
    # print("lift Off")
    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()