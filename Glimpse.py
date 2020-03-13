## Workspace setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

## Open File
df = pd.read_csv(
    'algo-talent-master/retail.csv', 
    encoding= 'unicode-escape', 
    parse_dates=[2, 3],
    index_col= 'Row ID'
)

## Check for missing value and data types
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 9994 entries, 1 to 9994
# Data columns (total 14 columns):
#  #   Column        Non-Null Count  Dtype
# ---  ------        --------------  -----
#  0   Order ID      9994 non-null   object
#  1   Order Date    9994 non-null   datetime64[ns]
#  2   Ship Date     9994 non-null   datetime64[ns]
#  3   Ship Mode     9994 non-null   object
#  4   Customer ID   9994 non-null   object
#  5   Segment       9994 non-null   object
#  6   Product ID    9994 non-null   object
#  7   Category      9994 non-null   object
#  8   Sub-Category  9994 non-null   object
#  9   Product Name  9994 non-null   object
#  10  Sales         9994 non-null   float64
#  11  Quantity      9994 non-null   int64
#  12  Discount      9994 non-null   float64
#  13  Profit        9994 non-null   float64
# dtypes: datetime64[ns](2), float64(3), int64(1), object(8)
# memory usage: 1.1+ MB

## Take a peek on what is in the dataset
print(df.head(10))
#               Order ID Order Date  Ship Date       Ship Mode Customer ID  \
# Row ID
# 1       CA-2016-152156 2016-11-08 2016-11-11    Second Class    CG-12520
# 2       CA-2016-152156 2016-11-08 2016-11-11    Second Class    CG-12520
# 3       CA-2016-138688 2016-06-12 2016-06-16    Second Class    DV-13045
# 4       US-2015-108966 2015-10-11 2015-10-18  Standard Class    SO-20335
# 5       US-2015-108966 2015-10-11 2015-10-18  Standard Class    SO-20335
# 6       CA-2014-115812 2014-06-09 2014-06-14  Standard Class    BH-11710
# 7       CA-2014-115812 2014-06-09 2014-06-14  Standard Class    BH-11710
# 8       CA-2014-115812 2014-06-09 2014-06-14  Standard Class    BH-11710
# 9       CA-2014-115812 2014-06-09 2014-06-14  Standard Class    BH-11710
# 10      CA-2014-115812 2014-06-09 2014-06-14  Standard Class    BH-11710

#           Segment       Product ID         Category Sub-Category  \
# Row ID
# 1        Consumer  FUR-BO-10001798        Furniture    Bookcases
# 2        Consumer  FUR-CH-10000454        Furniture       Chairs
# 3       Corporate  OFF-LA-10000240  Office Supplies       Labels
# 4        Consumer  FUR-TA-10000577        Furniture       Tables
# 5        Consumer  OFF-ST-10000760  Office Supplies      Storage
# 6        Consumer  FUR-FU-10001487        Furniture  Furnishings
# 7        Consumer  OFF-AR-10002833  Office Supplies          Art
# 8        Consumer  TEC-PH-10002275       Technology       Phones
# 9        Consumer  OFF-BI-10003910  Office Supplies      Binders
# 10       Consumer  OFF-AP-10002892  Office Supplies   Appliances

#                                              Product Name     Sales  Quantity  \
# Row ID
# 1                       Bush Somerset Collection Bookcase  261.9600         2
# 2       Hon Deluxe Fabric Upholstered Stacking Chairs,...  731.9400         3
# 3       Self-Adhesive Address Labels for Typewriters b...   14.6200         2
# 4           Bretford CR4500 Series Slim Rectangular Table  957.5775         5
# 5                          Eldon Fold 'N Roll Cart System   22.3680         2
# 6       Eldon Expressions Wood and Plastic Desk Access...   48.8600         7
# 7                                              Newell 322    7.2800         4
# 8                          Mitel 5320 IP Phone VoIP phone  907.1520         6
# 9       DXL Angle-View Binders with Locking Rings by S...   18.5040         3
# 10                       Belkin F5C206VTEL 6 Outlet Surge  114.9000         5

#         Discount    Profit
# Row ID
# 1           0.00   41.9136
# 2           0.00  219.5820
# 3           0.00    6.8714
# 4           0.45 -383.0310
# 5           0.20    2.5164
# 6           0.00   14.1694
# 7           0.00    1.9656
# 8           0.20   90.7152
# 9           0.20    5.7825
# 10          0.00   34.4700

