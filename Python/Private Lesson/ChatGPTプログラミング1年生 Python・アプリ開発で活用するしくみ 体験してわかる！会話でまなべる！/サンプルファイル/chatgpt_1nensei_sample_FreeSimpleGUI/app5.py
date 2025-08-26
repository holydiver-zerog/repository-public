from openai import OpenAI
import FreeSimpleGUI as sg
sg.theme("DarkBrown3")

client = OpenAI(
    api_key = "<OpenAIのAPIキー>"
)

selects = ["お客様宛て", "学校の先生宛て", "親しい友人宛て", "親しくない友人宛て"]
layout = [[sg.T("メール："), 
          sg.ML("明日の打ち合わせ、都合が悪いから、延期して。", s=(50,3), k="in")],
          [sg.Im("futaba.png"),
          sg.Combo(selects, default_value = selects[0], s=(15), k="cb"),
          sg.T("のメールに変換するよ。"),
          sg.B("実行", k="btn")],
          [sg.ML(k="txt", font=(None,14), s=(60,13))]]
win = sg.Window("メールの文調変換", layout,
                font=(None,14), size=(550,400))

def execute():
    prompt = f"以下のメールを{v['cb']}に変換してください。\n###{v['in']}"

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
