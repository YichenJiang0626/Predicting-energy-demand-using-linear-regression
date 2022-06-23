import random
import csv
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import random
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



def training_validation(city_data):
    with open(f'filled_training_{city_data}.csv') as csv_file:
        city = pd.read_csv(csv_file)

    with open(f'test_{city_data}.csv') as csv_file:
        test_city = pd.read_csv(csv_file)
    '''
    X_test = [column for column in test_city.columns if (column != 'Date' and column != 'avg_demand')]
    y_COLS = ['avg_demand']
    y_test = test_city[y_COLS]
    '''
    city.drop("Unnamed: 0", inplace = True, axis = 1)

    for col in city.columns:
        print(col)
    X_COLS = [column for column in city.columns if (column != 'Date' and column != 'avg_demand')]
    X = city[X_COLS]
    y = city['avg_demand']
    X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=0.2, random_state=0)

    
    lm = LinearRegression()

    # Fit to the train dataset
    lm.fit(X_train, y_train)


    # HOW TO DETERMINE EFFECTIVENESS
    # alpha = intercept parameter (aka beta0)
    alpha = lm.intercept_

    # betas = coefficients
    betas = lm.coef_
    print('Intercept', alpha)
    print('Coefficients', betas)
    y_pred = lm.predict(X_validation)
    r2 = lm.score(X_validation, y_validation)
    mse = mean_squared_error(y_validation, y_pred)
    print('r2 = ', r2)
    print('mse = ', mse)
    '''
    y_pred2 = lm.predict(X_test)
    r2t = lm.score(X_test, y_test)
    mset = mean_squared_error(y_test, y_pred2)
    print('test set r2 = ', r2t)
    print('test set mse = ', mset)
    '''
    return

training_validation('melbourne')
training_validation('adelaide')
training_validation('sydney')
training_validation('brisbane')
