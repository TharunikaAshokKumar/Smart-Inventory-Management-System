import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_stock_level(data):
    df = pd.DataFrame(data)
    model = LinearRegression()
    X = df[['current_stock']]
    y = df['sales']
    model.fit(X, y)
    df['predicted_stock'] = model.predict(X)
    return df['predicted_stock'].tolist()

