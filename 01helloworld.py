print("Hello, world!")
'''这里是多行注释'''
# 单行注释
mean_c = ((22+23+26)/3)
print("平均温度为：", mean_c)
if mean_c > 20:
    print("温度大于20度")
    print('请检查记录')
print('程序执行完毕')
'''缩进错误 IndentationError'''
print(
    (20+22+23+20+22+23+20+22+23+20+22+23)
     /3
)
a = (20+22+23+20+22+23+20
     +22+23+20+22+23) / 12 # 括号内可以自动匹配（但是不能拆变量，数据）
'''a = (20+22+23+20+22+23+20+2
        2+23+20+22+23) / 12 # 这样会报错'''
a = (20+22+23+20+22+23+20+22+23+20+22+23) \
/ 12 # 反斜杠用于分行，但是反斜杠后面不能有任何字符，包括空格和注释
'''Python3 默认使用 UTF-8 编码'''
# 这是一个注释
'''错误：print(“Hello, world!”) # 语法错误 SyntaxError 中文标点'''
'''错误：Print('Hello,world!') # 语法错误 NameError 首字母大写'''
'''错误：print("Hello" # 语法错误 SyntaxError 缺少右括号'''
'''如果要除的数是一个正数，但是有等于零的风险，可以这样'''
b = 0
shu = max(b,10**-10) # 这样可以避免除数为零的情况
print(20/shu)

import math
print('圆片面积 / mm² =')
print(round(math.pi * 10**2, 2)) # round() 函数用于四舍五入，保留两位小数
print(math.sqrt(25)) # 平方根

'''或者，只是用库里面的一个或几个函数'''
'''from math import pi, sqrt # 只导入pi和sqrt函数'''
'''print(sqrt(pi))'''

'''或者，完整导入一个库（对于未知库要小心）'''
'''from math import * # 导入math库的所有函数'''

'''可以简化昵称'''
'''import math as m'''

print('圆片面积 / mm² =')
print(round(math.pi * 5**2, 2)) # round() 函数用于四舍五入，保留两位小数

# %%
# print(20/0) # 运行时错误 ZeroDivisionError 除数为零
# %% # 这样可以进行调试(是一个单独的模块，可以用于代码块的调试)
a=100
b=200
if a > b:
    print("a大于b")
else:
    print("a小于b")