import pandas as pd
df = pd.DataFrame()
global data
df = None

def gerarDataFrame():
    try:
        colunas = int(
            input("Insira o numero de colunas que pretende adicionar no Dataframe: ")
        )
        data = {}

        for i in range(colunas):
            nomeColuna = input(f"Insira o nome da coluna {i+1}: ")
            if nomeColuna in data:
                print(f"A coluna {nomeColuna} já existe")
                return None
            dados = input(
                f"Introduza os valores a adicionar na coluna {nomeColuna}, separados por vírgulas: "
            ).split(",")
            data[nomeColuna] = dados
            print(f"Coluna com o nome {nomeColuna} adicionada com sucesso. \n")
        return pd.DataFrame(data)
    except:
        print("Ocorreu um erro ao adicionar as colunas")

def filtrarColuna():
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

def removerColuna():
    global df
    global data
    nomeColuna = input("Introduza o nome da coluna que deseja remover: ")
    if nomeColuna not in df.columns:
        print(f"A coluna {nomeColuna} não existe no Dataframe")
        return
    data = df.drop(columns=[nomeColuna], inplace=True)
    print(f"Coluna {nomeColuna} removida com sucesso!")

def listarDataframe():
    global df
    print("Lista de Dataframe: \n", df)


while True:
    print("Bem-Vindo(a)! ")
    print("1. Criar DataFrame: ")
    print("2. Filtrar por Coluna: ")
    print("3. Remover Coluna: ")
    print("4. Listar Dataframe: ")
    print("0. Sair")

    opcao = input("Escolha a opção a executar: ")

    if opcao == "1":
        df = gerarDataFrame()
    elif opcao == "2":
        if df is None:
            print("Dataframe não criada! Por favor corra primeiro a opção 1")
        else:
            filtrarColuna()
    elif opcao == "3":
        if df is None:
            print("Dataframe não criada! Por favor corra primeiro a opção 1")
        else:
            removerColuna()
    elif opcao == "4":
        if df is None:
            print("Dataframe não criada! Por favor corra primeiro a opção 1")
        else:
            listarDataframe()
    elif opcao == "0":
        print("Programa fechado.")
        break
    else:
        print("Opção inválida, selecione a opção correta!")
