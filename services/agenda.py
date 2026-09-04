from models.contato import Contato
from data.banco import BancoDB

class Agenda:
    def __init__(self):
        self.repo = BancoDB()
        self.contatos = self.repo.ler_contatos()

    def adicionar(self, contato=None, nome=None, telefone=None, email=None):
        if contato is None:
            contato = Contato(nome, telefone, email)

        if contato in self.contatos:
            print(f"Contato com email '{contato.email}' já existente.")
            return

        self.repo.inserir(contato)        # ← só insere um
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def remover(self, indice):
        if not self.contatos:
            print("[INFO] Nenhum contato cadastrado.")
            return

        if indice < 0 or indice >= len(self.contatos):
            raise IndexError("[ERRO] Índice inválido.")
        
        contato_removido = self.contatos.pop(indice)
        self.repo.remover_por_email(contato_removido.email)  # ← só remove um
        print(f"Contato '{contato_removido.nome}' removido com sucesso!")

    def editar(self, indice, nome=None, telefone=None, email=None):
        if indice < 0 or indice >= len(self.contatos):
            raise IndexError("[ERRO] Índice inválido.")
        
        contato = self.contatos[indice]
        email_original = contato.email   # ← guarda antes de alterar

        if nome:
            contato.nome = nome
        if telefone:
            contato.telefone = telefone
        if email:
            contato.email = email

        for i, c in enumerate(self.contatos):
            if i != indice and c == contato:
                raise ValueError("[ERRO] Contato duplicado.")

        self.repo.atualizar(email_original, contato)  # ← só atualiza um

    def listar(self):
        if not self.contatos:
            print("[INFO] Nenhum contato cadastrado.")
            return
        
        for i, contato in enumerate(self.contatos):
            print(f"{i} - {contato}")

    def buscar(self, termo):
        return [c for c in self.contatos if c.corresponde(termo)]