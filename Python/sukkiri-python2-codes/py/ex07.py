#!/usr/bin/env python
# coding: utf-8

# In[ ]:


file = open('sample.txt', 'r')
for line in file:
    print(line)
    file.close() 


# In[ ]:


nums = list()
for n in range(3):
    data = int(input(f'{n + 1}個目の整数を入力してください >>'))
    nums.append(data)
print(max(nums))


# In[ ]:


pi = 3.141519
print(round(pi))
for n in range(4):
    print(round(pi, n + 1))


# In[ ]:


file_r = open('sample.txt', 'r')
file_w = open('copy.txt', 'w')
for line in file_r:
    file_w.write(line)
file_r.close()
file_w.close()


# In[ ]:


# randomモジュールのrandint関数を取り込む
from random import randint
print('数当てゲームを始めます。3桁の数を当ててください!')

# 正解を作成
answer = list()
for n in range(3):
    answer.append(randint(0, 9))

is_continue = True
while is_continue == True:
    # 予想の入力
    prediction = list()
    for n in range(3):
        data = int(input(f'{n + 1}桁目の予想入力(0~9)>>'))
        prediction.append(data)

    # 答え合わせ
    hit = 0
    blow = 0
    for n in range(3):
        if prediction[n] == answer[n]:
            hit += 1
        else:
            for m in range(3):
                if prediction[n] == answer[m]:
                    blow += 1
                    break

    # 結果発表
    print(f'{hit}ヒット!{blow}ボール!')
    if hit == 3:
        print('正解です!')
        is_continue = False
    else:
        if int(input('続けますか? 1:続ける 2:終了 >>')) == 2:
            print(f'正解は{answer[0]}{answer[1]}{answer[2]}でした')
            is_continue = False

