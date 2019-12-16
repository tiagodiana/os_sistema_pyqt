import requests
from datetime import datetime


class Ordem():
    id = None
    tipo = None
    marca = None
    num_serie = None
    defeito = None
    solucao = None
    valor = None
    status = None
    nome_cliente = None
    data_entrada = None
    data_saida = None

    def __init__(self):
        pass

    def inserindodados_nova(self,nome_cliente, tipo, marca, num_serie, defeito, solucao, valor):
        self.nome_cliente = nome_cliente
        self.tipo = tipo
        self.marca = marca
        self.num_serie = num_serie
        self.defeito = defeito
        self.solucao = solucao
        self.valor = valor

    def inserindodados_alt(self, id, nome_cliente, tipo, marca, num_serie, defeito, solucao, valor):
        self.id = id
        self.nome_cliente = nome_cliente
        self.tipo = tipo
        self.marca = marca
        self.num_serie = num_serie
        self.defeito = defeito
        self.solucao = solucao
        self.valor = valor

    def novaos(self):
        data = datetime.now()
        data = data.strftime('%Y-%m-%d %H:%M:%S')
        print(data)
        try:
            data = {'nome': self.nome_cliente, 'tipo': self.tipo, 'marca':self.marca, 'num_serie':self.num_serie, 'defeito':self.defeito, 'solucao':self.solucao, 'valor':self.valor}
            req = requests.post('http://localhost/osapp/server/webservice.php', data=data, timeout=3000)

        except:
            return False
            print('Erro na conexão com o banco de dados')

