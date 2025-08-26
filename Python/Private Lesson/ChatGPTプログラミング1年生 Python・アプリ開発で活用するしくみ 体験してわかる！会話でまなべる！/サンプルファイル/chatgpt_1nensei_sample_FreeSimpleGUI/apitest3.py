from openai import OpenAI

client = OpenAI(
    api_key = "<OpenAIのAPIキー>"
)

role = "あなたは優れたプログラマーです。"
Q1 = "何が好きですか？"

stream = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": role},
        {"role": "user", "content": Q1}
    ],
    stream=True
)
for chunk in stream:
    content = chunk.choices[0].delta.content or ""
    print(content, end="")
print("\n【終了】")