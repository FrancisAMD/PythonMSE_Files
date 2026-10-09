# 材料程序语言基础（Python） 第1—3章随堂编程练习
# 学号：526051910085
# 姓名：张展飞
# 请另存为“学号_姓名.py”，提交前保存并从头运行。
# 各题独立。不能直接输出预期答案代替计算、提取或列表操作。
# 第1题错误代码以注释给出，请在其下方写出修正后的程序。
# 其余题目已提供初始数据，请在相应位置继续编写。

# %% 第1题 修正平均温度程序（10分）
# 待修改程序：
# temperature_1 = 20
# temperature_2 = 24
# temperature_3 = 28
# average_c = temperature_1 + temperature_2 + temperature_3 / 3
# Print("平均温度：", average)
# 在下方写出修正后的程序，并添加一条用途注释：
temperature_1 = 20
temperature_2 = 24
temperature_3 = 28
average_c = (temperature_1 + temperature_2 + temperature_3) / 3
print("平均温度：", average_c)
# 忽略了运算符的先后顺序，运算错误，这样是先求和，下面变量名也搞错了，print而非Print


# %% 第2题 计算圆片面积并判断范围（15分）
radius_text = "4.0"

# 1. 导入 math 模块，将 radius_text 转换为浮点数，保存为 radius_mm。
# 2. 按“面积 = π × 半径²”计算 area_mm2，其中 π 使用 math.pi；用 f-string 输出面积，保留两位小数。
# 3. 用比较表达式判断面积是否在 40～60 mm² 范围内（包含两个端点），输出 True 或 False。不需要写 if 语句。
# 在下方继续编写：

import math as m
from unittest import result
radius_mm = float(radius_text)
area_mm2 = m.pi*radius_mm**2
print(f'面积是{area_mm2:.2f}')
print(40 <= area_mm2 <= 60)


# %% 第3题 整理并提取试样编号（15分）
raw_code = "  b02-s05  "

# 1. 去掉两端空格，将字母统一为大写，把结果保存为 clean_code，保留 raw_code 不变。
# 2. 用切片提取前三个字符作为批次编号 batch_id，提取最后三个字符作为试样编号 sample_id。
# 3. 输出完整编号、批次编号和试样编号。
# 在下方继续编写：

clean_code = raw_code.strip()
clean_code = clean_code.upper()
# 相当于一步：clean_code = raw_code.strip().upper()
print(clean_code)
batch_id = clean_code[:3]
sample_id = clean_code[-3:]
print(clean_code,batch_id,sample_id)

'''字符：   B   0   2   -   S   0   5
   正索引： 0   1   2   3   4   5   6
   负索引：-7  -6  -5  -4  -3  -2  -1'''
'''字符串[start:end]
包含 start，不包含 end，即左闭右开。
start 省略表示从头开始。
end 省略表示到末尾结束。
正索引从左往右，从 0 开始。
负索引从右往左，-1 是最后一个字符。'''

# %% 第4题 维护待测试样清单（20分）
pending = ["S01", "S02", "S04"]

# 1. 将第2个编号 "S02" 更正为 "S03"。
# 2. 在末尾追加 "S05"。
# 3. 将优先测试的 "S00" 插入最前面。
# 4. 使用 pop() 取出当前清单的第2个试样，将其编号保存为 current_id。
# 5. 使用 remove() 按值删除 "S04"。完成全部操作后，输出 current_id 和剩余清单 pending。
# 在下方继续编写：

pending[1] = "S03"
pending.append("S05")
pending.insert(0,'S00')
current_id = pending.pop(1)
pending.remove("S04")
print(current_id,pending)


# %% 第5题 保留原始记录并整理副本（20分）
raw_c = [32, 20, 28, 24, 36]

# 1. 复制一份列表并命名为 work_c；后续整理不得改变 raw_c。
# 2. 先将 work_c 中的第1个读数改为 30，再使用 sort() 对 work_c 进行升序排序。
# 3. 分别输出原始列表 raw_c、整理后的 work_c，以及用切片取得的 work_c 前3项。
# 在下方继续编写：

work_c = raw_c.copy()
work_c[0] = 30
work_c.sort()
print(raw_c,work_c,work_c[0:3])


# %% 第6题 批量换算并汇总载荷（20分）
loads_n = [1000, 1500, 1200, 1800, 2000]

# 1. 用一条单层列表推导式将所有读数换算为 kN，保存为 loads_kn 并输出。
# 2. 使用 sum()、len()、max() 计算平均载荷和最大载荷；均保留两位小数输出，并标明单位 kN。
# 3. 用另一条单层列表推导式，筛选 loads_kn 中不小于 1.5 kN 的值，保存为 selected_kn 并输出，保持它们原有的先后顺序。
# 在下方继续编写：

loads_kn = [m/1000 for m in loads_n]
print(loads_kn)
ave_kn = sum(loads_kn)/len(loads_kn)
max_kn = max(loads_kn)
print(f'平均载荷：{ave_kn:.2f}kN，最大载荷：{max_kn:.2f}kN')
selected_kn = [m for m in loads_kn if m >= 1.5]
print(selected_kn)

# %% 第7题 提取一组测量数据（补充练习）
hardness = [198, 205, 201, 210, 196, 203]

# 1. 输出第1个测量值和最后1个测量值。
# 2. 使用切片取得第2～第4个测量值，保存为 middle_data。
# 3. 输出测量值的个数。
# 在下方继续编写：

print(hardness[0],hardness[-1])
middle_data = hardness[1:3]
print(len(hardness))

# %% 第8题 整理试样编号（补充练习）
raw_ids = "S01,S02,AL01,S03"

# 1. 使用 split() 将字符串拆分为列表，保存为 sample_ids。
# 2. 输出试样列表、试样数量和第2个试样编号。
# 3. 在列表末尾追加 "S04"。
# 4. 使用 join() 将修改后的列表重新连接为字符串，各编号之间使用 " | " 分隔，保存为 result 并输出。
# 在下方继续编写：

sample_ids = raw_ids.split(",")
print(sample_ids,len(sample_ids),sample_ids[1])
sample_ids.append('S04')
result = "|".join(sample_ids)
print(result)
