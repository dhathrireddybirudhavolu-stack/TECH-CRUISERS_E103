from intent_parser import extract_intent
from agent import handle_intent

print("AI Website Assistant (Universal Demo)")
print("Type 'exit' to stop\n")

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    intent = extract_intent(user_input)
    response = handle_intent(intent, user_input)

    print("\nAI Agent:", response)
    print("-" * 50)
