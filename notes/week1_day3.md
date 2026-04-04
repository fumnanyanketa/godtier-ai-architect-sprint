# Week 1 Day 3 — First API Call

## What I built
A Python script that sends a message to Claude and prints the response.

## What each part does
- `.env` file: stores my API key securely so it never appears in my code
- `.gitignore` file: tells Git to never upload the `.env` file to GitHub
- `pip install`: downloaded the anthropic and python-dotenv packages
- `import`: fetches a package so the script can use it
- `load_dotenv()`: reads the .env file and loads the API key into memory
- `client = anthropic.Anthropic()`: opens the connection to Anthropic's servers
- `client.messages.create()`: sends the message to Claude and gets a response
- `message.content[0].text`: pulls the actual text out of Claude's response

## What a token is
A token is a small chunk of text which is about 1 token per word. 256 tokens = roughly 190 words maximum. Claude had to clarify this: 
 token is not exactly one word. A token is a chunk of text — and that chunk can be:

A whole word: cat = 1 token
Part of a word: un, believ, able = 3 tokens for "unbelievable"
A punctuation mark: . or , = 1 token
A space + word combined:  hello = 1 token

So the real ratio is approximately:
100 tokens ≈ 75 words
Or put another way:
1 token ≈ 0.75 words
That is why 256 tokens comes out to roughly 190 words — not 256 words. Because many of those 256 tokens are being "spent" on punctuation, spaces, word fragments, and short connecting words like "the", "and", "is."
The reason tokens exist at all — rather than just counting words — is that Claude's underlying system (like all large language models, LLM = Large Language Model) doesn't actually read text the way humans do. It breaks everything into these small chunks first, processes the chunks, and then reassembles meaning from them. Tokens are the unit of measurement for that process.
This also means longer, complex words cost more tokens than short simple words. The word "unbelievable" costs more tokens than the word "cat."


## What an API key is
API is an acronym for application programming interface which is like a doorway through which the code we write can access Claude's servers

## Exam domain this maps to
Domain 1: Agentic Architecture — understanding how code connects to AI models
is the foundation of every agent you will ever build.

## What confused me today
so i kinda struggled with doing everything on my own without hand holding especially from the python side of things. setting up the environment from the ground up. the tutor from the youtube video suggested that we do this before moving forward and i had to repeat the particular steps about four times before I could do it without errors. but I have learned that making mistakes and figuring out what went wrong is the best way to learn. Then I also made some mistakes with creating files, specifically with naming them. when Claude gave the instruction that I should write code .env, I thought that was the file name so i created it directly throught the left hand panel by clicking the create file icon but when we tried to communicate with claude servers throught the api keys, ofcourse it didn't work and when claude askeed to see the error, it became clear what had gone wrong.

## Week 1 Friday Build — Terminal Handshake

### What I built
A Python script that reads messy Finnish vocabulary notes from a text file,
sends them to Claude via the API, and saves a clean organised list as a new file.

### What hallucination means
When an AI model generates content that was not in the original input.
Claude invented hundreds of Finnish words that were never in my notes.
This happened because the input was too large for the output space.

### What fixed it
Reducing the input to 20 words gave Claude enough output space to 
process the notes faithfully without inventing content.

### What a context window is
The maximum amount of text a model can read and process in one API call.
Too much input with too little output space causes the model to improvise.

### What this maps to in the exam
Domain 4 — Prompt Engineering. How you write instructions and manage
input size directly affects the quality and accuracy of the output.