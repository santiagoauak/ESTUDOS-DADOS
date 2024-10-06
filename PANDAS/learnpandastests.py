import pandas as pd
pagamento = {'data': ['06/10/2024', '05/10/2024', '05/10/2024', '04/10/2024'],
             'nome': ['Thaynara', 'Eduardo', 'Julia', 'Hanrry'],
             'aulas': ['4 Aulas', '6 Aulas', '8 Aulas', '6 Aulas'],
             'valor': ['R$100', 'R$225', 'R$180', 'R$140']
             }

aulas_df = pd.DataFrame(pagamento)

print(aulas_df)