import mysql . # iMPORTANDO a Biblioteca do connector do MySQL
from mysql.connector import Error # IMPORTANDO a classe Error para tratar as mensagens de erro do código
from dotenv import load_dotenv # IMPORTANDO a função load_dotenv
from os import getenv

import mysql.connector # IMPORTANDO a função getenv

class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv('DB_HOST')
        self.username = getenv('DB_USER')
        self.password = getenv('DB_PSWD')
        self.database = getenv('DB_NAME')
        self.connection = None # Inicialização da conexão 
        self.cursor = None # Inicialização do cursor

    def conectar(self):
        """Estabelece uma conexão com o banco de dados."""
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                database = self.database

            )
