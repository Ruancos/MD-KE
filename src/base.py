import pandas as pd 

df = pd.read_excel("../data/tabela_fonte.xlsx")

# Função para boolean no padrão Prolog
def bool_to_prolog(value):
    return "true" if value else "false"

# Função para limpar texto (evita erro no Prolog)
def clean_text(text):
    return str(text).lower().replace(" ", "_")

# Formatação para Prolog
def format_prolog(row):
    return (
        f"partida({clean_text(row.game_mode)}, "
        f"{clean_text(row.champion_name)}, "
        f"{bool_to_prolog(row.win)}, "
        f"{int(row.kills)}, {int(row.deaths)}, {int(row.assists)}, "
        f"{int(row.game_duration)}, {int(row.total_damage_dealt)})."
    )

# Criar arquivo .pl para colar no swish
with open("base.pl", "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        linha = format_prolog(row)
        f.write(linha + "\n")
