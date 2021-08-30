
from models import create_course
from flask import Flask, render_template, url_for, request



app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("tela1.html")

@app.route('/tela2' , methods = ['GET%', 'POST'])
def register_page():
    if request.method == 'POST':
        nome_curso = request.form.get('nome_curso')
        nome_facilitaor = request.form.get('nome_facilitador')
        link = request.form.get('link')
        info = request.form.get('info')
        valor = request.form.get('valor')
        validacao = request.form.get('validacao')
        create_course(nome_curso, nome_facilitaor, link, info, valor, validacao)
        
    return render_template("tela2.html")

@app.route('/tela3')
def feed():
    return render_template("tela3.html")

@app.route('/tela4')
def publication_effected():
    return render_template("tela4.html")
    

if __name__ == "__main__":
    app.run(debug=True)