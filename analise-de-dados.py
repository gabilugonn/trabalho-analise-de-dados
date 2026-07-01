import pandas as pd

# Carregando os arquivos (separador ; e encoding pra lidar com acentuação)
df_ocorrencia = pd.read_csv('ocorrencia.csv', sep=';', encoding='iso-8859-1')
df_aeronave = pd.read_csv('aeronave.csv', sep=';', encoding='iso-8859-1')
df_tipo = pd.read_csv('ocorrencia_tipo.csv', sep=';', encoding='iso-8859-1')

# Questão A: quantidade de ocorrências por tipo
print(df_tipo['ocorrencia_tipo'].value_counts().head(10))
print("\n")

# Questão B: tipo de aeronave que mais sofre sinistros
print(df_aeronave['aeronave_tipo_equipamento'].value_counts())
print("\n")

# Questão C: fabricante com maior número de sinistros
print(df_aeronave['aeronave_fabricante'].value_counts().head(10))
print("\n")

# Questão D: fatalidades por tipo de motorização
fatalidades_motor = df_aeronave.groupby('aeronave_motor_tipo')['aeronave_fatalidades_total'].sum()
print(fatalidades_motor.sort_values(ascending=False))
print("\n")

# Questão E: ocorrências de falha do motor em voo por UF
# preciso cruzar a tabela de ocorrências (tem a UF) com a de tipos (tem o nome do evento)
df_cruzado = pd.merge(
df_ocorrencia[['codigo_ocorrencia', 'ocorrencia_uf']],
df_tipo[['codigo_ocorrencia1', 'ocorrencia_tipo']],
left_on='codigo_ocorrencia',
right_on='codigo_ocorrencia1'
)
df_falha_motor = df_cruzado[df_cruzado['ocorrencia_tipo'] == 'FALHA DO MOTOR EM VOO']
print(df_falha_motor['ocorrencia_uf'].value_counts())
