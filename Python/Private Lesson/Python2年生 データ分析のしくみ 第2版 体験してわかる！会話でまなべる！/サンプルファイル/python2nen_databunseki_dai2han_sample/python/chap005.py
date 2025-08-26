# -*- coding: utf-8 -*-
"""chap005.ipynb

# 第5章 これって普通なこと？　特殊なこと？：正規分布

**※Colab Notebookのみ、以下のセルを実行（このColab Notebookで日本語フォントを使う命令）**
"""

!pip install japanize-matplotlib
import japanize_matplotlib

"""## 15 データのばらつきを数値で表す

リスト5.1
"""

import pandas as pd
data = {
    "ID": [0,1,2,3,4,5,6,7,8,9],
    "A" : [59, 24, 62, 48, 58, 19, 32, 88, 47, 63],
    "B" : [49, 50, 49, 54, 45, 52, 56, 48, 45, 52]
}
df = pd.DataFrame(data)
print(df["A"].mean())
print(df["B"].mean())

"""リスト5.2"""

import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

df.plot.scatter(x="ID", y="A", color="b", ylim=(0,100))
plt.axhline(y=50, c="Magenta")
plt.title("Aのばらつき：大きい")
plt.show()

df.plot.scatter(x="ID", y="B", color="b", ylim=(0,100))
plt.axhline(y=50, c="Magenta")
plt.title("Bのばらつき：小さい")
plt.show()

"""リスト5.3"""

print(df.var())

"""リスト5.4"""

print(df.std())

"""### ある範囲にどのくらいデータがあるかがわかる

リスト5.5
"""

meanA = df["A"].mean()
stdA = df["A"].std()
print(meanA - stdA, "〜", meanA + stdA)

"""リスト5.6"""

meanB = df["B"].mean()
stdB = df["B"].std()
print(meanB - stdB, "〜", meanB + stdB)

"""リスト5.7"""

bins=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

df["A"].plot.hist(bins=bins, color="c",ylim=(0,6))
plt.title("Aのばらつき：大きい")
plt.show()

df["B"].plot.hist(bins=bins, color="c",ylim=(0,6))
plt.title("Bのばらつき：小さい")
plt.show()

"""リスト5.8"""

df["A"].plot.hist(bins=bins, color="c",ylim=(0,6))
plt.axvline(x=meanA, color="magenta")
plt.axvline(x=meanA - stdA, color="blue", linestyle="--")
plt.axvline(x=meanA + stdA, color="red", linestyle="--")
plt.title("Aのばらつき：大きい")
plt.show()

df["B"].plot.hist(bins=bins, color="c",ylim=(0,6))
plt.axvline(x=meanB, color="magenta")
plt.axvline(x=meanB - stdB, color="blue", linestyle="--")
plt.axvline(x=meanB + stdB, color="red", linestyle="--")
plt.title("Bのばらつき：小さい")
plt.show()

"""# 16 自然なばらつき

### ゴルトンボードをシミュレート

リスト5.9
"""

import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

# ゴルトンボード表示関数：段数、玉数を指定する
def galton(steps, count) :
   # 玉が落ちた位置を入れる空のリストを用意する
    ans = []
    # 指定された玉数だけくり返す
    for i in range(count):
        # 玉を落とす最初の位置を50にする
        val = 50
        # 指定された段数だけくり返す
        for j in range(steps):
            # 0か1のランダムで、0なら-1、1なら+1
            if random.randint(0, 1) == 0:
                val = val -1
            else :
                val = val + 1
        # 最終的に玉が落ちた位置をリストに追加する
        ans.append(val)

    # 落下した結果のリストをデータフレームにして
    df = pd.DataFrame(ans)
    # 0列目（落とした結果の列）をヒストグラムで表示
    df[0].plot.hist()
    plt.title(str(steps)+"段："+str(count)+"個")
    plt.ylabel("")
    plt.show()

galton(1, 10000)

"""リスト5.10"""

