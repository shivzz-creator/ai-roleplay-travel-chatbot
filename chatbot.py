import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

prompt = (
    "You are a friendly travel guide. "
    "Greet the user and ask where they want to go."
)

# Conversation history is kept in memory while this program runs.
messages = [{"role": "system", "content": prompt}]

print("Travel Bot: Hello! Welcome! Where would you like to travel?")
print("Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Travel Bot: Happy travels! Goodbye!")
        break

    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    nameresponse = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=messages,
        temperature=0.7,
        max_tokens=100,
    )

    assistant_reply = nameresponse.choices[0].message.content or ""
    messages.append({"role": "assistant", "content": assistant_reply})

    print(f"Travel Bot: {assistant_reply}\n")
