# 列表
sample_ids = ["S01","AL01","S02",4,6,7,9] # 元素类型是任意的
print(sample_ids)
print(type(sample_ids).__name__)
print(len(sample_ids))
print(sample_ids[0],sample_ids[-1]) # -1 是最后一个
print(sample_ids[1:3]) # 索引1到3，不包括右边，只是1，2两个，就是第二第三位
print(sample_ids[1:2]) # 单个也是列表，就像字符串那样

# 改动
sample_ids = ["S01","AL01","S02"]
first_id = sample_ids[0] # 新开一个地址，多一个罐子，单元素的
sample_ids_new = sample_ids # 贴一个标签，引用原内存地址
sample_ids[0] = 'x'
print(first_id)
print(sample_ids)
print(sample_ids_new)

# 各种复用
raw = [7.8, 2.7]
work = raw # 这是不拷贝，只是一个别名 y is x，同一个对象
work[0] = 7.9 
print(raw) # [7.9,2.7]
work = [8.0, 3.0] # 重新给 work 赋值会改变这个名称的关联，不会把 raw 一起改成新列表
print(raw) # 7.9
print(work) # 8.0

x=[1,2]
y = x.copy() # 这是浅拷贝，快速的，新列表，但是元素引用相同，等价于y=x[:]
raw = [0, 2, [3, 4]]  
shallow_copy = raw.copy()
shallow_copy == raw # True 两者是相等的
shallow_copy is raw # False 两者不是一个（已经有两个容器了）
shallow_copy[0] = 1 # 把新的的第一个位置的值变成1                  
shallow_copy[2].append(5)  # 第二位添加了一个5   
print(raw) # [0, 2, [3, 4, 5]]
print(shallow_copy) # [1, 2, [3, 4, 5]]
# 原来的和新的，前面的浅层的相对独立，但是二层嵌套的容器时共享的内存地址
import copy
y = copy.deepcopy(x)
# 深拷贝这样没有什么好说的，完全独立的内存地址

# S01
# ['x', 'AL01', 'S02']
# ['x', 'AL01', 'S02']

# 创建列表
print(["Fe"]) # 这是直接得到 ['Fe']
print(list("Fe")) # ['F', 'e'] list这个函数，list(数据来源) 依次读取其中的元素，组成一个新列表
print(list())
print([])
print(list([7.8, 2.7]))

# 转换为列表
'''list()这个函数本身就可以把别的转换进来'''
list((3,5,7,9,11)) # [3, 5, 7, 9, 11] 元组
list(range(1, 10, 2)) # [1, 3, 5, 7, 9] range 步长的这个运算可以一下子搞出来
list({3,7,5}) # [3, 5, 7] 集合转换，怎么直接升序排序了
list({3,7,5}) # ['a', 'c', 'b']
list({'a':3, 'b':5, 'c':7}.items()) # [('b', 5), ('c', 7), ('a', 3)]





# 访问，通过索引，0，。。。长度-1
sample_ids = ["S01", "AL01", "S02"]
first_id = sample_ids[0] # 这是又打了一个标签
print(first_id) # S01 也可以用-3来访问这个 S01
print(type(first_id)) # <class 'str'> 一个字符串

# 嵌套列表
measurements = [[7.8, 7.9], [2.7, 2.8]] 
print(measurements[1])
print(measurements[1][0]) # 多个访问的时候要各个方括号，而不是[1,0]
print(len(measurements), len(measurements[0])) # 2 2

# 字符串可拆分各个单字
raw = "S01,7.85,1.0"
fields = raw.split(",") # 用,来分隔，最后得到一个列表
print(fields)
print(" S01   7.85 ".split())
print("S01,,1.0".split(","))
# fields = "S01,,1.0".split(",")
# float(fields[1]) 拆完了以后，[1]是一个空的字符串，不能用float转换，（只能是浮点数的字符串），这样两个一起的 TypeError

# join() 把字符串列表连接成字符串
ids = ["S01", "S02", "AL01"]
print(", ".join(ids)) # S01, S02, AL01
fields = ["S01", f"{7.85:.2f}", "1.0"]
print(",".join(fields)) # 这样返回的就是一个字符串 S01,7.85,1.0
# ",".join(["S01", 7.85]) 这样不行，7.85是float，必须是join字符串才可以

# 修改元素，是对原来的内存地址的对象操作，改变的是原来的列表
ali = [0,1,2,3]
ali.append(5)
print(ali)
sample_ids = ["S01", "S02"]
sample_ids.append("AL01")
print(sample_ids) # ['S01', 'S02', 'AL01']
# 将任意对象object追加至列表尾部，不影响已有元素的下标和列表在内存中的起始地址

# 删除列表中的所有元素
ids = ["S01", "S02"]
shared = ids # 标签
ids.clear() # 对ids清空操作
print(shared) # [] 指向一个空的罐子
ids = ["S03"]
shared = ids
del ids # 只是移除ids的标签
print(shared) # ['S03'] 另外的标签不受影响（原来的东西没有变化）

