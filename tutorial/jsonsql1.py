# -*- coding: utf-8 -*-

import MySQLdb
import json

data = []
conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='zhaoping1')
cur = conn.cursor()
with open('dmoz_data_utf8.json') as f:
    for line in f:
        tsql = "insert into jsondataTest2(info) values('{json}')"
        print(MySQLdb.escape_string(line))
        sql = tsql.format(json=MySQLdb.escape_string(line))
        cur.execute(sql)
        conn.commit()