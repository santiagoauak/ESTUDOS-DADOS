#IMPORTANDO ARQUIVOS DE BASE DE DADOS
import pandas as pd
vendas_df = pd.read_excel('Vendas.xlsx')
#print(vendas_df) #visualização de mais ou menos como a tabela funciona

#METODOS PARA ANALISAR OS DADOS
# -head MOSTRA AS 5 PRIMEIRAS LINHAS
# -shape MOSTRA QUANTAS LINHAS E QUANTAS COLUNAS TEM A TABELA
# -describe VISÃO GERAL DAS INFORMAÇÕES DA UM RESUMO DA QUANTIDADE, MÉDIA DE COMPRA, MÉDIA DE FATURAMENTO, PORCENTAGEM DE FATURAMENTO, MIN MAX.
#print(vendas_df.head(10)) #visualisação das 10 primeiras tabelas
#print(vendas_df.shape)
#print(vendas_df.describe())

# PUXANDO SÓ 1 COLUNA DE PRODUTOS
#produtos = vendas_df['Produto'] #pega só uma coluna  É UMA SERIE NÃO UM DATAFRAME UM DATAFRAME É FORMADO POR SERIES
#print(produtos)

# PUXANDO 2 COLUNAS
#produtos2 = vendas_df[['Produto', 'ID Loja']]
#print(produtos2)

#METODO LOC -PEGAR UMA UNICA LINHA 
# -PEGAR LINHAS DE ACORDO COM CONDIÇÃO
# - PEGAR LINHAS E COLUNAS ESPECIFICAS 
# -PEGAR 1 VALOR ESPECIFICO
#METODO LOC OLHA SEMPRE OS INDICES
#PEGAR 1 LINHA
#print(vendas_df.loc[1:5])


#PEGAR LINHAS QUE CORRESPONDEM A UMA CONDIÇÃO
 
# vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'] #PEGA TODAS LINHAS ONDE A COLUNA DE LOJA É IGUAL A NORTE SHOPPING

#PEGAR VÁRIAS LINHAS E COLUNAS USANDO O LOC

#vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']] #PADRAO DO LOC É LINHAS, COLUNAS
#print(vendas_norteshopping_df)

#PEGAR VALOR ESPECIFICO
#print(vendas_df.loc[93716, 'Produto']) #PARA PEGAR VALOR ESPECIFICO SÓ É NECESSARIO PASSAR LINHA E COLUNA

#ADICIONAR 1 COLUNA
#A PARTIR DE UMA COLUNA QUE EXISTE EX: COLUNA DE COMISSÃO QUE NADA MAIS É QUE O VALOR FINAL*COMISSAO
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05 #como não existe coluna comissão ele cria
#print(vendas_df)


#CRIAR UMA COLUNA VALOR PADRAO ou seja apartir do zero
#vendas_df['Imposto'] = 0 #POSSIFVEL FAZER POREM O PANDA RECLAMA DA MANEIRA QUE É FEITA
vendas_df.loc[:, 'Imposto'] = 0 #Mais facil de executar preenche todas colunas do imposto com 0
#print(vendas_df)


#ADICIONAR 1 LINHA
vendas_dez_df = pd.read_excel('Vendas - Dez.xlsx') #TABELA ORIGINAL COM AS VENDAS DE DEZEMBRO
#print(vendas_dez_df)
#ADICIONAR VENDAS DE DEZEMBRO NO FINAL DE VENDAS DF
vendas_df = pd.concat([vendas_df, vendas_dez_df])
#print(vendas_df)

#EXCLUIR LINHAS E COLUNAS
vendas_df = vendas_df.drop('Imposto', axis=1) #Colunas usam eixos 1
#print(vendas_df)
#EXCLUIR LINHA 0
vendas_df = vendas_df.drop(0, axis=0)
#print(vendas_df)

#COMANDOS ESSENCIAIS ANALISE DE DADOS
# TRATAR VALORES VAZIOS 
# DELETAR LINHAS/COLUNAS VAZIAS (COMPLETAMENTE)
vendas_df = vendas_df.dropna(how='all') #VAI EXCLUIR LINHAS E COLUNAS QUE ESTÃO COMPLETAMENTE VAZIOS
vendas_df = vendas_df.dropna(how='all', axis=1) #VAI EXCLUIR COLUNAS ONDE TODOS OS VALORES ESTÃO VAZIOS
# DELETAR LINHAS QUE POSSUEM VALORES VAZIOS
vendas_df = vendas_df.dropna() #ELE EXCLUI AS LINHAS QUE TEM PELO MENOS UM VALOR VAZIO
# PREENCHER VALORES VAZIOS (MEDIA E ULTIMO VALOR)
#PREENCHER COM A MÉDIA DA COLUNA
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean()) #PREENCHE TODOS OS VALORES VAZIOS COM A CONDIÇÃO
#print(vendas_df)
#PREENCHER COM O ULTIMO VALOR
vendas_df = vendas_df.ffill() #preenche com o ultimo valor correspondente

#CALCULAR INDICADORES
#-Groupby
#-Value Counts
#QUANTAS TRANSAÇÕES POR LOJA? VALUE COUNTS
#transacoes_loja = vendas_df['ID Loja'].value_counts()
#print(transacoes_loja)

#GROUPBY AGRUPA AS INFORMAÇÕES
#faturamente_produto = vendas_df.groupby('Produto').sum() #AGRUPA A COLUNA DE PRODUTOS E SOMA AS COLUNAS NUMERICAS POIS QUERO SABER O TOTAL DE FATURAMENTO
#print(faturamente_produto)

#MESCLAR 2 DATAFRAMES
gerentes_df = pd.read_excel('Gerentes.xlsx')
#print(gerentes_df)
vendas_df = vendas_df.merge(gerentes_df)
print(vendas_df)