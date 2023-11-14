from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# 合成された回帰データセットを生成
X, y = make_regression(n_samples=1000, n_features=20, noise=0.1)

# データセットをトレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# ランダムフォレスト回帰モデルのインスタンスを作成
regressor = RandomForestRegressor(n_estimators=100)

# モデルのトレーニング
regressor.fit(X_train, y_train)

# テストデータで予測
y_pred = regressor.predict(X_test)

# 平均二乗誤差（MSE）による性能評価
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
