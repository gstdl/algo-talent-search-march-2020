# 1. Apparently, the company has 4 different modes of shipping; `First Class`, `Second Class`, `Standard Class` and `Same Day`. 
# Suppose, they want to perform an efficiency by eliminate one of the shipping mode which has the **least** shipment in the last two years.
# Which of the shipment mode do you think would be the most reasonable to eliminate?
#     - [ ] First Class
#     - [ ] Second Class
#     - [ ] Standard Class
#     - [ ] Same Day


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

## Filter file to orders in the last 2 years (2016 & 2017)
df2years = df[df['Order Date'].apply(lambda x: x.year) > 2015].copy()
## Sanity Check
print(df2years[['Order Date', 'Ship Date']].describe())
## Count order frequency of each ship mode for every month
count_df2monthly= df2years.groupby(['Order Date', 'Ship Mode'])['Profit'].count().unstack().resample('M').sum()
## Plot the result
count_df2monthly.plot(title= 'Monthly Order Frequency')
plt.ylabel('Frequency')
plt.xlabel('Month')
plt.savefig('assets/2 Year Monthly Order Frequency by Ship Mode')
plt.show()

############
#          #
#  ANSWER  #
#  START   #
#          #
############

# Based on the monthly frequency of orders, the answer for this question will be option 4 (Same Day)

############
#          #
#  ANSWER  #
#  END     #
#          #
############

### Deeper Analysis

## See the visualization result in numbers
print(count_df2monthly.assign(**{f'{i} pct_change':count_df2monthly[i].pct_change() for i in count_df2monthly.columns}))
# Ship Mode   First Class  Same Day  Second Class  Standard Class
# Order Date
# 2016-01-31          7.0       1.0          22.0            59.0
# 2016-02-29         11.0      13.0          14.0            45.0
# 2016-03-31         26.0      11.0          39.0            87.0
# 2016-04-30         18.0       5.0          32.0           115.0
# 2016-05-31         30.0      20.0          20.0           155.0
# 2016-06-30         48.0      14.0          52.0            85.0
# 2016-07-31         23.0      20.0          44.0           114.0
# 2016-08-31         31.0       5.0          38.0           102.0
# 2016-09-30         45.0      14.0          69.0           235.0
# 2016-10-31         27.0      18.0          20.0           131.0
# 2016-11-30         71.0      10.0          72.0           217.0
# 2016-12-31         50.0      27.0          68.0           207.0
# 2017-01-31         21.0       3.0          37.0            94.0
# 2017-02-28         18.0       0.0          21.0            68.0
# 2017-03-31         36.0      27.0          59.0           116.0
# 2017-04-30         62.0       2.0          22.0           117.0
# 2017-05-31         42.0      15.0          39.0           146.0
# 2017-06-30         45.0       6.0          50.0           144.0
# 2017-07-31         25.0       9.0          44.0           148.0
# 2017-08-31         37.0      13.0          48.0           120.0
# 2017-09-30         93.0      36.0          91.0           239.0
# 2017-10-31         60.0      16.0          42.0           180.0
# 2017-11-30         70.0      35.0         109.0           245.0
# 2017-12-31         63.0      24.0          95.0           280.0

# Ship Mode   First Class pct_change  Same Day pct_change  \
# Order Date
# 2016-01-31                     NaN                  NaN
# 2016-02-29                0.571429            12.000000
# 2016-03-31                1.363636            -0.153846
# 2016-04-30               -0.307692            -0.545455
# 2016-05-31                0.666667             3.000000
# 2016-06-30                0.600000            -0.300000
# 2016-07-31               -0.520833             0.428571
# 2016-08-31                0.347826            -0.750000
# 2016-09-30                0.451613             1.800000
# 2016-10-31               -0.400000             0.285714
# 2016-11-30                1.629630            -0.444444
# 2016-12-31               -0.295775             1.700000
# 2017-01-31               -0.580000            -0.888889
# 2017-02-28               -0.142857            -1.000000
# 2017-03-31                1.000000                  inf
# 2017-04-30                0.722222            -0.925926
# 2017-05-31               -0.322581             6.500000
# 2017-06-30                0.071429            -0.600000
# 2017-07-31               -0.444444             0.500000
# 2017-08-31                0.480000             0.444444
# 2017-09-30                1.513514             1.769231
# 2017-10-31               -0.354839            -0.555556
# 2017-11-30                0.166667             1.187500
# 2017-12-31               -0.100000            -0.314286

