from openai import OpenAI
import FreeSimpleGUI as sg
sg.theme("DarkBrown3")

client = OpenAI(
    api_key = "<OpenAIのAPIキー>"
)

selects = ["誤字脱字", "わかりにくい表現"]
layout = [[sg.T("入力文："), 
           sg.ML("今日わ、いい天気だ。だから、雨が降っています、", s=(50,3), k="in")],
          [sg.Im("futaba.png"),
          sg.Combo(selects, default_value = selects[0], s=(14), k="cb"),
          sg.T("のチェックをするよ。"),
          sg.B("実行", k="btn")],
          [sg.ML(k="txt", font=(None,14), s=(60,13))]]
win = sg.Window("誤字脱字チェック", layout,
                font=(None,14), size=(550,400))

def execute():
    prompt = f"以下の文章の{v['cb']}を調べて、修正してください。\n###{v['in']}"

    stream = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user","content": prompt}
        ],
        stream=True
    )
    win["txt"].update("")
    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        win["txt"].update(content, append=True)
        win.read(timeout=0)
    win["txt"].update("\n【以上です。】", append=True)

while True:
    e, v = win.read()
    if e == "btn":
        execute()
    if e == None:
        break
win.close()
