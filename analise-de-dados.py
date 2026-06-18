import pandas as pd

# ==============================================================================
# CARREGAMENTO DOS DADOS (Ajustado para o formato dos seus arquivos)
# ==============================================================================
# Lendo os arquivos usando o separador ';' e tratando caracteres especiais
df_ocorrencia = pd.read_csv('ocorrencia.csv', sep=';', encoding='iso-8859-1')
df_aeronave = pd.read_csv('aeronave.csv', sep=';', encoding='iso-8859-1')
df_tipo = pd.read_csv('ocorrencia_tipo.csv', sep=';', encoding='giso-8859-1')

print("Dados carregados com sucesso! Processando as respostas...\n")

# ==============================================================================
# QUESTÃO A: Qual a quantidade de ocorrências por tipo?
# ==============================================================================
print("=" * 70)
print("RESPOSTA QUESTÃO A: Quantidade de ocorrências por tipo (Top 10)")
print("=" * 70)
# Mostra os tipos de ocorrência mais frequentes
print(df_tipo['ocorrencia_tipo'].value_counts().head(10))
print("\n")

# ==============================================================================
# QUESTÃO B: Qual o tipo de aeronave que mais sofre sinistros?
# ==============================================================================
print("=" * 70)
print("RESPOSTA QUESTÃO B: Tipo de aeronave que mais sofre sinistros")
print("=" * 70)
# Identifica o equipamento (Avião, Helicóptero, etc.) com mais registros
print(df_aeronave['aeronave_tipo_equipamento'].value_counts())
print("\n")

# ==============================================================================
# QUESTÃO C: Qual o fabricante com maior número de sinistros?
# ==============================================================================
print("=" * 70)
print("RESPOSTA QUESTÃO C: Fabricantes com maior número de sinistros (Top 10)")
print("=" * 70)
# Conta os incidentes por fabricante de aeronave
print(df_aeronave['aeronave_fabricante'].value_counts().head(10))
print("\n")

# ==============================================================================
# QUESTÃO D: Qual a quantidade de fatalidades por tipo de motorização?
# ==============================================================================
print("=" * 70)
print("RESPOSTA QUESTÃO D: Quantidade de fatalidades por tipo de motorização")
print("=" * 70)
# Agrupa pelo tipo de motor e soma o total de fatalidades
fatalidades_motor = df_aeronave.groupby('aeronave_motor_tipo')['aeronave_fatalidades_total'].sum()
print(fatalidades_motor.sort_values(ascending=False))
print("\n")

# ==============================================================================
# QUESTÃO E: Qual o número total de ocorrências de falha do motor em voo por UF?
# ==============================================================================
print("=" * 70)
print("RESPOSTA QUESTÃO E: Ocorrências de 'FALHA DO MOTOR EM VOO' por UF")
print("=" * 70)

# Cruzando a tabela de ocorrências (que tem a UF) com a de tipos (que tem o nome do evento)
df_cruzado = pd.merge(
    df_ocorrencia[['codigo_ocorrencia', 'ocorrencia_uf']], 
    df_tipo[['codigo_ocorrencia1', 'ocorrencia_tipo']], 
    left_on='codigo_ocorrencia', 
    right_on='codigo_ocorrencia1'
)

# Filtrando apenas por "FALHA DO MOTOR EM VOO"
df_falha_motor = df_cruzado[df_cruzado['ocorrencia_tipo'] == 'FALHA DO MOTOR EM VOO']

# Contando a quantidade por Estado (UF)
print(df_falha_motor['ocorrencia_uf'].value_counts())
print("=" * 70)