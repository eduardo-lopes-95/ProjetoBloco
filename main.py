import pandas as pd 
import colorama

colorama.init()

pd.set_option('display.colheader_justify', 'left')

df_chamados = pd.read_csv('.\\data\\chamados.csv')
df_departamentos = pd.read_csv('.\\data\\departamentos.csv')
df_usuarios = pd.read_csv('.\\data\\usuarios.csv')

def todos_usuario_por_departamento_ordenado_por_usuario():
    merged_df = pd.merge(df_usuarios, df_departamentos, left_on='departamento_id', right_on='id')
    merged_df.rename(columns={'nome_x':'Usuario', 'nome_y':'Departamento'}, inplace=True)
    return merged_df[['Usuario', 'Departamento']].sort_values(by='Usuario')

def todos_chamados_por_prioridade():
    chamados_por_prioridade = df_chamados.sort_values(by='prioridade')
    return chamados_por_prioridade[['titulo', 'descricao', 'prioridade']]

def usuario_maior_quantidade_chamados():
    merged_df = pd.merge(df_usuarios, df_chamados, left_on='id', right_on='usuario_id')
    usuario_mais_chamados = merged_df['nome'].value_counts().idxmax()
    numero_chamados = merged_df['nome'].value_counts().max()
    usuario_maior_numero_chamados = f'O usuario {usuario_mais_chamados} tem o maior número de chamados: {numero_chamados}'
    return usuario_maior_numero_chamados

def quantidade_chamados_por_departamento():
    merged_df = pd.merge(df_chamados, df_departamentos, left_on='departamento_id', right_on='id')
    qtde_chamado_usuario = merged_df['nome'].value_counts()
    return qtde_chamado_usuario

if __name__ == "__main__":
    print('## todos usuario por departamento ordenado por nome de usuario ##')
    print(todos_usuario_por_departamento_ordenado_por_usuario())
    print('\n## todos chamados por prioridade ##')
    print(todos_chamados_por_prioridade())
    print('\n## usuario maior quantidade chamados ##')
    print(usuario_maior_quantidade_chamados())
    print('\n## quantidade chamados por departamento ##')
    print(quantidade_chamados_por_departamento())