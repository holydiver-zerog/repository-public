import os
import analyzer # analyzerモジュールをインポート

def read_dictionary():
    """辞書ファイルから名詞データを読み込む

    Returns:
        list: 辞書ファイルから抽出した名詞のリスト
    """
    # モジュールのパスを取得してdictionary.txtのフルパスを作成
    path = os.path.join(
        os.path.dirname(__file__), 'dics', 'dictionary.txt')
    # 辞書ファイルを読み出し専用でオープン
    pfile = open(path, 'r', encoding = 'utf_8')
    # 1行ずつ読み込んでリストの要素にする
    p_lines = pfile.readlines()
    # ファルクローズ
    pfile.close()

    # 辞書ファイルの名詞を保持するリスト
    noun_lst = []
    # p_linesから1行データを順番に抽出
    for line in p_lines:
        # 1行のデータの末尾から改行文字を取り除く
        str = line.rstrip('\n')
        # 1行のデータが空文字ではない場合
        if (str!=''):
            # noun_lstに追加する
            noun_lst.append(str)
    # ファイルから抽出した名詞のリストを返す
    return noun_lst

def save(noun_lst):
    """noun_lstの要素を辞書ファイルに書き込む

    Args:
        noun_lst (list): 登録済みの名詞と新たに登録する名詞のリスト
    """
    # 辞書ファイルに書き込むデータを保持するリスト
    nouns = []
    # noun_lstから名詞データを1つずつ取り出す
    for noun in noun_lst:
        # 末尾に改行を付けてnounsに追加する
        nouns.append(noun + '\n')
    # モジュールのパスを取得してdictionary.txtのフルパスを作成
    path = os.path.join(
        os.path.dirname(__file__), 'dics', 'dictionary.txt')
    # 辞書ファイルを書き込みモードで開く
    with open(path, 'w', encoding = 'utf_8') as f:
        # nounsの1行ごとの名詞データを書き込む
        f.writelines(nouns)

def study_noun(parts, noun_lst):
    """名詞を学習する関数

    Args:
        parts (list): 形態素解析の結果のリスト
        noun_lst (list): 登録済みの名詞のリスト
    """
    # 多重リスト(形態素解析の結果)の要素を2つのパラメーターに取り出す
    for word, part in parts:
        # keyword_check()関数の戻り値がTrueの場合
        if (analyzer.keyword_check(part)):
            # ヘルパー関数is_not_exist()を呼ぶ
            if (is_not_exist(word, noun_lst)):
                # リストnoun_lstに存在しない名詞なので追加する
                noun_lst.append(word)
    # save()でnoun_lstを辞書ファイルに書き込む
    save(noun_lst)

def is_not_exist(word, noun_lst):
    """登録候補の名詞がすでに登録されていないかを調べる

    Args:
        word (str): 登録候補の名詞
        noun_lst (list): 登録済みの名詞のリスト

    Returns:
        bool: 同じ名詞が存在しなければTrue、存在すればFalse
    """
    # リストnoun_lstを反復処理
    for element in noun_lst:
        if(element == word):
            # noun_lstに同じ名詞があればFalseを返す
            return False
    # 同じ名詞が存在しなければTrueを返す
    return True

#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    # 辞書ファイルを読み込んで登録済みの名詞のリストを取得
    n_lst = read_dictionary()

    print('文章を入力')
    # 文章を取得
    inp = input()
    # 入力された文章を解析
    result = analyzer.analyze(inp)            
    # 解析結果と登録済みの名詞のリストをを引数にして学習関数を呼ぶ
    study_noun(result, n_lst)
    
    print('\n')
    input('[Enter]キーで終了します。')

