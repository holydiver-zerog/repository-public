import random     # randomモジュールをインポート
import responder  # responderモジュールをインポート

class Controller:
    """ 応答オブジェクトを呼び分けるためのクラス
    """
    # 応答オブジェクトを生成してインスタンス変数に格納
    def __init__(self):
        # LuckyResponderを生成
        self.lucky = responder.LuckyResponder()        
        # MediumResponderを生成      
        self.draw  = responder.DrawResponder()
        # BadResponderを生成
        self.bad   = responder.BadResponder()

    def attack(self, point):
        """サブクラスのresponse()を呼び出して応答文字列と変動値を取得する

        Args:
            point (int): 変動値

        Returns:
            list: response()から返されるメッセージと変動値
        """
        # 1から100をランダムに生成
        x = random.randint(1, 100)
        # 30以下ならLuckyResponderオブジェクトにする
        if x <= 30:
            self.responder = self.lucky
        # 31～60以下ならDrawResponderオブジェクトにする
        elif 31 <= x <= 60:
            self.responder = self.draw
        # それ以外はBadResponderオブジェクトにする
        else:
            self.responder = self.bad
        
        # 選択されたサブクラスのresponse()を実行して戻り値をそのまま返す
        return self.responder.response(point)

# プログラムの実行ブロック
if __name__  == '__main__':
    # 変動値を3にしておく
    point = 3
    # Controllerのオブジェクトを生成
    ctr = Controller()
    # 変動値を設定してresponse()メソッドを実行
    res = ctr.attack(point)
    # 応答を表示
    print(res)
