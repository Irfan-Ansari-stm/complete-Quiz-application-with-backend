from flask import Flask,render_template,request,url_for, redirect,session
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL, MySQLdb
import math


app = Flask(__name__)   

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Irfan@mysql'
app.config['MYSQL_DB']='learncity'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)

app.secret_key="login"


@app.route('/',methods=['GET','POST'])  
def index():
    cur = mysql.connection.cursor()
    cur.execute("select * from courses")
    dat = cur.fetchall()
    cur.close()
    

    return render_template('index.html',question=dat)


if __name__=='__main__':
    app.run(debug=True)    