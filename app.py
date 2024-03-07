from flask import Flask, render_template, request, redirect, url_for
from requisicoes import *

app = Flask(__name__)

#Rotaas do site

@app.route('/')
def index():
    return render_template('./template/html/main.html')

@app.route('/login')
def login():
    return render_template('./template/html/login.html')

@app.route('/register')
def register():
    return render_template('./template/html/register.html')

@app.route('/evento')
def eventos():
    return render_template('./template/html/eventos.html')

@app.route('/Bazar')
def bazar():
    return render_template('./template/html/bazar.html')

@app.route('/faca_parte')
def faca_parte():
    return render_template('./template/html/faca_parte.html')

@app.route('/historia_para_contar')
def historia_para_contar():
    return render_template('./template/html/historia_para_contar.html')



if __name__ == '__main__':
    app.run(debug=True)