from openai import OpenAI
import FreeSimpleGUI as sg
sg.theme("DarkBrown3")

client = OpenAI(
    api_key = "<OpenAIのAPIキー>"
)

selects = [ "不思議な昔話", "悲しい昔話", "怖い昔話", "教訓的な昔話", "心に染みるいい話"]
layout = [[sg.T("テーマ："), 
          sg.ML("夏休みの学校", s=(50,3), k="in")],
          [sg.Im("futaba.png"),
          sg.Combo(selects, default_value = selects[0], s=(16), k="cb"),
          sg.T("を書くよ。"),
          sg.B("実行", k="btn")],
          [sg.ML(k="txt", font=(None,14), s=(60,13))]]
win = sg.Window("昔話自動生成", layout,
                font=(None,14), size=(550,400))

def execute():
    role = "あなたは昔話の語り部です。語尾に「だそうな」「じゃった」などをつけて話します。"
    prompt = f"以下のテーマで、{v['cb']}を語ってください。\n###{v['in']}"

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
