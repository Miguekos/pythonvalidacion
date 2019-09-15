import os
from flask import Flask, render_template, request, jsonify
from dataSetGenerator import indentificar

app = Flask(__name__)

# Home apge
@app.route('/', methods=['GET'])
def home_page():
    return 'Micro servicio para resolver indentificar'


@app.route('/indentificar/<int:tipo>/<int:id>', methods=['GET', 'POST'])
def multas(tipo, id):
    if tipo == 1:
        if request.method == 'POST':
            try:
                json = request.get_json()
                # print(json)
                json_forma = json['base']
                x = json_forma.split(',', 1)
                x_base = x[1]
                result = jsonify(indentificar(x_base, tipo, id))
                return result
            except:
                json = request.get_json()
                json_forma = json['base']
                result = jsonify(indentificar(json_forma, tipo, id))
                return result
    elif tipo == 2:
        if request.method == 'POST':
            try:
                json = request.get_json()
                # print(json)
                json_forma = json['base']
                x = json_forma.split(',', 1)
                x_base = x[1]
                result = jsonify(indentificar(x_base, tipo, id))
                return result
            except:
                json = request.get_json()
                json_forma = json['base']
                result = jsonify(indentificar(json_forma, tipo, id))
                return result
    else:
        return 'Tipo incorrecto'
        # return todas(json_forma)


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', debug=True)
