import MySQLdb
import json

data = []
conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='keykid', db='zhaoping')
cur = conn.cursor()
with open('dmoz_data_utf8.json') as f:
    for line in f:
        tsql = "insert into jsondata(data) values('{json}')"
        print(line)
        sql = tsql.format(json=MySQLdb.escape_string(line))
        cur.execute(sql)
        conn.commit()