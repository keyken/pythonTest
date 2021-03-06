# -*- coding: utf-8 -*-
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
        self.file.write(line.encode("utf-8"))
        conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='zhaoping1')
        cur = conn.cursor()
        tsql = "insert into jsondataTest1(info) values('{json}')"
        sql = tsql.format(json=MySQLdb.escape_string(line))
        cur.execute(sql)
        conn.commit()
        return item
