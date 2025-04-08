def item_quary():
    fruit_dict = {
        "apple": 5,
        "durian": 7,
        "jackfruit": 6,
        "kiwi": 4,
        "rambutan": 15,
        "mango": 10
    }
    for fruit_name in fruit_dict:
        item = int(input(f"How many ({fruit_name}) do you want?: "))
        price = item * int(fruit_dict[fruit_name])
        fruit_dict[fruit_name] = price
    return fruit_dict

def calculate_price(list_item):
    total = 0
    for fruite_name in list_item:
        total += int(list_item[fruite_name])
    print(f"${total}")



def main():
    items_lst = item_quary()
    calculate_price(items_lst)

if __name__ == '__main__':
    main()