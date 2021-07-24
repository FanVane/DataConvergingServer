import os

from flask import Flask
from flask import request
import os

app = Flask(__name__)


def get_file_name():
    json_list = []
    for root, dirs, files in os.walk("./datasets", topdown=False):
        for filename in files:
            json_list.append(filename)
    index = 0
    while True:
        file_name = "dataset" + str(index) + ".json"
        if file_name in json_list:
            index += 1
            continue
        return file_name


# 将收集到的文件存储到文件夹中
@app.route('/upload_file_json', methods=['POST'])
def upload_list():
    assert request.method == 'POST'
    file_name = get_file_name()
    data_collected = request.form["data_collected"]
    print(str(len(data_collected)) + " elements received")
    with open("datasets/" + file_name, 'w') as fp:
        fp.write(data_collected)
    return "successfully stored into server disk with name " + file_name


def list2html(res, headline):
    ans = ["<table><tr>", "<td>序号</td>"]
    for i in range(len(headline)):
        ans.append("<td>" + headline[i] + "</td>")
    ans.append("</tr>")
    for row_number in range(len(res)):
        ans.append("<tr>")
        ans.append("<td>" + str(row_number) + "</td>")
        for col_number in range(len(headline)):
            ans.append("<td>" + str(res[row_number][col_number]) + "</td>")
        ans.append("</tr>")
    ans.append("</table>")
    print("".join(ans))
    return "".join(ans)


# 查看服务器中的所有文件
@app.route('/status', methods=['GET'])
def status():
    pass


@app.route('/select/<table_name>', methods=['GET'])
def select_table(table_name):
    pass


app.run()
