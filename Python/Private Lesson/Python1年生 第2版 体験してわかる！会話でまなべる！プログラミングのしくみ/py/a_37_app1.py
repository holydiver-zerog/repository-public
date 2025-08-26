# ラベルとボタンを表示するだけのアプリ
# from logging import root
import tkinter as tk  # tkinterをインポートしてtkと略して使う

root = tk.Tk()  # 画面を作る
root.geometry("200x100")  # 画面の大きさを決める

lbl = tk.Label(text="LABEL")  # ラベルを作る
btn = tk.Button(text="PUSH")  # ボタンを作る

lbl.pack()  # 画面にラベルを配置する
btn.pack()  # 画面にボタンを配置する
tk.mainloop()  # 作ったウィンドウを表示する
