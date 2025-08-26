# -*- coding: utf-8 -*-
"""chap006.ipynb

# 第6章 関係から予測しよう：回帰分析

## 20 2種類のデータの関係性の強さ：相関係数

リスト6.1
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

data = {
    "数学" : [100, 85, 90, 95, 80, 80, 75, 65, 65, 60, 55, 45, 45],
    "理科" : [94, 90, 95, 90, 85, 80, 75, 70, 60, 60, 50, 50, 48],
    "社会" : [80, 88, 70, 62, 86, 70, 79, 65, 75, 67, 75, 68, 60]
}
df = pd.DataFrame(data)
df.head()

"""**※Colab Notebookのみ、以下のセルを実行（このColab Notebookで日本語フォントを使う命令）**"""

!pip install japanize-matplotlib
import japanize_matplotlib

"""リスト6.2"""

df.plot.scatter(x="数学", y="理科", color="b")
plt.title("数学と理科の関係性")
plt.show()

df.plot.scatter(x="数学", y="社会", color="b")
plt.title("数学と社会の関係性")
plt.show()

"""### 相関係数

リスト6.3
"""

print("数学と理科 =", df.corr()["数学"]["理科"])
print("数学と社会 =", df.corr()["数学"]["社会"])

"""リスト6.4"""

print(df.corr())

"""## 21 散布図の上に線を引いて予測

リスト6.5
"""

sns.regplot(data=df, x="数学", y="理科", line_kws={"color":"red"})
plt.show()

sns.regplot(data=df, x="数学", y="社会", line_kws={"color":"red"})
plt.show()

"""リスト6.6"""

sns.jointplot(data=df, x="数学", y="理科", kind="reg", line_kws={"color":"red"})
plt.show()

sns.jointplot(data=df, x="数学", y="社会", kind="reg", line_kws={"color":"red"})
plt.show()

"""## 22 総当たりで表示させる散布図

###  相関行列を色の熱さで表現する：ヒートマップ

リスト6.7
"""

print(df.corr())

"""リスト6.8"""

sns.heatmap(df.corr(), annot=True, vmax=1, vmin=-1, center=0)
plt.show()

"""### 総当たりで表示させる散布図：散布図行列

リスト6.9
"""

sns.pairplot(data=df)
plt.show()

"""リスト6.10"""

sns.pairplot(data=df, kind="reg")
plt.show()

"""## 23 アヤメのデータを見てみよう

リスト6.11
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = sns.load_dataset("iris")
df.head()

"""リスト6.12"""

df.corr(numeric_only=True)

"""リスト6.13"""

sns.heatmap(df.corr(numeric_only=True), annot=True, vmax=1,vmin=-1, center=0)
plt.show()

"""リスト6.14"""

sns.pairplot(data=df)
plt.show()

"""リスト6.15"""

df.head()

"""リスト6.16"""

df["species"].unique()

"""リスト6.17"""

onespecies = "setosa"

one = df[df["species"]==onespecies]
sns.heatmap(one.corr(numeric_only=True), annot=True, vmax=1,vmin=-1, center=0)
plt.title(onespecies, fontsize=18)
plt.show()

"""リスト6.18"""

onespecies = "versicolor"

one = df[df["species"]==onespecies]
sns.heatmap(one.corr(numeric_only=True), annot=True, vmax=1,vmin=-1, center=0)
plt.title(onespecies, fontsize=18)
plt.show()

"""リスト6.19"""

onespecies = "virginica"

one = df[df["species"]==onespecies]
sns.heatmap(one.corr(numeric_only=True), annot=True, vmax=1,vmin=-1, center=0)
plt.title(onespecies, fontsize=18)
plt.show()

"""リスト6.20"""

onespecies = "setosa"

one = df[df["species"]==onespecies]
sns.pairplot(data=one, kind="reg")
plt.show()

"""リスト6.21"""

sns.pairplot(data=df, hue="species")
plt.show()