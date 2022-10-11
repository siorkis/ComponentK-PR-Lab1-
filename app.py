import imp
from multiprocessing import Lock
from flask import Flask, request
import requests
import cook
import random 
import threading 
import json
import time

app = Flask(__name__)
mutex = Lock() # acquire() ~ lock | release() ~ unlock
data_pool = []
current_response = []
ides = []
c_pool = []
C1 = cook.Cook(1, "Gordon Ramsay says: Work bitch, we are not done yet", 3, 4, c_pool, 4)
C2 = cook.Cook(2, "Paul Bocuse says: looks good, like from Golden Bocuse", 3, 3, c_pool, 3)
C3 = cook.Cook(3, "Wolfgang Puck: excellent, do we serving that for Oskar?", 3, 2, c_pool, 2)
C4 = cook.Cook(4, "Konstantin Ivlev says: done, Wicked...", 3, 2, c_pool, 2)
cooks = [C1, C2, C3, C4]
threads = list()


@app.route('/order', methods=['POST'])
def answer():
    global current_response
    global ides
    global data_pool

    res = request.get_json()
    # current_response = res
    current_response.append(res["items"])
    ides.append(res["table_id"])
    # mutex.acquire()
    data_pool.append(res["items"])
    # mutex.release()
    print(data_pool, "DATA LIST ANSWER()")
    print("data has been received from compD")
    return "data has been received from compD"

def send_to_comp_d(index_cook):
    global current_response
    global ides 
    global data_pool

    # print(data_pool, "BEFORE TRUE DATA")
    current_cook = cooks[index_cook]
    while True:
        # print(data_pool, "AFTER TRUE DATA")
        if (len(data_pool) == 0):
            # print(orders_pool, "ORDERS POOL SEND TO HALL")
            time.sleep(1)
            continue
        # current_len = len(data_pool)
        try:
            if len(data_pool) > 0:
                while len(data_pool[0]) > 0:   
                    # print(data_pool[0], "DATA POOL AFTER WHILE")
                    # current_len = len(data_pool) 
                    # print(current_len, "CURRENT LEN -")
                    # print(ides, "IDES SUKKKAAAA")
                    current_cook.preparing(data_pool, 0, current_response, ides)
                    
                    # print(current_len, "CURRENT LEN AFTER PREPARING -")
                    # if len(data_pool) < current_len:
                    #     print(current_len, "CURRENT LEN AFTER IF -")
                    #     break
            print("data has been sended to compD")
        except:
            pass
            
            
        # payload = current_cook.serve_data(current_response)
        # post = requests.post("http://26.249.68.98:5000/distribution", json = payload)
        
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
