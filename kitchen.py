import json
import time


class Cook:
    def __init__(self, id, phrase, rank, prof, personal_pool):
        # self.name = name
        self.id = id
        self.phrase = phrase
        self.rank = rank
        self.prof = prof
        self.personal_pool = personal_pool
        # self.my_orders = my_orders

    def preparing(self, order_list, full_menu):
        index = str(order_list[0])

        if full_menu[index]["complexity"] == 3 and 3 == self.rank:
            preparation_time = full_menu[index]["preparation-time"]
            order_list.pop(0)
            time.sleep(preparation_time / 10)
            print(self.id, "cooked the meal at", int(time.time()))

        elif full_menu[index]["complexity"] == 2 and 2 <= self.rank:
            preparation_time = full_menu[index]["preparation-time"]
            order_list.pop(0)
            time.sleep(preparation_time / 10)
            print(self.id, "cooked the meal at", int(time.time()))

        elif full_menu[index]["complexity"] == 1:
            preparation_time = full_menu[index]["preparation-time"]
            order_list.pop(0)
            time.sleep(preparation_time / 10)
            print(self.id, "cooked the meal at", int(time.time()))


hall_message = {"items": [9, 6, 5, 5, 2, 13, 2, 11, 4, 6],
                "max_wait": 45.5,
                "order_id": 3,
                "pick_up_time": 1663070601,
                "priority": 2,
                "table_id": 1,
                "waiter_id": 1}

order_list = []

f = open('food.json')
full_menu = json.load(f)
f.close()

menu_list_tier1 = []
menu_list_tier2 = []
menu_list_tier3 = []

for line in full_menu:
    complexity = full_menu[line]["complexity"]
    if complexity == 1:
        menu_list_tier1.append(full_menu[line]["name"])
    elif complexity == 2:
        menu_list_tier2.append(full_menu[line]["name"])
    elif complexity == 3:
        menu_list_tier3.append(full_menu[line]["name"])
print(menu_list_tier2, "DEBUG tier list")


def taskManager():
    for item in hall_message["items"]:
        order_list.append(item)
    return order_list


c1_pool = []
C1 = Cook(1, "Work bitch", 3, 3, c1_pool)

taskManager()

while len(order_list) > 0:
    C1.preparing(order_list, full_menu)
    print(order_list)

print('Order is done!')
