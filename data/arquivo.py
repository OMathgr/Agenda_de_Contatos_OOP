import csv
import os
from models.contato import Contato

class ArquivoCSV:
    CAMPOS = ['nome', 'telefone', 'email']

    def __init__(self, nome_arquivo='Contatos.csv'):
        self.nome_arquivo = nome_arquivo

    #Verificação e correção de cabeçalho
    def verificar_e_corrigir_cabecalho(self):
        if not os.path.exists(self.nome_arquivo) or os.path.getsize(self.nome_arquivo) == 0:
            return
    
        with open (self.nome_arquivo, mode= 'r', encoding= 'utf-8') as f:
            primeira_linha = f.readline().strip()
            resto = f.read()

        cabecalho_esperado = ','.join(self.CAMPOS)

        if primeira_linha != cabecalho_esperado:
            print("Cabeçalho incorreto detectado, corrigindo...")
            with open (self.nome_arquivo, mode= 'w', encoding= 'utf-8') as f:
                f.write(cabecalho_esperado + '\n')
                f.write(resto.lstrip('\n'))
            print("Cabeçalho corrigido!")

    #Ler Contatos
    def ler_contatos(self):
        contatos = []

        try:
            with open (self.nome_arquivo, mode='r', encoding='utf-8') as arquivo:
                leitor = csv.DictReader(arquivo)

                for linha in leitor:
                    if linha.get('nome'):
                        contato = Contato(
                            linha['nome'],
                            linha['telefone'],
                            linha['email']
                        )
                        contatos.append(contato)

        except FileNotFoundError:
            pass
    
        return contatos
    
    #Salvar Contatos
    def salvar_contatos(self, contatos):
        with open (self.nome_arquivo, mode='w', encoding= 'utf-8', newline='') as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=self.CAMPOS)
            writer.writeheader()

            for contato in contatos:
                writer.writerow(contato.to_dict())