'''copy()
# 返回当前列表对象的浅复制
count(value, /)
# 返回value在列表中的出现次数
extend(iterable, /)
将可迭代对象iterable中所有元素追加至列表尾部，不影响列表引用和原有元素的下标
insert(index, object, /)
在列表的index位置前面插入对象object，该位置及后面所有元素自动向后移动，索引加1
index(value, start=0,
      stop=10000,  /)
返回下标[start, stop)中第一个值为value元素的下标，若不存在值为value的元素则抛出异常，start默认为0表示从头开始，stop默认值表示最大允许的下标值
pop(index=-1, /)
删除并返回下标为index的元素，该位置后面的所有元素向前移动，索引减1。index默认为-1，表示删除并返回列表中最后一个元素。列表为空或者下标index不存在时抛出异常
remove(value, /)
删除第一个值为value的元素，被删除元素位置之后的所有元素向前移动，索引减1；列表中不存在值为value的元素时抛出异常
reverse()
对列表进行原地翻转，逆序
sort(*,key=None, reverse=False)
对元素进行原地排序，参数key指定排序规则，给定规则下相等的元素保持原来的相对顺序，参数reverse表示升序（False）或降序（True）

'''
# append extend 区别
new_ids = ["S02", "S03"]
grouped = ["S01"]
flat = ["S01"]
grouped.append(new_ids)
flat.extend(new_ids)
print(grouped) # ['S01', ['S02', 'S03']] append 只是把这个东西塞到后面
print(flat) # ['S01', 'S02', 'S03'] extend会拆开列表

ids = ["S01"]
ids.extend("S02")
print(ids) # ['S01', 'S', '0', '2']

# insert 插入元素
sample_ids = ["S01", "S03"]
sample_ids.insert(1, "S02")
sample_ids.insert(0, "S00")
print(sample_ids) # ['S00', 'S01', 'S02', 'S03']

# del 删除
sample_ids = ["S01", "S02", "S03"]
del sample_ids[1]
print(sample_ids)
print(sample_ids[1])

# pop 删除并取得末尾元素
pending_ids = ["S01", "S02", "S03"]
current_id = pending_ids.pop() # 对原来的用.pop，然后这下current 被赋值上了末位的元素
print(pending_ids) # ['S01', 'S02']
print(f"Selected: {current_id}") # Selected: S03
# 带上参数可以指定索引，弹出相应的元素
pending_ids = ["S01", "S02", "S03"]
current_id = pending_ids.pop(1) # 把扔出来的索引1 的弹出来赋值给current
print(f"Testing: {current_id}") # Testing: S02
print(pending_ids) #['S01', 'S03']
# 这样的返回删掉的值，相当于是一种回显，侦听到你删掉的是什么

# remove 不依靠索引，只是匹配第一个出现的值
pending_ids = ["S01", "S02", "S03"]
cancelled_id = "S02"
pending_ids.remove(cancelled_id)
print(pending_ids) # ['S01', 'S03']
print(f"Cancelled: {cancelled_id}") # Cancelled: S02

# 删掉不存在的会bug
sample_ids = ["S01", "S02", "S01"]
sample_ids.remove("S01")
print(sample_ids) # ['S02', 'S01']
# sample_ids.remove("S99")  # ValueError

# 成员检测
sample_ids = ["S01", "S02", "AL01"]
print("S02" in sample_ids) #T
print("S03" not in sample_ids) #T
print("S0" in sample_ids) #F
print("S0" in "S01") #T

# 计算出现的次数，以及某个元素首次出现的索引
ids = ["S01", "S02", "S01", "S03"]
print(ids.count("S01")) # 2
print(ids.index("S01")) # 0
print(ids.index("S01", 1)) # 2 从1号索引开始找，发现在2索引上有
print(ids.count("S99")) # 0

# 列表拼接和重复
morning = ["S01", "S02"]
afternoon = ["S03"]
print(morning + afternoon)
print(morning)
print([0] * 3)
print([2, 3] * 2)

# 重新赋值
a = ["S01"]
shared = a
a += ["S02"] # 扩展当前的列表，而不是新赋值
print(shared) # ['S01', 'S02']
a = a + ["S03"] 
print(a) # ['S01', 'S02', 'S03'] 建立了新的列表，是无关的
print(shared) # ['S01', 'S02']

# sort 是修改源列表
# sort() 直接改变原列表的排列，对统一格式的编号，可按字符串的比较顺序排序
sample_ids = ["S03", "S01", "S02"]
sample_ids.sort()
print(sample_ids) # ['S01', 'S02', 'S03']

# 降序排列
masses_g = [7.80, 7.70, 7.90]
masses_g.sort(reverse=True)
print(masses_g) # [7.9, 7.8, 7.7]

