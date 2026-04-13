from models.contato import Contato
from data.arquivo import ArquivoCSV

class Agenda:
    def __init__(self):
        self.repo = ArquivoCSV()
        self.repo.verificar_e_corrigir_cabecalho()
        self.contatos = self.repo.ler_contatos()

    def adicionar(self, contato=None, nome=None, telefone=None, email=None):
        if contato is None:
            contato = Contato(nome, telefone, email)

        if contato in self.contatos:
            print(f"Contato com email '{contato.email}' já existente.")
            return

        self.contatos.append(contato)
        self.repo.salvar_contatos(self.contatos)
        print("Contato adicionado com sucesso!")