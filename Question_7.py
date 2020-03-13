# 7. Throughout 2017, which month appear to be the busiest (has highest number of orders) for the company? *Hint*: Try to count how many unique `Order.ID` made in `2017` (year of `Order.Date`)
#     - [ ] September
#     - [ ] October
#     - [ ] November
#     - [ ] December


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
### Filter the data to order made in 2017 only and count the quantity of unique orders of each month
print(df[df['Order Date'].apply(lambda x: x.year) == 2017]\
    .set_index('Order Date').resample('M')['Order ID'].nunique()\
    .sort_values().tail(1)
)
# Order Date
# 2017-11-30    261
# Name: Order ID, dtype: int64