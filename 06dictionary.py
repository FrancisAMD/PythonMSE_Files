# Python 字典
sample = {'sample_id': 'S01', 'mass_g': 7.80} # Key:Value
print(sample['sample_id'])
# 字典的键一定是唯一的，值随意
# 键必须可哈希，只能是一个正常的不变的这种，不能说键是一个列表，值随意
# 元组本身是不可变的，可以作为键值
names = {("B01","B02"): "B name", ("C01","C02"): "Cname"}
# 加值比较方便
sample["volume_cm3"] = 1.00
print(
    f'{sample["sample_id"]}的密度是：{sample["mass_g"] / sample["volume_cm3"]}'
)

# 访问
for sam in sample:
    print(sam) 
'''sample_id
mass_g
volume_cm3'''

# 首先可以定义空的字典，也可以先写出来key，value先填充上None。

# dict 构造函数
a = dict(id="S01",mass_g=7.8) # 来自成对数据
pairs = [("id","S01"),("mass_g",7.8)]
b = dict(pairs)
print(a == b) # ???

# from keys 初始化已知字段
fields = ["mass_g","volume_cm3"]
record = dict.fromkeys(fields)
record["mass_g"] = 7.80
print(record) # {'mass_g': 7.8, 'volume_cm3': None}

# pop 移除字段并且返回原值
record = {'id':'S01', 'note':'复核'}
note = record.pop('note')
print(note)
print(record)

# popitem
record = {'id':'S01', 'note':'复核'}
key, value = record.popitem() # 直接输出最后一个
print(key, value)

# get 获取key对应的值了
sample = {'sample_id': 'S01'}
state = sample.get('sample_id')
print(state)

# 打印键和值获取
print('============')

sample = {}
sample['id'] = 'S02'
sample['material'] = 'Steel'
sample['status'] = 'Annealed'
sample['mass'] = '10.00g'
for key,value in sample.items(): # 这样可以全把键和值都打印出来
    print(key,value)

for s in sample:
    print(f'{s}={sample[s]}') # 可以去套if 来做到

# 字典遍历
# 质量百分比到原子数百分比的转换
# Fe-16Cr-1Mn-0.1C 这样是质量的百分比
print('============')

composition_wt_list = [('Cr',16),('Mn',1),('C',0.1)]
composition_wt = dict(composition_wt_list)

s = 0.0
for elem in composition_wt:
    s += composition_wt[elem]
# print(s)
composition_wt['Fe'] = 100 - s

# for elem in composition_wt:
#    print(elem,composition_wt[elem])

atomic_mass_list = [('Cr',51.996),('Fe',55.845),('C',12.011),('Mn',54.938)]
atomic_mass = dict(atomic_mass_list)

molar_pct = {}
total_mole = 0.0
for elem in composition_wt:
    total_mole += composition_wt[elem] / atomic_mass[elem]
for elem in composition_wt:
    molar_pct[elem] = composition_wt[elem] / atomic_mass[elem] / total_mole * 100
    print(f'{elem} 的摩尔百分比是 {molar_pct[elem]:.2f}%')