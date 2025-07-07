from openai import OpenAI 

client = OpenAI(
    api_key="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")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role":"system", "content":"you are a virtual assistant named Nova skilled in general task like alexa and google cloud"},
        {"role": "user", "content":"what is coding"}
    ]
)
print(completion.choices[0].message.content)
