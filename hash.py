import hashlib

def file_md5(file_path):
    """计算文件的MD5哈希值"""
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            md5.update(chunk)
    return md5.hexdigest()

# 需要计算哈希值的文件路径列表
files = [
    'data/train.csv',
    'data/val.csv',
    'data/test.csv',
    'data/class0_only.csv',
    'data/class1_only.csv'
]

for file in files:
    md5 = file_md5(file)
    print(f"{file}: {md5}")

# # 保存哈希值到txt文件
# with open('data/hash_reference.txt', 'w', encoding='utf-8') as out:
#     for file in files:
#         md5 = file_md5(file)
#         out.write(f"{file}: {md5}\n")
#         print(f"{file}: {md5}")