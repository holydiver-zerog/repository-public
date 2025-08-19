#!/usr/bin/env python
# coding: utf-8

# In[ ]:


student_list = ['浅木', '松田']
for student in student_list:
    print(f'{student}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点? >>'))
    database = int(input('データベースの得点? >>'))
    security = int(input('セキュリティの得点? >>'))
    if student == '浅木':
        asagi_scores = [network, database, security]
        asagi_avg = sum(asagi_scores) / len(asagi_scores)
    else:
        matsuda_scores = [network, database, security]
        matsuda_avg = sum(matsuda_scores) / len(matsuda_scores)
print(f'浅木さんの平均点は{asagi_avg}です')
print(f'松田さんの平均点は{matsuda_avg}です')


# In[ ]:


# 得点を入力
asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')
# 平均点を計算
asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)
# 結果を出力
output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)


# In[ ]:


def hello():
    print('こんにちは。工藤です。')


# In[ ]:


def hello():
    print('こんにちは。工藤です。')

hello()


# In[ ]:


def input_scores():
    name = ''
    print(f'{name}の試験結果を入力してください')

name = '浅木'
input_scores()
name = '松田'
input_scores()


# In[ ]:


def hello(name):
    print(f'こんにちは。{name}です。')

hello('浅木')
hello('松田')


# In[ ]:


def profile(name, age, hobby):
    print(f'私の名前は{name}です。')
    print(f'年齢は{age}歳です。')
    print(f'趣味は{hobby}です。')

profile('浅木', 24, 'カフェ巡り')


# In[ ]:


def calc_average(scores):
    avg = sum(scores) / len(scores)
    print(f'平均点は{avg}です')


# In[ ]:


def input_scores(name):
    print(f'{name}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点? >>'))
    database = int(input('データベースの得点? >>'))
    security = int(input('セキュリティの得点? >>'))
    scores = [network, database, security]

def calc_average(scores):
    avg = sum(scores) / len(scores)
    print(f'平均点は{avg}です')


# In[ ]:


def input_scores(name):
    print(f'{name}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点? >>'))
    database = int(input('データベースの得点? >>'))
    security = int(input('セキュリティの得点? >>'))
    scores = [network, database, security]

def calc_average(scores):
    avg = sum(scores) / len(scores)
    print(f'平均点は{avg}です')

input_scores('浅木')
calc_average(scores)


# In[ ]:


def plus(x, y):
    answer = x + y
    return answer

answer = plus(100, 50)
print(f'足し算の答えは{answer}です')    


# In[ ]:


def input_scores(name):
    print(f'{name}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点? >>'))
    database = int(input('データベースの得点? >>'))
    security = int(input('セキュリティの得点? >>'))
    scores = [network, database, security]
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    return avg

def output_result(name, avg):
    print(f'{name}さんの平均点は{avg}です')

# 浅木と松田の得点入力
asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')
# 平均点を計算
asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)
# 結果を出力
output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)


# In[ ]:


def plus_and_minus(a, b):
    return a + b, a - b

next, prev = plus_and_minus(1978, 1)


# In[ ]:


def plus_and_minus(a, b):
    return (a + b, a - b)

(next, prev) = plus_and_minus(1978, 1)


# In[ ]:


def eat(breakfast, lunch, dinner):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')

print('8月1日')
eat('トースト', 'おにぎり', 'カレー')
print('8月2日')
eat('納豆ごはん', 'ラーメン', 'カレー')
print('8月3日')
eat('バナナ', 'そば', '焼肉')
print('8月4日')
eat('サンドウィッチ', 'しゅうまい弁当', 'カレー')


# In[ ]:


def eat(breakfast, lunch, dinner='カレー'):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')

print('8月1日')
eat('トースト', 'おにぎり')
print('8月2日')
eat('納豆ごはん', 'ラーメン')
print('8月3日')
eat('バナナ', 'そば', '焼肉')
print('8月4日')
eat('サンドウィッチ', 'しゅうまい弁当')


# In[ ]:


def eat(breakfast, lunch='ラーメン', dinner='カレー'):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')

eat('納豆ごはん', 'ラーメン', 'カレーうどん')


# In[ ]:


eat(breakfast='納豆ごはん', dinner='カレーうどん') # 1
eat(dinner='カレーうどん', breakfast='納豆ごはん') # 2
eat('納豆ごはん', dinner='カレーうどん')           # 3


# In[ ]:


def eat(breakfast, lunch, dinner='カレー', desserts=()):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')
    for d in desserts:
        print(f'おやつに{d}を食べました')

eat('トースト', 'パスタ', 'カレー', ('アイス', 'チョコ', 'パフェ'))


# In[ ]:


def eat(breakfast, lunch, dinner='カレー', *desserts):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')
    for d in desserts:
        print(f'おやつに{d}を食べました')

eat('トースト', 'パスタ', 'カレー', 'アイス', 'チョコ', 'カレー')


# In[ ]:


name = '松田'
def hello():
    print('こんにちは' + name + 'さん')

hello()


# In[ ]:


name = '松田'
def change_name():
    name = '浅木'
def hello():
    print('こんにちは' + name + 'さん')

change_name()
hello()


# In[ ]:


name = '松田'
def change_name():
    global name
    name = '浅木'
def hello():
    print('こんにちは' + name + 'さん')

