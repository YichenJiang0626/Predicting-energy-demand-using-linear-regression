import random
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression


def linear_regression(city_data):
    
    with open(f'filled_training_{city_data}.csv') as csv_file:
        train = pd.read_csv(csv_file)

    with open(f'filled_test_{city_data}.csv') as csv_file:
        test = pd.read_csv(csv_file)

    X_COLS = [column for column in train.columns if (column != 'Date' and column != 'avg_demand')]
    y_COLS = ['avg_demand']

    X_train = train[X_COLS]
    y_train = train[y_COLS]
    X_test = test[X_COLS]
    y_test = test[y_COLS]

    # Create and fit the linear model
    # lm = Linear Model (variable name)
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
    
    y_pred = lm.predict(X_test)
    r2 = lm.score(X_test, y_test)
    mse = mean_squared_error(y_test, y_pred)

    print('R2', r2)
    print('MSE', mse)
    

    plt.scatter(y_test, y_pred, alpha=0.3)

    plt.title(f'Linear Regression for {city_data}')
    plt.xlabel('Actual Value')
    plt.ylabel('Predicted Value')
    plt.grid()
    plt.savefig(f"lr_{city_data}_ns.jpg")
    plt.close()

    y_test = pd.DataFrame(y_test)
    y_pred = pd.DataFrame(y_pred)
    y_pred = y_pred.rename(columns = {0:'predicted_demand'})
    y_test = pd.cut(y_test['avg_demand'], 5, labels=[1,2,3,4,5])
    y_pred = pd.cut(y_pred['predicted_demand'], 5, labels=[1,2,3,4,5])
    y_test = list(y_test)
    y_pred = list(y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    ConfusionMatrixDisplay(confusion_matrix=cm).plot()
    plt.title('Confusion matrix for imbalanced dataset')
    plt.show()
    plt.savefig(f'cm_{city_data}.jpg')
    plt.close()
    return
    
    
linear_regression('melbourne')
linear_regression('adelaide')
linear_regression('brisbane')
linear_regression('sydney')
