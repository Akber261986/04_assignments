def get_user_num():
    lst: list = []
    user_input = input("Enter a number: ")
    while user_input != "":
        int(user_input)
        lst.append(user_input)
        user_input = input("Enter a number: ")
    return lst

def count_nums(num_lst):
    num_dic = {}
    for num in num_lst:
        if num not in num_dic:
            num_dic[num] = 1
        else:
            num_dic[num] += 1
    return num_dic

def print_num(num_dict):
    for key in num_dict:
        print(f"{key} appears {num_dict[key]} times")
    

def main():
    user_num = get_user_num()
    dict = count_nums(user_num)
    print_num(dict)
if __name__ == '__main__':
    main()