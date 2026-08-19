import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_ai(question):
    print("Question:", question)

    prompt = f"""
    You are Jarvis.

    Answer in less than 40 words.
    Don't use markdown.
    Don't use bullet points.
    Speak like a human.

    Question: {question}
    """

    try:
        # Send the prompt to Gemini
        response = model.generate_content(prompt)
        if not response.text:
            return "Sorry Boss. Gemini didn't return any response."

        print("=" * 50)
        print("response.text =", repr(response.text))
        print("type =", type(response.text))
        print("=" * 50)

        # Clean the response
        answer = response.text
        answer = answer.replace("*", "")
        answer = answer.replace("\n", " ")
        answer = answer.replace("`", "")

        return answer

    except Exception as e:

        error = str(e)

        print("=" * 50)
        print("Gemini Error:", error)
        print("=" * 50)

        if "429" in error:
            return "Sorry Boss. I have reached my Gemini request limit. Please wait a minute and try again."

        elif "API_KEY" in error or "api key" in error.lower():
            return "Sorry Boss. There seems to be a problem with my Gemini API key."

        elif "503" in error:
            return "Sorry Boss. Gemini servers are currently unavailable. Please try again later."

        elif "404" in error:
            return "Sorry Boss. I couldn't reach the Gemini service."

        else:
            return "Sorry Boss. Something went wrong while contacting Gemini."