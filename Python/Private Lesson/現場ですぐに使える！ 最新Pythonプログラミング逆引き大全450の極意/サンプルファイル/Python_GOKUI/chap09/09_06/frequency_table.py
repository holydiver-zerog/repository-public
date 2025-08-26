import os
import re
import analyzer # analyzerモジュールをインポート

def make_freq(file):
    """テキストファイルを読み込んで形態素解析結果を返す
    
    Args:
        file (str): テキストファイルのパス
    Returns:
        list: 解析結果を格納した多重リスト
    """
    print('テキストを読み込んでいます...')
    # カレントディレクトリのパスにテキストファイルのパスを連結
    path = os.path.join(
        os.path.dirname(__file__), file)
    # 読み取り専用でファイルをオープン
    with open(path, 'r', encoding = 'utf_8') as f: 
        text = f.read() # 全データをtextに格納
    # 文末の改行文字を取り除く
    text = re.sub('\n', '', text)
    # 頻度表としての辞書
    word_dic = {}
    # 形態素解析の結果をリストとして取得
    analyze_list = analyzer.analyze(text)

    # 多重リストの要素を2つのパラメーターに取り出す
    for wd, part in analyze_list:
        # keyword_check()関数の戻り値がTrueの場合
        if (analyzer.keyword_check(part)):
            # 辞書に語と同じキーがあればキーの値に1加算
            if wd in word_dic:
                word_dic[wd] += 1
            else:
                # 該当するキーがなければ単語をキーにして値を1にする
                word_dic[wd] = 1
    
    # 頻度表としての辞書を返す
    return(word_dic)

def show(word_dic):
    """頻度表を出力する
    
    Args:
        word_dic (dict): 頻度表としての辞書
    """
    # 頻度表の辞書から頻度順に抽出する
    for word in sorted(
        word_dic,                  # 対象の辞書
        key = word_dic.get,        # 並べ替えの基準(key)を辞書の値にする
        reverse = True             # 降順で並べ替え
        ):
        # キー(単語)と値(頻度)を出力
        print(word + '(' + str(word_dic[word]) + ')')


#=================================================
# プログラムの実行ブロック
#=================================================
if __name__  == '__main__':
    file_name = input('ファイルパスを入力してください>>>')
    # 頻度表を取得する
    freq = make_freq(file_name)
    # 頻度表を出力
    show(freq)                    
    
    input('[Enter]キーで終了します。')