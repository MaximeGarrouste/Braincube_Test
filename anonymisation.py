import pandas as pd

df = pd.read_csv('depenses.csv')
df['nom'] = df[['nom']].sum(axis=1).map(hash)
df['ville'] = df[['ville']].sum(axis=1).map(hash)
