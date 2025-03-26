numbers: list[int] = [15, 12, 35, 25, 19]

def main():
    sum_all = 0
    for num in numbers:
        sum_all += num
    return sum_all

print(main())
if __name__ == '__main__':
    main()