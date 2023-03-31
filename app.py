# Impotação das bibliotecas
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

# Instancía o FLask
app = Flask(__name__)

# Função que pega os valores da tabela do arquivo db e retorna os jogos
def getTable():
    db = sqlite3.connect("JOGO.db")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM jogo')
    rows = cursor.fetchall()
    db.close()

    # Armazena os valores das características dos jogos presentes na tabela
    games = []
    for row in rows:
        game = {}
        game['nome'] = row[0]
        game['plataforma'] = row[1]
        game['preco'] = row[2]
        game['quantidade'] = row[3]
        games.append(game)
    print(games)
    return games

# Rota para a página principal
@app.route("/", methods=['GET'])
# Retorna os jogos da tabela para uma página html
def GamePage():
    games = getTable()
    return render_template(
        "index.html",
        games=games,
        )

# Rota para adicionar os jogos
@app.route("/postGame", methods=['POST'])
# Função que posta na tabela os valores fornecidos no formulário
def addGame():
    nm = request.form["nome"]
    pl = request.form["plataforma"]
    pr = request.form["preco"]
    qt = request.form["quantidade"]
    
    db = sqlite3.connect("JOGO.db")
    cursor = db.cursor()
    cursor.execute('INSERT INTO jogo (nome,plataforma,preco,quantidade) VALUES (?,?,?,?)', (nm, pl, pr, qt))
    db.commit()
    db.close()

    return redirect(url_for('GamePage'))

# Roda a api
if __name__ == "__main__":
    app.run(debug=True)