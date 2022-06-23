import csv
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.metrics import normalized_mutual_info_score
import pandas as pd
from itertools import permutations

def feature_scaling(city_data):
    
    with open (f"filled_training_{city_data}.csv") as csv_file:
        city = pd.read_csv(csv_file)
    with open (f"filled_test_{city_data}.csv") as csv_file:
        city_test = pd.read_csv(csv_file)
    city.drop("Unnamed: 0", inplace = True, axis = 1) 
    city_test.drop("Unnamed: 0", inplace = True, axis = 1) 
    numeric_features = [column for column in city.columns if column not in ['Date', 'avg_demand']]
    
    # print(numeric_features)
    
    normalise_scaler = MinMaxScaler()

    city[numeric_features] = normalise_scaler.fit_transform(city[numeric_features])
    city_test[numeric_features] = normalise_scaler.fit_transform(city_test[numeric_features])

    # after selection
    if city_data == 'melbourne':
        feature_left = ['9am Temperature (°C)', 'Evaporation (mm)', '3pm MSL pressure (hPa)', '9am relative humidity (%)', '3pm wind speed (km/h)', 'Sunshine (hours)']
    elif city_data == 'adelaide':
        feature_left = ['9am Temperature (°C)', '9am relative humidity (%)', '3pm MSL pressure (hPa)', 'Rainfall (mm)']
    elif city_data == 'brisbane':
        feature_left = ['Minimum temperature (°C)', '3pm MSL pressure (hPa)', '9am cloud amount (oktas)', 'Rainfall (mm)', 'Speed of maximum wind gust (km/h)']
    elif city_data == 'sydney' :
        feature_left = ['Minimum temperature (°C)', 'Evaporation (mm)','3pm relative humidity (%)', '3pm wind speed (km/h)', '9am relative humidity (%)', '9am cloud amount (oktas)']
    feature_left.append('avg_demand')
    for feature in numeric_features:
        if feature not in feature_left:
            city.drop(feature, inplace=True, axis=1)
            city_test.drop(feature, inplace=True, axis=1)
            
    city.to_csv(f"s_filled_training_{city_data}.csv")
    city_test.to_csv(f"s_filled_test_{city_data}.csv")
    return


def calc_mi(city_data):
    with open (f"filled_training_{city_data}.csv") as csv_file:
        city = pd.read_csv(csv_file)
    city.drop("Unnamed: 0", inplace = True, axis = 1)
    equal_freq_6 = KBinsDiscretizer(n_bins= 6, encode = 'ordinal', strategy = 'quantile')
    numeric_features = [column for column in city.columns if column != 'Date']


    mi_score = []

    permutation = list(permutations(numeric_features, 2))
    for comb in permutation:
        feature_one = city[comb[0]]
        feature_two = city[comb[1]]
        feature_one = pd.DataFrame(feature_one)
        feature_two = pd.DataFrame(feature_two)
        feature_one[f'binned {comb[0]}'] = equal_freq_6.fit_transform(city[[comb[0]]]).astype(int)
        feature_two[f'binned {comb[1]}'] = equal_freq_6.fit_transform(city[[comb[1]]]).astype(int)
        score = normalized_mutual_info_score(feature_one[f'binned {comb[0]}'], feature_two[f'binned {comb[1]}'], average_method='min')
        mi_score.append([comb[0], comb[1], score])

    mi_score = sorted(mi_score, key=lambda x: (x[2]), reverse=True)
    for i in range(len(mi_score)):
        print(mi_score[i])

# from sklearn.metrics import normalized_mutual_info_score
# normalized_mutual_info_score(data['binned_time_on_site'], data['binned_quantity'], average_method='min')
# we use min here because in NMI, we want to have our demoninator
# to be min(H(X), H(Y))

    return

feature_scaling("melbourne")
feature_scaling("adelaide")
feature_scaling("sydney")
feature_scaling("brisbane")



calc_mi("melbourne")
calc_mi("adelaide")
calc_mi("sydney")
calc_mi("brisbane")




