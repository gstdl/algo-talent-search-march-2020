# 8. You were asked to perform an analysis on how often a customer makes a purchase from the company historical transactions in the year 2016 and 2017. 
# Which customer (`Customer.ID`) are **not** amongst the top five customer with the highest buying frequency? 
# *Hint*: Distinct the value of `Customer.ID` and `Order.ID`, then count how many unique order processed by each `Customer.ID`
#     - [ ] EP-13915
#     - [ ] EH-13765
#     - [ ] PK-19075
#     - [ ] SH-19975


## Workspace setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
plt.style.use('ggplot')

## Open File
df = pd.read_csv(
    'algo-talent-master/retail.csv', 
    encoding= 'unicode-escape', 
    parse_dates=[2, 3],
    index_col= 'Row ID'
)

## Get answer for question
### Filter the dataframe
top_5 = (df[df['Order Date'].apply(lambda x: x.year).isin([2016, 2017])]\
    .groupby('Customer ID')['Order ID'].nunique().sort_values().tail(5)).index
### Loop through the provided options and print it if it's not in the top_5 index
for item in ['EP-13915', 'EH-13765', 'PK-19075', 'SH-19975']:
    if item not in top_5:
        print(item)
# EH-13765