# CreditCardViz
Visualization tool for credit card exploratory. This dataset is obtained from Kaggle site
[Kaggle Credit Card Fraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)

All the variables for this dataset are transformed using PCA dimension reduction algorithm. PCA ensures that we will not abuse user information. However, it also made analysis more difficult. To help visualize and explore data I built this simple app.

While bokeh is a powerful tool, it could be slow to paint large dataset locally. For the purpose of exploration, I keep all the fraud transactions and samples 10% of normal transactions. Sampling helped in quick visualization.

This app requires installing python3 or above to view the app.

## Play the app
To play with the app clone this repo and run the following command line within the folder.
```
bokeh serve --show creditcardvizapp.py
```

## Visual elements
Transaction types describe whether the transaction is fraud or normal. Orange points are fraud transactions.

Circle sizes are in proportion to the amount of the transactions.

Use buttons to select which variables to show. X and Y selections are for variables and transaction type button let users choose which subset of data to show.

![alt text](https://github.com/sophiarora/CreditCardViz/blob/master/vizboard_demo.png)



## Requirements

This repository require pandas, sklearn and bokeh to be install in order to view. Could use pip to download the required packages. Run the following command line to install
```
pip install -U numpy scipy scikit-learn
pip install bokeh
```
