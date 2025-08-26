import sys
import mainwindow
from PyQt5 import QtWidgets

# モジュールが直接実行された場合に以下の処理を行う
if __name__ == "__main__":
    # QApplication()のコマンドライン引数を使用してアプリケーションオブジェクトを生成
    app = QtWidgets.QApplication(sys.argv)
    # 画面を構築するMainWindowクラスのオブジェクトを生成
    win = mainwindow.MainWindow()
    # メインウィンドウを画面に表示
    win.show()
    # イベントループを開始、プログラムが終了されるまでイベントループを維持
    # 終了時に0が返される
    ret = app.exec()
    # exec_()の戻り値をシステムに返してプログラムを終了
    sys.exit(ret)