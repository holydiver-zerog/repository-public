#!/usr/bin/env python
# coding: utf-8

# In[ ]:


month = int(input('今は何月ですか?(数字を入力) >>'))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print('31日までありますね')
else:
    if month != 2:
        print('30日までですね')
    else:
        print('1年で一番寒い月ですね')
    print('年が明けてから')
print(f'{month}箇月が過ぎました')


# In[ ]:


isError = False
n = 99
if isError == False and n < 100:
    print('正解です')


# In[ ]:


number = int(input('数値を入力してください >>'))
if number % 2 == 0:
    print('偶数です')
else:
    print('奇数です')


# In[ ]:


greeting = input('挨拶をどうぞ >>')
if greeting == 'こんにちは':
    print('ようこそ!')
elif greeting == '景気は?':
    print('ぼちぼちです')
elif greeting == 'さようなら':
    print('お元気で!')
else:
    print('どうしました?')

