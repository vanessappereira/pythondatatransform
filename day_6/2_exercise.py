"""_summary_
 adaptar exercicio do dia 5 de forma a que deixe de trabalhar do modo estático e que permita ao utilizador acrescentar/construir o dataframe.
    """
import pandas as pd
global data
df = pd.DataFrame()
df = None   

def gerarDataFrame():
    try:
        data = {}
        colunas = int(input("Insira o número de colunas que pretende criar no Dataframe: "))
        for i in range(colunas):
            nomeColuna = input(f"Insira o nome da coluna: {i+1} ")
            if nomeColuna in data:
                print("Coluna já existente, por favor insira um nome diferente.")
                return None
            dados = input(f"Introduza os valores a adicionar na coluna {nomeColuna}, separados por vírgulas: ").split(",")
            data[nomeColuna] = dados
            print(f"Coluna com o nome {nomeColuna} adicionada com sucesso. \n")
            return pd.DataFrame(data)
    except:
        print("Ocorreu um erro ao adicionar as colunas")

def listarDataFrame():
    global df
    print("Lista de Dataframe: \n", df)

def filtroColuna():
    global df
    global data
    nomeColuna = input("Introduza o nome da coluna que deseja filtrar: ")
    if nomeColuna not in df.columns:
        print(f"A coluna {nomeColuna} não existe no Dataframe")
        return
    dado = input("Introduza o dado que deseja filtrar: ")
    filtro = df[df[nomeColuna] == dado]
    print(f"Valores da coluna {nomeColuna}, filtrados por {dado}")
    print(filtro, "\n") 

def renomearCol():
    nomeColunas = df.columns.to_list()
    print(*nomeColunas, sep=", ")
    renomeCol = input("Por favor insira a coluna a renomear: ").title()
    # Verificar se a coluna existe
    if renomeCol not in nomeColunas:
        print(f"A coluna {renomeCol} não existe")
        return
    else:
        novoNome = input("Por favor insira o novo nome: ").title()
        confirmation = input(
            f"Está prestes a renomear a coluna {renomeCol} para {novoNome}. \n Pretende continuar? S/N "
        )
        if confirmation.lower() == "n":
            print("A operação não foi realizada.")
            return
        else:
            df.rename(columns={renomeCol: novoNome}, inplace=True)
            print(f"A coluna {renomeCol} foi renomeada para {novoNome}")   
            
def removerCol():
    listaColunas = df.columns.to_list()
    print(*listaColunas, sep=", ")
    removeCol = input("Por favor insira a coluna a remover: ").title()
    if removeCol not in listaColunas:
        print(f"A coluna {removeCol} não existe")
        return
    else:
        confirmation = input(
            f"Está prestes a remover a coluna {removeCol} \n Pretende continuar? S/N "
        )
        if confirmation.lower() == "n":
            print("A operação não foi realizada.")
            return
        else:
            df.drop(columns=[removeCol], inplace=True)
            print(f"A coluna {removeCol} foi removida com sucesso.")           
    
def menu():
    while True:
        print("Bem-Vindo(a)! ")
        print("1. Criar DataFrame: ")
        print("2. Listar Dataframe: ")
        print("3. Filtrar por Coluna: ")
        print("4. Renomear coluna: ")
        print("5. Remover Coluna: ")
        print("0. Sair")

        opcao = input("Escolha a opção a executar: ")
        if opcao == "1":
            gerarDataFrame()
        elif opcao == "2":
            listarDataFrame()
        elif opcao == "3":
            filtroColuna()
        elif opcao =="4":
            renomearCol()
        elif opcao == "5":
            removerCol()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida, por favor escolha uma das opções mencionadas.")