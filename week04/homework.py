import pandas as pd
import numpy as np
import pymysql

#####作业:请将以下的 SQL 语句翻译成 pandas 语句：#####
conn = pymysql.connect('ip','name','password','dbname','charset=utf8')

# 1. SELECT * FROM data;
sql  =  'SELECT * FROM data'
df = pd.read_sql(sql,conn)
print(df)


# 2. SELECT * FROM data LIMIT 10;
print(df.head(10))


# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(df['id'])


# 4. SELECT COUNT(id) FROM data;
print(df['id'].count())


# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(df[(df['id']<1000)&(df['age']>30)])


# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
sql2  =  'SELECT * FROM table1'
df2 = pd.read_sql(sql2,conn)
print(df2.groupby('id').order_id.unique())


# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
sql1  =  'SELECT * FROM table1'
sql2  =  'SELECT * FROM table2'
data1 = pd.read_sql(sql1,conn)
data2 = pd.read_sql(sql2,conn)
print(pd.merge(data1, data2, on= 'id', how='inner'))


# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([data1, data2]))
print(pd.merge(data1, data2, how='outer'))


# 9. DELETE FROM table1 WHERE id=10;
idx_id10=data1[data1['id']==10].index
new_data1=data1.drop(idx_id10)
print(new_data1)


# 10. ALTER TABLE table1 DROP COLUMN column_name;
new2_data1=data1.drop( 'column_name' ,axis = 1)
print(new2_data1)

