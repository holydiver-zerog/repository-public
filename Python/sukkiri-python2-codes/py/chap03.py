#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name = input('あなたの名前を教えてください >>')
print(f'{name}さん、こんにちは')
food = input(f'{name}さんの好きな食べ物を教えてください >>')
print(f'私も{food}が好きですよ')


# In[ ]:


name = input('あなたの名前を教えてください >>')
print(f'{name}さん、こんにちは')
food = input(f'{name}さんの好きな食べ物を教えてください >>')
if food == 'カレー':
    print('素敵です。カレーは最高ですよね!!')
else:
    print(f'私も{food}が好きですよ')


# In[ ]:


score = int(input('試験の点数を入力してください >>'))
if score >= 60:
    print('合格!')
    print('よくがんばりましたね')
else:
    print('残念ながら不合格です')
print('追試を受けてください')


# In[ ]:


name = input('あなたの名前を教えてください >>')
print(f'{name}さん、こんにちは')
food = input(f'{name}さんの好きな食べ物を教えてください >>')
if 'カレー' in food:
    print('素敵です。カレーは最高ですよね!!')
else:
    print(f'私も{food}が好きですよ')


# In[ ]:


scores = [80, 100, 20, 60]
if 100 in scores:
    print('100点満点の試験があったんですね。おめでとう!')
else:
    print('次はどれか1つでも100点満点をとろう')


# In[ ]:


scores = {'network': 60, 'database': 80, 'security': 50}
key = input('追加する科目名を入力してください >>')
if key in scores:
    print('すでに登録済みです')
else:
    data = int(input('得点を入力してください >>'))
    scores[key] = data
print(scores)


# In[ ]:


score = int(input('試験の点数を入力 >>'))
print(score >= 60)


# In[ ]:


name = input('あなたの名前を教えてください >>')
print(f'{name}さん、こんにちは')
if name == '松田':
    print('松田さんに会えてうれしいです')
food = input(f'{name}さんの好きな食べ物を教えてください >>')
if 'カレー' in food:
    print('素敵です。とにかくカレーは最高ですよね!!')
else:
    print(f'私も{food}が好きですよ')


# In[ ]:


score = int(input('試験の点数を入力してください >>'))
if score < 0 or score > 100:
    print('異常な得点です')
    print('入力し直してください')
elif score >= 60:
    print('合格!')
    print('よくがんばりましたね')
else:
    print('残念ながら不合格です')
    print('追試を受けてください')


# In[ ]:


print('すべての質問に y または n で答えてください')
okane_aruka = input('お金に余裕はありますか? >>')
if okane_aruka == 'y':
    onaka_suiteruka = input('お腹がすごく空いてますか? >>')
    nomitai_kibunka = input('ビールを飲みたいですか? >>')
    if onaka_suiteruka == 'y' and nomitai_kibunka == 'y':
        print('焼き肉はいかがですか')
    elif onaka_suiteruka == 'y':
        print('カレーはいかがですか')
    elif nomitai_kibunka == 'y':
        print('焼き鳥はいかがですか')
    else:
        print('パスタはいかがですか')
    yashoku_iruka = input('夜食は必要ですか? >>')
    if yashoku_iruka == 'y':
        print('コンビニのチキンはいかがですか')
else:
    print('家で食べましょう')