# Ship Mode   Second Class pct_change  Standard Class pct_change
# Order Date
# 2016-01-31                      NaN                        NaN
# 2016-02-29                -0.363636                  -0.237288
# 2016-03-31                 1.785714                   0.933333
# 2016-04-30                -0.179487                   0.321839
# 2016-05-31                -0.375000                   0.347826
# 2016-06-30                 1.600000                  -0.451613
# 2016-07-31                -0.153846                   0.341176
# 2016-08-31                -0.136364                  -0.105263
# 2016-09-30                 0.815789                   1.303922
# 2016-10-31                -0.710145                  -0.442553
# 2016-11-30                 2.600000                   0.656489
# 2016-12-31                -0.055556                  -0.046083
# 2017-01-31                -0.455882                  -0.545894
# 2017-02-28                -0.432432                  -0.276596
# 2017-03-31                 1.809524                   0.705882
# 2017-04-30                -0.627119                   0.008621
# 2017-05-31                 0.772727                   0.247863
# 2017-06-30                 0.282051                  -0.013699
# 2017-07-31                -0.120000                   0.027778
# 2017-08-31                 0.090909                  -0.189189
# 2017-09-30                 0.895833                   0.991667
# 2017-10-31                -0.538462                  -0.246862
# 2017-11-30                 1.595238                   0.361111
# 2017-12-31                -0.128440                   0.142857


## Calculate mean of order frequency in each ship mode
print(count_df2monthly.mean())
# Ship Mode
# First Class        39.958333
# Same Day           14.333333
# Second Class       47.791667
# Standard Class    143.708333
# dtype: float64


## Calculate average profit of each ship mode for every month 
avg_profit_df2monthly= df2years.groupby(['Order Date', 'Ship Mode'])['Profit'].sum().unstack().resample('M').sum() / count_df2monthly
## Plot the result
avg_profit_df2monthly.plot(title= 'Monthly Average Profit')
plt.ylabel('Average Profit')
plt.xlabel('Month')
plt.savefig('assets/2 Year Monthly Average Profit by Ship Mode')
plt.show()
## See the visualization result in numbers
print(avg_profit_df2monthly.assign(**{f'{i} pct_change':avg_profit_df2monthly[i].pct_change() for i in avg_profit_df2monthly.columns}))
# Ship Mode   First Class    Same Day  Second Class  Standard Class
# Order Date
# 2016-01-31    26.517043  -15.582600      3.407695       43.725717
# 2016-02-29    26.071145   54.870531    222.027093       19.913349
# 2016-03-31    38.357473   90.890418    -21.041459       27.994207
# 2016-04-30    34.488628   28.380560     26.590191       11.862876
# 2016-05-31     4.969227   18.162045     64.164570       44.300241
# 2016-06-30    24.077877   55.942579     20.767337       20.371087
# 2016-07-31    13.909539   -5.148620     41.933180       20.797114
# 2016-08-31     5.175616   25.534440     12.756868       12.639137
# 2016-09-30    26.001253   69.577414      3.669799       29.494899
# 2016-10-31   -27.765696   34.796600    140.247335      103.523136
# 2016-11-30    47.539368   -7.759660     35.569647       -8.512929
# 2016-12-31    33.690022   33.594619     41.484529       60.255099
# 2017-01-31    51.512919   -0.141967     73.476808       35.536721
# 2017-02-28    -1.464406         NaN     27.845562       15.521684
# 2017-03-31   212.572311   37.481915     50.271949       26.907169
# 2017-04-30    28.391147   11.986350      8.816100       -8.930667
# 2017-05-31     6.366736   70.199347     26.359377       27.357356
# 2017-06-30    17.358004  -25.515933     55.238312       33.565316
# 2017-07-31    14.176528  207.020044     15.550209       27.370395
# 2017-08-31    22.503235   56.615023     31.214948       49.783527
# 2017-09-30     9.323628   52.244758      9.925390       30.713123
# 2017-10-31   104.492723   26.457263      7.417338       12.615932
# 2017-11-30   -36.391030  -95.860289     39.824733       45.925265
# 2017-12-31    49.220902   -4.802962     27.345042       10.356865

# Ship Mode   First Class pct_change  Same Day pct_change  \
# Order Date
# 2016-01-31                     NaN                  NaN
# 2016-02-29               -0.016816            -4.521269
# 2016-03-31                0.471262             0.656452
# 2016-04-30               -0.100863            -0.687750
# 2016-05-31               -0.855917            -0.360053
# 2016-06-30                3.845397             2.080192
# 2016-07-31               -0.422310            -1.092034
# 2016-08-31               -0.627909            -5.959473
# 2016-09-30                4.023799             1.724846
# 2016-10-31               -2.067860            -0.499887
# 2016-11-30               -2.712162            -1.223001
# 2016-12-31               -0.291324            -5.329393
# 2017-01-31                0.529026            -1.004226
# 2017-02-28               -1.028428             0.000000
# 2017-03-31             -146.159454          -265.019123
# 2017-04-30               -0.866440            -0.680210
# 2017-05-31               -0.775749             4.856607
# 2017-06-30                1.726359            -1.363478
# 2017-07-31               -0.183286            -9.113364
# 2017-08-31                0.587359            -0.726524
# 2017-09-30               -0.585676            -0.077193
# 2017-10-31               10.207303            -0.493590
# 2017-11-30               -1.348264            -4.623213
# 2017-12-31               -2.352556            -0.949896

