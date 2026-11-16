# AI Role-Play Travel Chatbot

A command-line travel assistant built with Python and the OpenAI-compatible Chat Completions API. A system prompt gives it a friendly travel-guide persona, and in-memory conversation history lets it answer follow-up questions using earlier turns.

## Features

- Friendly travel-guide persona.
- Interactive command-line chat.
- Sends conversation history with each API request.
- Type `exit` to end the conversation.

## Requirements

- Python 3.10+
- API credentials and endpoint supplied by your provider or lab.
- Access to the `gpt-5.6-luna` model.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configure environment variables

```bash
export OPENAI_API_KEY="your-api-key"
export OPENAI_API_BASE="your-api-base-url"
```

For the KodeKloud lab, load the provided variables as instructed, for example:

```bash
source /root/.bash_profile
```

Never commit API keys, `.bash_profile`, or `.env` files.

## Run

```bash
python chatbot.py
```

## How conversation history works

The `messages` list starts with a `system` message defining the chatbot's role. Each user message is appended with role `user`, and each model reply is appended with role `assistant`. The full list is sent on every API request so the model receives earlier context.

**Limitation:** History exists only in the running Python process. Restarting the program clears it. This project does not use a database or persistent memory.

## API settings

- Model: `gpt-5.6-luna`
- Temperature: `0.7`
- Maximum output tokens: `100`

## Concepts learned

- OpenAI-compatible API client
- Environment variables
- System prompts and message roles
- Chat Completion API
- In-memory conversation history
- Interactive loops and user input

## Security

Keep credentials outside source code. Do not upload API keys, `.bash_profile`, virtual environments, or `.env` files to GitHub.
