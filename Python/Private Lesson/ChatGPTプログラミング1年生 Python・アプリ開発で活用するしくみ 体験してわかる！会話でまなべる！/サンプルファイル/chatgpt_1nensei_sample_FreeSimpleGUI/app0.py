import FreeSimpleGUI as sg
sg.theme("DarkBrown3")

selects = ["英語", "フランス語", "ドイツ語"]
layout = [[sg.T("入力文："), 
           sg.ML("こんにちは。私はChatGPTの勉強をしています。", s=(50,3), k="in")],
          [sg.Im("futaba.png"),
          sg.Combo(selects, default_value = selects[0], s=(10), k="cb"),
          sg.T("に翻訳するよ。"),
          sg.B("実行", k="btn")],
          [sg.ML(k="txt", font=(None,14), s=(60,13))]]
win = sg.Window("アプリテスト", layout,
                font=(None,14), size=(550,400))

def execute():
    prompt = f"以下の文章を{v['cb']}に翻訳してください。\n###{v['in']}"
    win["txt"].update(prompt)
  
while True:
    e, v = win.read()
    if e == "btn":
        execute()
    if e == None:
        break
win.close()
