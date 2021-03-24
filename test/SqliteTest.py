# -*- coding = utf-8 -*-
# @author tangwenbo
# @File SqliteTest
# @date 2021/3/24 15:27
import sqlite3

connect = sqlite3.connect("sq.db")

cursor = connect.cursor()

createSql = """
create table python
    (id int primary key not null,
    name text not null ,
    age int not null default 10,
    address text)
"""

insertSql = """
insert into python (id,name,age) values (2,3,4)

"""

selectSql = """
select * from python
"""

execute = cursor.execute(selectSql)
for row in cursor:
    print(row)
connect.commit()
connect.close()
