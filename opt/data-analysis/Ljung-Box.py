import numpy as np
from statsmodels.stats.diagnostic import acorr_ljungbox

# ランダムな時系列データを生成
np.random.seed(0)
data = np.random.randn(100)

# ラユング＝ボックス検定を実施し、結果をデータフレームで受け取る
lb_test_result = acorr_ljungbox(data, lags=[10], return_df=True)

# 検定結果を表示
print("Ljung-Box test statistic:", lb_test_result['lb_stat'])
print("P-value:", lb_test_result['lb_pvalue'])

