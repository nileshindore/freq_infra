import redis
import mysql.connector
import time
import datetime
import os

mysqlHost = os.environ['MYSQL_HOST']
redisHost = os.environ['REDIS_HOST']

while True:
    mydb = mysql.connector.connect(host=mysqlHost,user='root',passwd='root',db='BHARATINDEX')   
    mycursor = mydb.cursor()
    query = "select s_name from s_detail"
    mycursor.execute(query)
    indexValue = 0
    for i in mycursor:
        r = redis.Redis(host=redisHost)
        print(i[0])
        indexValue += int(r.get(i[0]))
    print(indexValue)
    query = "select i_id from i_detail where i_name='BHARATINDEX'"
    mycursor.execute(query)
    i_id = mycursor.fetchone()[0]
    print(type(i_id))
    tick_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #tick_time = datetime.datetime.now()
    print(tick_time)
    #insertQuery = "insert into i_price VALUES ({},{},{})".format(i_id,tick_time,indexValue)
    mycursor.execute("""insert into i_price (i_id,i_ttime,i_price) values (%s,%s,%s)""",(i_id,tick_time,indexValue))
    mydb.commit()
    mycursor.close()
    mydb.close()
    time.sleep(5)