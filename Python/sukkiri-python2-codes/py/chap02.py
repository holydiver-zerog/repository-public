#!/usr/bin/env python
# coding: utf-8

# In[ ]:


network = 88
database = 95
security = 90
total = network + database + security
avg = total / 3
print(f'合計点:{total}')
print(f'平均点:{avg}')


# In[ ]:


members = ['工藤', '松田', '浅木']
print(members)


# In[ ]:


members = ['工藤', '松田', '浅木']
print(members[0])


# In[ ]:


members = ['工藤', '松田', '浅木']
print(members[3])


# In[ ]:


# ネットワーク、データベース、セキュリティ試験の点数
scores = [88, 90, 95]
total = scores[0] + scores[1] + scores[2]
print(f'合計{total}点')


# In[ ]:


scores = [88, 90, 95]
total = sum(scores)
print(f'合計{total}点')


# In[ ]:


scores = [88, 90, 95]
total = sum(scores)
avg = total / len(scores)
print(f'合計{total}点、平均{avg}点')


# In[ ]:


members = ['工藤', '松田', '浅木']
members.append('菅原')
members.append('湊')
members.append('朝香')
print(members)


# In[ ]:


members = ['工藤', '松田', '浅木']
members.remove('松田')
print(members)


# In[ ]:


members = ['工藤', '松田', '浅木']
members[0] = '菅原'
print(members)


# In[ ]:


a = [10, 20, 30, 40, 50]
print(a[1:3]) # 添え字が1以上3未満の要素
print(a[2:])  # 添え字が2以上のすべての要素
print(a[:3])  # 添え字が3未満のすべての要素


# In[ ]:


a = [10, 20, 30, 40, 50]
print(a[-1]) # 末尾の要素を参照
print(a[-2]) # 末尾から2番目の要素を参照


# In[ ]:


scores = {'network':60, 'database':80, 'security':50}
print(scores) 


# In[ ]:


scores = {'network':60, 'database':80, 'security':50}
print(scores['database'])


# In[ ]:


scores = {'network':60, 'database':80, 'security':50}
scores['programming'] = 65
scores['security'] = 55
print(scores)


# In[ ]:


scores = {'network':60, 'database':80, 'security':55}
del scores['security']
print(scores)


# In[ ]:


scores = (70, 80, 55)
print(scores)
print(scores[0])
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')


# In[ ]:


scores = (70, 80, 55)
scores[0] = 80


# In[ ]:


members = ['松田']       # 要素数1のリスト
scores = {'network':82} # 要素数1のディクショナリ


# In[ ]:


members = ('松田') # 要素数1のタプルを定義(したつもり)
print(type(members))


# In[ ]:


members = ('松田', ) # 要素数1のタプルの正しい定義
print(type(members))


# In[ ]:


scores = {70, 80, 55, 80}
scores.add(80)
print(scores)
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')


# In[ ]:


scores = {'network':60, 'database':80, 'security':60}
members = ['松田', '浅木', '工藤']
print(tuple(members))       # リストmembersをタプルに変換して表示
print(list(scores))         # scoresのキーをリストに変換して表示
print(set(scores.values())) # scoresの値をセットに変換して表示


# In[ ]:


matsuda_scores = {'network':60, 'database':80, 'security':50}
asagi_scores = {'network':80, 'database':75, 'security':92}
member_scores = {
    '松田': matsuda_scores,
    '浅木': asagi_scores
}


# In[ ]:


member_hobbies = {
'松田': {'SNS', '麻雀', '自転車'},
'浅木': {'麻雀', '食べ歩き', '数学', '数学', '数学'}
}
# 全員の趣味一覧を表示する
print(member_hobbies)
# 松田くんの趣味一覧を表示する
print(member_hobbies['松田'])
# 浅木さんの趣味一覧を表示する
print(member_hobbies['浅木'])


# In[ ]:


a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]     # aを0番目、bを1番目とする2次元リストcを定義

print(c)       # リストc全体を参照
print(c[0])    # リストcの0番目(リストa)だけを参照
print(c[1][2]) # リストcの1番目(リストb)の2番目だけを参照


# In[ ]:


member_hobbies = {
    '松田': {'SNS', '麻雀', '自転車'},
    '浅木': {'麻雀', '食べ歩き', '数学', '数学', '数学'}
}
common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies) # 2人に共通する趣味一覧を表示する


# In[ ]:


A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
print(A | B)
print(A & B)
print(A - B)
print(A ^ B) 

