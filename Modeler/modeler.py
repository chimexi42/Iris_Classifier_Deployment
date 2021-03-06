import os
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

class Modeler:
    def __init__(self):
        self.df = pd.read_csv('iris.csv')

        try: self.model = joblib.load('Models/iris.model')
        except: self.model = None

    def fit(self):
        x = self.df.drop('species', axis=1)
        y = self.df['species']
        self.model = DecisionTreeClassifier().fit(x, y)
        joblib.dump(self.model, 'Models/iris.model')
        
    def predict(self, measurement):
        if not os.path.exists('Models/iris.model'):
            raise Exception('Model is not trained yet, call .fit() before making predictions')
        if len(measurement) != 4:
            raise Exception(f'Expected sepal_length, sepal_width, petal_length, petal_width but got{measurement}')
        prediction = self.model.predict(measurement)
        return prediction[0]
        