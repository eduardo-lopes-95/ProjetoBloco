import pandas as pd 

# Configuração para justificar os cabeçalhos das colunas à esquerda
pd.set_option('display.colheader_justify', 'left')

# Carregar os DataFrames a partir de arquivos CSV
df_chamados = pd.read_csv('.\\data\\chamados.csv')
df_departamentos = pd.read_csv('.\\data\\departamentos.csv')
df_usuarios = pd.read_csv('.\\data\\usuarios.csv')

# Função para combinar informações de usuários e departamentos e ordenar pelo nome do usuário
def todos_usuario_por_departamento_ordenado_por_usuario():
    merged_df = pd.merge(df_usuarios, df_departamentos, left_on='departamento_id', right_on='id')
    merged_df.rename(columns={'nome_x':'Usuario', 'nome_y':'Departamento'}, inplace=True)
    return merged_df[['Usuario', 'Departamento']].sort_values(by='Usuario')

# Função para listar todos os chamados ordenados por prioridade
def todos_chamados_por_prioridade():
    chamados_por_prioridade = df_chamados.sort_values(by='prioridade')
    return chamados_por_prioridade[['titulo', 'descricao', 'prioridade']]

# Função para identificar o usuário com o maior número de chamados
def usuario_maior_quantidade_chamados():
    merged_df = pd.merge(df_usuarios, df_chamados, left_on='id', right_on='usuario_id')
    usuario_mais_chamados = merged_df['nome'].value_counts().idxmax()
    numero_chamados = merged_df['nome'].value_counts().max()
    usuario_maior_numero_chamados = f'O usuario {usuario_mais_chamados} tem o maior número de chamados: {numero_chamados}'
    return usuario_maior_numero_chamados

# Função para contabilizar a quantidade de chamados por departamento
def quantidade_chamados_por_departamento():
    merged_df = pd.merge(df_chamados, df_departamentos, left_on='departamento_id', right_on='id')
    qtde_chamado_usuario = merged_df['nome'].value_counts()
    return qtde_chamado_usuario

# Bloco principal que chama e imprime os resultados das funções
if __name__ == "__main__":
    print('## todos usuario por departamento ordenado por nome de usuario ##')
    print(todos_usuario_por_departamento_ordenado_por_usuario())
    print('\n## todos chamados por prioridade ##')
    print(todos_chamados_por_prioridade())
    print('\n## usuario maior quantidade chamados ##')
    print(usuario_maior_quantidade_chamados())
    print('\n## quantidade chamados por departamento ##')
    print(quantidade_chamados_por_departamento())
