'''The coaching layer is a function that takes structured data in and returns a formatted coaching response out. 
It does not make decisions about whether to run or when. 
It only knows how to turn data into a message.'''

'''
import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_coaching_message(sleep, water, bench, hit_goal, confidence):
    prompt = (f"Athlete data: sleep {sleep}h, water {water} glasses, "
              f"bench {bench}kg. "
              f"Goal prediction: {'HIT' if hit_goal else 'MISS'} ({confidence:.0%} confidence). "
              "Give a 2-sentence coaching response. Be direct and specific.")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": ("You are an SMP performance coach. "
                          "You give direct, data-driven coaching feedback. "
                          "No filler. Two sentences maximum.")},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
    '''
