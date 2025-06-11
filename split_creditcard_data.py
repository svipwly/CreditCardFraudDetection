import pandas as pd
from sklearn.model_selection import train_test_split

# 1. 读取数据
df = pd.read_csv('data/creditcard.csv')

# 2. 特征和标签分开
X = df.drop('Class', axis=1)
y = df['Class']

# 3. 分层划分数据集（直接按70:20:10三分）
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=1/3, stratify=y_temp, random_state=42
)
# 这样验证集占全部的20%，测试集占全部的10%，且都分层

# 4. 输出各集类别分布，检查分层效果
print("训练集类别分布：", y_train.value_counts(normalize=True))
print("验证集类别分布：", y_val.value_counts(normalize=True))
print("测试集类别分布：", y_test.value_counts(normalize=True))

# 5. 可选：保存分好集的数据
X_train.assign(Class=y_train).to_csv('data/train.csv', index=False)
X_val.assign(Class=y_val).to_csv('data/val.csv', index=False)
X_test.assign(Class=y_test).to_csv('data/test.csv', index=False)

# import pandas as pd
# from sklearn.model_selection import train_test_split
#
# # 1. 读取数据
# df = pd.read_csv('data/creditcard.csv')
#
# # 2. 特征和标签分开
# X = df.drop('Class', axis=1)
# y = df['Class']
#
# # 3. 三分法（分层采样，70:20:10）
# # 第一步：分出70%做训练集，剩余30%再分验证集和测试集
# X_train, X_temp, y_train, y_temp = train_test_split(
#     X, y, test_size=0.30, stratify=y, random_state=42
# )
# # 第二步：将剩余30%按2:1分为验证集和测试集（即20%:10%）
# X_val, X_test, y_val, y_test = train_test_split(
#     X_temp, y_temp, test_size=1/3, stratify=y_temp, random_state=42
# )
#
# # 4. 还原为完整DataFrame
# train_df = X_train.assign(Class=y_train)
# val_df = X_val.assign(Class=y_val)
# test_df = X_test.assign(Class=y_test)
#
# # 5. 额外输出全为0和全为1的子集
# df_0 = df[df['Class'] == 0]
# df_1 = df[df['Class'] == 1]
#
# # 6. 保存结果
# train_df.to_csv('data/train.csv', index=False)
# val_df.to_csv('data/val.csv', index=False)
# test_df.to_csv('data/test.csv', index=False)
#
# # 7. 可选：打印数量确认
# print(f"全量数据:{len(df)}, 全是0:{len(df_0)}, 全是1:{len(df_1)}")
# print(f"训练集:{len(train_df)}, 验证集:{len(val_df)}, 测试集:{len(test_df)}")
#
# # 8. 输出各集类别分布，检查分层效果
# print("训练集类别分布：", y_train.value_counts(normalize=True))
# print("验证集类别分布：", y_val.value_counts(normalize=True))
# print("测试集类别分布：", y_test.value_counts(normalize=True))