## Count number of unique values of index
print(df.index.nunique())
# 9994


## Count number of unique values for every column 
print(df.agg(pd.Series.nunique))
# Order ID        5009
# Order Date      1237
# Ship Date       1334
# Ship Mode          4
# Customer ID      793
# Segment            3
# Product ID      1862
# Category           3
# Sub-Category      17
# Product Name    1850
# Sales           5825
# Quantity          14
# Discount          12
# Profit          7287
# dtype: int64


## Count composition of unique value in several categorical data
for col in ['Ship Mode', 'Segment', 'Category', 'Sub-Category', 'Quantity', 'Discount']:
    print(df[col].value_counts())
# dtype: int64
# Standard Class    5968
# Second Class      1945
# First Class       1538
# Same Day           543
# Name: Ship Mode, dtype: int64
# Consumer       5191
# Corporate      3020
# Home Office    1783
# Name: Segment, dtype: int64
# Office Supplies    6026
# Furniture          2121
# Technology         1847
# Name: Category, dtype: int64
# Binders        1523
# Paper          1370
# Furnishings     957
# Phones          889
# Storage         846
# Art             796
# Accessories     775
# Chairs          617
# Appliances      466
# Labels          364
# Tables          319
# Envelopes       254
# Bookcases       228
# Fasteners       217
# Supplies        190
# Machines        115
# Copiers          68
# Name: Sub-Category, dtype: int64
# 3     2409
# 2     2402
# 5     1230
# 4     1191
# 1      899
# 7      606
# 6      572
# 9      258
# 8      257
# 10      57
# 11      34
# 14      29
# 13      27
# 12      23
# Name: Quantity, dtype: int64
# 0.00    4798
# 0.20    3657
# 0.70     418
# 0.80     300
# 0.30     227
# 0.40     206
# 0.60     138
# 0.10      94
# 0.50      66
# 0.15      52
# 0.32      27
# 0.45      11
# Name: Discount, dtype: int64


## Count composition of unique values in sub category column divided by category column
for val in df['Category'].unique():
    print(f"Category = {val}\n{df[df['Category']==val]['Sub-Category'].value_counts()}")
# Category = Furniture
# Furnishings    957
# Chairs         617
# Tables         319
# Bookcases      228
# Name: Sub-Category, dtype: int64
# Category = Office Supplies
# Binders       1523
# Paper         1370
# Storage        846
# Art            796
# Appliances     466
# Labels         364
# Envelopes      254
# Fasteners      217
# Supplies       190
# Name: Sub-Category, dtype: int64
# Category = Technology
# Phones         889
# Accessories    775
# Machines       115
# Copiers         68
# Name: Sub-Category, dtype: int64


## Obtain brief information about the time data in the dataset
print(df[['Order Date', 'Ship Date']].describe())
#                  Order Date            Ship Date
# count                  9994                 9994
# unique                 1237                 1334
# top     2016-09-05 00:00:00  2015-12-16 00:00:00
# freq                     38                   35
# first   2014-01-03 00:00:00  2014-01-07 00:00:00
# last    2017-12-30 00:00:00  2018-01-05 00:00:00


## Obtain brief information about numerical data in the dataset
print(df[['Sales', 'Quantity', 'Discount', 'Profit']].describe())
#               Sales     Quantity     Discount       Profit
# count   9994.000000  9994.000000  9994.000000  9994.000000
# mean     229.858001     3.789574     0.156203    28.656896
# std      623.245101     2.225110     0.206452   234.260108
# min        0.444000     1.000000     0.000000 -6599.978000
# 25%       17.280000     2.000000     0.000000     1.728750
# 50%       54.490000     3.000000     0.200000     8.666500
# 75%      209.940000     5.000000     0.200000    29.364000
# max    22638.480000    14.000000     0.800000  8399.976000


## Obtain information on numerical features when profit is lower than 0
print(df[df['Profit'] < 0].describe())
#               Sales     Quantity     Discount       Profit
# count   1871.000000  1871.000000  1871.000000  1871.000000
# mean     250.511574     3.762694     0.480887   -83.448042
# std      715.067296     2.141347     0.235080   284.423422
# min        0.444000     1.000000     0.100000 -6599.978000
# 25%       12.503000     2.000000     0.200000   -58.660950
# 50%       71.088000     3.000000     0.400000   -18.088200
# 75%      284.922000     5.000000     0.700000    -6.261500
# max    22638.480000    14.000000     0.800000    -0.089500


