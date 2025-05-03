# desafio03.py

# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações visuais
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Carregando os dados
emprestimos = pd.read_csv('../dados/emprestimos.csv')

# (Opcional) Visualização inicial
# print(emprestimos.head())

# Remoção de duplicatas por `id_emprestimo`
emprestimos = emprestimos.drop_duplicates(subset='id_emprestimo')

# Convertendo coluna de data
emprestimos['data_emprestimo'] = pd.to_datetime(emprestimos['data_emprestimo'])

# Criando colunas auxiliares para análise temporal
emprestimos['ano'] = emprestimos['data_emprestimo'].dt.year
emprestimos['mes'] = emprestimos['data_emprestimo'].dt.to_period('M')
emprestimos['hora'] = emprestimos['data_emprestimo'].dt.hour

# Análise por ano
emprestimos_ano = emprestimos.groupby('ano')['id_emprestimo'].count()
emprestimos_por_ano = emprestimos_ano.reset_index()
emprestimos_por_ano.columns = ['ano', 'quantidade_emprestimos']

# Análise por mês
emprestimos_mes = emprestimos.groupby('mes')['id_emprestimo'].count()
emprestimos_por_mes = emprestimos_mes.reset_index()
emprestimos_por_mes.columns = ['mes', 'quantidade_emprestimos']
emprestimos_por_mes['mes'] = emprestimos_por_mes['mes'].astype(str)

# Análise por hora
emprestimos_hora = emprestimos.groupby('hora')['id_emprestimo'].count()
emprestimos_por_hora = emprestimos_hora.reset_index()
emprestimos_por_hora.columns = ['hora', 'quantidade_emprestimos']

# Gráfico: Empréstimos por Ano
plt.figure(figsize=(10, 5))
sns.barplot(data=emprestimos_por_ano, x='ano', y='quantidade_emprestimos', palette='viridis')
plt.title('Quantidade de Empréstimos por Ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Empréstimos')
plt.tight_layout()
plt.savefig('graficos/emprestimos_por_ano.png')
plt.close()

# Gráfico: Empréstimos por Mês
plt.figure(figsize=(14, 6))
sns.lineplot(data=emprestimos_por_mes, x='mes', y='quantidade_emprestimos', marker='o')
plt.xticks(rotation=45)
plt.title('Quantidade de Empréstimos por Mês')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Empréstimos')
plt.tight_layout()
plt.savefig('graficos/emprestimos_por_mes.png')
plt.close()

# Gráfico: Empréstimos por Hora
plt.figure(figsize=(10, 5))
sns.barplot(data=emprestimos_por_hora, x='hora', y='quantidade_emprestimos', palette='rocket')
plt.title('Distribuição Horária de Empréstimos')
plt.xlabel('Hora do Dia')
plt.ylabel('Quantidade de Empréstimos')
plt.tight_layout()
plt.savefig('graficos/emprestimos_por_hora.png')
plt.close()

# Print final (opcional)
print("Análises concluídas e gráficos salvos na pasta 'graficos/'.")