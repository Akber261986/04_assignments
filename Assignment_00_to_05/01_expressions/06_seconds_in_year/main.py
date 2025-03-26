def main():
    mins = 60
    hour = 60
    day = 24
    year = 365
    sec_in_year = mins * hour * day * year
    sec_in_leap_year = mins * hour * day * (year+1)
    print(f"There are {sec_in_year} second in a year\nand")
    print(f"There are {sec_in_leap_year} second in a leap year")

if __name__ == "__main__":
    main()
