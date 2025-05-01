# Desafio 02 - #7DaysOfCode | Alura

## 🧠 Objetivo
Neste segundo desafio da série #7DaysOfCode da Alura, o foco foi realizar a **limpeza e o enriquecimento dos dados** previamente organizados no desafio 01.

A ideia é preparar o dataset para análises mais robustas, ajustando formatos, removendo ruídos e criando uma nova camada semântica a partir da Classificação Decimal Universal (CDU).

## ✅ Tarefas realizadas
- Remoção da coluna `registro_sistema` (irrelevante para a análise).
- Conversão da coluna `matricula_ou_siape` para o tipo `string`, padronizando o formato.
- Conversão da coluna `localizacao` de `float` para `int`, após tratamento de valores nulos.
- Criação da coluna `classe_cdu`, categorizando os documentos com base nos códigos da CDU:

| Faixa de Código | Classe CDU |
|-----------------|-------------|
| 000–099         | Generalidades. Ciência e conhecimento |
| 100–199         | Filosofia e psicologia |
| 200–299         | Religião |
| 300–399         | Ciências sociais |
| 400–499         | Classe vaga |
| 500–599         | Matemática e ciências naturais |
| 600–699         | Ciências aplicadas |
| 700–799         | Belas artes |
| 800–899         | Linguagem. Língua. Linguística |
| 900–999         | Geografia. Biografia. História |

## 🛠️ Tecnologias utilizadas
- Python
- Pandas
- Jupyter Notebook

## 📁 Estrutura do desafio
- `desafio02.ipynb`: Notebook com execução passo a passo.
- `desafio02.py`: Script Python com a lógica do desafio.
- `dataset_completo.csv`: Arquivo final exportado para o próximo desafio.

---

📅 Publicado em: 01/05/2025  
👨‍💻 Autor: Jhonny Marcelo de Oliveira