# desafio05.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 1. Importação dos Dados
# =========================

df = pd.read_csv('../desafio05/dataset_completo.csv')

# =========================
# 2. Filtro e Preparação
# =========================

# Seleciona apenas alunos de graduação e pós-graduação
df = df[df['tipo_vinculo_usuario'].isin(['ALUNO DE GRADUAÇÃO', 'ALUNO DE PÓS-GRADUAÇÃO'])]

# Garante que a coluna de data esteja como datetime
df['data_emprestimo'] = pd.to_datetime(df['data_emprestimo'], errors='coerce')

# Filtra os anos entre 2010 e 2020
df = df[(df['data_emprestimo'].dt.year >= 2010) & (df['data_emprestimo'].dt.year <= 2020)]

# Verifica a coleção mais emprestada
mais_frequente = df['colecao'].value_counts().idxmax()
df = df[df['colecao'] == mais_frequente]

# =========================
# 3. Agrupamento Mensal
# =========================

df['ano'] = df['data_emprestimo'].dt.year
df['mes'] = df['data_emprestimo'].dt.month

df_graduacao = df[df['tipo_vinculo_usuario'] == 'ALUNO DE GRADUAÇÃO']
df_pos = df[df['tipo_vinculo_usuario'] == 'ALUNO DE PÓS-GRADUAÇÃO']

df_grad_box = df_graduacao.groupby(['ano', 'mes'])['id_emprestimo'].count().reset_index()
df_grad_box.columns = ['Ano', 'Mês', 'Quantidade Mensal de Empréstimos']

df_pos_box = df_pos.groupby(['ano', 'mes'])['id_emprestimo'].count().reset_index()
df_pos_box.columns = ['Ano', 'Mês', 'Quantidade Mensal de Empréstimos']

# =========================
# 4. Função para Plotagem
# =========================

def plot_boxplot_melhorado(df_boxplot, titulo, cor='skyblue'):
    plt.figure(figsize=(14, 6))
    sns.boxplot(x='Ano', y='Quantidade Mensal de Empréstimos', data=df_boxplot, color=cor)
    plt.title(titulo, fontsize=14, weight='bold')
    plt.xlabel('Ano')
    plt.ylabel('Quantidade Mensal de Empréstimos')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# =========================
# 5. Geração dos Gráficos
# =========================

plot_boxplot_melhorado(df_grad_box, 'Distribuição Mensal de Empréstimos por Ano (ALUNO DE GRADUAÇÃO)', cor='skyblue')
plot_boxplot_melhorado(df_pos_box, 'Distribuição Mensal de Empréstimos por Ano (ALUNO DE PÓS-GRADUAÇÃO)', cor='lightgreen')