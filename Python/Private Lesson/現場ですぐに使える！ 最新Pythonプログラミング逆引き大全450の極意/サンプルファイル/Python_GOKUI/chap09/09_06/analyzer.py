import re
from janome.tokenizer import Tokenizer

def analyze(text):
    """形態素解析を行う

    Args:
        text (str): 解析対象の文章
    Returns:
        list: 解析結果の多重リスト
    """
    # Tokenizerオブジェクトを生成
    t = Tokenizer()
    # 形態素解析を実行
    tokens = t.tokenize(text)
    # 形態素と品詞のリストを格納するリスト
    result = []
    # リストからTokenオブジェクトを1つずつ抽出
    for token in tokens:
        # 形態素と品詞情報のリストを作成してresultに追加
        result.append([token.surface, token.part_of_speech])
    # 解析結果の多重リストを返す
    return(result)

def keyword_check(part):
    """品詞が名詞であるかを調べる

    Args:
        part (str): 形態素解析の品詞の部分
    Returns:
        bool: 名詞であればTrue、そうでなければFalse
    """
    # 名詞,一般
    # 名詞,固有名詞
    # 名詞,サ変接続
    # 名詞,形容動詞語幹
    # のいずれかにマッチすればTrue、それ以外ばFalseを返す
    return re.match(
        '名詞,(一般|固有名詞|サ変接続|形容動詞語幹)', part)
