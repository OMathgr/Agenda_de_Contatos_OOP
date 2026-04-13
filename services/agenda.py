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

    def listar(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
            return
        
        for i, contato in enumerate(self.contatos):
            print(f"{i} - {contato}")

    def remover(self, indice):
        if not self.contatos:
            print ("Nenhum contato cadastrado.")
            return

        if indice < 0 or indice >= len(self.contatos):
            print("Número inválido.")
            return
        
        contato_removido = self.contatos.pop(indice)
        self.repo.salvar_contatos(self.contatos)

        print(f"Contato '{contato_removido.nome}' removido com sucesso!")

    def buscar(self, termo):
        return [c for c in self.contatos if c.corresponde(termo)]