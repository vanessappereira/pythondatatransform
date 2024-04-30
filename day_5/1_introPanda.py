import pandas as pd

pessoas = {
    "Nome": ["Ana", "Rui", "Pedro", "Sara"],
    "Idade": [19, 29, 48, 32],
    "Cidade": ["Porto", "Lisboa", "Coimbra", "Faro"],
}

df = pd.DataFrame(pessoas)
print("Dataframe com Nome, Idade e Cidade: ")
print(df + "\n")

df["Profissão"] = ["Engenheiro", "Médico", "Professor", "Enfermeira"]
print("Dataframe com Nome, Idade, Cidade e Profissão: ")
print(df + "\n")

# Filtro consulta de pessoas que moram no Porto
filtro2 = df[df["Cidade"].str.contains("Porto")]
print("Dataframe com habitantes do Porto: ")
print(filtro2 + "\n")

# Filtro consulta de pessoas maiores de 22 e menor que 40
filtro = df[(df["Idade"] > 22) & (df["Idade"] < 40)]
print("Dataframe com pessoas maiores de 22 e menor que 40: ")
print(filtro + "\n")

# Filtro sem a consulta da cidade
df2 = df.drop(columns=["Cidade"])
print("Dataframe sem a coluna Cidade: ")
print(df2 + "\n")

# Filtro com a idade arredondada a 2 casas decimais
df["Idade"] = df["Idade"].round(2)
print("Dataframe com a idade arredondada a 2 casas decimais: ")
print(df + "\n")

# Filtro com as idades em ordem
df_asc = df.sort_values(by=["Idade"], ascending=True)
df_desc = df.sort_values(by=["Idade"], ascending=False)

print("Dataframe com as idades em ordem ascendente: ")
print(df_asc + "\n")

print("Dataframe com as idades em ordem descendente: ")
print(df_desc + "\n")

# Filtro para alterar o nome da coluna
df.rename(columns={"Idade": "Anos"}, inplace=True)
print("Dataframe com o nome da coluna Idade alterado para Anos: ")
print(df + "\n")

# Média de idades
media = df["Anos"].mean()
print(f"A média de idades é: {media}")
