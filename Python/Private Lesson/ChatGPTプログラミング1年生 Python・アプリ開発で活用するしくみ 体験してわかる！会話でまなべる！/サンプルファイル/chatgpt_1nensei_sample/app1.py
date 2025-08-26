from openai import OpenAI
import PySimpleGUI as sg
sg.theme("DarkBrown3")

client = OpenAI(
    api_key = "<OpenAIのAPIキー>"
)

selects = ["英語", "フランス語", "ドイツ語", "スペイン語", "ロシア語", "中国語", "韓国語", "日本語"]
layout = [[sg.T("入力文："), 
           sg.ML("こんにちは。私はChatGPTの勉強をしています。", s=(50,3), k="in")],
          [sg.Im("futaba.png"),
          sg.Combo(selects, default_value = selects[0], s=(10), k="cb"),
          sg.T("に翻訳するよ。"),
          sg.B("実行", k="btn")],
          [sg.ML(k="txt", font=(None,14), s=(60,13))]]
win = sg.Window("自動翻訳", layout,
                font=(None,14), size=(550,400))

def execute():
    prompt = f"以下の文章を{v['cb']}に翻訳してください。\n###{v['in']}"

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
