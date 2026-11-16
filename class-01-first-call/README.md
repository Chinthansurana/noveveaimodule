# Class 1 — First call

One Python file. It loads a Groq key, asks for one thing to do in Leh, and prints the reply.

Get a key at [console.groq.com/keys](https://console.groq.com/keys). It starts with `gsk_`.

From the **repo root**:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

In **this folder**, copy the example env and put your key in:

```bash
cp .env.example .env
```

Open `.env` and put your key on the line, with no spaces around the `=`:

```
GROQ_API_KEY=gsk_your_key_here
```

`.env` must sit in **this same folder** as `first_call.py`.

```bash
python first_call.py
```

The call goes to `https://api.groq.com/openai/v1` and uses `openai/gpt-oss-120b`. If the script stops before a reply, the message in the terminal lists the three things to check. Your key stays in `.env`, which git ignores.
