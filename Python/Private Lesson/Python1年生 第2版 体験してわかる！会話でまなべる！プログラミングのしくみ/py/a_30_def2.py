# 商品の本体価格を渡すと、消費税計算を行い、消費税込みの金額がわかる関数
def postTaxPrice(price):
    ans = price * 1.1
    print(str(price) + " * 1.1 = " + str(ans))
    return ans


print(postTaxPrice(120), "円")
print(postTaxPrice(128), "円")
print(postTaxPrice(980), "円")
