# week1_terminal_handshake.py
# Week 1 Friday Build — The Terminal Handshake
#
# What this does:
#   1. Reads a text file of messy Finnish vocabulary notes
#   2. Sends the contents to Claude via the Anthropic API
#   3. Asks Claude to return a clean, organised vocabulary list
#   4. Prints the result in the terminal
#   5. Saves the clean result as a new file
#
# Why this matters:
#   This is your first complete AI-powered tool.
#   It combines three things you now know how to do:
#   - Navigate the terminal
#   - Write Python
#   - Call the Claude API
#   This is the pattern every future build will expand on.

import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

input_file = "finnish_notes.txt"

if not os.path.exists(input_file):
    print(f"Error: '{input_file}' not found.")
    print("Make sure finnish_notes.txt is in the same folder as this script.")
    exit()

with open(input_file, "r", encoding="utf-8") as f:
    file_content = f.read()

print("Notes loaded. Sending to Claude...\n")

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"""You are helping a Finnish language student organise their vocabulary notes.

Please take the messy notes below and return a clean, organised vocabulary list.

Format the output exactly like this:
- Each word on its own line
- Finnish word on the left, English translation on the right, separated by a dash
- Group words alphabetically
- Fix any spelling errors if obvious
- Do not add any words that are not in the original notes

Here are the messy notes:

{file_content}"""
        }
    ]
)

clean_notes = response.content[0].text

print("── Claude's Organised Notes ───────────────────────────")
print(clean_notes)
print("───────────────────────────────────────────────────────\n")

output_file = "finnish_notes_clean.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(clean_notes)

print(f"Clean notes saved to '{output_file}'")