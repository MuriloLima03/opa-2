from __main__ import app
from flask_mysqldb import MySQL

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '4321' #Insira aqui a senha do seu servidor local do MYSQL
app.config['MYSQL_DB'] = 'contatos'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

def insere_usuario(form):
  cur = mysql.connection.cursor()
  cur.execute(f"insert into usuarios (email_usuario, assunto_usuario, descricao_usuario) values (%s, %s, %s)", (form["email"], form["assunto"], form["descricao"]))
  mysql.connection.commit()
  cur.close()
  return None

def retorna_usuarios():
  cur = mysql.connection.cursor()
  cur.execute("select * from usuarios")
  usuarios = cur.fetchall()
  cur.close()
  return usuarios