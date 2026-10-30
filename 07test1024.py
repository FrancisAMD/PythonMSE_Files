
# %% 第1题 读取并计算试样密度
# 使用input()依次读取试样质量（g）和体积（cm³），转换为浮点数。
# 计算密度，并输出结果，保留两位小数。
# 假设输入均为合法的正数，不需要校验。
# 示例输入：7.8、1.0
# 预期输出：密度：7.80 g/cm³
# 评分：读取两个输入1分，正确转换1分，计算1分，输出格式1分。

# ---------- 开始作答 ----------

mass_g = float(input("请输入试样质量（g）："))
volume_cm3 = float(input("请输入试样体积（cm³）："))
density_gcm3 = mass_g / volume_cm3
print(f'密度: {density_gcm3:.2f} g/cm3')

# ---------- 作答结束 ----------


# %% 第2题 使用while收集试样编号
# 创建空列表samples，用while循环反复读取编号。
# 每次先用strip()去除首尾空格，再用upper()统一为大写。
# 输入q（不区分大小写）时结束；空编号跳过；其余编号加入列表。
# 结束后输出samples。本题允许重复编号。
# 示例：依次输入s01、空字符串、s02、q
# 预期输出：['S01', 'S02']
# 评分：列表初始化1分，循环及退出2分，跳过空编号1分，添加与输出1分。

# ---------- 开始作答 ----------

samples = []
while True:
    sid = input("请输入试样编号（输入q退出）：").strip().upper()
    if sid == "Q":
        break
    if not sid:
        continue
    samples.append(sid)
print(samples)

# ---------- 作答结束 ----------


# %% 第3题 使用while转移列表元素
# 已给出原始列表original，请补充代码：
# 复制original为pending，创建空列表completed。
# 使用while和pop()，将pending末尾的元素逐个移入completed。
# 依次输出original、pending、completed，要求original保持不变。
# 预期输出：
# ['S01', 'S02', 'S03']
# []
# ['S03', 'S02', 'S01']
# 评分：复制列表1分，completed初始化1分，循环转移2分，输出1分。

original = ["S01", "S02", "S03"]

# ---------- 开始作答 ----------

pending = original.copy()
completed = []
while pending:
    completed.append(pending.pop())
print(original)
print(pending)
print(completed)



# ---------- 作答结束 ----------


# %% 第4题 使用字典登记质量
# 用下列题干代码完成登记程序，将1至4的pass替换为正确代码。
# 输入q时结束；空编号或重复编号跳过本轮；其余编号读取质量并存入字典。
# 假设输入的质量均为合法的正数，无需校验。
# 字典以试样编号为键，以质量（g）为值。
# 验证：依次输入s01、7.8、S01、s02、2.7、q。
# 注意：输入重复编号S01后，不应再询问质量。

# 请取消下面代码的注释并补全4处pass，再运行本题。
# 未完成代码暂用注释关闭，避免直接运行时无法退出。
# pass只是占位语句，作答时需替换，不是本题答案。
#
records = {}  # 1 创建空字典records
while True:
    sid = input("编号，q退出：").strip().upper()
    if sid == "Q":
        break
    if sid == "" or sid in records:
        continue
    mass_g = float(input("质量/g："))
    records[sid] = mass_g
print(records)
#
# 请将验证结果写在下一行注释中：
# 验证结果：{'S01': 7.8, 'S02': 2.7}

# %%