## Take a peek on data with loss more than 1000
print(df[df['Profit'] < -1000])
#               Order ID Order Date  Ship Date       Ship Mode Customer ID  \
# Row ID
# 28      US-2015-150630 2015-09-17 2015-09-21  Standard Class    TB-21520
# 166     CA-2014-139892 2014-09-08 2014-09-12  Standard Class    BM-11140
# 684     US-2017-168116 2017-11-04 2017-11-04        Same Day    GT-14635
# 1200    CA-2016-130946 2016-04-08 2016-04-12  Standard Class    ZC-21910
# 1804    CA-2017-158379 2017-09-22 2017-09-26    Second Class    JA-15970
# 2698    CA-2014-145317 2014-03-18 2014-03-23  Standard Class    SM-20320
# 2847    CA-2017-152093 2017-09-10 2017-09-15  Standard Class    SN-20560
# 2929    US-2017-120390 2017-10-19 2017-10-26  Standard Class    TH-21550
# 3012    CA-2017-134845 2017-04-17 2017-04-23  Standard Class    SR-20425
# 3152    CA-2015-147830 2015-12-15 2015-12-18     First Class    NF-18385
# 3325    CA-2014-165309 2014-11-11 2014-11-15  Standard Class    KD-16270
# 4356    CA-2015-155600 2015-12-04 2015-12-07    Second Class    RO-19780
# 4821    CA-2015-140025 2015-04-07 2015-04-11  Standard Class    PF-19120
# 4992    US-2017-122714 2017-12-07 2017-12-13  Standard Class    HG-14965
# 5311    CA-2017-131254 2017-11-19 2017-11-21     First Class    NC-18415
# 5321    US-2017-162558 2017-10-02 2017-10-05     First Class    Dp-13240
# 6049    CA-2015-105571 2015-11-07 2015-11-11  Standard Class    CP-12340
# 7773    CA-2016-108196 2016-11-25 2016-12-02  Standard Class    CS-12505
# 7899    CA-2017-128363 2017-08-13 2017-08-18  Standard Class    DC-12850
# 8641    US-2017-148551 2017-01-12 2017-01-16  Standard Class    DB-13120
# 9640    CA-2015-116638 2015-01-28 2015-01-31    Second Class    JH-15985
# 9775    CA-2014-169019 2014-07-26 2014-07-30  Standard Class    LF-17185

#             Segment       Product ID         Category Sub-Category  \
# Row ID
# 28         Consumer  FUR-BO-10004834        Furniture    Bookcases
# 166        Consumer  TEC-MA-10000822       Technology     Machines
# 684       Corporate  TEC-MA-10004125       Technology     Machines
# 1200       Consumer  OFF-BI-10004995  Office Supplies      Binders
# 1804       Consumer  OFF-SU-10002881  Office Supplies     Supplies
# 2698    Home Office  TEC-MA-10002412       Technology     Machines
# 2847    Home Office  OFF-BI-10003527  Office Supplies      Binders
# 2929    Home Office  OFF-BI-10004995  Office Supplies      Binders
# 3012    Home Office  TEC-MA-10000822       Technology     Machines
# 3152       Consumer  TEC-MA-10000418       Technology     Machines
# 3325       Consumer  OFF-BI-10001359  Office Supplies      Binders
# 4356       Consumer  OFF-BI-10000545  Office Supplies      Binders
# 4821       Consumer  OFF-AP-10002651  Office Supplies   Appliances
# 4992      Corporate  OFF-BI-10001120  Office Supplies      Binders
# 5311       Consumer  OFF-BI-10003527  Office Supplies      Binders
# 5321    Home Office  FUR-TA-10000198        Furniture       Tables
# 6049      Corporate  OFF-BI-10001359  Office Supplies      Binders
# 7773       Consumer  TEC-MA-10000418       Technology     Machines
# 7899       Consumer  OFF-BI-10001359  Office Supplies      Binders
# 8641      Corporate  OFF-BI-10000545  Office Supplies      Binders
# 9640       Consumer  FUR-TA-10000198        Furniture       Tables
# 9775       Consumer  OFF-BI-10004995  Office Supplies      Binders

