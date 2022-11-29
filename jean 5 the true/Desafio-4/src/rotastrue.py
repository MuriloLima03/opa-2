from __main__ import app
from flask import Flask, render_template, request
import conexao

@app.route("/")
@app.route("/home")
def index():
  return render_template("index.html")

@app.route("/quem_somos")
def quem_somos():
  return render_template("quem-somos.html")

@app.route("/contatos", methods = ["GET", "POST"])
def contatos():
  if request.method == "POST":
    form = request.form
    conexao.insere_usuario(form)
    return render_template("contatos.html")
  else:
    return render_template("contatos.html")

@app.route("/usuarios")
def usuarios():
  usuarios = conexao.retorna_usuarios()
  return render_template("usuarios.html", usuarios = usuarios)