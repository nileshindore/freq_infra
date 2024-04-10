import random
import datetime
import time
import redis
import mysql.connector
import os

mysqlHost = os.environ['MYSQL_HOST']
redisHost = os.environ['REDIS_HOST']

class calcStockPrice:
    def __init__(self,sname,minprice,maxprice):
        self.sname = sname
        self.minprice = minprice
        self.maxprice = maxprice
    
    def calcPrice(self):
        while 2>1:
            stockPrice = random.randint(self.minprice,self.maxprice)
            tick_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            msg = "{},{},{}".format(self.sname , stockPrice , tick_time)
            #print(msg)
            r = redis.Redis(host=redisHost)
            r.set(self.sname,stockPrice)
            mydb = mysql.connector.connect(host=mysqlHost,user='root',passwd='root',db='BHARATINDEX')   
            mycursor = mydb.cursor()
            query = "select s_id from s_detail where s_name='%s'" % (self.sname)
            mycursor.execute(query)
            s_id = list(mycursor.fetchone())
            query = "insert into s_price values ('%s','%s',%i)" % (s_id[0], tick_time, stockPrice)
            mycursor.execute(query)
            mydb.commit()
            mycursor.close()
            mydb.close()
            time.sleep(10)