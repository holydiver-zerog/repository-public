from datetime import datetime
import tkinter as tk


def onChange(e):
    # 寿命年齢
    jyumyou = 80

    if not (year.get() or month.get() or day.get()):
        lifedays.configure(text="今日までの日数も計算します")
        nokoridays.configure(text="寿命までの日数も計算します")
        return

    try:
        delta1 = datetime.now() - datetime(int(year.get()), int(month.get()), int(day.get()))
        delta2 = datetime(int(year.get())+jyumyou, int(month.get()), int(day.get())) - datetime.now()
    except ValueError:
        lifedays.configure(text="正しい日付を入れてください。")
        nokoridays.configure(text="正しい日付を入れてください。")
    else:
        lifedays.configure(text="あなたは今日まで{0}日生きています。".format(delta1.days))
        nokoridays.configure(text="あなたは寿命まであと{0}日です。".format(delta2.days))

def btn_click():
    nikki = comment.get()
    f = open("mynikki.txt", "a")
    f.write(nikki+"\n")  # str()キャストがいわゆるtoString()のこと
    today = datetime.now()
    datalist = ["日記の投稿日時\n", str(today)+"\n"]
    f.writelines(datalist)
    f.close()
    #※テキストボックス２の内容を消去する処理を加える

# テキストボックスの内容を削除する
def clearTextInput():
    comment.delete(0, tk.END)    # delete(はじめの文字数、終わり)

# キーワード検索して結果をテキストボックスに挿入
def kensakuKekka():
    word = keyword.get()
    f = open("mynikki.txt", "r")
    wordlist = f.readlines()
    for i in wordlist:
        if word in i:
            kekka.insert(0,wordlist[wordlist.index(i)])
    f.close()


# ウィンドウの設定
root = tk.Tk()
root.title("あと何日？日記！")
root.geometry("800x400")
label_top = tk.Label(root, text="今まで何をしてきたか。今何をやるか。いつまでに何をやるか。考えよう")
# 表示する
label_top.pack()

lifedays = tk.Label(text="生年月日を入力してください今日までの日数を計算します", font=('*', 18))
lifedays.place(x=40, y=20)

nokoridays = tk.Label(text="寿命まであと何日あるでしょう", font=("", 18))
nokoridays.place(x=40, y=50)

# 生年月日のラベルタイトル
lbl_7 = tk.Label(root, text="生年月日（西暦）を入力",font=("",10))
lbl_7.place(x=30, y=140)
#入力ボックスのラベルタイトル
lbl_4 = tk.Label(root, text="日記/ｺﾒﾝﾄを入力",font=("",10))
lbl_4.place(x=30, y=190)

#キーワードボックスのラベルタイトル
lbl_5 = tk.Label(root, text="日記帳からワード/日付検索\n検索ワードを入力",font=("",10))
lbl_5.place(x=30, y=260)

#検索結果コメントのラベルタイトル
lbl_6 = tk.Label(root, text="ｷｰﾜｰﾄﾞを含む１行",font=("",10))
lbl_6.place(x=30, y=340)

# 生年月日入力ボックス
year = tk.Entry(bg="Cyan")
year.place(x=30, y=160 ,width=40,height=20)
month = tk.Entry(bg="Cyan")
month.place(x=70, y=160 ,width=20,height=20)
day = tk.Entry(bg="Cyan")
day.place(x=90, y=160 ,width=20,height=20)

year.bind('<KeyRelease>', onChange)
month.bind('<KeyRelease>', onChange)
day.bind('<KeyRelease>', onChange)

# テキストボックスを作る（日記コメント入力用）
# 日記記入ボックス
comment = tk.Entry(bg="Cyan")
comment.place(x=150, y=190 ,width=400,height=60)

nyuuryoku=comment.get()
print(str(nyuuryoku))

keyword = tk.Entry(bg="Green")
keyword.place(x=150, y=300 ,width=200,height=20)

kekka = tk.Entry(bg="blue",font=("",12))
kekka.place(x=150, y=340 ,width=400,height=30)


# 保存ボタン設置 ボタン押下後のイベント追加
btn = tk.Button(root, text = "コメントを保存" ,bg="Yellow",font=("",14), command= btn_click )
btn.place(x = 400, y = 140)
#コメントの削除ボタン
sakujyo_btn = tk.Button(root,  text = "コメントを削除",font=("",12),
                        command= clearTextInput )
sakujyo_btn.place(x = 260, y = 140)

# キーワード検索ボタン
kensaku_btn = tk.Button(root,text = "キーワード検索",bg="Yellow",font=("",12),
                        command= kensakuKekka )
kensaku_btn.place(x = 400, y = 300)


# ウィンドウの表示を続ける
root.mainloop()

    