#montando a lista

estoque = {}

while True:
    print("\n1 - entrada do produto")
    print("2 - saída do produto")
    print("3 - ver estoque")
    print("4 - sair")

    opcao = input("escolha uma opção: ")

#opção 1

    if opcao == "1":
        produto = input("produto: ").lower()
        quantidade = int(input("quantidade: "))

        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade

        print("estoque atualizado")

#opção 2

    elif opcao == "2":
        produto = int(input("produto: "))
        quantidade = int(input("quantidade: "))

        if produto in estoque and estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
            print("saída registrada")
        else:
             print("produto não existe ou estoque insuficiente")

#opção 3

    elif opcao == "3":
        print("\nestoque:")

        if estoque:
            for produto, quantidade in estoque.items():
                print(f"{produto}: {quantidade} ")
        else:
            print("estoque vazio")

#opção 4

    elif opcao == "4":
        print("sistema encerrado")
        break

    else: 
        print("opção invalida")