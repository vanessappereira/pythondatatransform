#Criar lista de compras com 2 ou mais arrays
#To-do
#1. Criar um array para a lista de frutas e outra de quantidade
#2. Ver lista de frutas
#3. Adicionar/remover frutas da lista
#   3.1 - Não deixar adicionar à lista de frutas em vazio
#   3.2 - Não deixar adicionar à lista de quantidaeds em vazio
#4. Limpar listas
import pickle;

listaDeFrutas = [];
quantidade = [];

#Consultar lista de frutas
def consultarLista():
    if not listaDeFrutas:
        print("A lista encontra se vazia:");
    else:
        print("A lista contém as seguintes frutas:");
        for i, (listaDeFrutas, quantidade) in enumerate(listaDeFrutas, start=1):
            print(f"{i} - {listaDeFrutas} com {quantidade} unidades.");

#Adicionar frutas e quantidade
def addFrutas():
    try:
        addfruta = input("Por favor introduza a fruta que pretende adicionar: ")
        if addfruta == "":
            raise ValueError("Não pode adicionar uma fruta vazia.");
        listaDeFrutas.append(addfruta);
        addQnt = input("Por favor introduza a quantidade: ");
        if addQnt == "":
            raise ValueError("Não pode adicionar uma quantidade vazia.");
        quantidade.append(addQnt);
        print(f"{addfruta} com a quantidade de {addQnt} foi adicionado com sucesso à lista.")
    except ValueError:
        print("Não pode adicionar uma fruta vazia.");

#Remover fruta e quantidade
def removFruta():
    consultarLista();
    try:
        index = int(input("Por favor introduza o ID da fruta que pretende eliminar: "))
        if 1 <= index <= len(listaDeFrutas):
            listaDeFrutas.pop(index - 1);
            quantidade.pop(index - 1);
            print(f"A fruta {index} foi removida com sucesso.");
        else:
            raise ValueError("ID incorreto!");
    except ValueError:
        print("Não pode remover uma fruta vazia.");

#Limpar lista
def limparListaDeFrutas():
    listaDeFrutas.clear();
    quantidade.clear();

    print("A lista foi limpa com sucesso.");

def createFile():
    with open("lista_frutas.pickle", "wb") as file:
        pickle.dump((listaDeFrutas, quantidade), file);
    print("O ficheiro foi criado com sucesso.");
def loadFile():
    global listaDeFrutas, quantidade;
    try:
        with open("lista_frutas.pickle","rb") as file:
            listaDeFrutas, quantidade = pickle.load(file);
            print("O ficheiro foi carregado com sucesso.");
    except FileNotFoundError:
        print("O ficheiro não existe.");
        createFile();

def menu():
    while True:
        try:
            print("Lista de frutas")
            print("1 - Adicionar frutas");
            print("2 - Remover frutas");
            print("3 - Ver lista de frutas");
            print("4 - Limpar lista");
            print("9 - Terminar programa");

            selected = int(input("Digite a opção pretendida: \n"));
            if selected == 1:
                addFrutas();
            elif selected == 2:
                removFruta();
            elif selected == 3:
                listaDeFrutas();
            elif selected == 4:
                limparListaDeFrutas();
            elif selected == 9:
                print("Programa terminado.");
                break;
            elif selected < 1 or selected >= 5 or selected <= 8 or selected > 9:
                print("Opção inválida, por favor escolha uma das seguintes opções: ");
                continue;
           
        except ValueError:
            print("Opção inválida, por favor selecione umas das seguintes opções:");
            continue;
#Terminal
menu();