import re

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome} | {self.telefone} | {self.email}"
    
    def __repr__(self):
        return f"Contato('{self.nome}', '{self.telefone}', '{self.email}')"
    
    def __eq__(self, outro):
        if not isinstance(outro, Contato):
            return False
        return self.email.lower() == outro.email.lower()

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("Nome não pode ser vazio!")
        self.__nome = valor

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, valor):
        limpo = re.sub(r'\D', '', valor)
        if len(limpo) < 10 or len(limpo) > 11:
            raise ValueError("Telefone Inválido!")
        self.__telefone = limpo

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", valor):
            raise ValueError("Email inválido!")
        self.__email = valor.lower()

    def to_dict(self):
        return{
            'nome':self.nome,
            'telefone':self.telefone,
            'email':self.email
        }