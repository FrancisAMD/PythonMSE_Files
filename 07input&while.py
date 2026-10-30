# input 用户输入
from itertools import count
from sqlite3 import SQLITE_CREATE_TEMP_TABLE


sample_id = input("Please input the id of the sample: ")
material_type = input("Please input the material of the sample")
density_gcm3 = float(input("Please input the density of the sample[g]: "))

# print(type(sample_id)__name__, type(mass_g)__name__)

if material_type == "steel" and density_gcm3 >= 8.0:
    print("Error")

# 加上格式化的语句
raw_id = input("试样编号： ")
sample_id = raw_id.strip().upper()
print(repr(raw_id)) # 带有''号的print输出，比较好，容易看出是否存在空格
print(repr(sample_id))

# 提示词
prompt = "登记试样质量，单位为g。"
prompt += "\n只输入数值，例如7.80："
raw_mass = input(prompt)
print(f'收到原文：{raw_mass}g')

# count 数量
count = int(input("试样数量"))
print(count>=8)

# 数字字符判断和转换
for raw in ["-5","7.8","1e3"]:
    print(raw,raw.isdecimal())

# 例子
'''
???
'''

# while
volumn_ml = 0 
target_ml = 30
while volumn_ml < target_ml:
    volumn_ml += 5
    print(f'Current volumn[ml]:{volumn_ml}.')
print(f'End')

# 批量输入，并且指定结束
index = 0
sample_id = ['block']
while sample_id[index] != 'quit':
    index += 1
    sample_id[index] = input("请输入编号，输入quit以结束： ")
    if sample_id[index] != 'quit':
        print(f'已登记ID {sample_id[index]}')
print('结束')