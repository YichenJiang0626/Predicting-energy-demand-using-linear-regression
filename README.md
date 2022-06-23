
# Introduction of intended use for code
   This program intakes data of a city's weather attributions, including 
   temperature, wind, rain, pressure etc. It trains a model which outputs
   a prediction of the energy demand of a day, given a set of comprehensive
   weather attributes on that day.


# File structure and use of each file
   plots.py 
        - plots feature data across time
    
   For example:
   
   ![Screen Shot 2022-06-23 at 10 51 43 pm](https://user-images.githubusercontent.com/107828138/175302832-63f9ee6b-5579-4489-a5b6-93affd0230e7.png)


   fill_missing_data.py
       - Fills the missing values for train and validation datasets using the
      mean of the corresponding attributes from the corresponding season.
        
   price_demand_average.py
       - Computes daily average of the price demand data is computed
    
   split.py
       - Unused features are removed from the data
       - Daily average price demand is added to the data
       - Splits the weather data into train and validate sets.
    
   feature_scaling.py
       - Feature standardised for PCA
       - Mutual information calculated between attributes, avoid selecting
          features that are highly correlated.

   feature_selection.py
       - Takes in the filled train datasets, calculates and prints the mutual
         information score between attributes and average demand, enabling selection of feature with highest correlation to predictor variable.

   train_validate.py
       - Trains a linear regression model using the filled training dataset
         based on the attributes selected based on the MI score.
       - The model is assessed against the original unfilled validation dataset,
         outputting R Square and MSE values.

   PCA.py
       - Each of the attributes are normalised by the MinMaxScaler.
       - PCA dimension reduction is performed on the dataset.
       - The dataset is split into training and validation data.
       - Linear regression model is used and assessed against the validation data.
       - The linear regression model is assessed on the test data. 

# Some Linear Regression results

![Screen Shot 2022-06-23 at 10 53 26 pm](https://user-images.githubusercontent.com/107828138/175303166-84fb7307-a63d-4a84-bed2-be8032cc8bd8.png)

![Screen Shot 2022-06-23 at 10 53 47 pm](https://user-images.githubusercontent.com/107828138/175303236-380888ea-20ae-4255-8808-2a5395c53681.png)


# Instructions on how to run your code.

   Order of running files:
   
   data.py
        
   price_demand_average.py
        
   split.py
        
   fill_missing_data.py
        
   feature_scaling.py
        
   feature_selection.py
        
   train_validate.py
        
   PCA.py
        
   plots.py
        
