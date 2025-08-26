class Responder:
    """応答クラスのスーパークラス
    """
    def response(self, point):
        """ 応答を返すメソッド
            オーバーライドを前提
        Args:
            point(int): 変動値
        Returns:
            str: 空の文字列
        """
        return ''

class LuckyResponder(Responder):
    """モンスターにダメージを与えるサブクラス
    """
    def response(self, point):
        """ response()をオーバーライド

        Args:
            point(int): 変動値
        Returns:
            list: メッセージと変動値
        """
        return ['モンスターにダメージを与えた！', point]
    
class DrawResponder(Responder):
    """ 引き分けに持ち込むサブクラス
    """
    def response(self, point):
        """ response()をオーバーライド
            pointの値を0にする

        Args:
            point(int): 変動値
        Returns:
            list: メッセージと変動値
        """
        point = 0
        return ['モンスターは身を守っている！', point]

class BadResponder(Responder):
    """ プレイヤーにダメージを与えるサブクラス
    """
    def response(self, point):
        """ response()をオーバーライド
            pointの値をマイナスにする

        Args:
            point(int): 変動値
        Returns:
            list: メッセージと変動値
        """
        return ['モンスターが反撃した！', -point]


# プログラムの実行ブロック
if __name__  == '__main__':
    # 変動値を3にしておく
    point = 3
    # LuckyResponderのオブジェクトを生成
    responder = LuckyResponder()
    # 変動値を設定してresponse()メソッドを実行
    res = responder.response(point)
    # 戻り値を表示
    print(res)
    
    # DrawResponderのオブジェクトを生成
    responder = DrawResponder()
    # 変動値を設定してresponse()メソッドを実行
    res = responder.response(point)
    # 戻り値を表示
    print(res)

    # BadResponderのオブジェクトを生成
    responder = BadResponder()
    # 変動値を設定してresponse()メソッドを実行
    res = responder.response(point)
    # 戻り値を表示
    print(res)
