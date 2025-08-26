from openai import OpenAI
import FreeSimpleGUI as sg
sg.theme("DarkBrown3")

client = OpenAI(
    api_key = "<OpenAIのAPIキー>"
)

selects1 = ["Python", "Java", "JavaScript", "C++", "C#", "Swift", "Visual Basic"]
selects2 = ["言語の特徴", "名前の起源", "用途", "便利な機能", "隠れた機能", "データ", "バグ"]
layout = [[sg.T("言語の種類："), sg.Combo(selects1, default_value = selects1[0], s=(15), k="cb1")],
          [sg.T("テーマ内容："), sg.Combo(selects2, default_value = selects2[0], s=(15), k="cb2")],
          [sg.Im("futaba.png"),
          sg.T("これに関するトリビアを書くよ。"),
          sg.B("実行", k="btn")],
          [sg.ML(k="txt", font=(None,14), s=(60,13))]]
win = sg.Window("プログラムのトリビア自動生成", layout,
                font=(None,14), size=(550,400))

def execute():
    role = "あなたは、優れた女子高生プログラマーです。親しい口調で話します。"
    prompt = f"プログラミング言語が{v['cb1']}の{v['cb2']}に関するトリビアを1つ教えて。"

    stream = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": role},
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
