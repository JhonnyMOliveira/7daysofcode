# 7DaysOfCode - Python e Pandas (Alura)

Este repositório contém minha participação no desafio **#7DaysOfCode** da Alura, com foco em análise de dados usando **Python** e **Pandas**. A cada dia, é proposto um novo exercício com base em dados reais das bibliotecas da UFRN (Universidade Federal do Rio Grande do Norte), envolvendo etapas fundamentais de um projeto de ciência de dados.

Cada desafio está em sua própria pasta com:
- Script Python (`.py`)
- Jupyter Notebook (`.ipynb`)
- Um `README.md` com o enunciado e explicações do desafio

---

## ✅ Desafio 01 - Importação e Organização dos Dados

**Objetivo:**
Importar, organizar e tratar dados reais de empréstimos e acervo das bibliotecas da UFRN.

**Tarefas:**
- Automatizar o download e a organização de mais de 20 arquivos CSV.
- Tratar valores nulos e remover linhas duplicadas.
- Unificar os dados de acervo e empréstimos por meio de merge.

📁 Acesse a pasta: `/desafio01`

---

## 🧹 Desafio 02 - Limpeza e Enriquecimento de Dados

**Objetivo:**
Realizar a limpeza e enriquecimento dos dados para torná-los mais úteis e preparados para análises.

**Tarefas:**
- Excluir a coluna `registro_sistema` que não é relevante para a análise.
- Converter a coluna `matricula_ou_siape` para o formato string.
- Criar uma nova coluna com base na `localizacao`, mapeando os números para suas respectivas classes gerais segundo a **CDU (Classificação Decimal Universal)**:

```
000 a 099: Generalidades. Ciência e conhecimento.
100 a 199: Filosofia e psicologia.
200 a 299: Religião.
300 a 399: Ciências sociais.
400 a 499: Classe vaga.
500 a 599: Matemática e ciências naturais.
600 a 699: Ciências aplicadas.
700 a 799: Belas artes.
800 a 899: Linguagem. Língua. Linguística.
900 a 999: Geografia. Biografia. História.
```

📁 Acesse a pasta: `/desafio02`

---

## 🗂️ Organização

```
7DaysOfCode-Pandas/
│
├── desafio01/
│   ├── desafio01.ipynb
│   ├── desafio01.py
│   └── README.md
│
├── desafio02/
│   ├── desafio02.ipynb
│   ├── desafio02.py
│   └── README.md
│
└── README.md  <- este arquivo geral
```

---

## 🚧 Em andamento...

📌 Em breve: desafio03, desafio04...

---

## 🔗 Referências
- [Alura - 7DaysOfCode](https://7daysofcode.io/)
- Dados reais extraídos do repositório da UFRN

---

📅 Projeto iniciado em: **Abril de 2025**

👤 Autor: **Jhonny Marcelo de Oliveira**

📫 Conecte-se comigo no [LinkedIn]([https://www.linkedin.com](https://www.linkedin.com/in/jhonny-oliveira-247826114/)) e acompanhe a jornada #7DaysOfCode!

