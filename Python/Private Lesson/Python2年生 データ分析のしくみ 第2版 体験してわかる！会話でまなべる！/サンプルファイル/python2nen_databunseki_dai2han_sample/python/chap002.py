# -*- coding: utf-8 -*-
"""chap002.ipynb

# 第2章 集めたデータは前処理が必要

## 04 表データを読み込もう

### データフレームを作る

リスト2.1
"""

import pandas as pd
data = [
    [60,65,66],
    [80,85,88],
    [100,100,100]
]
df = pd.DataFrame(data)
df

"""リスト2.2"""

df.columns=["国語","数学","英語"]
df.index=["A太","B介","C子"]
df

"""リスト 2.3"""

import pandas as pd
data = [
    [60,65,66],
    [80,85,88],
    [100,100,100]
]
col = ["国語","数学","英語"]
idx =  ["A太","B介","C子"]
df = pd.DataFrame(data, columns=col, index=idx)
df

"""リスト2.4"""

import pandas as pd
data = {
    "国語" : [60,80,100],
    "数学" : [65,85,100],
    "英語" : [66,88,100]
}
idx =  ["A太","B介","C子"]
df = pd.DataFrame(data, index=idx)
df

"""### ファイルのデータ形式に注意しよう

リスト2.5
"""

import pandas as pd
df = pd.read_csv("test.csv")
df

"""リスト2.6"""

import pandas as pd
df = pd.read_csv("testSJIS.csv", encoding="Shift_JIS")
df

"""リスト2.7"""

import pandas as pd
df = pd.read_csv("test.csv", index_col=0)
df

"""リスト2.8"""

import pandas as pd
df = pd.read_csv("testNoHeader.csv", index_col=0, header=None)
df

"""## 05 データをざっくりと眺める

### データを眺める

リスト2.9
"""

import pandas as pd
df = pd.read_csv("test.csv", index_col=0)
df.head()

"""リスト2.10"""

df.columns

"""リスト2.11"""

df.index

"""リスト2.12"""

# 列名をリストに変換する
list1 = [i for i in df.columns]
print(list1)

# インデックス名をリストに変換する
list2 = [i for i in df.index]
print(list2)

"""リスト2.13"""

df.dtypes

"""リスト2.14"""

len(df)

"""### 列データをシリーズ（1次元データ）として取り出す

リスト2.15
"""

df["国語"]

"""リスト2.16"""

df[["国語","数学"]]

"""### 行データをデータフレーム（2次元データ）として取り出す

リスト2.17
"""

df.iloc[[0]]

"""リスト2.18"""

df.iloc[[0,3]]

"""## 要素データを取り出す

リスト2.19
"""

df.iloc[0]["国語"]

"""## 06 データのどこを使う？

### 列データや行データを追加する

リスト2.20
"""

import pandas as pd
dfA = pd.read_csv("test.csv", index_col=0)

dfB = pd.DataFrame()
dfB["国語"] = dfA["国語"]
dfB

import pandas as pd
dfA = pd.read_csv("test.csv", index_col=0)

dfB = pd.DataFrame()
dfB[["国語"]] = dfA[["国語"]]
dfB

"""リスト2.21"""

dfA = pd.read_csv("test.csv", index_col=0)

dfB = pd.DataFrame()
dfB = pd.concat([dfB, dfA.iloc[[0]]])
dfB

"""### 列データや行データを削除する

リスト2.22
"""

dfA = pd.read_csv("test.csv", index_col=0)
dfA = dfA.drop("国語", axis=1)
dfA

"""リスト2.23"""

dfA = pd.read_csv("test.csv", index_col=0)
dfA = dfA.drop(dfA.index[3])
dfA

"""### 条件でデータを抽出する

リスト2.24
"""

dfA = pd.read_csv("test.csv", index_col=0)
dfA["国語"] > 80

"""リスト2.25"""

dfB = dfA[dfA["国語"] > 80]
dfB

"""リスト2.26"""

dfB = dfA[(dfA["国語"] > 80) & (dfA["数学"] > 80)]
dfB

"""## 07 データのミスをチェックする

### 欠損値の処理

リスト2.27
"""

import pandas as pd
data = {
    "国語" : [90,50,None,40],
    "数学" : [80,None,None,50]
}
idx =  ["A太","B介","C子","D郎"]
dfA = pd.DataFrame(data, index=idx)
dfA

"""リスト2.28"""

dfA.isnull().sum()

"""リスト2.29"""

dfB = dfA.dropna()
dfB

"""リスト2.30"""

dfB = dfA.dropna(subset=["国語"])
dfB

"""リスト2.31"""

dfB = dfA.fillna(dfA.mean())
dfB

"""リスト2.32"""

dfB = dfA.ffill()
dfB

"""## 重複したデータを削除する

リスト2.33
"""

import pandas as pd
data = [
    [10,30,40],
    [20,30,40],
    [20,30,40],
    [30,30,50],
    [20,30,40]
        ]
dfA = pd.DataFrame(data)
dfA

"""リスト2.34"""

dfA.duplicated().value_counts()

"""リスト2.35"""

dfB = dfA.drop_duplicates()
dfB

"""### 文字列型のデータを数値に変換する

リスト2.36
"""

import pandas as pd
data = {
    "A" : ["100","300"],
    "B" : ["500","1,500"]
}
dfA = pd.DataFrame(data)
dfA

"""リスト2.37"""

dfA.dtypes

"""リスト2.38"""

dfA["A"] = dfA["A"].astype(int)
dfA.dtypes

"""リスト2.39"""

dfA["B"] = dfA["B"].str.replace(",","").astype(int)
dfA.dtypes

"""リスト2.40"""

dfA