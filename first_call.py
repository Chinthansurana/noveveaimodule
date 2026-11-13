# first_call.py
# Loads the key, creates a client, sends messages, prints the reply.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()                    # reads .env so the key is available

key = os.getenv("GROQ_API_KEY")
if not key:
    raise SystemExit(
        "No GROQ_API_KEY found.\n"
        "Check three things, in this order:\n"
        "  1. The file is named exactly .env, not .env.txt\n"
        "  2. It sits in the same folder as this file\n"
        "  3. The line reads GROQ_API_KEY=gsk_... with no spaces around the ="
    )

# The same library talks to Groq. Only these two lines name a provider.
client = OpenAI(
    api_key=key,
    base_url="https://api.groq.com/openai/v1",
)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    temperature=0.2,             # low, because we want consistency
    messages=[
        {"role": "system", "content": "You are a witty travel guide."},
        {"role": "user",   "content": "Suggest one thing to do in Bangalore."},
    ],
)

print(response.choices[0].message.content)
