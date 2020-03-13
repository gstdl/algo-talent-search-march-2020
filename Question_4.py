# 4. The company wants to initiate a stock clearance sale and the offered products will be the items from `Office Supplies` category which has total quantity sold below 20. Among four products below, which one is **NOT** on the list?
#     - [ ] 4009 Highlighters
#     - [ ] Easy-staple paper
#     - [ ] Staple envelope
#     - [ ] Staples


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
### Obtain items with less than 20 quantity sold in office supplies category
office_supplies_20_mask = df[df['Category'] == 'Office Supplies'].groupby('Product Name')['Quantity'].sum() < 20
office_supplies_20_product_name = office_supplies_20_mask[office_supplies_20_mask==True].index
### Loop through the provided options and print it if it's sold quantity is less than 20
for item in ['4009 Highlighters', 'Easy-staple paper', 'Staple envelope', 'Staples']:
    if item not in office_supplies_20_product_name:
        print(item)
# Easy-staple paper
# Staple envelope
# Staples