# 画像表示アプリ
#from curses import newwin
#from os import fpathconf, fspath
import tkinter as tk                                        # tkinterをインポートしてtkと略して使う
import tkinter.filedialog as fd                             # ファイルダイアログを使うモジュール
import PIL.Image                                            # 画像を扱うモジュール
import PIL.ImageTk                                          # tkinterで作った画面上に画像を表示させるモジュール

def dispPhoto(path):                                        # 画像ファイルを表示する関数
    # 画像を読み込む
    newImage = PIL.Image.open(path).resize((300,300))       # 画像を読み込む
    # そのイメージをラベルに表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)            # イメージをラベルに表示する
    imageLabel.configure(image = imageData)                 # イメージをラベルに表示する
#   imageLabel.image_names = imageData                      # イメージをラベルに表示する
#   imageLabel.image_types = imageData                      # イメージをラベルに表示する
    imageLabel.image = imageData                            # type: ignore

def openFile():                                             # ファイルダイアログを開くための関数
    fpath = fd.askopenfilename()                            # ファイルダイアログを開いて、選択したファイル名を取得する
    if fpath:                                               # もしファイルがあったら
        dispPhoto(fpath)                                    # そのファイル名で関数を呼び出す

root = tk.Tk()                                              # 画面を作る
root.geometry("400x350")                                    # 画面の大きさを決める

btn = tk.Button(text="ファイルを開く",command=openFile)       # ボタンを作って関数を設定する
imageLabel = tk.Label()                                     # 画面表示用のラベルを作る
btn.pack()                                                  # 画面にボタンを配置する
imageLabel.pack()                                           # 画面にラベルを配置する
tk.mainloop()                                               # 作ったウィンドウを表示する