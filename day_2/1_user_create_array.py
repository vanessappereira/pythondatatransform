# Array criado pelo utilizador em que faça gestão de números, que permita adicionar, remover e listar os números da lista. Verificar o número máximo, mínimo, média e somatório

# To-do
# 1. Criar uma lista vazia para números
# 2. Adicionar os números à lista
#   2.1. Criar um ciclo para pedir números ao utilizador
# 3. Remover números da lista
#   3.1. Criar um ciclo para pedir números ao utilizador
# 4. Imprimir lista
# 5. Calcular o somatório, comprimento da lista e média
# 6. Verificar o número máximo e mínimo
# 7. Terminar o programa


# Criação da Lista vazia
listaDeNumeros = []


# Criação das funções a ser utilizadas:
# Função para adicionar números à lista
def addNumero(number):
    try:
        listaDeNumeros.append(number)
        print(f"O número {number} foi adicionado à lista.")
        addMaisNum = input("Deseja adicionar mais números? (S/N) \n")
        if addMaisNum.lower() == "s":
            newNumber = int(input("Insira o número que deseja adicionar: \n"))
            addNumero(newNumber)
        else:
            return
    except:
        print("O valor inserido não é um número.")


# Função para remover números da lista
def removeNumero(number):
    try:
        if number in listaDeNumeros:
            listaDeNumeros.remove(number)
        print(f"O número {number} foi removido da lista.")
        removMaisNum = input("Deseja adicionar mais números? (S/N) \n")
        if removMaisNum.lower() == "s":
            newNumber = int(input("Insira o número que deseja remover: \n"))
            removeNumero(newNumber)
        else:
            return
    except ValueError:
        print("O valor inserido não é um número.")


# Função para mostrar a lista de números
def listaDeNumeros():
    print(listaDeNumeros)


# Função para calcular a soma, média dos números e o comprimento da lista
def somaMediaComprimento():
    soma = 0
    for i in listaDeNumeros:
        soma += i
    media = soma / len(listaDeNumeros)

    print(f"A soma dos números é {soma}.")
    print(f"A média dos números é {media}.")
    print(f"O comprimento da lista é {len(listaDeNumeros)}.")


# Função para verificar o número máximo e mínimo da lista
def maxMinLista():
    numMaximo = max(listaDeNumeros)
    numMinimo = min(listaDeNumeros)

    print(f"O número mínimo da lista é {numMinimo}.")
    print(f"O número máximo da lista é {numMaximo}.")


def menu():
    while True:
        print("Lista")
        print("1 - Adicionar número")
        print("2 - Remover número")
        print("3 - Verificar lista")
        print("4 - Soma, média e comprimento da lista")
        print("5 - Valor mínimo e máximo da lista")
        print("9 - Terminar programa")

        selected = int(input("Enter the option of your choice: \n"))
        if selected == 1:
            item = input("Insira o item que deseja adicionar: \n")
            addNumero(item)
        elif selected == 2:
            listaDeNumeros()
            item = int(input("Insira o item que deseja remover: \n"))
            removeNumero(listaDeNumeros[item - 1])
        elif selected == 3:
            listaDeNumeros()
        elif selected == 4:
            somaMediaComprimento()
        elif selected == 9:
            print("Programa terminado.")
            break


menu()
