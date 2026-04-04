# week1_hello_claude.py
# Day 3 — First API call to Claude
#
# What this does:
#   Sends a single message to Claude and prints the response.
#   That's it. Simple on purpose — we're testing the connection.
#
# Why this matters:
#   Every AI system you build for the next 16 weeks starts here.
#   This is the core pattern: send a message, receive a response.
#   Everything else is built on top of this.

import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "Hello Claude. I am Fumnanya. I am building AI systems. Introduce yourself in two sentences."
        }
    ]
)

print("Claude says:")
print(message.content[0].text)