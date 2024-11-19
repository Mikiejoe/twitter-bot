import google.generativeai as genai
from decouple import config

genai.configure(api_key=config("GEMINI_API_KEY"))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


def generate_tweet():
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=(
            "Generate a series of short, motivational posts about software development suitable for Twitter. Each post should be concise (under 280 characters), insightful, and engaging. Avoid starting with a question. Incorporate humor, but keep it professional and relatable for developers. Ensure each post resonates with software developers across all levels. One tweet at time."
        ),
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message("Generate a tweet for me")
    return response.text
