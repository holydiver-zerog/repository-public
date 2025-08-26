import tkinter as tk
import random


def dispLabel():
    kuji = ["大吉", "中吉", "小吉", "凶", "半吉", "末吉", "大凶", "大大吉"]
    lbl.configure(text=random.choice(kuji))


root = tk.Tk()  # 画面を作る
root.geometry("200x100")  # 画面の大きさを決める
# root.geometry("400x200")                           # 画面の大きさを決める

lbl = tk.Label(text="LABEL")  # ラベルを作る
btn = tk.Button(
    text="PUSH", command=dispLabel
)  # ボタンを作る、ボタンで関数を実行するように修正する

lbl.pack()  # 画面にラベルを配置する
btn.pack()  # 画面にボタンを配置する
tk.mainloop()  # 作ったウィンドウを表示する
