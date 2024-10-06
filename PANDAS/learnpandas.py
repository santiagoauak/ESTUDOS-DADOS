#PANDAS É A MELHOR BIBLIOTECA PARA ANALISE DE DADOS
#BIBLIOTECA É UM PACOTE DE CODIGOS QUE ALGUEM CONSTRUIU UMA VEZ E QUE É POSSIVEL USAR DE FORMA GRATUITA
import pandas as pd #as PD pd é um apelido pro panda para chamar ele resumidamente

#PANDA FUNCIONA COM DATAFRAME
#SEMPRE QUE FOR TRABALHAR COM DADOS VAMOS PRECISAR IMPORTAR UM DATAFRAME
#Criando um dataframe a partir de um dicionario
#Dataframe 'tabela no python'

#METODOS PARA CRIAÇÃO DE DATAFRAME
# dataframe = pd.DataFrame() #Cria dataframe vazio
#Criar um dataframe apartir de um dicionario
venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijão', 'arroz'],
         'qtde': [50, 70],
        }
vendas_df = pd.DataFrame(venda) #df no final é um dataframe de vendas

#visualização dos dados -print -display
print(vendas_df)
print('=+'*15)

