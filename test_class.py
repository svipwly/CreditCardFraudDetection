import pandas as pd

# 读取原始数据
df = pd.read_csv('data/test.csv')
0
# 筛选 Class=0 和 Class=1 的数据
df_0 = df[df['Class'] == 0]
df_1 = df[df['Class'] == 1]

# 分别保存为新文件
df_0.to_csv('data/test_class_0.csv', index=False)
df_1.to_csv('data/test_class_1.csv', index=False)