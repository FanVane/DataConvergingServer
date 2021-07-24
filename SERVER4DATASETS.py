from flask import Flask
from flask import request
import psycopg2
import json

app = Flask(__name__)


@app.route('/upload_list', methods=['POST'])
def upload_list():
    assert request.method == 'POST'
    data = json.loads(request.form["data_collected"])
    table_name = request.form["table_name"]
    conn = psycopg2.connect(database='datasets', user='postgres',
                            password='vane2001', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    sql = ["drop table if exists " + table_name + "; create table " + table_name + "(AIO real);"]
    for item in data:
        # 有用的数据 加工并发送到数据库
        sql.append("insert into " + table_name + " values (" + str(item) + ");")
    cursor.execute("".join(sql))
    conn.commit()
    cursor.close()
    conn.close()
    return "successfully stored into database"


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


@app.route('/status', methods=['GET'])
def status():
    conn = psycopg2.connect(database='datasets', user='postgres',
                            password='vane2001', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    sql = "select tablename from pg_tables where schemaname = 'public';"
    cursor.execute(sql)
    res = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    for row_number in range(len(res)):
        res[row_number] = ["<a href='" + "http://127.0.0.1:5000/select/" + str(res[row_number][0]) + "'>" + \
                           str(res[row_number][0]) + "</a>"]
    return list2html(res, ["表名"])


@app.route('/select/<table_name>', methods=['GET'])
def select_table(table_name):
    conn = psycopg2.connect(database='datasets', user='postgres',
                            password='vane2001', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    sql = "select * from " + table_name + ";"
    cursor.execute("".join(sql))
    res = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return list2html(res, ["数据值"])


app.run()
