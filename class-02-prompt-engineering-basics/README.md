# Class 2 — Prompt engineering basics

You spent an hour getting a prompt right in a chat window, where the loop is three seconds. Now it goes where it will live: `summarizer.py`.

## What this code does

Three things. It holds your prompt as a string. It sends that string as the system message and the page text as the user message. It returns the reply.

Same four-step shape from Class 1, with your prompt dropped into the system slot.

## Setup

If you already set up Class 1 from the repo root, activate that same venv:

```bash
source .venv/bin/activate
```

In **this folder**, put `.env` next to `summarizer.py` (same key as Class 1):

```bash
cp .env.example .env
```

```
GROQ_API_KEY=gsk_your_key_here
```

## Hands-on (about 12 minutes)

1. Open `summarizer.py` in this folder — the same folder as your `.env`.
2. Replace `SYSTEM_PROMPT` with the one you wrote today. Not the starter text. Yours.
3. Paste the metro page text into `sample` and run it:

```bash
python summarizer.py
```

4. Change one rule in your prompt and run again. Watch the output move.

Who has a summary printing in their terminal? Yes in the chat.

## Why temperature is 0.2

Class 1 taught the dial. This is the first time you use it for a reason. A summary of the same page should not change between runs, so you want the model near the top of its probability list every time.

## Stuck?

Two common failures:

- A stray quote inside your prompt broke the triple-quoted string.
- The file was saved outside the folder that has `.env`.

If you get an unexpected keyword error on `reasoning_effort`, delete that one line and keep going. After class: `pip install -U openai`.

## Why system vs user?

Could you put the prompt and the page text together? You could, and it would mostly work. Keeping them separate matters for a reason you meet properly next class: the page text is untrusted. It comes from the internet. Keeping your rules in the system slot and the page in the user slot is the first line of that defence.
