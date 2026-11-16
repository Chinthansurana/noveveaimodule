# summarizer.py
# Your prompt, now in the place that runs it.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

key = os.getenv("GROQ_API_KEY")
if not key:
    raise SystemExit("No GROQ_API_KEY found. Is your .env in this same folder?")

client = OpenAI(
    api_key=key,
    base_url="https://api.groq.com/openai/v1",
)

# Everything you wrote in Sections 2 to 8 goes here, between the triple quotes.
SYSTEM_PROMPT = """You summarise web pages for people who are deciding
whether to read them.

Every summary you write:
- opens with the single most useful fact, not a description of the page
- is under 80 words
- uses plain language a commuter would use
- keeps any number that affects a decision: times, fares, dates, distances
- ignores navigation menus, adverts, cookie notices and "also read" links

If the page does not say something, do not fill the gap. Say the page
does not mention it."""

SYSTEM_PROMPT_1 = """Return the summary as JSON with exactly these keys:

{
  "headline": "Pune Metro Line 3 opens Monday",
  "bullets": ["...", "..."],
  "numbers_mentioned": ["Rs 10 to Rs 45", "06:00 to 22:00"],
  "page_type": "news"
}

Rules:
- bullets: between 2 and 4 items, each under 15 words
- numbers_mentioned: copy figures exactly as written on the page, or []
- page_type: one of news, product, blog, documentation, other
- Return only the JSON object. No explanation, no code fences, no preamble."""


def summarize(page_text):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        temperature=0.2,            # low: a summary should not vary run to run
        reasoning_effort="low",     # summarising has no dependent steps
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_1},
            {"role": "user",   "content": f"Summarise this page:\n\n{page_text}"},
        ],
    )
    return response.choices[0].message.content


# Next class this text arrives from a real web page. For now, paste some in.
if __name__ == "__main__":
    sample = """Home  News  City  Sport  Business  Subscribe  Login

Pune Metro Line 3 opens to the public from Monday

PUNE, 24 Oct -- The 23.3 km Hinjawadi to Shivajinagar line will open to
passengers from Monday, the Maharashtra Metro Rail Corporation said on Friday.

Services run 06:00 to 22:00 on weekdays, with trains every 8 minutes at peak
and every 15 minutes off-peak. Fares range from Rs 10 to Rs 45 depending on
distance. The line has 23 stations, of which 21 are elevated.

Officials said the line is expected to carry around 90,000 passengers a day in
its first year, and that a feeder bus service will connect six stations to
nearby IT parks. Parking is available at nine stations at Rs 20 for two hours.

The corporation said the remaining two stations will open in March once
construction of the Shivajinagar interchange is complete.

Also read: Ten things to do in Pune this weekend
Advertisement
Copyright 2026. All rights reserved.
"""
    print(summarize(sample))
