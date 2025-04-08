Peturksbouipo, Stanlau, Mayengua = (16, 25, 48)

def main():
    usera_input = int(input("Enter your age: "))
    if usera_input >= Peturksbouipo:
        print(f"You can vote in Peturksbouipo where the voting age is {Peturksbouipo}")
    else: 
        print(f"You cannot vote in Peturksbouipo where the voting age is {Peturksbouipo}")
    if usera_input >= Stanlau:
        print(f"You can vote in Stanlau where the voting age is {Stanlau}")
    else: 
        print(f"You cannot vote in Stanlau where the voting age is {Stanlau}")
    if usera_input >= Mayengua:
        print(f"You can vote in Mayengua where the voting age is {Mayengua}")
    else: 
        print(f"You cannot vote in Mayengua where the voting age is {Mayengua}")

if __name__ == "__main__":
    main()