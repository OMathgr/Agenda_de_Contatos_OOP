import csv
from models.contato import Contato

class Agenda:
    def __init__(self):
        self.contatos = []

    def carregar(self, arquivo):
        with open (arquivo, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                self.contatos.append(
                    Contato(linha['nome'], linha['telefone'], linha['email'])
                )