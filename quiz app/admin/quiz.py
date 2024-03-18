from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH



app = Flask(__name__)


def quiz():

    

    c = 0
    name = input("Enter your name", type="text")
    
    q1 = radio("What is the PH of H2O?",["6", "7", "8", "9"])
    

    if q1 == "7":
        c += 1
    
    
    q2 = radio(" Which of the following gas is reduced in the reduction process?", ["Oxygen", "Helium", "Carbon", "Hydrogen"])
    

    if q2 == "Hydrogen":
        c += 1
    q3 = radio("Who invented Java Programming?", ["Guido Van Rossum", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup"])
    

    if q3 == "James Gosling":
        c += 1
    q4 = radio("What is the extension of java code files?", [".js", ".txt", ".class", ".java"])

    if q4 == ".java":
        c += 1

    q5 = radio(" Which type of Programming does Python support?", ["object-oriented programming", "structured programming", "functional programming", " all of the mentioned"])

    if q5 == " all of the mentioned":
        c += 1    

    if c > 4:
        put_text(name+" your score is "+str(c))
        style(put_text("Result : passed"), "color:green")
    else:
        put_text(name + "your score is "+str(c))
        style(put_text("Result : failed"), "color:red")

    put_text("thanks for your participation")









app.add_url_rule('/', 'webio_view', webio_view(quiz),
                 methods=['GET', 'POST', 'OPTIONS'])



app.run(host="localhost", port=5000)
