import os
import pandas as pd
import matplotlib.pyplot as plt

# CSVを格納するディレクトリを指定
os.chdir('/Users/kiyosetomohiro/PycharmProjects/stock_test/data')

code = 9749
start = 2018
end = 2019

x = []
y = []

for n in range(start, end + 1):
    file_name = str(code) + '_%d.csv' % n
    # 日本語を読ませるためencoding 指定
    df_csv = pd.read_csv(file_name, header=1, encoding='cp932')
    x += list(pd.to_datetime(df_csv.iloc[:, 0], format='%Y-%m-%d'))
    y += list(df_csv.iloc[:, 4])

data_frame = pd.DataFrame(y)

# 移動平均線を作成
sma75 = pd.DataFrame.rolling(data_frame, window=75, center=False).mean()
sma25 = pd.DataFrame.rolling(data_frame, window=25, center=False).mean()

plt.plot(x, y, color="blue", linewidth=1, linestyle="-")
plt.plot(x, sma25, color="green", linewidth=1, linestyle="-", label="SMA25")
plt.plot(x, sma75, color="red", linewidth=1, linestyle="-", label="SMA75")

plt.title("Alt Plus (" + str(code) + ")", fontsize=16, fontname='Times New Roman')
plt.xlabel("Year-Month", fontsize=14, fontname='Times New Roman')
plt.ylabel("Stock price", fontsize=14, fontname='Times New Roman')

plt.legend(loc="best")

plt.show()
