# sklearnにどんなデータが用意されているかの確認
# データを読み込んで、そのデータを表示する、データの個数と1つ目の画像データと1つ目の数字が何なのかを表示する
import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("データの個数=", len(digits.images))
print("画像データ=", digits.images[0])
print("何の数字か=", digits.target[0])
