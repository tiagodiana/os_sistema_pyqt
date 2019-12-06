from Classes.Conexao import Conexao


# CLASSE CLIENTE HERDA A CLASSE CONEXAO
class Cliente(Conexao):
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
        Conexao.__init__(self)

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
        self.nome = name
        self.cpf = self.limpaMask(cpf)
        self.tel = self.limpaMask(tel)
        self.cel = self.limpaMask(cel)
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = self.limpaMask(estado)
        self.cep = self.limpaMask(cep)

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
            sql = 'INSERT INTO clientes VALUES(null,%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            self.cursor.execute(sql, (
                self.nome, self.cpf, self.tel, self.cel, self.rua, self.bairro, self.cidade, self.estado, self.cep))
            self.conn.commit()
            self.conn.close()
            return True

        except:
            return False

    def buscauser(self, cpf):
        self.cpf = self.limpaMask(cpf)
        try:
            if cpf != "":
                sql = 'SELECT * FROM clientes WHERE cpf LIKE %s'
                self.cursor.execute(sql % self.cpf)
                result = self.cursor.fetchone()
                self.conn.close()
                return result
            else:
                return False
        except:
            print("ERRO NA BUSCA")
            return False

    def alterarcliente(self):
        try:
            sql = 'UPDATE clientes SET nome = %s, cpf = %s, telefone = %s, celular = %s, rua = %s, bairro = %s, cidade = %s, estado = %s, cep = %s WHERE id = %s'
            self.cursor.execute(sql, (self.nome, self.cpf, self.tel, self.cel, self.rua, self.bairro, self.cidade, self.estado, self.cep, int(self.id)))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            print('Erro ao atualizar')
            return False
