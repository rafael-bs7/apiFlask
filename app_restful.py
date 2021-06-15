
from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json


app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'nome': 'Rafael',
     'habilidades':['Python', 'Flask']},
    {'nome': 'Joao',
     'habilidades':['Python', 'Django']}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'ERRO', 'mensagem': 'Desenvolvedor de ID não existe' }
        except Exception as e:
            response = {'Erro': e}
        return response
    
    def put(self,id):
        dados =json.loads(request.data)
        desenvolvedores[id] = dados
        return desenvolvedores
    def delete(self):
        dados =json.loads(request.data)
        desenvolvedores[id] = dados
        return desenvolvedores

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    




api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/lista/')
api.add_resource(Habilidades, '/habilidades/')
if __name__=="__main__":
    app.run(debug=True)