import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for rand_num in range(N_NUMBERS):
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        print(random_number, end=" ")

if __name__ == '__main__':
    main()