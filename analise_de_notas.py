import pandas as pd

arq_df = pd.read_csv('notas_alunos.csv', sep=',')
media = (arq_df['Nota_1'] + arq_df['Nota_2']) / 2
arq_df['Média'] = media

arq_df.loc[arq_df['Média'] >= 7, 'Situação'] = 'APROVADO'
arq_df.loc[arq_df['Média'] < 7, 'Situação'] = 'REPROVADO'
arq_df.loc[arq_df['Faltas'] > 5, 'Situação'] = 'REPROVADO'

mais_faltas = arq_df['Faltas'].max()
media_geral = (arq_df['Média'].sum()) / 4
maior_media = arq_df['Média'].max()

print('O maior número de faltas: {} faltas.'.format(mais_faltas))
print('A média geral das notas dos alunos foi {}'.format(media_geral))
print('A maior média foi {}'.format(maior_media))

arq_df.to_csv('alunos_situacao.csv')
