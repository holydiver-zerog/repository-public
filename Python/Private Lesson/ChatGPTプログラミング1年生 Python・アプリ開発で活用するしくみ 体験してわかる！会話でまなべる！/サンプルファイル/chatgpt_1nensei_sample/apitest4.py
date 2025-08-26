from openai import OpenAI

client = OpenAI(
    api_key = "<OpenAIのAPIキー>"
)

role = "あなたは優れたプログラマーです。"
Q1 = "Pythonでのデータ解析のヒントを教えて。"
A1 = "pandasとNumPyを活用すると効果的です。"
Q2 = "データに欠損値があるときの処理方法は？"

stream = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
            {"role": "system", "content": role},
            {"role": "user", "content": Q1},
            {"role": "assistant", "content": A1},
            {"role": "user", "content": Q2},
    ],
    stream=True
)
for chunk in stream:
    content = chunk.choices[0].delta.content or ""
    print(content, end="")
print("\n【終了】")