# 3. In general, the company is selling three different item categories; `Furniture`, `Office Supplies`, and `Technology`. One day, they want to make a `Furniture` catalog and you were asked to put "Best-Selling Item" section on it.  The "Best-Selling Item" is showing a list of ten Furniture product with the highest total quantity sold. Among the four products below, which one is **INCLUDED** on the list?
#     - [ ] GBC Premium Transparent Covers with Diagonal Lined Pattern
#     - [ ] Global High-Back Leather Tilter, Burgundy
#     - [ ] Global Stack Chair without Arms, Black
#     - [ ] Bevis 36 x 72 Conference Tables


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
### Obtain top 10 items in Furniture Category
top_10 = df[df['Category'] == 'Furniture'].groupby('Product Name')['Quantity'].sum().sort_values().tail(10)
### Loop through the provided options and print it if it's in top 10 furniture items
for item in [
    'GBC Premium Transparent Covers with Diagonal Lined Pattern',
    'Global High-Back Leather Tilter, Burgundy',
    'Global Stack Chair without Arms, Black',
    'Bevis 36 x 72 Conference Tables'
]:
    if item in top_10.index:
        print(item)
# Global High-Back Leather Tilter, Burgundy          14