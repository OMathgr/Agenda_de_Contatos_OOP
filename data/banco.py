import sqlite3
from models.contato import Contato

class BancoDB:

    def __init__(self, nome_arquivo='Contatos.db'):
        self.nome_arquivo = nome_arquivo
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.nome_arquivo) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS contatos (
                    id       INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome     TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    email    TEXT NOT NULL UNIQUE
                )
            """)
        
    #Ler Contatos
    def ler_contatos(self):
        with sqlite3.connect(self.nome_arquivo) as conn:
            cursor = conn.execute("SELECT nome, telefone, email FROM contatos")
            return [Contato(row[0], row[1], row[2]) for row in cursor.fetchall()]
    
    #Salvar Contatos
    def salvar_contatos(self, contatos):
        with sqlite3.connect(self.nome_arquivo) as conn:
            conn.execute("DELETE FROM contatos")
            conn.executemany(
                "INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)",
                [(c.nome, c.telefone, c.email) for c in contatos]
            )

    #Addicionar Contatos
    def inserir(self, contato):
        with sqlite3.connect(self.nome_arquivo) as conn:
            conn.execute(
                "INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)",
                (contato.nome, contato.telefone, contato.email)
        )

    #Remover Contatos
    def remover_por_email(self, email):
        with sqlite3.connect(self.nome_arquivo) as conn:
            conn.execute(
                "DELETE FROM contatos WHERE email = ?",
                (email,)
            )

    #Atualizar Contatos
    def atualizar(self, email_original, contato):
        with sqlite3.connect(self.nome_arquivo) as conn:
            conn.execute(
                "UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE email = ?",
                (contato.nome, contato.telefone, contato.email, email_original)
            )