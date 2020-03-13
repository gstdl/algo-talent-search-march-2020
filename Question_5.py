# 5. `Home Office` has been the least profitable segment for the company in the past years. Say, the company wants to target more `Home Office` customer by giving 
# special offers on products from a sub category which has highest **total Sales** from the particular segment. Which sub category do you think would be suitable for the promotion?
#     - [ ] Copiers
#     - [ ] Phones
#     - [ ] Binders
#     - [ ] Fasteners


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
### Obtain sub-category with max sale sum of 'home office' segment
print(df[df['Segment'] == 'Home Office'].groupby('Sub-Category')['Sales'].sum().sort_values().tail(1))
# Sub-Category
# Phones    68920.876
# Name: Sales, dtype: float64