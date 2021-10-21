from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from urllib import parse, request as req


app = Flask(__name__)
CORS(app)


transcendental = {'operation':'/transcendental', 'address':'localhost', 'port':5002, 'route':'/fatorial'}
service_registry = [transcendental]


@app.route('/api_gateway/<operation>')
def api_gateway(operation):
    for service_config in service_registry:
        if service_config['operation'] == ('/'+operation):
            parameters = { 'int_input': request.args.get('int_input')}
            url =f"http://{service_config['address']}:{str(service_config['port'])}{service_config['route']}"
            url_request = req.urlopen(f"{url}?{parse.urlencode(parameters)}")
            result = url_request.read()
            print(url_request)
            return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
