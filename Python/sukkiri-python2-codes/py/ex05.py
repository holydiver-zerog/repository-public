#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def take_bus():
    print('バスに乗ります')
def run():
    print('走ります!')
def walk():
    print('ちょっと歩きます')

print('行ってきます!')
walk(); take_bus(); run(); run()
print('ただいま')


# In[ ]:


def analyze_scores(sansu, kokugo, rika, syakai, eigo=None, *others):
    # 処理内容は省略
    return [max_score, min_score, avg_score] 


# In[ ]:


# 計算データの入力
amount = int(input('支払総額を入力してください >>'))
people = int(input('参加人数を入力してください >>'))

# 割り勘の計算
dnum = amount / people   # 総額を人数で割る(端数も保持)
pay = dnum // 100 * 100  # 100円未満を切り捨てる
if dnum > pay:           # 元の値と比較して、
    pay = int(pay + 100) # 小さければ100円未満があったので上乗せ

# 幹事の支払額の計算
payorg = amount - pay * (people - 1)

# 結果の表示
print('*** 支払額 ***')
print(f'1人あたり{pay}円({people}人)、幹事は{payorg}円です')


# In[ ]:


def is_leapyear(y):
    return (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0))

current_year = int(input('現在の西暦を入力してください >>'))
if is_leapyear(current_year):
    print(f'西暦{current_year}年は、うるう年です')
else:
    print(f'西暦{current_year}年は、うるう年ではありません')


# In[ ]:


def int_input(msg):
    return int(input(f'{msg}を入力してください >>'))
def calc_payment(amount, people=2):
    dnum = amount / people # 総額を人数で割る(端数も保持)
    pay = dnum // 100 * 100 # 100円未満を切り捨てる
    if dnum > pay: # 元の値と比較して、
        pay = pay + 100 # 小さければ100円未満があったので上乗せ
    payorg = amount - pay * (people - 1)
    return [int(pay), int(payorg)]
def show_payment(pay, payorg, people=2):
    print('*** 支払額 ***')
    print(f'1人あたり{pay}円({people}人)、幹事は{payorg}円です')

# 計算データの入力
amount = int_input('支払総額'); people = int_input('参加人数')
# 割り勘の計算
[pay, payorg] = calc_payment(amount, people)
# 結果の表示
show_payment(pay, payorg, people)

