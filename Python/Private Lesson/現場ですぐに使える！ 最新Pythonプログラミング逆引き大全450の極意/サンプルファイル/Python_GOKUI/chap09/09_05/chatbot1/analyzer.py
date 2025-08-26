from janome.tokenizer import Tokenizer

def parse(text):
    """形態素解析で形態素に分解する

    Args:
        text (str): テキストデータ
    Returns:
        list: 形態素のリスト
    """
    t = Tokenizer()
    tokens = t.tokenize(text)
    result = []
    for token in tokens:
        result.append(token.surface)

    return(result)
