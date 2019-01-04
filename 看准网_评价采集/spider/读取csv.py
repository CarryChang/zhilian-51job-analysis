import pandas as pd
# salary为索引
# data = pd.read_csv('data.csv',index_col='real_salary')
# 直接写出列的数

data = pd.read_csv('data.csv',usecols=['com1_salary'])
# 打印全部
print(data)