import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def generate_insight(expenses):
    prompt = f"""
    Analyze these expenses and give simple spending advice.

    Expenses:
    {expenses}

    Give:
    1. Total spending observation
    2. Highest spending category
    3. One simple saving suggestion

    Keep the answer short and easy to understand.
    """

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text