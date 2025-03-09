from openai import OpenAI
import os

client = OpenAI()

def get_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

prompt = ''
response = get_response(prompt)
print(response)
