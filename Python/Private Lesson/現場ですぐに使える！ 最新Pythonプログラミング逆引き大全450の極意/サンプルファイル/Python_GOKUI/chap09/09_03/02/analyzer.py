from janome.tokenizer import Tokenizer # janome.tokenizerをインポート
import pprint 

def analyze(text):
    """形態素解析を行う

    Args:
        text (str): 解析対象の文章
        Returns:
            list: 見出しと品詞のペアを格納した多重リスト
    """
    # Tokenizerオブジェクトを生成
    t = Tokenizer()
    # 形態素解析を実行
    tokens = t.tokenize(text)
    # 形態素と品詞を格納するリスト
    result = []
    
    # リストからTokenオブジェクトを1つずつ取り出す
    for token in tokens:
        # 形態素と品詞情報をリストにしてresultに追加
        result.append(              
            [token.surface,        # 形態素を取得
            token.part_of_speech]) # 品詞情報を取得
    # 解析結果の多重リストを返す
    return(result)
    

#=================================================
# プログラムの実行部
#=================================================
if __name__  == '__main__':
    print('文章を入力')
    # 文章を取得
    inp = input()
    # 入力された文章を解析
    pprint.pprint(analyze(inp))
    
    print('\n')
    input('[Enter]キーで終了します。')
