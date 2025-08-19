#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tpl = '3人目は{}さん'
names = ['松田', '浅木']
names.append('工藤')
message = tpl.format(names[2])
print(message)


# In[ ]:


num = 10
print(num.bit_length())
names = ['松田', '浅木']
names.append('工藤')


# In[ ]:


userinfo = input('名前と血液型をカンマで区切って1行で入力 >>')
[name, blood] = userinfo.split(',')
blood = blood.upper().strip()
print(f'{name}さんは{blood}型なので大吉です')


# In[ ]:


int_value1 = 0
int_value2 = int()
int_value3 = int(9)
list_value1 = []
list_value2 = list()
list_value3 = list(('松田', '浅木'))


# In[ ]:


class Hero:
    name = '松田'
    hp = 100
    def sleep(self, hours):
        print(f'{self.name}は{hours}時間寝た!')
        self.hp += hours

# ゲーム開始
print('スッキリファンタジーXII ~金色の理想郷~')
h = Hero()
h.sleep(3)
print(f'{h.name}のHPは現在{h.hp}です')


# In[ ]:


scores1 = [80, 40, 50]
scores2 = [80, 40, 50]
print(f'scores1のidentity: {id(scores1)}')
print(f'scores2のidentity: {id(scores2)}')

if scores1 == scores2:
    print('scores1とscores2は同じ内容です')
else:
    print('scores1とscores2は違う内容です')

if id(scores1) == id(scores2):
    print('scores1とscores2は同じ存在です')
else:
    print('scores1とscores2は違う存在です')


# In[ ]:


scores1 = [80, 40, 50]
scores2 = [80, 40, 50]
print(f'scores1の先頭要素は{scores1[0]}')
print(f'scores2の先頭要素は{scores2[0]}')

print('変数scores2の中身を変数scores1に代入（コピー）します')
scores1 = scores2

print('scores1の先頭要素を90に書き換えます')
scores1[0] = 90

print(f'90を代入したscores1の先頭要素は{scores1[0]}')
print(f'90を代入していないscores2の先頭要素は{scores2[0]}')


# In[ ]:


def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
    return names

before_names = ['松田', '浅木', '工藤']
after_names = add_suffix(before_names)
print('さん付け後:' + after_names[0])
print('さん付け前:' + before_names[0])


# In[ ]:


def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
    return names

before_names = ['松田', '浅木', '工藤']
copied_names = list()
for n in before_names:
    copied_names.append(n)
after_names = add_suffix(copied_names)
print('さん付け後:' + after_names[0])
print('さん付け前:' + before_names[0])


# In[ ]:


def add_suffix(name):
    name = name + 'さん'
    return name

before_name = '松田'
after_name = add_suffix(before_name)
print('さん付け後:' + after_name)
print('さん付け前:' + before_name)


# In[ ]:


names = list() # リストの場合
print(f'list（変更前）: {id(names)}')
names.append('松田')
print(f'list（変更後）: {id(names)}')

name = '松田'   # 文字列の場合
print(f'str（変更前）: {id(names)}')
name = 'スーパー' + name
print(f'str（変更後）: {id(names)}')

