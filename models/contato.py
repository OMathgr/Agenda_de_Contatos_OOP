class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome} | {self.telefone} | {self.email}"
    
    def __repr__(self):
        return f"Contato('{self.nome})', '{self.telefone}', '{self.email}')"
    
    def __eq__(self, outro):
        return self.email.lower() == outro.email.lower()
