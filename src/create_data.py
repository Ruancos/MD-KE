import pandas as pd

df = pd.read_excel("../data/league_data.xlsx")

# Tipando algumas colunas
df["win"] = df["win"].astype(bool)
df["kills"] = df["kills"].astype(int)
df["deaths"] = df["deaths"].astype(int)
df["assists"] = df["assists"].astype(int)
df["game_duration"] = df["game_duration"].astype(int) 

# Seleciona apenas as colunas de interesse
tabela_fonte = df[
    ["game_mode","champion_name","win","kills","deaths","assists","game_duration","total_damage_dealt"]
].head(400) #Limitação para 400 linhas

tabela_fonte = tabela_fonte.reset_index(drop=True)

tabela_fonte.to_excel("../data/tabela_fonte.xlsx", index=False)


