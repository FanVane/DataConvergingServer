import psycopg2
import json
import os

# 1. 获取文件名列表
json_list = []
for root, dirs, files in os.walk("./datasets", topdown=False):
    for filename in files:
        json_list.append(filename)
print(json_list)


for json_file_name in json_list:
    # 2. 将list中某个文件存到数据库中
    conn = psycopg2.connect(database='datasets', user='postgres',
                            password='vane2001', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    with open("./datasets/" + json_file_name, 'r') as f:
        data = json.load(f)
    table_name = "xxx"
    sql = ["drop table if exists " + table_name + "; create table " + table_name + "(AIO real);"]
    for item in data:
        sql.append("insert into " + table_name + " values (" + str(item) + ");")
    cursor.execute("".join(sql))
    conn.commit()
    cursor.close()
    conn.close()
    print("stored " + table_name + " into database.")
print(done)