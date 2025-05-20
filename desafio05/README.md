# 📦 Desafio 05 - Análise Exploratória com Boxplot

Neste quinto desafio do #7DaysOfCode da Alura com Python e Pandas, o foco está na **análise exploratória de dados (EDA)** utilizando gráficos de **Boxplot**, uma ferramenta estatística poderosa para avaliar a distribuição dos dados.

## 🎯 Objetivo

Avaliar, por meio de boxplots, como os empréstimos mensais de alunos **de graduação** e **pós-graduação** se comportaram entre **2010 e 2020**, utilizando a **coleção com maior frequência de empréstimos** para cada grupo.

A análise ajudará a diretoria da biblioteca a entender padrões de uso ao longo do tempo e tomar decisões estratégicas com base no comportamento dos usuários.

## 🧭 Etapas

1. Verificar qual é a coleção com **maior frequência** para cada tipo de usuário.
2. Filtrar os dados para incluir:
   - Apenas **empréstimos**
   - Período de **2010 a 2020**
   - Apenas **graduação** e **pós-graduação**
3. Agrupar os dados por mês e ano, contando o número de empréstimos.
4. Criar uma **função** para geração de gráficos de boxplot por ano.
5. Gerar os **boxplots** para cada tipo de usuário (um gráfico por grupo).
6. Analisar visualmente as diferenças entre os anos e entre os tipos de usuários.

## 📊 Ferramentas e Bibliotecas

- `Pandas` para manipulação dos dados
- `Matplotlib` e/ou `Seaborn` para visualização
- `Plotly` (opcional) para gráficos interativos

## 🔎 O que observar?

- Existe estabilidade ou variação nas distribuições ao longo dos anos?
- Algum ano destoou significativamente?
- Como os padrões diferem entre alunos de graduação e pós-graduação?
- Indícios de impacto de eventos externos ou mudanças institucionais?

## 📁 Arquivos

- `desafio05.ipynb`: Notebook com todo o processo de análise
- `desafio05.py`: Versão em script Python