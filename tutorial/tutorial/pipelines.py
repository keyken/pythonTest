# -*- coding: utf-8 -*-
#coding=utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import MySQLdb

class TutorialPipeline(object):
    def __init__(self):
        self.file = codecs.open('dmoz_data_utf8.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item))+'\n'
        conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='zhaoping1')
        cur = conn.cursor()
        if line != "select * from jsondataTest2 order by info desc limit 1":
            tsql = "insert into jsondataTest2(info) values('{json}')"
            sql = tsql.format(json=MySQLdb.escape_string(line.decode('unicode_escape')))
            cur.execute(sql)
            conn.commit()
        self.file.write(line.decode('unicode_escape'))
        return item
