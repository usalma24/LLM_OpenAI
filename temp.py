import os
import openai
from openai import OpenAI

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a teacher, really great at explaining programming concepts in a few words."},
        {"role": "user", "content": "Explain what is an API"}
    ]
)
print(completion.choices[0].message.content) 
