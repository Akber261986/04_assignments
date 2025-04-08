def store_phone_numbers():
    pb_dic = {}
    user_name = input("Please Enter a name: ")
    while user_name != "":
        phone_number = input("Please Enter phone number: ")
        int(phone_number)
        pb_dic[user_name] = phone_number
        user_name = input("Please Type a name or press Enter to stop adding phone numbers: ")
    return pb_dic

def print_pb(pb):
    for name in pb:
        print(f"{name} : {pb[name]}")

def main():
    pb = store_phone_numbers()
    print_pb(pb)

if __name__ == "__main__":
    main()