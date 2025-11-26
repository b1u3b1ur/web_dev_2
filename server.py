from flask import Flask, redirect, url_for, session, request, render_template
import generador_de_contraseñas
import os

folder = os.getcwd()
app = Flask(__name__,template_folder=folder,static_folder=folder)

def first():
    global v_1, v_2
    if request.method == 'POST':
        v_1 = request.form["generate"]
        v_2 = request.form["long"]
    return render_template('dw2.html', value = 'Omg')

def second():
    if v_1 == '1':
        a = generador_de_contraseñas.gen(v_1,v_2)
        return render_template('sec.html', data = a)
    else:
        a = generador_de_contraseñas.cargar()
        return render_template('sec.html', data = a)

app.config['SECRET_KEY']= 'Shhhh'
app.add_url_rule('/', 'first', first, methods=['GET','POST'])
app.add_url_rule('/sec','second',second)
# app.add_url_rule('/test','test',test)
# app.add_url_rule('/result','result',result)
app.run()