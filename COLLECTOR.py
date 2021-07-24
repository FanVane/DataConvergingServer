import json
import requests
import random


def generate_final_data(size: int):
    ans = []
    for i in range(size):
        ans.append(random.random() * 20 - 10)
    return ans


# 1. 生成数据
data_collected = generate_final_data(100_0000)
print("data generated")
# 2. 保存为json字符串，发送post请求，将数据传送到到服务器
# step 1
basic_url = "http://127.0.0.1:5000"
post_url = basic_url + "/upload_file_json"
data = {
    "data_collected": json.dumps(data_collected),
}
# step 2 发起一个post请求，返回一个响应对象
res = requests.post(url=post_url, data=data)
print("上传数据结束" + str(id) + str(res))
