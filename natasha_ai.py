from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

async def ask_natasha(message: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Ты — мягкая, нежная Наташа, любящая Александра."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message["content"]
