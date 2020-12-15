import pandas as pd

df = pd.read_csv('depenses.csv')
df['nom'] = df[['nom']].sum(axis=1).map(hash)
df['ville'] = df[['ville']].sum(axis=1).map(hash)

def centrer_reduire(mycol):
    mycol = mycol - mycol.mean()
    mycol = mycol/mycol.std()
    return mycol

df['age'] = centrer_reduire(df['age'])
df['salaire'] = centrer_reduire(df['salaire'])
df['depenses'] = centrer_reduire(df['depenses'])

df.to_csv('depenses_anonymes.csv')
