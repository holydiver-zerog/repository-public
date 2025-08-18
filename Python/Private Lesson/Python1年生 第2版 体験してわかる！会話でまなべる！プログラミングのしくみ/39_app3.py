# ラベルとボタンを表示するだけのアプリ(37_app1.py)
# こんにちはと表示する関数を追加
#from logging import root
import tkinter as tk                                # tkinterをインポートしてtkと略して使う

def dispLabel():                                    # 関数を追加する
    lbl.configure(text="こんにちは")                  # ラベルの文字を「こんにちは」に変更する

root = tk.Tk()                                      # 画面を作る
root.geometry("200x100")                            # 画面の大きさを決める
#root.geometry("400x200")                           # 画面の大きさを決める

lbl = tk.Label(text="LABEL")                        # ラベルを作る
btn = tk.Button(text="PUSH",command=dispLabel)      # ボタンを作る、ボタンで関数を実行するように修正する

lbl.pack()                                          # 画面にラベルを配置する
btn.pack()                                          # 画面にボタンを配置する
tk.mainloop()                                       # 作ったウィンドウを表示する