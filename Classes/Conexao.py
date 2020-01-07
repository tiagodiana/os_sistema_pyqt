import MySQLdb
from tkinter import messagebox

class Conexao():
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host='localhost',
                                   user='root',
                                   passwd='1872',
                                   db='os')
            self.cursor = self.conn.cursor()
        except:
            print("Erro ao conectar ao banco de dados")

