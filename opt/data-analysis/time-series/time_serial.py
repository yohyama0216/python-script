# GoogleColabにて実行
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# サンプルデータの作成（日付と対応する数値）
data = {
    'Date': pd.date_range(start='2020-01-01', periods=100, freq='D'),
    'Value': np.random.randint(100, 1000, size=100)  # 100〜999のランダムな数値
}

# Pandas DataFrameに変換
df = pd.DataFrame(data)

# 日付をインデックスに設定
df.set_index('Date', inplace=True)

# 時系列プロットの作成
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'])
plt.title('Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
