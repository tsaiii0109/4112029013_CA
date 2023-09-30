# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 22:23:51 2023

@author: User
"""

import sqlite3

#連接到 SQlite 資料庫(如果不存在，將創建一個新的資料庫文件)
conn = sqlite3.connect('BBQ.db')

#創建一個游標對象，用於執行 SQL 查詢
cursor = conn.cursor()

#創建一個名為 meat 的表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS meat(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER
    )''')

#增加三筆資料
cursor.execute("INSERT INTO meat (name,price,quantity) VALUES ('chicken',30,5)")
cursor.execute("INSERT INTO meat (name,price,quantity) VALUES ('beaf',55,10)")
cursor.execute("INSERT INTO meat (name,price,quantity) VALUES ('pork',40,15)")
#提交事務
conn.commit()
#查詢資料
cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
#print出表格內容
print("meat列表:")
for BBQ in meat:
    print(BBQ)

#更改資料
cursor.execute("UPDATE meat SET price = 35 WHERE name = 'pork'")
cursor.execute("UPDATE meat SET quantity = 30 WHERE name = 'chicken'")
conn.commit()
#查詢資料
cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
#print出表格內容
print("(更改資料後)meat列表:")
for BBQ in meat:
    print(BBQ)

#刪除資料
#因為沒有price=40的資料，所以改成刪掉price=35的資料
#cursor.execute("DELETE FROM meat WHERE price = 40")
cursor.execute("DELETE FROM meat WHERE price = 35")
conn.commit()
#查詢資料
cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
#print出表格內容
print("(刪除資料後)meat列表:")
for BBQ in meat:
    print(BBQ)

#關閉游標和連結
cursor.close()
conn.close()