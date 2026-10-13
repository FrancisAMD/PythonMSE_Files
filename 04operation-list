# 操作列表
from re import A
from readline import append_history_file


print("hello world")

# 遍历列表
sample_ids = ["S01","AL01","S02"]
for sample_id in sample_ids:
    print(sample_id)
# 如果那个地方列表名称也是sample_id，那样自己前后就冲突了
# 这样print出来是换行输出的，sample_id 是不断变化的
# 不能一个变量名承担两个角色，最好list加s
# 可以通过zip将不同列表进行合并同时循环

# 拉伸力学性能测试：一个轴向知道拉断为止。应变：ε=ΔL/L，单位是1，无量纲。
# 另外应该标定材料的尺寸👉 应力：σ=F/A，单位是Pa，N/m^2，是压强的单位，一般常用单位N和mm^2算出来是MPa的10^6 的数量级
# 可以进行for的计算（应力）
forces_n = [0.0,1000.0,2000.0]
area_mm2 = 10.0
for force_n in forces_n:
    stress_mpa = force_n/area_mm2
    print(f'{stress_mpa:.1f}MPa')

# 后面加上总结性的语言
sample_ids = ["S01","AL01","S02"]
for sample_id in sample_ids:
    print(f'Ready: {sample_id}')
print(f'Total: {len(sample_ids)} samples')

# sample_ids 是空列表的话
sample_ids = []
for sample_id in sample_ids:
    print(f'Ready: {sample_id}')
print(f'Total: {len(sample_ids)} samples')
# 不会报错，0 samples

# 循环变量赋值，但是列表本身不修改
masses_g = [7.80, 2.70]
for mass_g in masses_g:
    mass_g = mass_g * 1000
    print(f'{mass_g:.0f} mg')
print(masses_g) # [7.8, 2.7]
# 反正这些mass_g就是一个新给出的元素，既然要for遍历列表的话，就不会当成一个i的计数器，不是range
pizza_list = ["pepperoni","mushroom","cheese"]
for pizza in pizza_list:
    print(f'I love {pizza} pizza!')

# zip 可以进行两个列表的同时遍历，是一个函数，for的时候分别对应同样的列表索引值
metal_list = ["S01","AL01","S02"]
metal_status = ["ready","pending","ready"]
for metal, status in zip(metal_list, metal_status) :
    print(f'I will test the sample {metal} today, current status: {status}')
# 对于for循环里面的缩进相关内容，如果少缩进了，identationError:expected an indented block，缩进多了，IndentationError: unexpected indent
# : 定义代码执行的范围

# 数值与推导式
for sample_no in range(1, 5):
    print(sample_no)
# 实际输出的是1,2,3,4,分别换行，包括start不包括stop
# range 默认的起点是0，步长是1,（4）这样是0,1,2,3；如果是反的（3,3） 得到空列表，range(3,0）也是空的，不会报错，数量为0
# range（5,1,-1）这样就可以向下计数，5,4,3,2
for i in range(5,1,-1):
    print(i)
# numpy的arange可以是小数，range只能是整数，可以实现更复杂的变换？？？

# range本身容易转换成list
sample_numbers = list(range(1, 6)) # 这样得到了1,2,3,4,5
print(sample_numbers)
print(sample_numbers[0],sample_numbers[-1]) # -1 也就是4,也就是len(sample_numbers)-1，最后一个数
temperatures_c = list(range(500,651,50)) # 500,550,600,650
print(temperatures_c)
ticks = range(0,6,2) # 0,2,4 tick 也就是数轴上面的小格点
# range 是序列，不是一个可以修改的列表，你可以读取ticks[1],输出2,但是不能ticks[0]=1，去修改元素
print(len(ticks), ticks[1])
print(type(list(ticks))) # list 可以进行转换
ticks_list = list(ticks)
ticks_list[0] = 1
print(ticks_list)

# 通过range 得到浮点数
for tick in range(4):
    extension_mm = tick / 10
    print(f'{extension_mm:.1f} mm')
# 这样得到了0.0mm，0.1mm，0.2mm，0.3mm

# 计算结果append，空列表要在循环的前面放好
areas_mm2 = []
for side_mm in range(1,5):
    area_mm2 = side_mm ** 2
    areas_mm2.append(area_mm2)
print(areas_mm2)

# 用 sum() 与 len() 计算平均值
masses_g = [7.78, 7.80, 7.82]
mean_mass_g = sum(masses_g) / len(masses_g)
spread_g = max(masses_g) - min(masses_g)
print(f"Mean: {mean_mass_g:.2f} g")
print(f"Range: {spread_g:.2f} g")
'''Mean: 7.80 g
Range: 0.04 g
'''

# 空列表的统计边界
print(len([])) # 0 len sum 为0
# min  max 会报错，没有可以比较的对象
# sum/len 出现 zerodivisionerror

