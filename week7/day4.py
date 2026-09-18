# In VS Code (requires: pip install openai, python-dotenv)
'''from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a direct, no-nonsense fitness coach."},
        {"role": "user",   "content": "James slept 6 hours and hit 7800 steps. What should he do tomorrow?"}
    ]
)

# Extract the text
reply = response.choices[0].message.content
print(reply)'''

# Simulates the object that response.choices[0].message.content extracts from
# This mirrors the actual OpenAI API response structure exactly

class Message:
    def __init__(self, content):
        self.content = content
        self.role = "assistant"

class Choice:
    def __init__(self, content):
        self.message = Message(content)

class SimulatedResponse:
    def __init__(self, content):
        self.choices = [Choice(content)]
        self.model = "gpt-4o-mini"
        self.usage = {"prompt_tokens": 45, "completion_tokens": 82, "total_tokens": 127}

# Simulated response as if the API returned it
sim_response = SimulatedResponse(
    "Sleep was the limiting factor today. James hit 7,800 steps but 6 hours is below optimal. "
    "Tomorrow: prioritize 8+ hours tonight. Keep the step target at 9,000, not 10,000, "
    "since recovery is still incomplete. Add a 20-minute walk after lunch to hit it without needing a long session."
)

# Extract the reply (same code you use with the live API)
reply = sim_response.choices[0].message.content
print("AI Coach Response:")
print(reply)
print(f"\nTokens used: {sim_response.usage['total_tokens']}")


#Building a conversation History
def simulate_ai_response(messages):
    """Simulates what the OpenAI API returns based on the last user message."""
    last_user_msg = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")

    if "7800" in last_user_msg or "low" in last_user_msg.lower():
        return "Sleep was the limiter today. Prioritize 8+ hours tonight and target 9,000 steps tomorrow."
    elif "bench" in last_user_msg.lower() or "88" in last_user_msg:
        return "88kg bench on deficit sleep is strong. Deload to 80% next session to protect the joints."
    elif "protocol" in last_user_msg.lower() or "OMAD" in last_user_msg:
        return "OMAD works on high-sleep days. On sub-7 sleep, consider 2MAD to reduce cortisol load."
    else:
        return "Noted. Keep tracking and adjust the inputs. Consistency over perfection."

# Build conversation manually (what your script would maintain)
conversation = [
    {"role": "system", "content": "You are a direct SMP fitness coach. Max 2 sentences per reply."}
]

user_inputs = [
    "James hit 7800 steps today and slept 6 hours. OMAD protocol, day 3.",
    "He also hit a bench press PR of 88kg despite the deficit.",
    "Should he switch from OMAD to 2MAD tomorrow?"
]

print("=== Conversation ===\n")
for user_msg in user_inputs:
    # Add user message
    conversation.append({"role": "user", "content": user_msg})
    print(f"User: {user_msg}")

    # Simulate AI response
    reply = simulate_ai_response(conversation)

    # Add assistant reply to history
    conversation.append({"role": "assistant", "content": reply})
    print(f"Coach: {reply}\n")