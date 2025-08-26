# テキストファイルを読み込んで文章の組み換えを行うプログラム

import random
import os, re
from janome.tokenizer import Tokenizer

# マルコフ辞書用のグローバル変数
markov = {}
# 生成した文章を保持するグローバル変数
sentence = ''

def parse(text):
    """形態素解析で形態素を取り出す

    Args:
        text (str): マルコフ辞書の元になるテキスト
    Returns:
        list: 形態素のリスト
    """
    t = Tokenizer()           # Tokenizerオブジェクトを生成
    tokens = t.tokenize(text) # 形態素解析を実行
    result = []               # 形態素を格納するリスト
    # リストからTokenオブジェクトを抽出
    for token in tokens:
        # 形態素をresultに追加
        result.append(token.surface)
    # 形態素のリストを戻り値として返す
    return(result)

def get_morpheme(filename):
    """ファイルを読み込んで形態素のリストを作成する

    Args:
        filename (str): テキストファイルの相対パス
    Returns:
        list: 形態素のリスト
    """
    # カレントディレクトリのパスを取得してテキストファイルのフルパスを作成
    path = os.path.join(
        os.path.dirname(__file__), filename)
    # テキストファイルを読み取り専用でオープン
    with open(path, 'r', encoding = 'utf_8') as f:
        # 全てのテキストをtextに代入
        text = f.read()
    # 文末の改行文字を取り除く
    text = re.sub("\n","", text)
    # 全テキストを引数にしてparse()を実行
    wordlist = parse(text)
    # 形態素のリストを戻り値として返す
    return wordlist

def create_markov(wordlist):
    """マルコフ辞書を作成する
    
    Args:
        wordlist (list): テキストファイルから抽出した形態素のリスト
    """
    p1 = ''  # プレフィックス用の変数
    p2 = ''  # プレフィックス用の変数
    p3 = ''  # プレフィックス用の変数
    # wordlistから形態素を抽出
    for word in wordlist:
        # p1、p2、p3のすべてに値が格納されているか
        if p1 and p2 and p3:
            # markovに(p1, p2, p3)キーが存在するか
            if (p1, p2, p3) not in markov:
                # なければキー：値のペアを追加
                markov[(p1, p2, p3)] = []
            # キーのリストにサフィックスを追加（重複あり）
            markov[(p1, p2, p3)].append(word)
        # 3つのプレフィックスの値を置き換える
        p1, p2, p3 = p2, p3, word

def generate(wordlist):
    """ マルコフ辞書から文章を作り出してsentenceに格納する
    
        wordlist (list): テキストファイルから抽出した形態素のリスト
    """
    # グローバル変数の使用
    global sentence    
    # markovのキーをランダムに抽出し、プレフィックス1～3に代入
    p1, p2, p3  = random.choice(list(markov.keys()))
    # カウンター変数
    count = 0
    # 単語リストの単語の数だけ繰り返す
    while count < len(wordlist):
        # キーが存在するかチェック
        if ((p1, p2, p3) in markov) == True:
            # 文章にする単語を取得
            tmp = random.choice(
                markov[(p1, p2, p3)])
            # 取得した単語をsentenceに追加
            sentence += tmp
        # 3つのプレフィックスの値を置き換える
        p1, p2, p3 = p2, p3, tmp
        count += 1
    
    # 最初に出てくる句点(。)までを取り除く
    sentence = re.sub('^.+?。', '', sentence)
    # 最後の句点(。)から先を取り除く
    if re.search('.+。', sentence):
        sentence = re.search('.+。', sentence).group()
    # 閉じ括弧を削除
    sentence = re.sub('」', '', sentence)
    # 開き括弧を削除
    sentence = re.sub('「', '', sentence)
    # 全角スペースを削除
    sentence = re.sub('　', '', sentence)

def overlap():
    """ sentenceの重複した文章を取り除く

    """
    # グローバル変数の使用
    global sentence
    # 「。」のところで分割してリストにする
    sentence = sentence.split('。')
    # 分割した要素に空文字があれば取り除く
    if '' in sentence:
        sentence.remove('')
    # 処理した文章を一時的に格納するリスト
    new = []
    # sentenceの要素を取り出し末尾に「。」を付ける
    for str in sentence:
        str = str + '。'
        # 「。」だけの場合は次の処理へ
        if str=='。':
            break
        # 「。」追加後の文章をnewに追加
        new.append(str)
    # newの中身を集合に変換して重複要素を除く
    new = set(new)
    # newの要素を連結してsentenceに再代入
    sentence=''.join(new)

#=================================================
# プログラムの実行ブロック
#=================================================
if __name__  == '__main__':
    # テキストファイルのパスを取得
    fname = input('ファイルのパスを入力してください>')
    # ファイルパスを指定して形態素のリストを作る
    word_list = get_morpheme(fname)
    # マルコフ辞書を作成
    create_markov(word_list)
    # sentenceの中身が空になるまで繰り返す
    while(not sentence):
        generate(word_list) # 文書を生成する
        overlap()           # 重複した文章を取り除く
    
    # 生成した文章を出力
    print(sentence)

    print('\n')
    input('[Enter]キーで終了します。')
