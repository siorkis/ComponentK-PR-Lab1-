import json
import time 
import requests

class Cook:

  f = open('food.json')
  full_menu = json.load(f)
  f.close()

  menu_list_tier1 = []
  menu_list_tier2 = []
  menu_list_tier3 = []

  counter = 0

  for line in full_menu:
    complexity = full_menu[line]["complexity"]
    if complexity == 1:
      menu_list_tier1.append(full_menu[line]["name"])
    elif complexity == 2:
      menu_list_tier2.append(full_menu[line]["name"])
    elif complexity == 3:
      menu_list_tier3.append(full_menu[line]["name"])
  # print(menu_list_tier2, "DEBUG tier list")

  
  def __init__(self, id, phrase, rank, prof, personal_pool, current_prof):
    # self.name = name 
    self.id = id
    self.phrase = phrase
    self.rank = rank
    self.prof = prof 
    self.personal_pool = personal_pool
    self.current_prof = current_prof
    # self.my_orders = my_orders


  # order_list = {1:[], 2:[], 3:[], 4:[], 5:[]}
  # def preparing(self, order_list, order_index):
  #   for i in reversed(range(1, 6)):

  #     # checking if there are orders in specific priority
  #     if order_list[i]:
  #       continue
      
  #     while self.current_prof > 0:
  #       # for items in orders
  #       for order in order_list[i]:
  #           for item in order:
  #             if Cook.full_menu[str(item)]["complexity"] == 3 and 3 == self.rank:
  #               preparation_time = Cook.full_menu[str(item)]["preparation-time"]
                

  def preparing(self, data_list, data_index, response, id):
    # print(id, "IDES SUKKKAAAA 2222222")
    if len(data_list) > 0:
      if len(data_list[data_index]) != 0:
        index = str(data_list[data_index][0])
        if Cook.full_menu[index]["complexity"] == 3 and 3 == self.rank:
            preparation_time = Cook.full_menu[index]["preparation-time"]
            data_list[data_index].pop(0)
            if len(data_list[data_index]) == 0:
              data_list.pop(0)
              payload = self.serve_data(response, id)
              post = requests.post("http://26.249.68.98:5000/distribution", json = payload)
              time.sleep(5)
            time.sleep(preparation_time / 10)
            print(self.id, "cooked the meal at", int(time.time() * 10))
            print(data_list, "DATA LIST AFTER PROCESSING")
            

        elif Cook.full_menu[index]["complexity"] == 2 and 2 <= self.rank:
            preparation_time = Cook.full_menu[index]["preparation-time"]
            data_list[data_index].pop(0)
            if len(data_list[data_index]) == 0:
              data_list.pop(0)
              payload = self.serve_data(response, id)
              post = requests.post("http://26.249.68.98:5000/distribution", json = payload)
              time.sleep(5)
            time.sleep(preparation_time / 10)
            print(self.id, "cooked the meal at", int(time.time()) * 10)
            print(data_list, "DATA LIST AFTER PROCESSING")

        elif Cook.full_menu[index]["complexity"] == 1:
            preparation_time = Cook.full_menu[index]["preparation-time"]
            data_list[data_index].pop(0)
            if len(data_list[data_index]) == 0:
              data_list.pop(0)
              payload = self.serve_data(response, id)
              post = requests.post("http://26.249.68.98:5000/distribution", json = payload)
              time.sleep(5)
            time.sleep(preparation_time / 10)
            print(self.id, "cooked the meal at", int(time.time()))
            print(data_list, "DATA LIST AFTER PROCESSING")
    

  def serve_data(self, message, id):
    print(message, "message SEND ORDER")
    # payload = {
    #   "order_id": int(message["order_id"]),
    #   "table_id": int(message["table_id"]),
    #   "waiter_id": int(message["waiter_id"]),
    #   "items": message["items"],
    #   "priority": int(message["priority"]),
    #   "max_wait": float(message["max_wait"]),
    #   "pick_up_time": int(message["pick_up_time"]), # UNIX timestamp
    #   "cooking_time": (int(time.time()) - int(message["pick_up_time"]))*10,
    #   "cooking_details": 
    #   [{
    #   "food_id": 3,
    #   "cook_id": self.id,
    #   },]
    # }
    # print(id, "IDES SUKKKAAAA 3333333")
    # payload = {
    #   "table_id": id[Cook.counter], 
    #   "items": message[Cook.counter]
    # }
    payload = {
      "table_id": id[Cook.counter],
      "status": 'object received processed data'
    }
    Cook.counter += 1
    print(payload, "PAYLOAD~")
    return payload
