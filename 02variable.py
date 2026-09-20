# import builtins
# dir(builtins)
sample_id = 'S01'
mass_g = 7.85
print('样品编号 =', sample_id)
print('样品质量 / g =', mass_g)
# 变量命名
# 小写，英文字母，数字，下划线，不以数字开头，不能用连字符（减号），不能关键字，一般不在前面加下划线（特殊意义）
mass_g = 7.84
# _moss 报问题
# 一般 要注意量和单位 mass_g，mass_kg，mass_mg，mass_t，mass_lb，mass_oz
# ｇ这是全角字符不要混了
# 如果不是单词里面的l，最好不要用，会和数字1混掉
# temperature_c = 22.5 cr_mass_fraction = 0.25 铬元素的质量分数 heat_treatment

# 关联紧密，属于一类的变量，希望同时赋值
width_mm, thickness_mm = 5.0, 2.0

# 如果变量名出错，报NameError: name 'width_mm' is not defined

# 自我累加
mass_g = 7.0
mass_g += 0.5
mass_g *= 2

# 相当于，先右边计算，再赋值给左边
mass_g = mass_g + 0.5

# 变量命名规范，判断一个字符串是否是 Python 的保留关键字
import keyword
mass_b = 'mass'
print(mass_b.isidentifier())

# 相等比较 还是同一个对象
count = 7
count_float = 7.0
print(count == count_float)  # True
print(count is count_float)  # False
copy_count = count
print(count is copy_count)  # True
print(count is not copy_count)  # False

# 注意，python里面bool类型的True和False是首字母大写的，不能写成true和false
# 0值是False，非0值是True，空的是False，非空的是True（列表，字典，字符串等，一个列表是[0]，这样判断是True）
temperature_c = 22.5
print(temperature_c > 20)  # True
print(bool(0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool("False"))  # True

# 当前没有值 None 类型是NoneType
temperature_c = None
print(temperature_c is None)  # True
print(temperature_c == 0 )  # False
print(type(temperature_c).__name__)  # NoneType

# 数的类型
this_is_a_int = 7
print(type(this_is_a_int))  # <class 'int'>
# 20/4 = 5.0，除法运算结果是浮点数，整除也是，只有4//2返回整数
this_is_a_float = 20 / 4
print(type(this_is_a_float))  # <class 'float'>
print(this_is_a_float)
# 乘方 10**3 = 1000
square = 10**3
print(square)

# 加上一个点
is_this_a_int = 20.
print(type(is_this_a_int))  # <class 'float'>

# 浮点的优先级比较高
test = 20 + 1.0
print(type(test))  # <class 'float'>
print(test)

# 类型转换，只是取整数
print(int(2.8))  # 2
print(int(-2.8))  # -2

# 不同进制
print(26,0b11010,0o32,0x1a)  # 26 26 26 26
print(bin(26),oct(26),hex(26))  # 0b11010 0o32 0x1a 返回字符串
print(int("1a",16))  # 26 转换字符串到数字，告诉python字符串内的是16进制数

# 整除与取余
print(7/3)  # 2.3333333333333335
print(7//3)  # 2
print(7%3)  # 1
print(int(7/3))  # 2

# 负数怎么取
print(-7/3)  # -2.3333333333333335
print(-7//3, -7 % 3)  # -3 2 负数除以几，取整了以后是向负无穷取的
print(divmod(-7,3))  # (-3, 2) 负数除以几，取整了以后是向负无穷取的，余数是正数，dvimod()函数返回一个元组，包含商和余数
# 所有的取整都是向下取整，但是int()操作完后是向0截断
print("测试一下", int(-7/3) == -7//3)

# 科学计数法
force_n = 2.0e3  # 2.0*10**3
print(force_n)  # 2000.0
length_m = 1.0e-3  # 1.0*10**-3
print(length_m)  # 0.001
a = 1000_000_532_000  # 1000000532000
print(a)  # 1000000532000

# 计算机bug
print(0.1+0.2)  # 0.30000000000000004
print((0.1+0.2)-0.3)  # 5.551115123125783e-17
print(0.3 == 0.1+0.2)
# 因此为了避免判断的bug，我们需要进行格式化
a==0 # 有可能是a是一个很小很小的值
a<10e-30 # 这种判断非常好
import math

# 复数类型 complex，以i，j表示虚数单位
z = 3 + 4j
print(z.real, z.imag) # 返回的是 float
print(z.conjugate()) # 返回共轭（3-4j）


# 常用的数值内置函数
mass_a_g = 7.85
mass_b_g = 0.90

# 全大写名称表达常量，但是并不会禁止重新赋值
CELSIUS_OFFSET = 273.15

# 格式化输出
'''多少有点困难'''

# 字符串
code = "001"
print(int(code)) # 转换过后变成了1，不再是001
material = "steel"
tag = "Ti-6AI-4V" # 文段内部含有-，防止被干成减号
# a = 'I'm a student' 这样就bug了
