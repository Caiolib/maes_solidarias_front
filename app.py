from flask import Flask, render_template, request, redirect, url_for, make_response
from requisicoes import *

app = Flask(__name__, static_url_path='/static')

#Rotaas do site

@app.route('/')
def index():
    return render_template('/main.html')

@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/submit_login', methods=['POST', 'GET'])
def login_submit():
    if request.method == 'POST':
        response = login_user(request.form)
        if response['Authorization']:
            token = response['Authorization']
            response = make_response("<meta http-equiv='refresh' content='0;url=/' />")
            response.set_cookie('Authentication', value=f"Bearer {token}", httponly=True)
            return response
        else:
            redirect('/login')
    return redirect('/')


@app.route('/register')
def register():
    return render_template('/register.html')

@app.route('/evento')
def eventos():
    return render_template('/eventos.html')

@app.route('/bazar')
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