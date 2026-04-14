from services.agenda import Agenda

def adicionar_contato(agenda):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    try:
        agenda.adicionar(nome=nome, telefone=telefone, email=email)
    except ValueError as e:
        print(f"[ERRO] {e}")

def buscar_contato(agenda):
    nome = input("Digite o nome para a busca: ").strip()
    resultados = agenda.buscar(nome)

    if not resultados:
        print("[INFO] Nenhum contato encontrado.")
    else:
        print("\nResultados:")
        for i, contato in enumerate(resultados):
            print(f"{i} - {contato}")

def excluir_contato(agenda):
    if not agenda.contatos:
        print("[INFO] Nenhum contato disponível.")
        return
    
    agenda.listar()

    try:
        indice = int(input("Número do contato para remover: "))
        contato = agenda.contatos[indice]

        confirmar = input(f"Remover '{contato.nome}'? (s/n): ").strip().lower()

        if confirmar in ['s', 'sim']:
            agenda.remover(indice)
                
        else:
            print("Cancelado.")

    except (ValueError, IndexError):
        print("[ERRO] Entrada inválida.")

def main():
    agenda = Agenda()

    while True:
        print("\n--- Menu ---")
        print("1 - Listar contatos")
        print("2 - Adicionar Contato")
        print("3 - Buscar Contato")
        print("4 - Remover Contato")
        print("5 - Sair")

        try:
            escolha = int(input("Digite o número da opção desejada: ").strip())
            if escolha <= 0 or escolha > 5:
                print("[ERRO] Número inválido.")
                continue

            #Listar
            if escolha == 1:
                agenda.listar()

            #Adicionar
            elif escolha == 2:
                adicionar_contato(agenda)

            #Buscar
            elif escolha == 3:
                buscar_contato(agenda)

            #Excluir
            elif escolha == 4:
                excluir_contato(agenda)
                
            #Encerrar
            elif escolha == 5:
                print("Saindo...")
                break

        except ValueError:
            print("[ERRO] Entrada inválida. Digite apenas números.")
            continue

#Main
if __name__ == "__main__":
    main()