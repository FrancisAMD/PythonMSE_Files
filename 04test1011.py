
# 材料程序语言基础 (Python) 第4章随堂编程练习
# 学号: 526051910085
# 姓名: 张展飞
# 建议用时: 10分钟.
# 请另存为 "学号_姓名.py", 保存后从头运行.
# 各题独立, 不能直接输出预期答案代替计算或列表操作.
# 第1题的待修改代码以注释给出, 请在其下方写出修正后的程序.
# 其余题目已提供初始数据, 请在相应位置继续编写.


# %% 第1题 修正循环程序
# 已知载荷单位为 N, 原始截面积单位为 mm².
# 应力 = 载荷 / 原始截面积, 计算结果单位为 MPa.
#
# 待修改程序:
# forces_n = [0, 500, 1100, 1600, 2000]
# area_mm2 = 10.0
# for force_n in forces_n
#     stress_mpa = force_n / area_mm2
# print(stress_mpa)
#
# 1. 程序中有两处错误, 请修改, 然后用 print() 逐点输出应力值.
# 2. 在循环结束后, 使用 len() 输出载荷列表中的采样点数量,
#    数量只输出一次.
# 3. 将逐点输出改为 f-string, 应力保留一位小数,
#    并在数值后显示单位 MPa.
# 在下方写出修正后的完整程序:

forces_n = [0, 500, 1100, 1600, 2000]
area_mm2 = 10.0
for force_n in forces_n:
    stress_mpa = force_n / area_mm2
    print(f"应力: {stress_mpa:.1f} MPa")
print(f"采样点数量: {len(forces_n)}")


# %% 第2题 构造应力列表
forces_n = [0, 450, 910, 1500]
area_mm2 = 10.0

# 1. 用一条列表推导式计算所有应力,
#    将生成的列表赋给变量 stresses_mpa, 并输出该列表.
# 2. 使用 max() 求最大应力, 将结果赋给变量 max_stress_mpa,
#    并输出该变量的值.
# 3. 使用 sum() 和 len() 计算平均应力,
#    将结果赋给变量 mean_stress_mpa, 并输出该变量的值.
# 在下方继续编写:

stresses_mpa = [force_n / area_mm2 for force_n in forces_n]
print(stresses_mpa)
max_stress_mpa = max(stresses_mpa)
print(f'最大应力: {max_stress_mpa} MPa')
mean_stress_mpa = sum(stresses_mpa)/len(stresses_mpa)
print(f'平均应力： {mean_stress_mpa} MPa')


# %% 第3题 复制与切片
raw_hv = [198, 205, 201, 210, 196]

# 1. 使用切片或 copy() 复制 raw_hv,
#    将新列表赋给变量 work_hv, 再将 work_hv 的第2项改为 207.
# 2. 用切片提取 work_hv 的前3项,
#    将得到的列表赋给变量 first_three_hv.
# 3. 使用 sum() 和 len() 计算 first_three_hv 的平均值,
#    输出平均值, 再分别输出 raw_hv 和 work_hv.
# 要求: 全部操作完成后, raw_hv 的内容保持不变.
# 在下方继续编写:

work_hv = raw_hv[:]
work_hv[1]=207
first_three_hv = work_hv[0:3]
mean_first = sum(first_three_hv)/len(first_three_hv)
print(f'平均值： {mean_first}，raw_hv: {raw_hv}, work_hv:{work_hv}')



# %% 第4题 解包几何参数并同步输出试样报告
geometry_mm = (5.0, 2.0, 50.0)
sample_ids = ["S01", "S02", "S03"]
forces_n = [1100, 1900, 1500]
extensions_mm = [0.05, 0.10, 0.20]

# 三个不同试样采用相同的原始几何尺寸, 每个试样提供一个采样点.
# 几何尺寸和标距伸长的单位为 mm, 载荷单位为 N.
#
# 1. 用一条解包赋值语句, 将 geometry_mm 的三项分别赋给变量
#    width_mm, thickness_mm, gauge_mm, 表示原始宽度, 厚度和标距.
# 2. 计算原始截面积, 将结果赋给变量 area_mm2.
#    公式: area_mm2 = width_mm * thickness_mm.
# 3. 使用 zip() 同步遍历编号, 载荷和标距伸长三个列表,
#    将每轮取得的值分别赋给循环变量 sample_id, force_n, extension_mm.
#    在每轮循环中计算工程应力和工程应变百分数,
#    将结果分别赋给变量 stress_mpa 和 strain_pct.
#    公式: stress_mpa = force_n / area_mm2.
#    公式: strain_pct = extension_mm / gauge_mm * 100.
# 4. 每个试样输出一行报告, 包含编号, 应力和应变百分数.
#    应力保留一位小数, 单位为 MPa.
#    应变百分数保留两位小数, 单位为 %.
# 在下方继续编写:

width_mm, thickness_mm, gauge_mm = geometry_mm
area_mm2 = width_mm * thickness_mm

for number,(sample_id, force_n, extension_mm) in enumerate(
    zip(sample_ids, forces_n, extensions_mm), start = 1
):
    stress_mpa = force_n / area_mm2
    strain_pct = extension_mm / gauge_mm * 100
    print(f'试样编号: {sample_id}, 应力： {stress_mpa:.1f} MPa 应变百分数：{strain_pct:.2f} %')

    
# %%
