# -*- coding: utf-8 -*-
"""chap004.ipynb

# 第4章 図で特徴をイメージしよう：グラフ

## 11 データのばらつきがわかる

### matplotlibの使い方

リスト4.1
"""

import matplotlib.pyplot as plt

plt.plot([0,100,200],[100,0,200])
plt.show()

"""### seabornの使い方

**※Colab Notebookのみ、以下のセルを実行（このColab Notebookで日本語フォントを使う命令）**
"""

!pip install japanize-matplotlib
import japanize_matplotlib

"""リスト4.2"""

import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

plt.plot([0,100,200],[100,0,200])
plt.title("タイトル")
plt.show()

"""リスト4.3"""

#sns.set(style="dark", font=["Meiryo"]) # Windows
#sns.set(style="dark", font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(style="dark", font=["IPAexGothic"]) # Colab Notebook

plt.plot([0,100,200],[100,0,200])
plt.title("タイトル")
plt.show()

"""### データのばらつきがわかる：ヒストグラム

リスト4.4
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

data = {
    "A案" : [1,10,1,10,1,10,1,10],
    "B案" : [5,5,5,5,6,6,6,6],
    "C案" : [1,2,3,4,7,8,9,10]
}
df = pd.DataFrame(data)
df

"""リスト4.5"""

bins=[1,3,5,7,9,11]

df.plot.hist(bins=bins)
plt.title("ケーキの感想はどのように違うか？")
plt.show()

"""リスト4.6"""

df["A案"].plot.hist(bins=bins)
plt.title("A案のケーキの感想")
plt.show()

df["B案"].plot.hist(bins=bins)
plt.title("B案のケーキの感想")
plt.show()

df["C案"].plot.hist(bins=bins)
plt.title("C案のケーキの感想")
plt.show()

"""## 12 基本的なグラフを作ろう

### 大小を比較できる：棒グラフ

リスト4.7
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

data = {
    "名前" :  ["A太","B介","C子"],
    "国語" : [60,80,100],
    "数学" : [65,85,100],
    "英語" : [66,88,100]
}
df = pd.DataFrame(data)
df

"""リスト4.8"""

df.plot.bar()
plt.title("3名の成績")
plt.show()

"""リスト4.9"""

df.set_index("名前", inplace=True)
df

"""リスト4.10"""

df.plot.bar()
plt.title("3名の成績")
plt.show()

"""リスト4.11"""

df["国語"].plot.bar()
plt.title("国語の成績")
plt.show()

"""### 変化がわかる：折れ線グラフ

リスト4.12
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

data = {
    "月" :  [1,2,3,4,5,6,7,8,9,10,11,12],
    "東京" : [5.6, 7.2, 10.6, 13.6, 20.0, 21.8, 24.1, 28.4, 25.1, 19.4, 13.1, 8.5],
    "那覇" : [18.1, 20.0, 19.9, 22.3, 24.2, 26.5, 28.9, 29.2, 28.0, 26.0, 23.1, 20.0],
    "札幌" : [-3.0, -2.6, 2.5, 8.0, 15.7, 17.4, 21.7, 22.5, 19.3, 13.3, 3.9, -0.8]
}
df = pd.DataFrame(data)
df.head()

"""リスト4.13"""

df.set_index("月", inplace=True)
df.head()

"""リスト4.14"""

df.plot()
plt.title("日本の気温の変化")
plt.show()

"""リスト4.15"""

df["東京"].plot()
plt.title("東京の気温の変化")
plt.show()

"""###  要素の割合を比較できる：円グラフ

リスト4.16
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

data = {
    "クッキー" : [35,47,18],
    "ケーキ" : [62,26,12]
}
idx = ["好き","普通", "嫌い"]
df = pd.DataFrame(data, index=idx)
df

"""リスト4.17"""

df["クッキー"].plot.pie()
plt.title("お菓子の好き嫌いは、どのような割合か？")
plt.show()

"""リスト4.18"""

df["クッキー"].plot.pie(startangle=90, counterclock=False,
                      labeldistance=0.5)
plt.title("お菓子の好き嫌いは、どのような割合か？")
plt.show()

"""リスト4.19"""

df["ケーキ"].plot.pie(startangle=90, counterclock=False,
                    labeldistance=0.5)
plt.title("お菓子の好き嫌いは、どのような割合か？")
plt.show()

"""## 13 ばらつきのわかるグラフ

###  データのばらつきを比較できる：箱ひげ図

リスト4.20
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

data = {
    "Aクラス" :[163.6, 172.6, 163.7, 167.1, 169.9, 173.9, 170.1, 166.2, 176.7, 165.4],
    "Bクラス" :[166.9, 172.7, 166.4, 173.4, 169.6, 171.8, 166.9, 168.2, 166.7, 169.8]
}
df = pd.DataFrame(data)
df.head()

"""リスト4.21"""

sns.boxplot(data=df, width=0.2)
plt.title("身長のばらつきに違いはあるか？")
plt.show()

"""リスト4.22"""

print(df.median())

"""### 2種類のデータの関係性がわかる：散布図

リスト4.23
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

data = {
    "身長" :[163.6, 172.6, 163.7, 169.9, 173.9, 166.2, 176.7, 165.4],
    "体重" :[50.5, 63.3, 48.5, 59.8, 69.8, 53.7, 70.3, 51.2]
}
df = pd.DataFrame(data)
df.head()

"""リスト4.24"""

df.plot.scatter(x="身長", y="体重", color="b")
plt.title("身長と体重に関係はあるか？")
plt.show()

"""## 14 グラフをわかりやすく調整する

### グラフのある点を目立たせる

リスト4.25
"""

df.plot.scatter(x="身長", y="体重", color="b")

x=df.iloc[3]["身長"]
y=df.iloc[3]["体重"]
plt.plot(x, y, color="r", marker="X", markersize=10)

plt.title("私はどこにいるか")
plt.show()

"""リスト4.26"""

df.plot.scatter(x="身長", y="体重", color="b")
plt.title("私はどこにいるか")

x=df.iloc[3]["身長"]
y=df.iloc[3]["体重"]
plt.plot(x, y, color="r", marker="X", markersize=10)

plt.axvline(x=x, color="r", linestyle="--")
plt.axhline(y=y, color="r", linestyle="--")

plt.show()