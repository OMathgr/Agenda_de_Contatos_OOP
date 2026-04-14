from services.agenda import Agenda

def main():
    agenda = Agenda()


    while True:
            print("\n--- Menu: ---")
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
            
                if escolha == 1:
                    agenda.listar()
            
                elif escolha == 2:
                    nome = input("Nome: ").strip()
                    telefone = input("Telefone: ").strip()
                    email = input("Email: ").strip()

                    agenda.adicionar(nome=nome, telefone=telefone, email=email)
            
                elif escolha == 3:
                    nome = input("Digite o nome para a busca: ").strip()
                    resultados = agenda.buscar(nome)

                    if not resultados:
                        print("Nenhum contato encontrado.")
                    else:
                        print("\nResultados:")
                        for i, contato in enumerate(resultados):
                            print(f"{i} - {contato}")
            
                elif escolha == 4:
                    if not agenda.contatos:
                        print("Nenhum contato disponível.")
                        continue

                    agenda.listar()

                    try:
                        indice = int(input("Número do contato para remover: "))
                        contato = agenda.contatos[indice]

                        confirmar = input(f"Remover '{contato.nome}'? (s/n): ").lower().strip()

                        if confirmar in ['s', 'sim']:
                            agenda.remover(indice)
                
                        else:
                            print("Cancelado.")

                    except (ValueError, IndexError):
                        print("[ERRO] Entrada inválida.")
            
                elif escolha == 5:
                    print("Saindo...")
                    break

            except ValueError:
                print("[ERRO] Entrada inválida. Digite apenas números.")
                continue

#Main
if __name__ == "__main__":
    main()