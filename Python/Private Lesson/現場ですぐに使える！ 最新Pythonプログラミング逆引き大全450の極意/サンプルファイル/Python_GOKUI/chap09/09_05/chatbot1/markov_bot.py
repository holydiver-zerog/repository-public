import os
import random
import re

import analyzer  # analyzerモジュールのインポート

class Markov:
    """マルコフ連鎖で文章を生成するクラス
    """
    def __init__(self, filename):
        """テキストファイルのデータをインスタンス変数に格納

        Args:
            filename (str): テキストファイルのパス
        """
        print('テキストを読み込んでいます...')
        # カレントディレクトリのパスにテキストファイルのパスを連結
        path = os.path.join(
            os.path.dirname(__file__), filename)
        # 読み取り専用でファイルをオープン
        with open(path, 'r', encoding = 'utf_8') as f:
            self.text = f.read()  # 全データをself.textに格納
        
    def make(self):
        """マルコフ連鎖を利用して文章を生成する
        
        Returns:
            str: マルコフ連鎖を利用して生成した文章
        """
        # 文末の改行文字を取り除く
        self.text = re.sub('\n', '', self.text)
        # 文章を形態素に分解したリストを取得
        wordlist = analyzer.parse(self.text)

        markov = {} # マルコフ辞書の用意
        p1 = ''     # プレフィックス用の変数
        p2 = ''     # プレフィックス用の変数
        p3 = ''     # プレフィックス用の変数

        # 形態素のリストから1つずつ抽出
        for word in wordlist:
            # p1、p2、p3に値が格納されているか
            if p1 and p2 and p3:
                # markovに(p1, p2, p3)キーが存在しなければキー：値のペアを追加
                if (p1, p2, p3) not in markov:
                    markov[(p1, p2, p3)] = []
                # キーのリストにサフィックスを追加
                markov[(p1, p2, p3)].append(word)
            # 3つのプレフィックスの値を置き換える
            p1, p2, p3 = p2, p3, word

        # 生成した文章を保持する変数
        sentence = ''
        # markovのキーをランダムに抽出し、プレフィックス1～3に代入
        p1, p2, p3  = random.choice(list(markov.keys()))

        # カウンター変数を初期化
        count = 0
        # マルコフ辞書を利用して文章を作り出す
        # 単語リストの単語の数だけ繰り返す
        while count < len(wordlist):
            # キーが存在するかチェック
            if ((p1, p2, p3) in markov) == True:
                # 文章にする単語を取得
                tmp = random.choice(markov[(p1, p2, p3)])
                # 取得した単語をsentenceに追加
                sentence += tmp
            # プレフィックスの値を置き換える
            p1, p2, p3 = p2, p3, tmp
            count += 1
        
        # 最初に出現する(。)までを取り除く
        sentence = re.sub("^.+?。", "", sentence)
        # 最後の句点(。)から先を取り除く
        if re.search('.+。', sentence):
            sentence = re.search('.+。', sentence).group()
        # 閉じ括弧を削除
        sentence = re.sub("」", "", sentence)
        # 開き括弧を削除
        sentence = re.sub("「", "", sentence)
        # 全角スペースを削除
        sentence = re.sub("　", "", sentence)

        # 生成した文章を戻り値として返す
        return sentence

#=================================================
# プログラムの実行ブロック
#=================================================
if __name__  == '__main__':
    fname = input('ファイルのパスを入力してください>')
    # Markovクラスをインスタンス化
    markov = Markov(fname)
    # make()メソッドで文章を生成
    text = markov.make()
    # 文末の。で切り分けてリストにする
    ans = text.split('。')
    # 空の要素を取り除く
    if '' in ans:
        ans.remove('')

    print ('会話をはじめましょう。')
    # 対話処理を実行
    while True:
        message = input('>')
        # 'close'と入力されたらプログラムを終了
        if message == 'close':
            input('[Enter]キーで終了します。')
            break
        # ユーザーの発言が入力されたら応答を返す
        if ans:
            # ansの中からランダムに1つの文章を抽出
            print(random.choice(ans))
