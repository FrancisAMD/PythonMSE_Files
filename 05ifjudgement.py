# if 语句
# 首先需要关心条件的判断
width_mm = 5.0
is_positive = width_mm > 0 
print(f'是否为阳性：{is_positive}')

# 检查是否相等
state = "annealed" # 退火状态
print(state == "quenched") # 是退火还是淬火状态 # False
# 因为大小写的状态类型在string里面不同，所以最好先转换相同，并且去掉空格
raw_state = " Annealed "
raw_state.strip().lower()
print(state == "annealed")
# >=一般用作是阈值检查的关系
for strength_mpa in [299.0, 300.0, 300.1]:
    print()
time_min = [5,10,17,24,30,35,40,50]
for time in time_min:
    if time<=10:
        print(f'time = {time}, status = eating')
    elif 10<=time<=30:
        print(f'time = {time}, status = annealing')
    else:
        print(f'time = {time}, status = quenching')
# and 连接条件
strength_mpa = 320.0
elongation_pct = 10.0
strength_ok = strength_mpa >= 300.0
ductility_ok = elongation_pct >= 12.0
print(strength_ok, ductility_ok)
print(strength_ok and ductility_ok) # 只有两个都成立，整体条件才成立

# 浮点近似比较
import math
measured_mm, reference_mm = 10.008, 10.000
print(math.isclose(
    measured_mm, reference_mm,
    rel_tol=0.0, abs_tol=0.01, # 相对误差（这里0.0表示禁用这个，绝对误差
)) # 近似比较是可以的

# in 检查是不是在列表中
print(5 in time_min) # True

# 允许状态清单
state = "normalized"
allowed_states = ["annealed", "normalized"]
print(state in allowed_states)
print("quenched" in allowed_states)
# 可以
status_list = ["pending","running","submitted","finished","error"]
# folder_list = [0,1,2,3,4]
folder_list = list(range(len(status_list))) # 这样扩展性更好
for folder,status in zip(folder_list, status_list):
    if status == "finished":
        print(folder, status) # 索引3 完成了
    elif status == "error":
        print(folder, status) # 索引4 错误了

# pass 保留一个合法的空操作
state = "ready"
if state == "ready":
    pass
    print("继续检查尺寸")
print("结束本次判断")

# 分支赋值判断
stresses_mpa = [230,450,100,300.1,299]
for num, stress in enumerate(
    stresses_mpa, start=1
):
    if stress >= 300:
        lebal = "meet threshold"
    else:
        lebal = "below threshold"
    print(f'编号{num}, {stress}, {lebal}')

# 简单书写 快速选择性赋值给一个变量
strength_mpa = 320.0
label = (
    "meets" if strength_mpa >= 300
    else "below"
)
print(label)

# 注意elif 的判断前提是包含上下文的
elongation_pct = 15.0
if elongation_pct < 10:
    band = "A"
elif elongation_pct < 20: # 注意这里已经内置了前提了，10-20已经内含了
    band = "B"
else:
    band = "C"
print(band)

# 校验密度
mass_g , volumn_cm3 = 7.8, 1.0
if mass_g <= 0 or volumn_cm3 <=0:
    print("invalid value")
elif 7.6 <= mass_g/volumn_cm3 <= 8.0:
    print("in the right range")
else:
    print("not in the right range")

# 练习
status_list = ["ready","missing","error"]
sample_ids = list(range(len(status_list)))
for id, status in zip(sample_ids, status_list):
    if status == "ready":
        print(f"id{id}, CONTINUE")
    elif status == "missing":
        print(f"id{id}, DATA MISSING")
    else:
        print(f"id{id}, IN NEED OF OPERATION")

# if 处理列表
sample_ids = ["T01", "T02", "T03"]
for sample_id in sample_ids:
    if sample_id == "T02":
        print(f"{sample_id}: "
                  "missing geometry")
    else:
        print(f"{sample_id}: inspect inputs")
# 一批待测试样中，T02 缺少几何记录，循环仍处理整批清单，并对该编号输出特定提示

# 3整除
nums = list(range(1,20))
list1, list2 = [], []
for num in nums:
    if num % 3 == 0:
        list1.append(num)
    else:
        list2.append(num)
print(f'被三整除:{list1}，不能被三整除:{list2}')

# 有些数据源用 NaN 表示未得到有效数值，仅用 x > 0 不能覆盖所有数值异常
import math
for value in [
    0.0,
    300.0,
    float("nan"),
    float("inf"), # inf 是无穷大
]:
    print(value, math.isfinite(value))
# math.isfinite(x) 检查 x 既不是 NaN 也不是正负无穷大，0.0也属于有限数
'''
0.0 True
300.0 True
nan False
inf False
'''

# 现有和需要交叉核对
available = ["mass", "dimensions", "tensile"]
requested = ["mass", "hardness", "tensile"]
for method in requested:
    if method in available:
        print(f"{method}: available")
    else:
        print(f"{method}: arrange separately")

# 首先规范化大小写
current = ["T01", "T02", "AL01"]
normalized = [sid.upper() for sid in current]
for raw_id in [" t02 ", "T03"]:
    sample_id = raw_id.strip().upper()
    if sample_id in normalized:
        print(f"{sample_id}: duplicate")
    else:
        print(f"{sample_id}: available")

# 简单是if列表推导式
strengths_mpa = [280.0, 300.0, 320.0]
selected = [
    x for x in strengths_mpa if x >= 300
]
print(selected)
print(strengths_mpa)

# all与any：汇总一组布尔检查
forces_n = [0.0, 1000.0, 2000.0]
nonnegative = [
    force >= 0 for force in forces_n # 输出的是三个True
]
print(nonnegative)
print(all(nonnegative)) # 全部都是在？？？？
print(any([force < 0 for force in forces_n]))
'''all 的输入是每条检查结果，any 的输入是是否异常的结果，名称应体现 True 的含义
本页先保存布尔列表，便于打印核查；也可使用第4章学过的生成器表达式逐项检查
all([]) 为 True，any([]) 为 False，要求存在记录时，应先检查列表非空
'''

# 为第1至第9个试样打印英文序数
for position in range(1, 10):
    if position == 1:
        suffix = "st"
    elif position == 2:
        suffix = "nd"
    elif position == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{position}{suffix}")

# 条件式多个需要进行规范化的处理
strength_mpa, elongation_pct = 320.0, 15.0
if (
    strength_mpa >= 300.0 # 写成多个两行
    and elongation_pct >= 12.0
):
    print("Meets both teaching thresholds")



# print(float('nan')==3/0)