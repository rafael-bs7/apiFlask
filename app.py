
from flask import Flask, jsonify, request
import json
app = Flask(__name__)


@app.route("/<id>")
def my_api(id):
    return jsonify({'id':id,'nome': 'Rafael'})


@app.route("/soma",methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma': total})


desenvolvedores = [
    {'nome': 'Rafael',
     'habilidades':['Python', 'Flask']},
    {'nome': 'Joao',
     'habilidades':['Python', 'Django']}
]

@app.route("/dev/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method =='GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'ERRO', 'mensagem': 'Desenvolvedor de ID não existe' }
        except Exception as e:
            reponse={'Erro': e}
        return jsonify(response)
    elif request.method=='PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados 
        return jsonify(desenvolvedores)
    elif request.method== 'DELETE':
        desenvolvedores.pop(id)
        return jsonify(desenvolvedores)
        











if __name__ == '__main__':
    app.run(debug=True)