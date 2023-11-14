from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# 合成された回帰データセットを生成
X, y = make_regression(n_samples=1000, n_features=20, noise=0.1)

# データの正規化
scaler = MinMaxScaler()
X = scaler.fit_transform(X)
y = scaler.fit_transform(y.reshape(-1, 1)).flatten()

# データセットをトレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# シーケンシャルモデルの初期化
model = Sequential()

# 入力層
model.add(Dense(128, activation='relu', input_dim=20))

# 隠れ層
model.add(Dense(64, activation='relu'))

# 出力層
model.add(Dense(1, activation='linear'))

# モデルのコンパイル
model.compile(optimizer='adam', loss='mean_squared_error')

# モデルのトレーニング
model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1, validation_data=(X_test, y_test))

# テストデータでモデルを評価
loss = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', loss)
