# Fazer a gestão de uma lista, ou seja, que permita adicionar, listar e remover os items da lista
# Salvaguarda de caso o utilizador querer executar algo com a lista vazia!
# To-do
# 1. Criar um ficheiro que faça a gestão de uma lista de compras
# 2. Adicionar, listar e remover os items da lista
# 3. Colocar o contador do id a começar a 1
# 4. Opção de limpar a lista
# 5. Terminar o programa

# Backend
listaCompras = []


def addItem(item):
    listaCompras.append(item)
    print(f"O item {item} foi adicionado à lista de compras.")
    maisItens = input("Deseja adicionar mais algum item? S/N: \n")
    if maisItens.lower() == "s":
        novoItem = input("Qual o novo item? \n")
        addItem(novoItem)
    else:
        return


def removeItem(item):
    listaCompras.remove(item)


def listaDeCompras():
    if len(listaCompras) != 0:
        for i in range(len(listaCompras)):
            print(f"{i+1} - {listaCompras[i]}")
    else:
        print("A lista de compras está vazia.")
        return


def limparLista():
    print("Está prestes a limpar toda a lista de compras. Tem a certeza?")
    confirmacao = input("S/N: \n")
    if confirmacao.lower() == "s":
        listaCompras.clear()
        print("A lista de compras foi limpa.")
    else:
        print("A lista de compras não foi limpa.")
        return


# Frontend
def main():
    while True:
        print("Lista de compras")
        try:
            print("1 - Adicionar item")
            print("2 - Remover item")
            print("3 - Lista de compras")
            print("4 - Limpar lista de compras")
            print("9 - Terminar programa")

            selected = int(input("Enter the option of your choice: \n"))
            if selected == 1:
                item = input("Insira o item que deseja adicionar: \n")
                addItem(item)
            elif selected == 2:
                listaDeCompras()
                item = int(input("Insira o item que deseja remover: \n"))
                removeItem(listaCompras[item - 1])
            elif selected == 3:
                listaDeCompras()
            elif selected == 4:
                limparLista()
            elif selected == 9:
                print("Programa terminado.")
                break
            elif selected < 1 or selected >= 5 or selected <= 8 or selected > 9:
                print("Opção inválida, por favor escolha uma das seguintes opções: ")
                continue

        except ValueError:
            print("Opção inválida, por favor selecione umas das seguintes opções:")
            continue


main()
