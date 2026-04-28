# Knowledge Engine com Prolog

Autor: __Ruan César Oliveira da Silva__

Link do dataset: [League of Legends Match Dataset (2024)](https://www.kaggle.com/datasets/jakubkrasuski/league-of-legends-match-dataset-2025/data)

## Descrição

Este projeto tem como objetivo a construção de uma base de conhecimento utilizando **Lógica de Primeira Ordem**, com posterior realização de consultas (*queries*) em Prolog. A proposta segue o paradigma lógico apresentado em aula, permitindo a extração de informações a partir de inferência sobre um conjunto de dados estruturados.

O dataset utilizado contém informações sobre partidas de **League of Legends**, incluindo métricas de desempenho como kills, deaths, assists, duração da partida e dano causado. A partir desses dados, foi construída uma base de conhecimento em Prolog e desenvolvidas queries sofisticadas que envolvem agregação, composição de regras, comparação e ordenação.

---

## Estrutura do Projeto

```
MD-KE/
├── data/
│   ├── base.pl
│   ├── queries.pl
│   ├── league_data.xlsx
│   └── tabela_fonte.xlsx
├── src/
│   ├── create_base.py
│   ├── create_data.py
│   └── create_queries.py
├── pyproject.toml
└── README.md
```

---

## Construção da Base de Conhecimento

A base de conhecimento foi gerada a partir de um script Python (`create_base.py`) utilizando a biblioteca `pandas`.

### Etapas realizadas

1. Leitura do dataset original
2. Seleção das colunas relevantes:
   - `game_mode`
   - `champion_name`
   - `win`
   - `kills`
   - `deaths`
   - `assists`
   - `game_duration`
   - `total_damage_dealt`
3. Limpeza e padronização dos dados:
   - Conversão para minúsculas
   - Substituição de espaços por underscores (`_`)
4. Geração dos fatos Prolog no seguinte formato:

```prolog
partida(GameMode, Champion, Win, K, D, A, GameDuration, TotalDamage).
```

**Exemplo:**

```prolog
partida(classic, yasuo, true, 10, 2, 5, 1800, 25000).
```

---

## Predicados Auxiliares (Regras)

Além dos fatos, foram definidos predicados auxiliares para permitir consultas mais sofisticadas.

### `total_partidas/2`

```prolog
total_partidas(Champion, Total)
```

Conta o número total de partidas jogadas por um campeão.

---

### `total_vitorias/2`

```prolog
total_vitorias(Champion, Total)
```

Conta o número de vitórias de um campeão.

---

### `winrate/2`

```prolog
winrate(Champion, Taxa)
```

Calcula a proporção de vitórias em relação ao total de partidas.

---

### `dano_medio/2`

```prolog
dano_medio(Champion, Media)
```

Calcula o dano médio causado por um campeão por partida.

---

### `kda_medio/2`

```prolog
kda_medio(Champion, Media)
```

Calcula a média do KDA de um campeão, definido como:

```
KDA = (Kills + Assists) / Deaths
```

---

## Execução do Projeto

### Instalar dependências do projeto e preparar ambiente

1. Utilize o seguinte comando para baixar as dependências presentes no arquivo `pyproject.toml`: 

```bash
pip install -e
```
> **Sugestão:** Se julgar necessário crie um ambiente virtual (.venv)

2. Baixe o dataset das partidas no link presente no começo do documento e insira-o no diretório `data/`, que precisa estar na raiz do repositório

3. Execute os seguintes comandos para preparar o dataset e criar a base/queries:

```bash
python create_data.py
python create_base.py
python create_queries.py
```
---

>__Resultado:__ Após a execução dos comandos, o arquivo `base.pl`, que contem os predicados e as regras, bem como o arquivo `queries.pl` devem ser criados no diretório `/data`. Use-os para a próxima etapa.

### Uso do SWISH para compilar Prolog

1. Acesse [https://swish.swi-prolog.org/](https://swish.swi-prolog.org/)
2. Cole o conteúdo do arquivo `base.pl` na área **Program**
3. Cole a query desejada do arquivo `queries.pl` na área **Query**
4. Execute a consulta

> **Observação:** Caso receba erros ao executar as queries, recomenda-se executá-las uma de cada vez. Copie apenas uma query por vez na área **Query** e execute-a antes de tentar a próxima.


---

## Queries Desenvolvidas

As queries foram elaboradas com base nos critérios de sofisticação definidos na rubrica, envolvendo agregação, composição de regras e ordenação.

### 1. KDA médio de um campeão

**Pergunta:** Qual o KDA (kills, deaths, assists) médio de um campeão?

```prolog
?- kda_medio(yasuo, Media).
```

---

### 2. Taxa de vitória (winrate)

**Pergunta:** Qual a taxa de vitória de um campeão?

```prolog
?- winrate(yasuo, Taxa).
```

---

### 3. Ranking de campeões por dano médio

**Pergunta:** Qual o ranking dos campeões com base no dano médio causado?

```prolog
?- setof(Media-Champion, dano_medio(Champion, Media), Lista),
   reverse(Lista, Ranking).
```
> **Observaçao:** Para fins de testes, a função `head(2000)`, na linha 15 do arquivo `create_data.py`, limita a criação para 2000 predicados, porem este número pode ser alterado para uma melhor fidelidade das consultas.
---

## Caracterização das Queries

As queries desenvolvidas envolvem: 

- Agregação de dados com `findall`, `sum_list` e `length`
- Cálculo de métricas derivadas
- Composição de predicados auxiliares
- Ordenação de resultados com `setof` e `reverse`
- Uso de variáveis e restrições lógicas

---

## Considerações Finais

O projeto demonstra a aplicação prática de **lógica de primeira ordem** na construção de sistemas de consulta baseados em conhecimento. A utilização de Prolog permite explorar um paradigma declarativo, no qual o foco está na definição de relações e não em procedimentos imperativos.

A integração com Python foi utilizada exclusivamente para o processo de **ETL** (Extração, Transformação e Carga), conforme exigido pela especificação do projeto.
