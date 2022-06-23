import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

r2_list = []
mse_list = []
def pca_function(city_data):
    with open (f"org_filled_training_{city_data}.csv") as csv_file:
        city_train = pd.read_csv(csv_file)
    with open (f"org_filled_test_{city_data}.csv") as csv_file:
        city_test = pd.read_csv(csv_file)

    city_train.drop(columns = ["Unnamed: 0" ,"Date"], inplace = True)
    city_test.drop(columns = ["Unnamed: 0" ,"Date"], inplace = True)

    # From the explained_variance is can be seen that PCA with 2 dimensions capture, on average, 99.7%+ of the variance
    pca = PCA(n_components=9)

    X_train = city_train.drop(columns = ["avg_demand"])
    Y_train = city_train["avg_demand"]
    X_test = city_test.drop(columns = ["avg_demand"])
    Y_test = city_test["avg_demand"]

    normalise_scaler = MinMaxScaler()

    X_train = normalise_scaler.fit_transform(X_train)
    X_test = normalise_scaler.fit_transform(X_test)

    X_train, X_validation, Y_train, Y_validation = train_test_split(X_train, Y_train, test_size=0.2, random_state=0)

    X_train = pca.fit_transform(X_train)
    X_test = pca.transform(X_test)
    print(pca.components_)

    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)
    Y_prediction = regressor.predict(X_test)
    print(regressor.coef_)

    r2 = regressor.score(X_test, Y_test)
    mse = mean_squared_error(Y_test, Y_prediction)
    r2_list.append(r2)
    mse_list.append(mse)

    print(f'{city_data}')
    print('R2', r2)
    print('MSE', mse)
    """
    a, b = np.polyfit(np.array(Y_validation), np.array(Y_prediction), 1)

    plt.scatter(Y_validation, Y_prediction)
    plt.plot(Y_validation, a*Y_validation + b, color="r")

    plt.ylabel("Predicted Energy Demand")
    plt.xlabel("Actual Energy Demand")
    plt.title(f"PCA + Linear Regression ({city_data})")
    plt.grid()
    plt.savefig(f"PCA + Linear Regression ({city_data}).jpg")
    plt.close() 
    """
    return

pca_function("melbourne")
pca_function("adelaide")
pca_function("brisbane")
pca_function("sydney")

print(sum(r2_list)/4)
print(sum(mse_list)/4)

