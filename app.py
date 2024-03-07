from flask import Flask, render_template, request, redirect, url_for
from requisicoes import *

app = Flask(__name__, static_url_path='/static')

#Rotaas do site

@app.route('/')
def index():
    return render_template('/main.html')

@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/submit_login')
def login_submit():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email, password)


@app.route('/register')
def register():
    return render_template('/register.html')

@app.route('/evento')
def eventos():
    return render_template('/eventos.html')

@app.route('/Bazar')
def bazar():
    return render_template('/bazar.html')

@app.route('/faca_parte')
def faca_parte():
    return render_template('/faca_parte.html')

@app.route('/historias')
def historia_para_contar():
    return render_template('/historias.html')



if __name__ == '__main__':
    app.run(debug=True)