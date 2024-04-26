#Criar um quadro de estatística
#Número de alunos em 5 escolas, com opção de atualizar os dados

#To-do
#1. Criar arrays
#2. Atualizar os dados: Adicionar, remover, atualizar campo
#3. Adicionar pelo menos dois cálculos com a biblioteca Numpy
#4. Criar um gráfico de barras através da MatPlotLib, com os valores dos arrays
#5. Opcionalmente, utilizar o módulo Pickle, para gerar e carregar ficheiros.
#6. Criar o menu do programa
import numpy as np;
import matplotlib.pyplot as plt;
import pickle;

escolas = ["Escola 1", "Escola 2", "Escola 3", "Escola 4", "Escola 5"];
grupoAlunos = [789567,234432,467678,578563,657456];

def verGrafico():
    plt.bar(escolas, grupoAlunos);
    plt.xlabel('Escolas');
    plt.ylabel('Alunos Registados');
    plt.title('Números de alunos por escola');
    plt.show();
    

#Função para consultar lista alunos
def consultarListaEscolas():
    if not escolas:
        print("Não existem escolas registadas.");
    else:
        print("A lista contém a seguinte quantidade de alunos: ");
        for i, (alumni, school) in enumerate(zip(grupoAlunos, escolas), start=1):
            print(f"{i} - {school} com {alumni} alunos.");

#Função para adicionar escolas
def addEscola():
    try:
        addSchool = input("Por favor introduza o nome da escola: ");
        if addSchool == "":
            raise ValueError;            
        addAlumni = int(input("Por favor introduza a quantidade total de alunos: "));
        if addAlumni == "":
            raise ValueError;
        escolas.append(addSchool);
        grupoAlunos.append(addAlumni);
        print("Escola adicionada com sucesso!");
    except ValueError:
        print("O valor introduzido não é válido.");

#Função para remover escolas
def removeEscola():
    consultarListaEscolas();
    try:
        removeSchool = int(input("Por favor introduza o número da escola a remover: "));
        if removeSchool == "":
            raise ValueError;
        if 1 <= removeSchool <= len(escolas):
            escolas.pop(removeSchool-1);
            grupoAlunos.pop(removeSchool-1);
            print("Escola removida com sucesso!");
        else:
            raise ValueError;
    except ValueError:
        print("O valor introduzido não é válido.");

#Função para atualizar escolas
def updateEscola():
    consultarListaEscolas();
    try:
        ind = int(input("Por favor introduza o ID da escola a alterar: "));
        if ind == "":
            raise ValueError;
        if 1 <= ind <= len(escolas):
            newAlumni = int(input("Por favor introduza a nova quantidade de alunos: "));
            if newAlumni == "":
                raise ValueError;
            grupoAlunos[ind-1] = newAlumni;
            print("Escola atualizada com sucesso!");
        else:
            raise ValueError;
    except ValueError:
        print("O valor introduzido não é válido.");
        
#Numpy
def desvioMediaAlunos():
    media = np.mean(grupoAlunos);
    desvio = round(np.std(grupoAlunos), 4);
    print("A média de alunos registada é: ", media);
    print("O desvio padrão de alunos registados é: ", desvio);
    
#Função para criar ficheiro com pickle
def criarFicheiro():
    try:
        with open("Lista_Escolas.pickle", "wb") as f:
            pickle.dump((escolas, grupoAlunos), f);
        print("Ficheiro criado com sucesso!");
    except IOError:
        print("Ocorreu um erro ao criar o ficheiro.");
        
#Função para ler ficheiro com pickle
def lerFicheiro():
    global escolas, grupoAlunos;
    try:
        with open("Lista_escolas.pickle", "rb") as f:
            escolas, grupoAlunos = pickle.load(f);
        print("O ficheiro foi carregado com sucesso");
    except FileNotFoundError:
        print("O ficheiro não existe.");
    
def menu():
    while True:
        try:
            print("1 - Consultar lista de escolas: \n"
                + "2 - Adicionar escola: \n" 
                + "3 - Remover escola: \n"
                + "4 - Atualizar quantidade de alunos da escola: \n"
                + "5 - Média e desvio padrão dos alunos registados: \n"
                + "6 - Gráfico de dados: \n"
                + "7 - Criar ficheiro com pickle: \n"
                + "8 - Ler ficheiro com pickle: \n"
                + "0 - Sair: \n");
        
            opcao = int(input("Selecione uma opção: "));
            if opcao == 1:
                consultarListaEscolas();
            elif opcao == 2:
                addEscola();
            elif opcao == 3:
                removeEscola();
            elif opcao == 4:
                updateEscola();
            elif opcao == 5:
                desvioMediaAlunos();
            elif opcao == 6:
                verGrafico();
            elif opcao == 7:
                criarFicheiro();
            elif opcao == 8:
                lerFicheiro();
            elif opcao == 0:
                print("Programa terminado.");
                break;
            else:
                raise ValueError;                    
        except ValueError:
            print("Opção inválida, por favor selecione umas das seguintes opções:");
            continue;
menu();