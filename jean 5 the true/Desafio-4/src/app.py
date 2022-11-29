from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
import rotas
import conexao

if __name__ == "__main__":
  app.run(debug=True)