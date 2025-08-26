def get_factorial(num):
    """階乗を計算する関数

    Args:
        num (int): 処理対象の整数値

    Returns:
        int: 階乗した値
    """
    num = 5
    # 掛け算の初期値を設定
    fact = 1
    # 1～num + 1になるまで繰り返す
    for i in range(1, num + 1):
        # factの値にiの値を掛けて再代入
        fact *= i
    # 階乗した値を返す
    return fact

# get_factorial()を呼び出して階乗を求める
get_factorial(5)