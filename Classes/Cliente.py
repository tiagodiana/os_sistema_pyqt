import requests
# http://localhost/osapp/server/webservice.php


class Cliente():
    id = ''
    nome = ''
    cpf = ''
    tel = ''
    cel = ''
    rua = ''
    bairro = ''
    cidade = ''
    estado = ''
    cep = ''

    def __int__(self):
        pass

    def limpaMask(self, txt):
        caracteres = ['(', ')', '-', '.', ' ', '\'', '\"']
        dados = ''
        for c in txt:
            if c in caracteres:
                dados += ''
            else:
                dados += c
        return dados

    # INSERINDO DADOS DO CLIENTE
    def inserirdados(self, name, cpf, tel, cel, rua, bairro, cidade, estado, cep):
        self.nome = str(name)
        self.cpf = str(self.limpaMask(cpf))
        self.tel = str(self.limpaMask(tel))
        self.cel = str(self.limpaMask(cel))
        self.rua = str(rua)
        self.bairro = str(bairro)
        self.cidade = str(cidade)
        self.estado = str(self.limpaMask(estado))
        self.cep = str(self.limpaMask(cep))

    def inserirdadosid(self,id, name, cpf, tel, cel, rua, bairro, cidade, estado, cep):
        self.id = id
        self.nome = name
        self.cpf = self.limpaMask(cpf)
        self.tel = self.limpaMask(tel)
        self.cel = self.limpaMask(cel)
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = self.limpaMask(estado)
        self.cep = self.limpaMask(cep)

    # FUNÇÃO PARA CADASTRAR CLIENTE
    def caduser(self):
        try:
            data = {'tipo': 'inserir', 'nome': self.nome, 'cpf': self.cpf, 'telefone': self.tel, 'celular':self.cel, 'rua': self.rua, 'bairro':self.bairro, 'cidade':self.cidade, 'estado':self.estado, 'cep':self.cep}
            req = requests.post('http://localhost/osapp/server/webservice.php', data=data, timeout=3000)
            if int(req.text) > 0:
                return True
            else:
                return False
        except:
            return False
            print('Erro na conexão com o banco de dados')

    def buscauser(self, cpf):
        try:
            data = {'tipo': 'buscar_user', 'cpf': self.limpaMask(cpf)}
            req = requests.post('http://localhost/osapp/server/webservice.php', data=data, timeout=3000)
            json = req.json()
            return json
        except:
            return False
            print('Erro na conexão com o banco de dados')

    def alterarcliente(self):
        try:
            data = {'tipo': 'alterar_user', 'nome': self.nome, 'cpf': self.cpf, 'telefone': self.tel, 'celular': self.cel, 'rua': self.rua, 'bairro': self.bairro, 'cidade': self.cidade, 'estado': self.estado, 'cep': self.cep, 'id': self.id}
            req = requests.post('http://localhost/osapp/server/webservice.php', data=data, timeout=3000)
            if int(req.text) > 0:
                return True
            else:
                return False
        except:
            return False
            print('Erro na conexão com o banco de dados')