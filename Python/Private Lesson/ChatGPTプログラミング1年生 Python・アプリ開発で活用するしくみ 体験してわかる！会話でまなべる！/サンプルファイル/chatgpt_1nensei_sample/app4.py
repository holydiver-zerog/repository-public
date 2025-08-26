from openai import OpenAI
import PySimpleGUI as sg
sg.theme("DarkBrown3")

client = OpenAI(
    api_key = "<OpenAIのAPIキー>"
)

selects = ["です・ます調", "だ・である調", "間接的表現", "文学的表現", "江戸時代風", "女子高生風", "大阪弁"]
layout = [[sg.T("入力文："), 
           sg.ML("今日はいい天気だ。遊びに行くぞ。", s=(50,3), k="in")],
          [sg.Im("futaba.png"),
          sg.Combo(selects, default_value = selects[0], s=(10), k="cb"),
          sg.T("に変換するよ。"),
          sg.B("実行", k="btn")],
          [sg.ML(k="txt", font=(None,14), s=(60,13))]]
win = sg.Window("文体・文調変換", layout,
                font=(None,14), size=(550,400))

def execute():
    prompt = f"以下の文章を{v['cb']}に変換してください。\n###{v['in']}"

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