# Ship Mode   Second Class pct_change  Standard Class pct_change
# Order Date
# 2016-01-31                      NaN                        NaN
# 2016-02-29                64.154617                  -0.544585
# 2016-03-31                -1.094770                   0.405801
# 2016-04-30                -2.263705                  -0.576238
# 2016-05-31                 1.413092                   2.734359
# 2016-06-30                -0.676343                  -0.540159
# 2016-07-31                 1.019189                   0.020913
# 2016-08-31                -0.695781                  -0.392265
# 2016-09-30                -0.712328                   1.333616
# 2016-10-31                37.216630                   2.509866
# 2016-11-30                -0.746379                  -1.082232
# 2016-12-31                 0.166290                  -8.078069
# 2017-01-31                 0.771186                  -0.410229
# 2017-02-28                -0.621029                  -0.563221
# 2017-03-31                 0.805385                   0.733521
# 2017-04-30                -0.824632                  -1.331907
# 2017-05-31                 1.989914                  -4.063305
# 2017-06-30                 1.095585                   0.226921
# 2017-07-31                -0.718489                  -0.184563
# 2017-08-31                 1.007365                   0.818882
# 2017-09-30                -0.682031                  -0.383067
# 2017-10-31                -0.252691                  -0.589233
# 2017-11-30                 4.369141                   2.640260
# 2017-12-31                -0.313365                  -0.774484


## Calculate average profit for each ship mode
print(avg_profit_df2monthly.mean())
# Ship Mode
# First Class       30.462258
# Same Day          31.258342
# Second Class      40.202606
# Standard Class    28.878609
# dtype: float64


## Calculate average monthly change of each ship mode
print(avg_profit_df2monthly.agg(pd.Series.pct_change).mean())
# Ship Mode
# First Class       -6.043674
# Same Day         -12.800243
# Second Class       4.539428
# Standard Class    -0.351714
# dtype: float64


##############
#            #
#  ANALYSIS  #
#            #
##############

# Based on average monthly profit 'Same Day' Ship Mode does not give the lowest profit.
# However, it has a very negative trend of profit which can be a huge source of loss. 

## Calculate delivery duration of each observation
df2years['Delivery Duration'] = (df2years['Ship Date'] - df2years['Order Date']).dt.days
## Calculate delivery duration of each ship mode for every month
duration_df2monthly= df2years.groupby(['Order Date', 'Ship Mode'])['Delivery Duration'].mean().unstack().resample('M').mean()
## Plot the result
duration_df2monthly.plot(title= 'Monthly Average Delivery Duration')
plt.ylabel('Average Delivery Duration')
plt.xlabel('Month')
plt.savefig('assets/2 Year Monthly Average Delivery Duration by Ship Mode')
plt.show()
## See the visualization in numbers
print(duration_df2monthly.assign(**{f'{i} pct_change':duration_df2monthly[i].pct_change() for i in duration_df2monthly.columns}))
# Ship Mode   First Class  Same Day  Second Class  Standard Class
# Order Date
# 2016-01-31     1.750000  0.000000      2.818182        4.985657
# 2016-02-29     1.857143  0.000000      3.095238        5.308333
# 2016-03-31     2.312500  0.000000      2.880000        4.755487
# 2016-04-30     2.454545  0.000000      3.663265        4.929951
# 2016-05-31     2.089947  0.111111      3.060606        4.862798
# 2016-06-30     2.244048  0.000000      2.870370        4.923392
# 2016-07-31     1.958333  0.062500      3.289021        5.057021
# 2016-08-31     2.044872  0.000000      2.958333        5.387931
# 2016-09-30     2.175439  0.142857      3.020551        4.845451
# 2016-10-31     1.833333  0.000000      3.863636        4.915726
# 2016-11-30     2.239146  0.000000      3.228924        4.952848
# 2016-12-31     2.073099  0.000000      3.179630        5.214434
# 2017-01-31     2.136364  0.000000      3.316667        4.822515
# 2017-02-28     2.660714       NaN      3.370370        5.007331
# 2017-03-31     2.138333  0.142857      3.327778        4.915254
# 2017-04-30     2.005764  0.000000      3.366667        4.861951
# 2017-05-31     1.872655  0.142857      3.536458        4.787282
# 2017-06-30     2.066667  0.200000      2.907407        5.072957
# 2017-07-31     2.348485  0.000000      3.023810        5.121275
# 2017-08-31     2.142857  0.000000      3.385802        5.215939
# 2017-09-30     2.172890  0.027273      3.320002        5.027924
# 2017-10-31     2.105602  0.000000      2.875170        5.179957
# 2017-11-30     2.382197  0.000000      3.428125        4.938695
# 2017-12-31     2.297180  0.075758      3.385884        5.057079

