import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf

# ランダムな時系列データを生成
np.random.seed(0)
data = np.random.randn(100)

# 自己相関を計算
lag_acf = acf(data, nlags=20)

# 自己相関をプロット
plt.figure(figsize=(10, 5))
plt.stem(range(len(lag_acf)), lag_acf, use_line_collection=True)
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Function (ACF)')
plt.show()
