import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Hiragino Maru Gothic Pro", "Hiragino sans", "BIZ UDGothic", "MS Gothic"]

# CSVファイルをデータフレームに読み込む
df = pd.read_csv("FEH_00200524_240108155037.csv", index_col="全国・都道府県", encoding="UTF-8")

# 2021年と2022年の列データで棒グラフを作って表示する
df = df.drop("全国", axis=0)
df["2021年"] = pd.to_numeric(df["2021年"].str.replace(",", ""))
df["2022年"] = pd.to_numeric(df["2022年"].str.replace(",", ""))
df["人口増減"] = df["2022年"] - df["2021年"]
df = df.sort_values("人口増減",ascending=False)
df["人口増減"].plot.bar(figsize=(10, 6))
plt.show()