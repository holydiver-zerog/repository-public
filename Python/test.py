# テスト用ディクショナリ
array_Dic = {
    "A": 123,
    "B": 456,
    "C": 789,
    "D": 321,
    "E": 654,
    "F": 987,
    "G": 741,
    "H": 852,
    "I": 963,
}

# 変数初期化
DIC = "array_Dic"
LIST = "array_List_Exchange"
NEW = "array_List_New"
count = 0
key = ""
array_List_New = []

# ディクショナリをリストに変換（キーのみになる）
array_List_Exchange = list(array_Dic)

# リストに変換したキーを利用してディクショナリから要素を抽出　array_List_Newに追加
for key in array_List_Exchange:
    get_Element = array_Dic[str(key)]
    array_List_New.append(get_Element)
    print(str(count) + ":" + str(get_Element))  # 確認用
    count += 1

# 確認用
print(DIC + ":" + str(array_Dic))
print(DIC + " TYPE :" + str(type(array_Dic)))
print(LIST + ":" + str(array_List_Exchange))
print(LIST + " TYPE :" + str(type(array_List_Exchange)))
print(NEW + ":" + str(array_List_New))
print(NEW + " TYPE :" + str(type(array_List_New)))
