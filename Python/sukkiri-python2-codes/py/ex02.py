#!/usr/bin/env python
# coding: utf-8

# In[ ]:


scores = []
scores.append(int(input('国語の点数 >>')))
scores.append(int(input('算数の点数 >>')))
scores.append(int(input('理科の点数 >>')))
scores.append(int(input('社会の点数 >>')))
scores.append(int(input('英語の点数 >>')))
print(f'合計{sum(scores)}点 平均{sum(scores) / len(scores)}点')


# In[ ]:


player1 = {'読書', '昼寝', '映画鑑賞', '散歩', '料理'}
player2 = {'テニス', '将棋', '料理', '読書', '旅行'}
input('心の準備ができたらEnterキーを押してください')
common = player1 & player2
total = player1 | player2
compatibility_rate = len(common) / len(total) * 100
print(f'相性度は{compatibility_rate}パーセントでした')

