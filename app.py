
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





if __name__ == '__main__':
    app.run(debug=True)