# -*- coding: utf-8 -*-
"""chap003.ipynb

# 第3章 データの集まりをひとことでいうと？：代表値

## 08 データを平らに均（なら）す

### 平均値を求める

リスト3.1
"""

import pandas as pd
data = {
    "Aクラス" : [82,89,93,85,76],
    "Bクラス" : [100,62,82,70,86]
}
df = pd.DataFrame(data)
df

"""リスト3.2"""

print("Aクラス =", df["Aクラス"].mean())
print("Bクラス =", df["Bクラス"].mean())

"""## 代表値は、「データの比較」に使う

リスト3.3
"""

print(df.mean())

"""リスト3.4"""

print(df.iloc[0]["Aクラス"])
print(df["Aクラス"].mean())

"""## 09 平均値を代表といっていいの？

### 平均値を代表としていいか調べる

リスト3.5
"""

import pandas as pd
data = {
    "予想価格" : [240,250,150,240,300,5000]
}
df = pd.DataFrame(data)
df

"""リスト3.6"""

print(df.mean())

"""リスト3.7"""

print(df.median())

"""リスト3.8"""

print(df.mode())

"""リスト3.9"""

import pandas as pd
data = {
    "予想価格" : [240,250,150,240,300]
}
df = pd.DataFrame(data)
print("平均値 =",df.mean())
print("中央値 =",df.median())
print("最頻値 =",df.mode())

"""## 10 平均値が同じなら、同じといっていいの？

リスト3.10
"""

import pandas as pd
data = {
    "A案" : [1,10,1,10,1,10,1,10],
    "B案" : [5,5,5,5,6,6,6,6],
    "C案" : [1,2,3,4,7,8,9,10]
}
df = pd.DataFrame(data)
df

"""リスト3.11"""

print(df.mean())

"""リスト3.12"""

print(df.median())

"""リスト3.13"""

print(df.mode())

"""リスト3.14"""

bins=[1,3,5,7,9,11]
cut = pd.cut(df["A案"], bins=bins, right=False)
print(cut.value_counts(sort=False))

"""リスト3.15"""

cut = pd.cut(df["B案"], bins=bins, right=False)
print(cut.value_counts(sort=False))

"""リスト3.16"""

cut = pd.cut(df["C案"], bins=bins, right=False)
print(cut.value_counts(sort=False))