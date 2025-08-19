#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def function_a():
    print('関数Aを実行')
    function_b() # function_bを呼び出し
    function_c() # function_cを呼び出し

def function_b():
    print('関数Bを実行')

def function_c():
    print('関数Cを実行')


# In[ ]:


'''
作成日: XXXX年YY月ZZ日
作成者: 松田
'''
# インポート

# グローバル変数の宣言

# 関数宣言
def main():
    print('*** Puzzle & Monsters ***')

# main関数の呼び出し
main()


# In[ ]:


def do_battle():
    # 省略

def go_dungeon():
    do_battle() # do_battle関数の呼び出し

def main():
    go_dungeon() # go_dungeon関数の呼び出し
# :


# In[ ]:


slime = {
    'name':'スライム',
    'hp':100,
    'max_hp':100,
    'element':'水',
    'ap':10,
    'dp':1
}


# In[ ]:


def print_monster_name(monster):
    # monsterはディクショナリで受け取る
    # (1)モンスターの名前をキーnameで取得する
    # (2)後述
    # (3)後述

    # モンスター名を表示する
    print(f'{monster.name}', end='')


# In[ ]:


ELEMENT_SYMBOLS = {
    '火': '$',
    '水': '~',
    '風': '@',
    '土': '#',
    '命': '&',
    '無': ' '
}


# In[ ]:


def print_monster_name(monster):
    # monsterはディクショナリで受け取る
    # (1)モンスターの名前と属性を取得する
    # (2)取得した属性に対応する記号をELEMENT_SYMBOLSから取得する
    # (3)後述

    # モンスター名を表示する
    print(f'{symbol}{monster.name}{symbol}', end='')


# In[ ]:


def print_monster_name(monster):
    # monsterはディクショナリで受け取る
    # (1)モンスターの名前と属性を取得する
    # (2)取得した属性に対応する記号をELEMENT_SYMBOLSから取得する
    # (3)取得した属性に対応する記号をELEMENT_COLORSから取得する

    # モンスター名を表示する
    print(f'\033[{color}m{symbol}{monster.name}{symbol}\033[0m ', end='')


# In[ ]:


def organize_party(player_name, friends):
    """
    引数
    player_name: プレイヤー名
    friends: 味方モンスターをディクショナリで管理したリスト
    """
    # (1)味方モンスターのHPの合計と防御力の平均を求める
    # (2)ディクショナリにパーティの情報をまとめる
    # (3)ディクショナリを戻り値に指定する


# In[ ]:


import random
print(random.uniform(-3, 3))

