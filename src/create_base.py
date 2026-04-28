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
with open("../data/base.pl", "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        linha = format_prolog(row)
        f.write(linha + "\n")
    
    # Regras para funcionamento da query
    f.write("\n% ===== REGRAS =====\n\n")
    f.write("% Query 1\n")
    f.write("kda(K, D, A, KDA) :-\n")
    f.write("    D > 0,\n")
    f.write("    KDA is (K + A) / D.\n\n")
    f.write("kda_medio(Champion, Media) :-\n")
    f.write("    findall(KDA,\n")
    f.write("        (partida(_, Champion, _, K, D, A, _, _),\n")
    f.write("         D > 0,\n")
    f.write("         KDA is (K + A) / D),\n")
    f.write("        Lista),\n")
    f.write("    sum_list(Lista, Soma),\n")
    f.write("    length(Lista, N),\n")
    f.write("    N > 0,\n")
    f.write("    Media is Soma / N.\n\n")
    f.write("% Query 2\n")
    f.write("total_partidas(Champion, Total) :-\n")
    f.write("    findall(1,\n")
    f.write("        partida(_, Champion, _, _, _, _, _, _),\n")
    f.write("        Lista),\n")
    f.write("    length(Lista, Total).\n\n")
    f.write("total_vitorias(Champion, Total) :-\n")
    f.write("    findall(1,\n")
    f.write("        partida(_, Champion, true, _, _, _, _, _),\n")
    f.write("        Lista),\n")
    f.write("    length(Lista, Total).\n\n")
    f.write("winrate(Champion, Taxa) :-\n")
    f.write("    total_partidas(Champion, Total),\n")
    f.write("    total_vitorias(Champion, Wins),\n")
    f.write("    Total > 0,\n")
    f.write("    Taxa is Wins / Total.\n\n")
    f.write("% Query 3\n")
    f.write("dano_medio(Champion, Media) :-\n")
    f.write("    partida(_, Champion, _, _, _, _, _, _),\n")
    f.write("    findall(Damage,\n")
    f.write("        partida(_, Champion, _, _, _, _, _, Damage),\n")
    f.write("        Lista),\n")
    f.write("    sum_list(Lista, Soma),\n")
    f.write("    length(Lista, N),\n")
    f.write("    N > 0,\n")
    f.write("    Media is Soma / N.\n")
