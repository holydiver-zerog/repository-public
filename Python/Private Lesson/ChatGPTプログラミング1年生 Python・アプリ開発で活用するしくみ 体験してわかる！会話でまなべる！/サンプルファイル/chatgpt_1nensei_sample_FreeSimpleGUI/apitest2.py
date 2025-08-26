from openai import OpenAI

client = OpenAI(
    api_key = "<OpenAIのAPIキー>"
)

Q1 = "ChatGPTってなに？"

stream = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user","content": Q1}
    ],
    stream=True
)
for chunk in stream:
    content = chunk.choices[0].delta.content or ""
    print(content, end="")
print("\n【終了】")