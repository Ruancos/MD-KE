import pandas as pd
import random

# Carregar tabela fonte
df = pd.read_excel("../data/tabela_fonte.xlsx")

# Pegar alguns champions aleatórios
champions = df["champion_name"].str.lower().str.replace(" ", "_").unique()
sample_champions = random.sample(list(champions), min(3, len(champions)))

# Criar queries
queries = []

# Pergunta 1 — KDA médio
queries.append("% KDA médio de um champion")
queries.append(f"?- kda_medio({sample_champions[0]}, Media).")

# Pergunta 2 — Winrate
queries.append("\n% Taxa de vitória de um champion")
queries.append(f"?- winrate({sample_champions[1]}, Taxa).")

# Pergunta 3 — Ranking de dano médio
queries.append("\n% Ranking de dano médio")
queries.append("?- setof(Media-Champion, dano_medio(Champion, Media), Lista), reverse(Lista, Ranking).")

# Salvar arquivo
with open("../data/queries.pl", "w", encoding="utf-8") as f:
    for q in queries:
        f.write(q + "\n")
