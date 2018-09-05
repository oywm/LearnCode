import numpy as np
import pandas as pd
import pymysql as pys

cnn = pys.connect(host='10.33.30.14', port=3306, user='oywm', password='oywm123', database='oywm_db', charset='utf8')
sql = 'select * from mushroom'
cursor = cnn.cursor()
cursor.execute(sql)
data = cursor.fetchall()
cnn.commit()
cursor.close()
cnn.close()

data_list = []
for line in data:
    data_list.append(list(line))

print(data_list)