# 推导式 中括号里面写
areas_mm2 = [
    side_mm ** 2 for side_mm in range(1, 5)
]
print(areas_mm2)
# side_mm 是 1234 ， side_mm 每一个都会来平方，得到一个新的列表area_mm2
# []相当于新列表的格式 数据来源range 当前值名称是for a in range 新元素的表达式是**2
forces_n = [0.0, 1000.0, 2000.0, 1500.0]
area_mm2 = 10.0
stresses_mpa = [
    force_n / area_mm2 for force_n in forces_n
]
print(stresses_mpa) # 0 100 200 150
# 定义在后面，force_n in forces_n
volumes_mm3 = [
    side_mm ** 3 for side_mm in range(1, 6)
]
print(volumes_mm3)
print(sum(volumes_mm3))
# 相当于 for 加 append 的循环

# 这里就是使用一个循环的参数变量了，实现次数
ids = ["S01", "S02"]
for sample_id in ids:
    for repeat in range(1, 3): # 两次
        print(sample_id, repeat)
'''S01 1
S01 2
S02 1
S02 2'''
# 两次嵌套推导式拆列表，合并成新的
batches_g = [[7.8, 7.9], [2.7, 2.8]]
flat_g = [
    mass_g for batch in batches_g # mass_g 是我们希望填充进去的，找batches 里面的两个batch batch 是两个小列表
    for mass_g in batch  # 再把 mass_g 拿出来的，从batch里面取值，先大后小拆掉
]
print(flat_g)
# [7.8, 7.9, 2.7, 2.8]

# 推导式变量的作用范围
temp_c = 99
values = [temp_c + 1 for temp_c in [20, 30]] # 希望得到的是temp_c+1 ，temp_c 的取值是20或者30,但是这个temp_c的取法 只是在中括号里面，中括号里面的是另一个temp_c ，作用范围只在括号内，外面没有影响
print(values, temp_c) # [20,30] 99
for temp_c in [20, 30]:
    last_c = temp_c
print(temp_c) # 30

# 生成1—20并逐项打印
for i in range(1,21):
    print(i)
# 生成1—1 000 000，仅打印摘要
s = 0
for j in range(1, 1000001):
    s = s + j
print(f'总和{s}')
# 用步长生成1—20的奇数
list_x = list(range(1,21))
list_odd = [
    i for i in list_x if i % 2 == 1
]
print(list_odd)

# 切片与复制
# 列表[start:stop] 取得从 start 开始、在 stop 之前结束的元素，返回一个新列表
forces_n = [0, 500, 1000, 1500, 1200, 800]
print(forces_n[0:3]) # [0,500,1000]
print(forces_n[2:5]) # [1000, 1500, 1200]
print(forces_n[:3]) # 等价于前面补充0
print(forces_n[3:]) # 等价于后面到最后的一个索引值
print(forces_n[:]) # 等价于整个列表，就是索引的范围
print(forces_n[-2:]) # 这样是左边从倒数第二个开始，到索引的最右边
print(forces_n[:-2]) # 这样是从最左边开始，到倒数第三个（索引值-3）,一共四个
print(forces_n[-4:-1]) # [1000, 1500, 1200] 这是倒数第四个到倒数第二个，一共三个
# 列表[start:stop:step] 的第三项控制取值间隔，例如 [::2] 取得索引 0、2、4 等位置
print(forces_n[::2]) # 整体的0,2,4的索引
print(forces_n[1::2]) # 1,3,5 索引
print(forces_n[::-1]) # -1,-2,-3,-4,-5,-6 这些索引

# 越界索引
forces_n = [0, 500, 1000]
print(forces_n[:10]) # 只有三个元素，现在你让一直取到第十个，不会报错，也是三个取出来
print(forces_n[5:10]) # [5:10] 与 [2:1] 在本例均返回空列表，不会报错
print(forces_n[2:1])
# 直接 forces_n[5] 则会出现 IndexError，这与切片语法的处理方式不同

# 切片复制和批量替换
temps_c = [20, 99, 99, 26]
temps_c[1:3] = [22, 24]
print(temps_c) # [20, 22, 24, 26]
temps_c[2:2] = [23] # 在2的索引前面插入一个23，也就是第二个的后面, [20, 22, 23, 24, 26]
print(temps_c)
del temps_c[1:3]  # [20, 24, 26]
print(temps_c)

# 加上步长
temps_c = [20, 21, 22, 23, 24, 25]
temps_c[::2] = [30, 32, 34] # 所有这样步长的合法的索引全部分别对应改变，024
print(temps_c) # [30, 21, 32, 23, 34, 25]
print(temps_c[::-1])  # [25, 34, 23, 32, 21, 30] 
temps_c = [30, 21, 32, 23, 34, 25]
temps_c[2:2] = [40] # 索引2的前面插入40
print(temps_c)

# 切片案例：选定载荷区间的平均值
forces_n = [0, 500, 1000, 1500, 1200, 800]
window_n = forces_n[1:4]
mean_force_n = sum(window_n) / len(window_n)
print(window_n)
print(f"Mean: {mean_force_n:.1f} N")

