from flask import Flask, request, jsonify
import requests
import pprint
import json

server = Flask(__name__)

@server.get('/pessoas')
def pegar_pessoas():
    return 'Programaticamente falando'


@server.route('/moedas/', methods=["GET"])
def pegar_valores():
    # try:
        # if not "from" in request.url and not "to" in request.url and not "amount" in request.url:
        #     return "Fora dos parametros legais exigidos!!! "
        # else:
            moeda_nome_origem = request.args.get('from')
            moeda_nome_convertido = request.args.get('to')
            moeda_valor = request.args.get('amount')

            print(moeda_nome_origem)

            retorno_api = consulta_api_externa(2, 'https://economia.awesomeapi.com.br/json/all')

            valor_moeda_api = retorno_api[moeda_nome_origem]["high"]
            # print(type(valor_moeda_api))
            # return valor_moeda_api
            # exit
            print(round(float(valor_moeda_api), 2))
            valor_moeda_convertido_real = float(valor_moeda_api) * float(moeda_valor)

            # if "BRL" in moeda_nome_convertido:
            # valor_moeda_convertido_real * valor_moeda_api_converte
            return jsonify({"from": moeda_nome_origem, "to": moeda_nome_convertido, "amount": moeda_valor, "totalConvertido":  valor_moeda_convertido_real})
            # else:
                # valor_moeda_api_converte = retorno_api[moeda_nome_convertido]["high"]
                # valor_moeda_convertido_real * valor_moeda_api_converte
                # return jsonify({"from": moeda_nome_origem, "to": moeda_nome_convertido, "amount": moeda_valor, "totalConvertido":  valor_moeda_convertido_real * valor_moeda_api_converte})
    # except:
    #     return jsonify({"ERRO": 'Erro nos parametros informados'})


def consulta_api_externa(tempoIntervalo, url):
    try:
        moeda = requests.get(url)
        buscar = json.loads(moeda.text)
        if moeda.status_code == 200:
            return buscar
        else:
            return -1
    except:
        return -1

server.run(debug=True)