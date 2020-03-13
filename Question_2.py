# 2. You were asked to analyze the company's **average daily profit** and found that not all transactions were profitable; a negative value on Profit expresses a loss rather than profit. Based on the analysis, on what date did the company suffer their biggest loss?   
# *Hint*: Aggregate your data based on `Order.Date` and find the average daily `Profit`!
#     - [ ] 2016-11-25
#     - [ ] 2015-01-28
#     - [ ] 2016-10-02
#     - [ ] 2015-01-10


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
### We know that the worse profit is less than -6000 from Glimpse.py
### So, we can filter the dataframe for profit less than -6000 and take its order date to get the answer
print(df[df['Profit'] < -6000][['Order Date', 'Profit']])
#        Order Date    Profit
# Row ID
# 7773   2016-11-25 -6599.978