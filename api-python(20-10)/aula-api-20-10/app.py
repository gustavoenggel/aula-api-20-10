#desenvolver um back end com api - 
#postman - teste http -> verificar respostas da API
#1. Objetivo
#2. URLBASE
#3. ENDPOINTS
#4. RECURSOS DISPONIBILIZADOS

#CRIAR UMA API:
"""
1. CONSULTAR
2. CRIAR
3. EDITAR
4. EXCLUIR
"""

from flask import Flask,jsonify,request

app = Flask(__name__)
#app -> Apresenta a aplicação flask
#Name Identifica que o modulo da aplicação

livros = [
    {"id": 1,
    "Titulo": "Brawl Stars",
    "autor": "G.G.Engel"
    },
    {"id": 2,
     "Titulo": "Red Dead Redemption",
     "autor": "A. Morgan"
     },
    {"id": 3,
     "Titulo": "Resident Evil",
     "autor": "L. S. Kennedy"
     },
    { "id": 4,
      "Titulo": "The Witcher",
        "autor": "G. of Rivia"
    },
    { "id": 5,
    "Titulo": "God of War",
        "autor": "K. of Sparta" 
        },
    { "id": 6,
      "Titulo": "Uncharted",
        "autor": "N. Drake" 
        },
    { "id": 7,
      "Titulo": "Halo",
        "autor": "J. Master Chief" 
        },
    { "id": 8,
      "Titulo": "Assassin's Creed",
        "autor": "E. Auditore" 
        },
    { "id": 9,
      "Titulo": "The Last of Us",
        "autor": "J. Miller" 
        },
    { "id": 10,
      "Titulo": "Tomb Raider",
        "autor": "L. Croft" 
        }

]

#Consultar todos os livros
def obter_livros():
    return jsonify(livros)

#criar as rotas
#a rota foi especificada para o método GET, que é utilizado para consultar os dados da API
@app.route("/livros",methods = ["GET"])
def obter_livros():
    return jsonify(livros)

#Criar as rotas/livrosid
@app.route("/livros/<int:id>",methods = ["GET"])
#<int:> Indica Inteiro
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)

        return jsonify("message:Livro não encontrado"),404







#PUT -> primeiro, os dados enviados serao obtidos
@app.route("/livros/<int:id>",methods = ["PUT"])
def editar_livro_por_id(id):
    #permite acessar os dados json ennviados no corpo da requisição

    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#CRIAÇÃO DE UM NOVO LIVRO
#decorador de rota 
@app.route("/livros",methods = ["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route("/livros/<int:id>",methods = ["DELETE"])
def excluir_livro(id):
    #remove pelo id
    #enumerate()
    for indice,livro in enumerate(livros):
        if livro.get("id")==id:
            livros.pop(indice)
            return jsonify(livros)
        










#INICIALIZAÇÃO DO SERVIDOR LOCAL
app.run(
    host="localhost",
    port=5000,
    debug=True

)