# Ship Mode   First Class pct_change  Same Day pct_change  \
# Order Date
# 2016-01-31                     NaN                  NaN
# 2016-02-29                0.061224                  NaN
# 2016-03-31                0.245192                  NaN
# 2016-04-30                0.061425                  NaN
# 2016-05-31               -0.148540                  inf
# 2016-06-30                0.073734                 -1.0
# 2016-07-31               -0.127321                  inf
# 2016-08-31                0.044190                 -1.0
# 2016-09-30                0.063851                  inf
# 2016-10-31               -0.157258                 -1.0
# 2016-11-30                0.221352                  NaN
# 2016-12-31               -0.074156                  NaN
# 2017-01-31                0.030517                  NaN
# 2017-02-28                0.245441                  NaN
# 2017-03-31               -0.196331                  inf
# 2017-04-30               -0.061996                 -1.0
# 2017-05-31               -0.066363                  inf
# 2017-06-30                0.103602                  0.4
# 2017-07-31                0.136364                 -1.0
# 2017-08-31               -0.087558                  NaN
# 2017-09-30                0.014015                  inf
# 2017-10-31               -0.030967                 -1.0
# 2017-11-30                0.131361                  NaN
# 2017-12-31               -0.035688                  inf

# Ship Mode   Second Class pct_change  Standard Class pct_change
# Order Date
# 2016-01-31                      NaN                        NaN
# 2016-02-29                 0.098310                   0.064721
# 2016-03-31                -0.069538                  -0.104147
# 2016-04-30                 0.271967                   0.036687
# 2016-05-31                -0.164514                  -0.013621
# 2016-06-30                -0.062156                   0.012461
# 2016-07-31                 0.145853                   0.027142
# 2016-08-31                -0.100543                   0.065436
# 2016-09-30                 0.021031                  -0.100684
# 2016-10-31                 0.279116                   0.014503
# 2016-11-30                -0.164278                   0.007552
# 2016-12-31                -0.015267                   0.052815
# 2017-01-31                 0.043098                  -0.075160
# 2017-02-28                 0.016192                   0.038324
# 2017-03-31                -0.012637                  -0.018388
# 2017-04-30                 0.011686                  -0.010844
# 2017-05-31                 0.050433                  -0.015358
# 2017-06-30                -0.177876                   0.059674
# 2017-07-31                 0.040036                   0.009525
# 2017-08-31                 0.119714                   0.018485
# 2017-09-30                -0.019434                  -0.036046
# 2017-10-31                -0.133985                   0.030238
# 2017-11-30                 0.192321                  -0.046576
# 2017-12-31                -0.012322                   0.023971


## Calculate Ratio of orders delivered earlier than their average delivery duration for each ship mode
print((duration_df2monthly <= duration_df2monthly.mean()).mean().to_frame()\
    .rename(columns={0:'Lower Than Mean Ratio'}).join(duration_df2monthly.mean().to_frame()\
    .rename(columns={0:'Mean'})).join(duration_df2monthly.median().to_frame()\
    .rename(columns={0:'Median'})).join(count_df2monthly.sum().to_frame()\
    .rename(columns={0:'Count'}))
)
#                 Lower Than Mean Ratio      Mean    Median   Count
# Ship Mode
# First Class                  0.541667  2.140088  2.137348   959.0
# Same Day                     0.666667  0.039357  0.000000   344.0
# Second Class                 0.458333  3.215496  3.258973  1147.0
# Standard Class               0.541667  5.006133  4.969252  3449.0


## Calculate the average number of orders that has been delivered earlier than their average delivery duration on a daily basis.
print((duration_df2monthly <= duration_df2monthly.mean()).mean() *
    count_df2monthly.sum() / (366 + 365)
)
# Ship Mode
# First Class       0.710613
# Same Day          0.313725
# Second Class      0.719163
# Standard Class    2.555689
# dtype: float64

##############
#            #
#  ANALYSIS  #
#            #
##############

# Based on delivery duration 'Same Day' Ship Mode has the highest 
# delivery ratio of orders delivered earlier than their average delivery duration.
# Even though it has the highest early delivery ratio, this ship mode has the lowest order frequency.