def main():
    userInput1 =  float(input("What is the length of side 1? "))
    userInput2 =  float(input("What is the length of side 2? "))
    userInput3 =  float(input("What is the length of side 3? "))

    result: float = userInput1 + userInput2 + userInput3
    print()
    print(f"The perimeter of the triangle is {result}")

    width = (userInput1 + userInput2) / 2
    height = userInput3 / 2

    area = width * height
    print(f"The area of triangle is {round(area, 2)} square\n")


if __name__ == '__main__':
    main()