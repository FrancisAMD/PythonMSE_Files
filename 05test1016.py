
# %% 5.7 实践与材料｜任务5A
import math
sample_ids = ['S01', 'S02', 'S03', 'S04', 'S05', 'S06']
masses_g = [7.80, 7.85, -1.00, 2.70, None, 7.80]
volumes_cm3 = [1.00, 0.00, 1.00, 1.00, 1.00, float('nan')]

valid_masses_g = []
valid_volumes_cm3 = []
for sample_id,mass_g,volume_cm3 in zip(sample_ids, masses_g, volumes_cm3):
    if mass_g is None:
        print(f'质量缺失')
    elif math.isfinite(volume_cm3) == False:
        print(f'体积非有限数')
    elif mass_g <= 0:
        print(f'质量必须为正')
    elif volume_cm3 <= 0:
        print(f'体积必须为正')
    else:
        print(f'有效，密度为{mass_g}g/cm^3')
        valid_masses_g.append(mass_g)
        valid_volumes_cm3.append(volume_cm3)
        density = [valid_mass_g / valid_volume_cm3 for valid_mass_g, valid_volume_cm3 in zip(valid_masses_g, valid_volumes_cm3)]
print(f'有效的数据的密度是{density}')


# %% 5.7 实践与材料｜任务5B
sample_ids = ['T01', 'T02', 'T03', 'T04']
temperatures_c = [500, 560, 600, 520]
strengths_mpa = [340, 310, 280, 290]

print(f'首先输出规则预测是否达到要求，后输出实测目标是否达到要求')
for sample_id, temperature_c, strength_mpa in zip(sample_ids, temperatures_c, strengths_mpa):
    print(temperature_c <= 550, strength_mpa >= 300)


