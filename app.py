from requests import request 
from flask import Flask, request, Response
from flask_restful import Api

from src.lib.cors import build_cors_response

from src.scripts.AnalisePorCliente import analise_por_cliente
from src.scripts.AnalisePorAssessor import analise_por_assessor


app = Flask(__name__)


api = Api(app)

class Main():

    @app.route("/api/v1/Query/AnalisePorCliente", methods=["GET"])       
    def analise_por_cliente(*self):
        if 'Access-Token' not in request.headers.keys(): return Response("Token não informado", 400, mimetype='text/plain')
        if 'User-Id' not in request.headers.keys(): return Response("Id não informado", 400, mimetype='text/plain')        
        token: str = request.headers.get('Access-Token')
        id_user: str = request.headers.get('User-Id')
    
        worker: analise_por_cliente = analise_por_cliente()

        return worker.analise_cliente(token, id_user)


    @app.route("/api/v1/Query/AnalisePorAssessor", methods=["GET"])       
    def analise_por_assessor(*self):
        if 'Access-Token' not in request.headers.keys(): return Response("Token não informado", 400, mimetype='text/plain')       
        token: str = request.headers.get('Access-Token')
        worker: analise_por_assessor = analise_por_assessor()

        return worker.analise_assessor(token)

    @app.after_request
    def AfterRequest(response: Response):
        return build_cors_response(response)

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=2000)