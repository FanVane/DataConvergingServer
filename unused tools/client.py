import sys
import time
import requests
import json
import threading


def uploadtest(id):
    # 在这里收集完了全部的笔画数据，并且将数据保存到了一个数组中
    # 下一步就是发送post请求，将数据传送到到服务器
    data_collected = []
    for i in range(10000):
        data_collected.append(i + id)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    # step 1
    post_url = "http://j46wofvt.shenzhuo.vip:16832/upload"
    # post_url = "http://127.0.0.1:5000/upload"
    # post请求参数处理同requests.get()
    data = {
        "data_collected": json.dumps(data_collected),
        "table_name": "dataset" + str(id)
    }
    # step 2 发起一个post请求，返回一个响应对象
    # 对制定的url发起的请求对应的url是携带参数的，并且在请求过程中处理了参数
    res = requests.post(url=post_url, data=data, headers=headers)
    print("上传数据结束" + str(id) + str(res))


def upload(data_collected: list, table_name: str):
    # 在这里收集完了全部的笔画数据，并且将数据保存到了一个数组中
    # 下一步就是发送post请求，将数据传送到到服务器
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    # step 1
    post_url = "http://j46wofvt.shenzhuo.vip:16832/upload"
    # post_url = "http://127.0.0.1:5000/upload"
    # post请求参数处理同requests.get()
    data = {
        "data_collected": json.dumps(data_collected),
        "table_name": table_name
    }
    # step 2 发起一个post请求，返回一个响应对象
    res = requests.post(url=post_url, data=data, headers=headers)
    print("上传数据结束" + str(id) + str(res))


threads = []
data_collected = []
for i in range(100_0000):
    data_collected.append(5.0)
print("start to transport ,size: " + str(sys.getsizeof(data_collected)))
start_time = time.time()
dataset_number = 1
for i in range(dataset_number):
    # t = threading.Thread(target=uploadtest, args=[i])
    t = threading.Thread(target=upload, args=[data_collected, "dataset"+str(i)])
    threads.append(t)
    t.start()
for i in range(dataset_number):
    threads[i].join()
total_time = time.time() - start_time
print("Time spent: " + str(total_time) + " seconds.")
