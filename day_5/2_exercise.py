"""_summary_
Adapte a maior parte dos excertos do ficheiro introPanda como filtros, listagens, cálculo da média, apagar colunas e renomear os nomes das mesmas

To-do:
1. Criar um DataFrame com os dados das pessoas
2. Criar um filtro dos habitantes por cada cidade
3. Criar uma listagem dos habitantes de cada cidade
4. Cálculo da média de habitantes
5. Apagar colunas
6. Renomear as colunas
"""

import pandas as pd

pessoas = {
    "Nome": ["Ana", "Rui", "Pedro", "Sara", "Francisco", "Filipa"],
    "Idade": [22, 30, 26, 40, 32, 24],
    "Cidade": ["Lisboa", "Porto", "Coimbra", "Faro", "Coimbra", "Lisboa"],
}

df = pd.DataFrame(pessoas)


def imprimir_dataframe_original(df):
    print("DataFrame original: ")
    print(df, "\n")


def filtrarHabitantesCidades():
    try:
        print(
            "Por favor escolha uma das cidades: \n"
            + "1. Lisboa \n"
            + "2. Coimbra \n"
            + "3. Porto \n"
            + "4. Faro"
        )
        cidade = input("Escolha a cidade: ")
        if cidade == "1":
            filtroLis = df[df["Cidade"].str.contains("Lisboa")]
            print("DataFrame com habitantes de Lisboa: ")
            print(filtroLis, "\n")
        elif cidade == "2":
            filtroCoi = df[df["Cidade"].str.contains("Coimbra")]
            print("DataFrame com habitantes de Coimbra: ")
            print(filtroCoi, "\n")
        elif cidade == "3":
            filtroPor = df[df["Cidade"].str.contains("Porto")]
            print("DataFrame com habitantes do Porto: ")
            print(filtroPor, "\n")
        elif cidade == "4":
            filtroFar = df[df["Cidade"].str.contains("Faro")]
            print("DataFrame com habitantes de Faro: ")
            print(filtroFar, "\n")
        else:
            print("Opção Inválida, Tente de novo!")
    except ValueError:
        print("Erro! Tente de novo!")


def mediaHabitantes():
    mediaHab = df["Idade"].mean()
    mediaLis = df[df["Cidade"].str.contains("Lisboa")]["Idade"].mean()
    mediaPor = df[df["Cidade"].str.contains("Porto")]["Idade"].mean()
    mediaFar = df[df["Cidade"].str.contains("Faro")]["Idade"].mean()
    mediaCoi = df[df["Cidade"].str.contains("Coimbra")]["Idade"].mean()

    print(f"A media de habitantes é {mediaHab}")
    print(f"A media de habitantes de Lisboa é {mediaLis}")
    print(f"A media de habitantes do Porto é {mediaPor}")
    print(f"A media de habitantes de Faro é {mediaFar}")
    print(f"A media de habitantes de Coimbra é {mediaCoi}")


# Função para alterar o nome da coluna do dataframe
def renomearCol():
    nomeColunas = df.columns.to_list()
    print(*nomeColunas, sep=", ")
    """_summary_
    O operador * serve para imprimir a lista de forma mais limpa e legível de cada elemento separadamente. 
    O operador sep serve para separar cada elemento da lista com um separador.
    """
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


# Função para remover colunas do dataframe
def removerColunas():
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


while True:
    print(
        "Bem-vindo(a) \n"
        + "1. Consultar DataFrame: \n"
        + "2. Filtrar Habitantes por cidade: \n"
        + "3. Média de habitantes  \n"
        + "4. Atualizar nome das colunas: \n"
        + "5. Remover colunas: \n"
        + "0. Sair: \n"
    )
    opcao = input("Escolha a opção a executar: ")

    if opcao == "1":
        imprimir_dataframe_original(df)
    elif opcao == "2":
        filtrarHabitantesCidades()
    elif opcao == "3":
        mediaHabitantes()
    elif opcao == "4":
        renomearCol()
    elif opcao == "5":
        removerColunas()
    elif opcao == "0":
        print("Obrigado! ")
        break
    else:
        print("Opção Inválida, Tente de novo!")
