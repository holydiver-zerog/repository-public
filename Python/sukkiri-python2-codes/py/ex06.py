#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = 'Python'
b = [1, 3, 5]
class MyClass:
    def hello(self):
        print('Hello' + a)
c = MyClass()
c.hello()  


# In[ ]:


x = ['ABC']
y = [input()]
print(x[0] == y[0])
print(id(x[0]) == id(y[0]))
y = x
y[0] = 'XYZ'
print(x[0])


# In[ ]:


def welcome(u):
    print(f'ようこそ{u["name"]}さん')
    u['age'] = u['age'] + 1
    print(f'あなたは来年{u["age"]}歳だから大吉です!')

username = input('名前を入力してください >>')
userage = int(input('年齢を入力してください >>'))
user = {'name': username, 'age': userage}
welcome(user)
print(f'{user["age"]}歳の{user["name"]}さん、またプレイしてくださいね')

