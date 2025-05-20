# 📚 Desafio 06 - Análise de Empréstimos por Curso (2015-2020)

Neste sexto desafio do projeto **#7DaysOfCode | Python & Pandas - Alura**, o foco está em consolidar dados de diferentes fontes para identificar a quantidade de empréstimos realizados por cursos de graduação entre os anos de **2015 e 2020**. A análise apoia processos de avaliação do Ministério da Educação (MEC), oferecendo indicadores sobre o uso do acervo das bibliotecas universitárias.

## 🎯 Objetivo

Gerar uma **tabela resumo** que mostre a **quantidade de empréstimos anuais** para os cursos de graduação abaixo, com base nos dados dos usuários (planilhas Excel + arquivo JSON) e nos dados de empréstimos processados anteriormente:

- Biblioteconomia
- Ciências Sociais
- Comunicação Social
- Direito
- Filosofia
- Pedagogia

## 🧪 Desafios Técnicos

- Manipular arquivos `.xlsx` e `.json`
- Unificar dados de usuários de diferentes formatos
- Garantir correspondência entre `matricula_ou_siape` e dados de empréstimo
- Criar tabela de frequência (`pivot_table`) com cursos como índice e anos como colunas
- Incluir total por curso e total por ano

## 📦 Etapas Realizadas

1. **Importação e padronização** dos dados dos usuários vindos de múltiplas fontes
2. **Limpeza e tratamento** dos campos de matrícula e curso
3. **Junção** com o dataset principal de empréstimos (`dataset_completo.csv`)
4. **Filtragem temporal** entre os anos de 2015 e 2020
5. **Contagem** de empréstimos por curso e ano
6. **Criação da tabela resumo** com totais de linha e coluna

## 📊 Resultado

A tabela final ajuda a universidade a identificar o comportamento de uso das bibliotecas pelos cursos que serão avaliados pelo MEC. Essa análise orienta decisões relacionadas a acervo, serviços e infraestrutura.

📁 Acesse a pasta: `/desafio06`

---