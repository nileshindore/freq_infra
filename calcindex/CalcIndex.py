import mysql.connector
import time
import datetime
import os

mysqlHost = os.environ['MYSQL_HOST']
mysqlUser = os.environ['MYSQL_USER']
mysqlPassword = os.environ['MYSQL_PASSWORD']
mysqlDbName = os.environ['MYSQL_DB']

while True:
    mydb = mysql.connector.connect(host=mysqlHost,user=mysqlUser,passwd=mysqlPassword,db=mysqlDbName)   
    mycursor = mydb.cursor()
    query = "select s_id from s_detail"
    mycursor.execute(query)
    ids = [] 
    for id in mycursor.fetchall():
        ids.append(id[0])
    mycursor.close()
    indexValue = 0
    for stockid in ids:
        mycursor = mydb.cursor(buffered=True)
        query = "select s_price from s_price where s_id = '%s' ORDER BY s_ttime DESC LIMIT 1" % stockid
        mycursor.execute(query)
        indexValue += mycursor.fetchall()[0][0]
        mycursor.close()
    print(indexValue)
    query = "select i_id from i_detail where i_name = '%s'" % mysqlDbName
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(query)
    i_id = mycursor.fetchone()[0]
    tick_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("tick_time = " + tick_time)
    print("index value = " + str(indexValue))
    mycursor.execute("""insert into i_price (i_id,i_ttime,i_price) values (%s,%s,%s)""",(i_id,tick_time,indexValue))
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("Pushed to DB")
    time.sleep(5)