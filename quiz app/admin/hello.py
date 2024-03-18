from flask import Flask,render_template,request,url_for, redirect,session
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL, MySQLdb
import math
from pywebio.input import *
from pywebio.output import *

app = Flask(__name__)   

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Irfan@mysql'
app.config['MYSQL_DB']='quezs'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)

app.secret_key="login"

@app.route('/',methods=['GET','POST'])  
def home():
    cur = mysql.connection.cursor()
    cur.execute("select distinct category from question")
    dat = cur.fetchall()
    cur.close()
    

    return render_template('home.html',question=dat)




@app.route('/quiz',methods=['GET','POST'],defaults={'page':1})  
def quiz(page):



    
 

    
    cur = mysql.connection.cursor()
    cur.execute("select * from question limit 1")
    data = cur.fetchall()
    cur.close()

    return render_template('quiz.html',question=data)    






@app.route('/contact',methods=['GET','POST'])  
def contact():

    if(request.method=='POST'):
        naam = request.form['naam']
        email = request.form['email']
        subject = request.form['subject']
        
        

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO register(nam,email,subject) VALUES (%s,%s,%s)",(naam,email,subject))
        mysql.connection.commit()
        cur.close()

    

    return render_template('contact.html')





@app.route('/about')  
def about():
    return render_template('about.html')


#admin login
def logout():
    session.pop('email',None)
    return render_template('index.html')


@app.route('/index',methods=['GET','POST'])  
def index():
    
    
    if(request.method=='POST'):
        username = request.form['username']
        password = request.form['password']
        if(username=="irfan" and password=="irfan@quiz"):
            session['email']=username
            return render_template('main.html',email=username)
        else:
            msg = "invalid username/password"
            return render_template('index.html',msg=msg)    
           


    return render_template('index.html')




@app.route('/main')  
def main():
    cur = mysql.connection.cursor()
    cur.execute("select * from question")
    data = cur.fetchall()
    cur.close()

    return render_template('main.html',question=data)  

   # return render_template('main.html')


@app.route('/cat',methods=['GET','POST'])  
def cat():
    return render_template('cat.html')



@app.route('/question',methods=['GET','POST'])  
def question():

    if(request.method=='POST'):
        category = request.form['category']
        question = request.form['question']
        optiona = request.form['optiona']
        optionb = request.form['optionb']
        optionc = request.form['optionc']
        optiond = request.form['optiond']
        correct = request.form['correct']
        

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO question(category,question,a,b,c,d,correct) VALUES (%s,%s,%s,%s,%s,%s,%s)",(category,question,optiona,optionb,optionc,optiond,correct))
        mysql.connection.commit()
        cur.close()


      
    return render_template('question.html')





if __name__=='__main__':
    app.run(debug=True)