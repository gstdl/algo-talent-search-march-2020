# 6. The dataset held the company historical transactions from `2014` to `2017`. From all those years, on what year did the company gain their highest `Profit`? *Hint*: Aggregate the data by the year of `Order.Date` and find the yearly **total** Profit!
#     - [ ] 2014
#     - [ ] 2015
#     - [ ] 2016
#     - [ ] 2017


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
### Groupby the data by year and sum its profit
print(df.set_index('Order Date').resample('A')['Profit'].sum().sort_values().tail(1))
# Order Date
# 2017-12-31    93439.2696
# Freq: A-DEC, Name: Profit, dtype: float64