import pickle

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
Sales = [[10000],[20000],[30000],[40000],[50000]]
Profit = [20,30,40,50,80]
model = lm.fit(Sales,Profit)





with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)