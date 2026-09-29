# 变量命名规范，判断一个字符串是否是 Python 的保留关键字
import keyword
mass_b = 'mass'
print(mass_b.isidentifier())  # True，这是说，判断mass是一个合法的标识符的名字，合法的变量名 identifier
print(keyword.iskeyword('mass')) # False，不是关键字

print = 1203
print(print)