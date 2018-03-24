# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import DataFrame
import matplotlib
import  sys
reload(sys)
sys.setdefaultencoding('utf-8')
from matplotlib import rc
# 藍色
fesm_data = read_csv('/home/zengxiaosen/BandWidthUsedRateStandardDeviation_PLLB_7.csv', header=None)
# 黃色
pllb_data = read_csv('/home/zengxiaosen/BandWidthUsedRateStandardDeviation_FESM_7.csv', header=None)
# 綠色
dij_data = read_csv('/home/zengxiaosen/BandWidthUsedRateStandardDeviation_Dijkstra_7.csv', header=None)
# 转换成mbps
# fesm_data = fesm_data / 1000


index1 = []
for i in range(len(fesm_data)):
    index1.append(i * 3 + 1)

index2 = []
for i in range(len(pllb_data)):
    index2.append(i * 3 + 1)

index3 = []
for i in range(len(dij_data)):
    index3.append(i * 3 + 1)

# 设置matplotlib可以显示中文
matplotlib.rcParams['font.family'] = 'SimHei'

plt.xlabel('time:second')
# 每link带宽标准差
# BandWidthStandardDeviation
plt.ylabel('BandWidthUsedRateStandardDeviation:mbps')
plt.title('BandWidthUsedRateStandardDeviation')
plt.plot(index1, fesm_data, index2, pllb_data, index3, dij_data)
# plt.plot(index1, fesm_data)
# plt.savefig('fesm.png', dpi=600)
plt.show()
plt.close()