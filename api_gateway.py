from flask import Flask, request
from flask_cors import CORS
from urllib import parse, request as req

import requests

app = Flask(__name__)
CORS(app)

transcendental = {'operation':'/transcendental', 'address':'localhost', 'port':5002, 'route':'/fatorial'}
soma           = {'operation':'/soma', 'address':'localhost', 'port':5001, 'route':'/soma'}
subtracao      = {'operation':'/subtracao', 'address':'localhost', 'port':5001, 'route':'/subtracao'}
multiplicacao  = {'operation':'/multiplicacao', 'address':'localhost', 'port':5001, 'route':'/multiplicacao'}
divisao        = {'operation':'/divisao', 'address':'localhost', 'port':5001, 'route':'/divisao'}

service_registry = [transcendental, soma, subtracao, multiplicacao, divisao]


@app.route('/api_gateway/<operation>')
def api_gateway(operation):
    print(operation)
    for service_config in service_registry:
        if service_config['operation'] == ('/'+operation):
            if operation == "transcendental":
                parameters = { 'arg1': request.args.get('arg1') }
                url =f"http://{service_config['address']}:{str(service_config['port'])}{service_config['route']}"
                url_request = req.urlopen(f"{url}?{parse.urlencode(parameters)}")
                result = url_request.read()
                persistenceBD(operation, 'fatorial', str(parameters['arg1']))
                return result
            parameters = { 'arg1': request.args.get('arg1'), 'arg2': request.args.get('arg2') }
            url =f"http://{service_config['address']}:{str(service_config['port'])}{service_config['route']}"
            url_request = req.urlopen(f"{url}?{parse.urlencode(parameters)}")
            result = url_request.read()
            persistenceBD('Elementar', operation, str(parameters['arg1'])+' & '+str(parameters['arg2']))
            return result

def persistenceBD(tipo_oper, operacao, args):
    parameters = { 'tipo_oper': tipo_oper, 'operacao': operacao, 'args': args }
    res = requests.post('http://localhost:5003/cadastrar', json=parameters)

    if res.status_code == 200:
        print('Success!')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
