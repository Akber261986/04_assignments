import random

def main():
    for i in range(10):
        rand_num = random.randint(1, 100)
        print(rand_num, end=" ")

if __name__ == "__main__":
    main()