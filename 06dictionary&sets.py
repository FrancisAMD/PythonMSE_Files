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
'''
for elem in composition_wt:
    s += composition_wt[elem]
# print(s)
composition_wt['Fe'] = 100 - s
'''
# 可以用sum value 替代
composition_wt['Fe'] = 100 - sum(composition_wt.values())

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

for elem, pt in (
    composition_wt.items()
):
    print(f'element:{elem},weight percent:{pt}') # 组合输出键和值
# 同理，.keys()或者不加，默认都输出键，.values()输出值

# key ijn dictionary 可以检查键
composition = {'Fe':88.0, 'Cr':12.0}
required_elements = ['Fe','Cr','Mn','Ni']
#??????

# 按照特定的顺序遍历键
composition = {'Fe':88.0, 'Cr':12.0}
# for element in composition.sorted():

# 字典视图与列表快照
mass_by_id = {"S01":7.8}
keys_view = mass_by_id.keys()
keys_snapshot = list(keys_view) # 拿出来了就是静止在新的里面的
mass_by_id['S02'] = 7.85
print(list(keys_view)) # ['S01','S02'] keys values items 返回的值会动态更新
print(keys_snapshot) # ['S01']

# 键和值的比较
a = {'S01': 7.8}
b = {'S02': 7.8}
print(a.keys() == b.keys)
print(a == b) # 都是 Ture

# 集合set 不同，自动去重
state_by_id = {"S01": "annealed",
               "S02": "normalized",
               "S03": "annealed"}
unique_states = set(state_by_id.values())
print(sorted(unique_states)) # 进行排序
print(len(unique_states))


elements = {"Fe", "Cr", "Fe"}
empty_mapping = {}
empty_set = set()
print(sorted(elements))
print(type(empty_mapping), type(empty_set))

# 字典的推导式
wt_pct = {'Fe':88.0, 'Cr':12.0}
fractions = {
    element : pct / 100
    for element, pct in wt_pct.items()
}
print(fractions)

# 两个列表建立字典
sample_ids = ["S01", "S02"]
masses_g = [7.8, 7.85]
if len(sample_ids) != len(set(sample_ids)): # 进行去重，防止mass有重复的
    print("Duplicate sample IDs")
else:
    mass_by_id = dict(zip(
        sample_ids, masses_g, strict=True))
    print(mass_by_id)

# 列表嵌套字典，然后二维地，从嵌套的里面进行取值
s1 = {"id": "S01", "mass_g": 7.80}
s2 = {"id": "S02", "mass_g": 7.85}
s3 = {"id": "AL01", "mass_g": 2.70}
samples = [s1, s2, s3]
for sample in samples:
    print(f"{sample['id']}: "
          f"{sample['mass_g']:.2f} g")