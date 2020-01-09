import requests
from datetime import datetime


class Ordem():
    url = 'http://localhost/sistema_os/server/webservice.php'

    id = None
    tipo = None
    marca = None
    modelo = None
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

    def inserindodados_nova(self,nome_cliente, tipo, marca, modelo, num_serie, defeito, solucao, valor):
        self.nome_cliente = nome_cliente
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.num_serie = num_serie
        self.defeito = defeito
        self.solucao = solucao
        self.valor = valor

    def inserindodados_alt(self, id, tipo, marca, modelo, num_serie, defeito, solucao, valor):
        self.id = id
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.num_serie = num_serie
        self.defeito = defeito
        self.solucao = solucao
        self.valor = valor

    def inserirId(self, id):
        self.id = id

    def novaos(self):
        data = datetime.now()
        data = data.strftime('%Y-%m-%d %H:%M:%S')
        print(data)
        try:
            data = {'tipo':'nova_os', 'nome': self.nome_cliente, 'hardware': self.tipo, 'marca':self.marca,'modelo':self.modelo, 'num_serie':self.num_serie, 'defeito':self.defeito, 'solucao':self.solucao, 'valor':self.valor}
            req = requests.post(self.url, data=data, timeout=3000)
            if int(req.text) > 0:
                return True
            else:
                return False
        except:
            print('Erro de Conexão com o banco de dados')
            return False
            
    def buscaros(self):
        try:
            data = {'tipo': 'buscar_os', 'id_os':self.id}
            req = requests.post(self.url, data=data, timeout=3000)
            json = req.json()
            return json
        except:
            print("Erro na conexão com banco de dados")
            return False

    def alteraros(self):
        try:
            data = {'tipo': 'alterar_os','id_os':self.id, 'hardware':self.tipo, 'marca':self.marca, 'modelo':self.modelo, 'num_serie':self.num_serie, 'defeito':self.defeito, 'solucao':self.solucao, 'valor':self.valor}
            req = requests.post(self.url, data=data, timeout=3000)
            print(req.text)
            if int(req.text) > 0:
                return True
            else:
                return False
        except:
            print("Erro na conexão com banco de dados")
            return False

    def deletaros(self):
        try:
            data = {'tipo':'deletar_os', 'id_os':self.id}
            req = requests.post(self.url, data=data, timeout=3000)
            if int(req.text) > 0:
                return True
            else:
                return False
        except:
            print("Erro na conexão com banco de dados")
            return False

    def finalizaros(self):
        try:
            data = {'tipo':'finalizar_os', 'id_os':self.id}
            req = requests.post(self.url, data=data, timeout=3000)
            if int(req.text) > 0:
                return True
            else:
                return False
        except:
            print("Erro na conexão com o banco de dados")
            return False
            
            