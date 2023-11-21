import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score, roc_curve, auc

from utils import get_add_AE_prediction_num
import pickle

source_df = pd.read_pickle('./resources/temp_file/2023_inves.pkl').iloc[:, 12:]
source_df: pd.DataFrame

a = list('1' * 15)
b = list('0' * 15)
c = list('1' * 15)
d = list('0' * 15)
answer_list = a + b + c + d
answer_list = list(map(int, answer_list))
print(len(answer_list))

# 查看每道题有多少人做
num_list = []
for i in range(60):
    num = np.sum(source_df.iloc[:, i] != -3)
    num_list.append(num)
num_list = np.array(num_list)
min_num = np.min(num_list)
mean_num = np.mean(num_list)
max_num = np.max(num_list)
print(min_num, mean_num, max_num)

# 查看是否有题没有人做
print(np.sum(np.array(num_list) == 0))

# 对应每一个人数，分别有多少道题被做
fig, ax = plt.subplots()
ax.set_xlim(min_num, max_num + 1)
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
for i in range(min_num, max_num + 1):
    i_th_num = np.sum(num_list == i)
    ax.bar(i, i_th_num)
plt.show()

# 计算每道题的概率，即患者有多少可能预测该图是AE
# 设概率为预测 AE 的概率
predict_AE_prob_list = []
all_num = source_df.shape[0]

for i, num in enumerate(num_list):
    predict_AE_num: int = np.sum(source_df.iloc[:, i] == 2)
    _predict_AE_prob = predict_AE_num / num

    # 随机真实数据
    prob_AE_list = []
    add_AE_num: int = get_add_AE_prediction_num(_predict_AE_prob, all_num - num)
    predict_AE_prob = (predict_AE_num + add_AE_num) / all_num
    prob_AE_list.append(predict_AE_prob)

    predict_AE_prob_list.append(np.mean(prob_AE_list))

predict_AE_prob_list = np.array(predict_AE_prob_list)
print(len(predict_AE_prob_list), predict_AE_prob_list[0], len(answer_list))

# 计算AUC
print(roc_auc_score(answer_list, predict_AE_prob_list))
fpr, tpr, thresholds = roc_curve(answer_list, predict_AE_prob_list, pos_label=1)
print(auc(fpr, tpr))

# 计算准确率
mask = predict_AE_prob_list < 0.69
predict_result = np.ones(60)
predict_result[mask] = 0
print(accuracy_score(answer_list, predict_result))

# 保存数据
inves_results_2023 = {
    'y_true': answer_list,
    'y_score': predict_AE_prob_list,
    'y_pred': predict_AE_prob_list
}
with open('./resources/temp_file/inves_results_2023.pkl', 'wb') as f:
    pickle.dump(inves_results_2023, f)
