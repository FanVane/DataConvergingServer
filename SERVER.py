from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/upload_file_json', methods=['POST'])
def upload_list():
    assert request.method == 'POST'
    table_name = request.form["table_name"]
    data_collected = request.form["data_collected"]
    print(len(data_collected))
    with open("datasets/" + table_name + ".json", 'w') as fp:
        fp.write(data_collected)
    return "successfully stored into server disk with name " + table_name


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
