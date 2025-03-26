import math

def main():
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    bc = (ab**2) + (ac**2)
    res = math.sqrt(bc)
    print(f"The length of BC (the hypotenuse) is: {res}")

if __name__ == "__main__":
    main()