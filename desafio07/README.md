# 📈 Desafio 07 - Comparação Percentual de Empréstimos por Curso | #7DaysOfCode - Python & Pandas (Alura)

No último desafio da jornada #7DaysOfCode da Alura, o foco foi realizar uma **análise comparativa percentual** de empréstimos realizados por cursos de **pós-graduação** da UFRN, com objetivo de apoiar o plano de marketing da biblioteca.

---

## 🎯 Objetivo

Gerar uma tabela HTML que mostra a **diferença percentual** no número de empréstimos entre os anos:

- **2017 → 2018**
- **2018 → 2019**
- **2019 → 2022** (sendo 2022 uma previsão já realizada por outro membro da equipe)

A análise foca **exclusivamente nos alunos da pós-graduação**.

---

## 🛠️ Etapas do desafio

- Filtrar o DataFrame de alunos para manter apenas **pós-graduandos**
- Realizar merge com os dados de empréstimos
- Manter apenas os registros dos anos 2017, 2018, 2019 e adicionar dados projetados para 2022
- Criar uma **tabela pivot** com:
  - Índice: nome do curso
  - Colunas: anos
  - Valores: quantidade de empréstimos
- Calcular a **variação percentual** ano a ano
- Exportar a tabela final como **HTML com estilo personalizado**:
  - ✅ Cabeçalho estilizado (cores, sombras, fonte)
  - ✅ Números positivos em verde
  - ✅ Números negativos em vermelho
  - ✅ Cursos com apenas a primeira letra maiúscula
  - ✅ Sem índice visível

---

## 💡 Extra (opcional)
- Exportar HTML com CSS já estilizado para facilitar o trabalho do time de front-end.

---

## 🗂️ Arquivos

📁 Acesse a pasta: `/desafio07`

- `desafio07.ipynb` → Notebook com explicações e análises
- `desafio07.py` → Script automatizado da lógica do desafio
- `comparativo_cursos.html` → Tabela final para o front-end

---

## 🔗 Referências

- [Pandas - Estilização de Tabelas HTML](https://pandas.pydata.org/docs/user_guide/style.html)
- [Pandas - Função `pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)
- [Documentação oficial Alura - 7DaysOfCode](https://7daysofcode.io/)

---

🚀 Projeto realizado por: **Jhonny Marcelo de Oliveira**
📆 Abril - Maio de 2025
🔗 GitHub: [JhonnyMOliveira/7daysofcode](https://github.com/JhonnyMOliveira/7daysofcode)