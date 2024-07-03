import re
from itertools import combinations
from pathlib import Path

delong_test_outline = Path('./DeLong_test_Outline.txt')
pattern = re.compile(r'p-value = (0.\w+)')

content = delong_test_outline.read_text('utf-8')
matches = re.findall(pattern, content)
p_values = [float(i) for i in matches]

alpha = 0.05  # 原始显著性水平
N = len(p_values) / 2  # 比较的次数

corrected_alpha = alpha / N  # 计算校正后的显著性水平

# 应用 Bonferroni 校正
corrected_significant = [p < corrected_alpha for p in p_values]
print(corrected_significant, corrected_alpha)
print(p_values)

outline_list = ['Outliner 1', 'Outliner 2', 'Outliner 3', 'Outliner 4', 'Outliner 5', 'Outliner 6']
outline_combinations = list(combinations(outline_list, 2))
text_list = []
for i in range(0, 15):
    item1, item2 = outline_combinations[i - 15]
    text = f"{item1} Vs {item2}: P = {p_values[i]:.3f}, "
    text_list.append(text)
print('\n'.join(text_list))
