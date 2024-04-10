import random
import mysql.connector
import numpy as np
from io import StringIO
from io import BytesIO

from flask import Flask, make_response, redirect
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import os

mysqlHost = os.environ['MYSQL_HOST']

app = Flask(__name__)

@app.route('/')
def indexpage():
    return redirect("/plot.png")

@app.route('/plot.png')
def plot():    
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    mydb = mysql.connector.connect(host=mysqlHost,user='root',passwd='root',db='BHARATINDEX') 
    mycursor = mydb.cursor()
    query = "select i_ttime,i_price from (select i_ttime,i_price from i_price ORDER BY i_ttime DESC LIMIT 10 )var1 ORDER BY i_ttime"
    mycursor.execute(query)
    index_time = list()
    index_price = list()
    for t,p in mycursor.fetchall():
        dt = str(t).split(" ")
        time = dt = str(t).split(":")
        index_time.append(str(dt[2]))
        index_price.append(p)
    
    xs = index_time
    ys = index_price

    '''
    for i in mycursor.fetchall():
        dt = str(i[0]).split(" ")
        index_time.append(dt[1])
    xs = index_time

    mydb = mysql.connector.connect(user='root',passwd='root',db='BHARATINDEX') 
    mycursor = mydb.cursor()
    query = "select i_price from i_price LIMIT 50"
    mycursor.execute(query)
    index_price = list()
    for i in mycursor.fetchall():
        index_price.append(i[0])
    #i_price = np.log(index_price)
    ys = index_price
    '''

    #axis.plot(xs, ys)
    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')