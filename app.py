import imp
from multiprocessing import Lock
from flask import Flask, request
import requests
import consumer
import random 
import threading 
import json
import time
import asyncio

app = Flask(__name__)
mutex = asyncio.Lock()
data_pool = []
current_response = []
ides = []
c_pool = []

eaters = [consumer.Consumer(i) for i in range(1, 5)]

threads = list()


@app.route('/order', methods=['POST'])
def answer():
    global current_response
    global ides
    global data_pool

    res = request.get_json()
   
    current_response.append(res["items"])
    ides.append(res["producer_id"])
    

    data_pool.append(res["items"])
   

    print(data_pool, "DATA LIST ANSWER()")
    print("data has been received from compD")
    return "data has been received from compD"

def send_to_comp_d(index_eater):
    global current_response
    global ides 
    global data_pool

    current_eater = eaters[index_eater]
    while True:
        if (len(data_pool) == 0):
            time.sleep(1)
            continue
        try:
            if len(data_pool) > 1:
                while len(data_pool[0]) > 0:   
                    current_eater.consume(data_pool, 0, current_response, ides)
                print("data has been sended to compD")
        except:
            pass
        
        return "data has been sended to compD"



if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0", port=6000, use_reloader=False)
    
    flask_thread = threading.Thread(target=lambda: app.run(debug=False, host="0.0.0.0", port=6000, use_reloader=False))

    threads = list()
    threads.append(flask_thread)
    for index in range(4):
        iterable = [index]
        print("Main    : create and start thread.", index)
        x = threading.Thread(target=send_to_comp_d, args=(iterable))
        threads.append(x)
    
    for index, thread in enumerate(threads):
        print("Main    : before joining thread.", index)
        thread.start()
        print("Main    : thread done", index)