galton(2, 10000)

"""リスト5.11"""

galton(6, 10000)
galton(10, 10000)

"""リスト5.12"""

galton(10, 10)

"""## 17 この値は普通なこと？　珍しいこと？

リスト5.13
"""

from scipy.stats import norm

mean = 166.8
std = 5.8
value = 160.0

cdf = norm.cdf(x=value, loc=mean, scale=std)
print(value,"は、下から", cdf*100,"%")

"""リスト5.14"""

mean = 166.8
std = 5.8
value = 178.0

cdf = norm.cdf(x=value, loc=mean, scale=std)
print(value,"は、上から", (1-cdf)*100,"%")

"""リスト5.15"""

mean = 166.8
std = 5.8
per = 0.20

ppf = norm.ppf(q=per, loc=mean, scale=std)
print("下から", per * 100, "%の値は、", ppf, "です。")

"""リスト5.16"""

mean = 166.8
std = 5.8
per = 0.01

ppf = norm.ppf(q=(1-per), loc=mean, scale=std)
print("上から", per * 100, "%の値は、", ppf, "です。")

"""### 違うばらつきのデータでの比較

リスト5.17
"""

from scipy.stats import norm

scoreM = 60
meanM = 50
stdM = 5

scoreE=80
meanE = 70
stdE = 8

cdf = norm.cdf(x=scoreM, loc=meanM, scale=stdM)
print("数学の", scoreM, "点は、上から", (1-cdf)*100, "%")

cdf = norm.cdf(x=scoreE, loc=meanE, scale=stdE)
print("英語の", scoreE, "点は、上から", (1-cdf)*100, "%")

"""## 18 このデータは自然なばらつき？

リスト5.18
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
#sns.set(font=["Meiryo"]) # Windows
#sns.set(font=["Hiragino Maru Gothic Pro"]) # macOS
#sns.set(font=["IPAexGothic"]) # Colab Notebook

def disp_histnorm(df, msg):
    sns.histplot(df, kde=True, color="blue", alpha=0.2, stat="density")
    mu, std = norm.fit(df)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, linewidth=2, color="red")
    plt.title(msg)
    plt.show()

df = pd.DataFrame({
    "A" : np.random.randint(0, 100, 15),
    "B" : np.random.normal(50, 10, 15)
})
disp_histnorm(df["A"], "かたよりのないランダムな値")
disp_histnorm(df["B"], "正規分布になるようなランダムな値")

"""リスト5.19"""

df = pd.DataFrame({
    "A" : np.random.randint(0, 100, 1500),
    "B" : np.random.normal(50, 10, 1500)
})
disp_histnorm(df["A"], "かたよりのないランダムな値")
disp_histnorm(df["B"], "正規分布になるようなランダムな値")

"""## 19 違うばらつきのデータでの比較ができる

### 偏差値：真ん中は50

リスト5.20
"""

from scipy.stats import norm

scorelist = [60, 70, 80]
for score in scorelist:
    cdf = norm.cdf(x=score, loc=50, scale=10)
    print("偏差値",score, "は、上から", (1-cdf) * 100, "%")

"""リスト5.21"""

perlist = [0.1586, 0.02275, 0.00134]
for per in perlist:
    ppf = norm.ppf(q=(1-per), loc=50, scale=10)
    print("上から", per * 100, "%以上に入るには、偏差値",ppf,"以上が必要")

"""### IQ：真ん中は100

リスト5.22
"""

from scipy.stats import norm

std = 15
IQlist = [110, 130, 148]
for IQ in IQlist:
    cdf = norm.cdf(IQ, loc=100, scale=std)
    print("IQ", IQ, "は、上から", (1-cdf) * 100, "%")

"""リスト5.23"""

std = 24
IQlist = [110, 130, 148]
for IQ in IQlist:
    cdf = norm.cdf(IQ, loc=100, scale=std)
    print("IQ", IQ, "は、上から", (1-cdf) * 100, "%")