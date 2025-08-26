# 身長と体重を入力すると、肥満度指数のBMI値を計算してくれるプログラム
h = float(input("身長何cmですか？")) / 100.0
w = float(input("体重何kgですか？"))
bmi = w / (h * h)
print("あなたのBMI値は,",bmi,"です")