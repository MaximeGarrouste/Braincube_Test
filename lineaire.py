import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('depenses_anonymes.csv')

df_prediction1 = pd.DataFrame({"salaire:":df['salaire'],"depenses":df['depenses']})

def prediction_1(df):
    X= df[['salaire']]
    Y= df[['depenses']]
    reg=LinearRegression().fit(X,Y)
    prediction = reg.predict(X)
    df_prediction1['prediction_depenses']=prediction



def prediction_2(df):
    X= df[['salaire','age']]
    Y= df[['depenses']]
    reg=LinearRegression().fit(X,Y)
    prediction = reg.predict(X)
    df['prediction_depenses']=prediction

prediction_1(df)
prediction_2(df)

df_prediction1.to_csv("predictions1.csv")
df.to_csv("predictions2.csv")
