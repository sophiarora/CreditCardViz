# CreditCardViz
Visualization tool for credict card exploratory. Data is from Kaggle site
[Kaggle Credit Card Fraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)

While bokeh is a powerful tool, it's not its expertise to paint large dataset. For the purpose of exploration, I keep all the fraud transactions and samples 10% of normal transactions. Sampling helped in quick visualization.

This app require installing python3 or above to view the app.

## Play the app
To play with the app clone this repo and run
```
bokeh serve --show creditcardvizapp.py
```

## Visual elements
Transaction type: describe whether the transaction is fraud or normal. Orange points are fraud transactions.

Circle Size: in proportion to the amount of the transactions.

Selections buttons: could select which elements to show. X and Y selections are for variables and transaction type select choose which subset of data to show.

![alt text](https://github.com/sophiarora/CreditCardViz/blob/master/vizboard_demo.png)



## Requirements

This repository require pandas, sklearn and bokeh to be install in order to view. Could us pip to download the required packages
```
pip install pandas sklearn bokeh
```
