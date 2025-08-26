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
print(array_Dic)
print(type(array_Dic.values))
array_Set = set(array_Dic.values())
print(array_Set)
print(type(array_Set))
array_List_2 = list(array_Set)
print(array_List_2)
print(type(array_List_2))

# QA表_2506e宮城/Excel:No.26/質問内容
# -------------------------------------------------------------------------------------------------
"""
ディクショナリ要素の順序に関して
Version3.7からは順序性が保証されたということは、
1 array_Dic = {'A':123,'B':456,'C':789,'D':321,'E':654,'F':987,'G':741,'H':852,'I':963}
2 print(array_Dic)
3 print(type(array_Dic.values))
4 array_Set = set(array_Dic.values())
5 print(array_Set)
6 print(type(array_Set))
7 array_List_2 = list(array_Set)
8 print(array_List_2)
9 print(type(array_List_2))
array_Dicをarray_Set経由でarray_List_2のリストに変換したのですがこの際の順番はarray_Dicの順序が間違いなく保証されていると考えて良いのでしょうか？
※P108でセットから変換すると順序は保証されない旨の記載見つけましたので自己解決です。

３行目のTYPE関数での結果が『<class 'builtin_function_or_method'>』となります。
当たり前のことなのでしょうがデータのまとまりが組み込み関数というのが理解できないのです。
理解しやすい表現があれば教えていただけないでしょうか。
"""
# -------------------------------------------------------------------------------------------------

# 回答
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