#                                              Product Name      Sales  \
# Row ID
# 28      Riverside Palais Royal Lawyers Bookcase, Royal...   3083.430
# 166             Lexmark MX611dhe Monochrome Laser Printer   8159.952
# 684             Cubify CubeX 3D Printer Triple Head Print   7999.980
# 1200            GBC DocuBind P400 Electric Binding System   1088.792
# 1804    Martin Yale Chadless Opener Electric Letter Op...   4663.736
# 2698    Cisco TelePresence System EX90 Videoconferenci...  22638.480
# 2847    Fellowes PB500 Electric Punch Plastic Comb Bin...    762.594
# 2929            GBC DocuBind P400 Electric Binding System   1633.188
# 3012            Lexmark MX611dhe Monochrome Laser Printer   2549.985
# 3152            Cubify CubeX 3D Printer Double Head Print   1799.994
# 3325           GBC DocuBind TL300 Electric Binding System    896.990
# 4356     GBC Ibimaster 500 Manual ProClick Binding System   1598.058
# 4821                  Hoover Upright Vacuum With Dirt Cup    463.248
# 4992                 Ibico EPK-21 Electric Binding System   1889.990
# 5311    Fellowes PB500 Electric Punch Plastic Comb Bin...   1525.188
# 5321    Chromcraft Bull-Nose Wood Oval Conference Tabl...   2314.116
# 6049           GBC DocuBind TL300 Electric Binding System   1345.485
# 7773            Cubify CubeX 3D Printer Double Head Print   4499.985
# 7899           GBC DocuBind TL300 Electric Binding System   1614.582
# 8641     GBC Ibimaster 500 Manual ProClick Binding System    760.980
# 9640    Chromcraft Bull-Nose Wood Oval Conference Tabl...   4297.644
# 9775            GBC DocuBind P400 Electric Binding System   2177.584

#         Quantity  Discount     Profit
# Row ID
# 28             7       0.5 -1665.0522
# 166            8       0.4 -1359.9920
# 684            4       0.5 -3839.9904
# 1200           4       0.8 -1850.9464
# 1804           7       0.2 -1049.3406
# 2698           6       0.5 -1811.0784
# 2847           3       0.8 -1143.8910
# 2929           4       0.7 -1306.5504
# 3012           5       0.7 -3399.9800
# 3152           2       0.7 -2639.9912
# 3325           5       0.8 -1480.0335
# 4356           7       0.7 -1065.3720
# 4821           8       0.8 -1181.2824
# 4992           5       0.8 -2929.4845
# 5311           6       0.8 -2287.7820
# 5321           7       0.4 -1002.7836
# 6049           5       0.7 -1031.5385
# 7773           5       0.7 -6599.9780
# 7899           6       0.7 -1237.8462
# 8641           5       0.8 -1141.4700
# 9640          13       0.4 -1862.3124
# 9775           8       0.8 -3701.8928


## Obtain general information about delivery duration (which is obtained by calculating the difference
## between ship date and order date)
df['Delivery Duration'] = df.apply(lambda x: (x['Ship Date'] - x['Order Date']).days, axis= 1)
def p25(ser): return np.percentile(ser, 25)
def p50(ser): return np.percentile(ser, 50)
def p75(ser): return np.percentile(ser, 75)
print(df.groupby('Ship Mode').agg(
    {
        'Delivery Duration':['count', pd.Series.nunique, 'mean', 'std', 'min', p25, p50, p75, 'max'],
        'Quantity':[pd.Series.nunique, 'mean', 'std'],
        'Discount':[pd.Series.nunique, 'mean', 'std'],
        'Profit':[pd.Series.nunique, 'mean', 'std'],
    }
))
#                Delivery Duration                                              \
#                            count nunique      mean       std min p25 p50 p75
# Ship Mode
# First Class                 1538       4  2.182705  0.773529   1   2   2   3
# Same Day                     543       2  0.044199  0.205726   0   0   0   0
# Second Class                1945       5  3.238046  1.188245   1   2   3   4
# Standard Class              5968       5  5.006535  1.010813   3   4   5   6

#                    Quantity                     Discount                      \
#                max  nunique      mean       std  nunique      mean       std
# Ship Mode
# First Class      4       14  3.701560  2.119098     11.0  0.164610  0.210319
# Same Day         1       12  3.609576  2.129233     10.0  0.152394  0.198365
# Second Class     5       14  3.816452  2.263673     12.0  0.138895  0.190728
# Standard Class   7       14  3.819873  2.246699     12.0  0.160023  0.210782

#                 Profit
#                nunique       mean         std
# Ship Mode
# First Class     1411.0  31.839948  257.794233
# Same Day         523.0  29.266591  226.689497
# Second Class    1793.0  29.535545  152.822263
# Standard Class  4827.0  27.494770  250.010543