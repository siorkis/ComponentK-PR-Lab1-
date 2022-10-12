import json
import time 
import requests

class Consumer:

  f = open('food.json')
  full_menu = json.load(f)
  f.close()
  counter = 0

  def __init__(self, id): 
    self.id = id

  def consume(self, data_list, data_index, response, id):
    if len(data_list) > 1:
      if len(data_list[data_index]) != 0:
        index = str(data_list[data_index][0])
        eating_time = Consumer.full_menu[index]["eating-time"]
        data_list[data_index].pop(0)
        if len(data_list[data_index]) == 0:
          data_list.pop(0)
          payload = self.serve_data(response, id)
          post = requests.post("http://192.168.1.128:5000/distribution", json = payload)
        time.sleep(eating_time / 10)
        print(data_list, "DATA LIST AFTER PROCESSING")

  def serve_data(self, message, id):
    while len(message[0]) == 0:
      message.pop(0)
    payload = {
      "producer_id": id[Consumer.counter],
      "items": message[Consumer.counter]
    }
    Consumer.counter += 1
    # print(payload, "PAYLOAD~")
    return payload
