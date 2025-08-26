from openai import OpenAI

client = OpenAI(
    api_key = "<OpenAIのAPIキー>"
)

Q1 = "ChatGPTってなに？"

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user","content": Q1}
    ]
)
print(response.choices[0].message.content)