# 使用 [:] 复制列表
raw_masses_g = [7.78, 7.80, 7.82]
work_masses_g = raw_masses_g[:] # 这是说从头到尾
# 但是这种复制也是浅复制 相当于 work = raw.copy() 浅复制只新建外层结构，下面以嵌套质量记录比较浅复制、逐行复制和深复制
work_masses_g[0] = 7.79
print(raw_masses_g)
print(work_masses_g)

# 简单赋值会共享同一个列表
raw_ids = ["S01", "S02"]
work_ids = raw_ids # 这是打一个标签
work_ids.append("S03")
print(raw_ids) # ['S01', 'S02', 'S03']
print(work_ids) # ['S01', 'S02', 'S03']
# 两条输出均为 S01、S02、S03，这是同一个列表的两个名称

# 切出来的是一个新的列表，那完全可以切上切
a = [1,2,3,4]
b = a[1:4][0:2]
print(b)

# 元组
# 同一条拉伸记录的原始截面尺寸与标距在计算期间应保持一致，元组适合表达一组固定位置的参数
geometry_mm = (5.0, 2.0, 50.0) # 方便地表示长宽高
area_mm2 = geometry_mm[0] * geometry_mm[1]
print(geometry_mm) # 前两个位置是宽度与厚度，面积为 10.0 mm²
print(f"Area: {area_mm2:.1f} mm^2")

# 只有一个元素的元组
geo = (10,)
print(type(geo)) # <class 'tuple'>
geo = (10) # 这样是一个int

# geometry_mm[0] = 6.0 TypeError: 'tuple' object does not support item assignment 错误原因是元组不支持元素赋值，索引 0 本身在合法范围内

# 遍历元组中的所有值
geometry_mm = (5.0, 2.0, 50.0)
for dimension_mm in geometry_mm:
    print(f"{dimension_mm:.1f} mm")

# 对于 list 和 tuple 的选用
# 保存不断追加的载荷记录	list 适合，使用 append()	tuple 不支持直接追加

# 元组中可变对象的边界
record = ("S01", [7.8, 7.9])
record[1].append(8.0) # 只是对里面的list进行一个append
print(record) # ('S01', [7.8, 7.9, 8.0])
print(type(record), type(record[1]))

# 读取长、宽、高三个尺寸后，给每个位置一个有含义的名称
dimensions_mm = (10, 5, 2)
length_mm, width_mm, height_mm = dimensions_mm # 这样是一下子取出多个值
volume_mm3 = length_mm * width_mm * height_mm
print(length_mm, width_mm, height_mm)
print(volume_mm3)

# 星号解包收集剩余元素，支持list和tuple
sample_id, *masses_g = ("S01", 7.8, 7.9)
print(sample_id)
print(masses_g)
first, *middle, last = (20, 22, 24, 26)
print(first, middle, last)
# 同一层解包只能有一个用于收集剩余元素的星号目标

# 遍历方法
# enumerate() 同时取得序号与值
sample_ids = ["S01", "AL01", "S02"]
for number, sample_id in enumerate(
    sample_ids, start=1 # 本例用 start=1 生成报告序号 1、2、3，不改变列表的实际索引
):
    print(f"{number}. {sample_id}")
'''
1. S01
2. AL01
3. S02
'''

# zip() 同步遍历两组数据
sample_ids = ["S01", "AL01", "S02"]
masses_g = [7.80, 2.70, 7.85]
for sample_id, mass_g in zip(
    sample_ids, masses_g # 使用前仍需确认长度和顺序一致，错位数据也可能正常运行
):
    print(f"{sample_id}: {mass_g:.2f} g")

sample_ids = ["S01", "AL01", "S02", "AL02"]
masses_g = [7.80, 2.70, 7.85] # 如果不匹配呢
for sample_id, mass_g in zip(
    sample_ids, masses_g
):
    print(f"{sample_id}: {mass_g:.2f} g")
''' 运行了，但是这样数据处理就不完全
S01: 7.80 g
AL01: 2.70 g
S02: 7.85 g
'''

# 迭代器与生成器
ids = ["S01", "S02"]
cursor = iter(ids) 
print(next(cursor))
print(next(cursor))
print(ids)

# 读取终点与 StopIteration
cursor = iter([20, 22])
print(next(cursor))
print(next(cursor))
print(next(cursor, "已读完"))
print(next(cursor, "已读完"))
'''
20
22
已读完
已读完
'''
'''
cursor = iter([])
next(cursor)
这样会报错
'''

# 生成器表达式
# 列表推导式先准备全部结果，生成器表达式把逐项计算留到读取时
masses_g = [7.8, 2.7, 8.9]
converted = (m * 1000 for m in masses_g)
print(type(converted))
print(next(converted))
print(list(converted))
print(list(converted))