# 字符串排序和数值排序
sample_ids = ["S1", "S10", "S2"]
masses_g = [7.8, 10.0, 2.7]
sample_ids.sort()
masses_g.sort()
print(sample_ids) # ['S1', 'S10', 'S2']
print(masses_g) # [2.7, 7.8, 10.0]
resample = ['A8','B7','C6']
resample.sort(reverse=1)
print(resample) # ['C6', 'B7', 'A8']

# sorted 返回一个新的列表
sample_ids = ["S03", "S01", "S02"]
report_ids = sorted(sample_ids,reverse=1)
print(report_ids) # ['S03', 'S02', 'S01']
print(sample_ids) # ['S03', 'S01', 'S02']

# key 指定排序的依据
ids = ["S100", "S2", "AL03"]
print(sorted(ids))
print(sorted(ids, key=len))
print(ids)

# lambda 可以写小函数，作为排序依据
print((lambda mass_g: mass_g * 1000)(2.7)) # 2700.0
print((lambda item: item[1])(["S01", 7.8])) # 7.8

# reverse 是按照索引来进行全部的反转，而不是sort(reverse=1)
sample_ids = ["S03", "S01", "S02"]
sample_ids.reverse()
print(sample_ids) # S02', 'S01', 'S03'] 直接对原来的操作
sample_ids.reverse()
print(sample_ids) # ['S03', 'S01', 'S02'] 回来了

# 列表大小比较是逐个进行的
print([7, 100] < [8, 0]) #1
print([7, 8] < [7, 8, 0]) #1
print([7, 8] == [8, 7]) #0
print((7 + 100) < (8 + 0)) #0

# len 看长度
sample_ids = ["S01", "AL01", "S02"]
print(len(sample_ids))
sample_ids.append("S03")
print(
    f"Registered: {len(sample_ids)}"
    " samples"
)
print(sample_ids[-1])

# shuffle 随机打乱列表
x = list(range(11)) # range 转换出来，也就是[1,2,3,4,5,6,7,8,9,10]
from json import load
from random import shuffle
shuffle(x) 
print(x) # [3, 10, 5, 2, 9, 0, 4, 1, 7, 6, 8]
print(all(x)) # False
print(any(x)) #True
max(x)
10
max(x, key=str) 
9
min(x)
0

# 简单计算
print(sum(x)) # 55
print(list(zip(x,[1*11]))) #[(0, 1), (6, 1), (10, 1), (9, 1), (8, 1), (7, 1), (4, 1), (5, 1), (2, 1), (1, 1), (3, 1)] 
print(list(zip(['a', 'b', 'c'], [1, 2]))) #[('a', 1), ('b', 2)]

# 列表批量计算
masses_g = [7.80, 2.70, 7.85]
masses_mg = [m * 1000 for m in masses_g] 
# 这样是从这个里面以此拉出来每一个元素，乘上，然后形成一个新的list
# 这种是列表推导式 
# [expression for item in source if condition] 可以在后面加if 表示对应条件的才进行运算
print(masses_mg) # [7800.0, 2700.0, 7850.0]
#逐项追加
masses_g = [7.80, 2.70, 7.85]
masses_mg = []
for m in masses_g:
    masses_mg.append(m * 1000)
    # 对我这个新的列表进行append追加的操作，可以一次次得到新的列表
print(masses_mg)
masses_g = [7.80, 2.70, 7.85]
masses_mg = [m*1000 for m in masses_g if m>3]

# 去除两端空白
raw_ids = [" S01", "AL01 ", " S02 "]
clean_ids = [s.strip() for s in raw_ids]
print(clean_ids) # ['S01', 'AL01', 'S02']
print(raw_ids) # [' S01', 'AL01 ', ' S02 ']
# 等价的处理
raw_ids = [" S01", "AL01 ", " S02 "]
clean_ids = []
for sample_id in raw_ids:
    clean_ids.append(sample_id.strip())

# 平铺嵌套列表
groups = [[180, 185], [190, 195], [200, 205]]
hardness = [h for group in groups for h in group] 
# 这个hardness 的新的列表是h的元素，h是在第二个for里面的，也就是一个个最基本的数
print(hardness) # [180, 185, 190, 195, 200, 205]
# 等价的
groups = [[180, 185], [190, 195], [200, 205]]
hardness = []
for group in groups:
    for h in group:
        hardness.append(h)
# 操作相当于深入两层，循环读取

# 列表切片
loads_n = [0, 10, 20, 30, 40, 50]
segment = loads_n[1:4]
print(segment) # [10, 20, 30]，这样取出来的是列表
segment2 = loads_n[1:2]
print(segment2) # [10]，即使是一个元素，仍然切片出来的也是列表
# [1:1] 得到的是空的列表
# items[start:end:step] 包含起点的索引，但是不包含终点

