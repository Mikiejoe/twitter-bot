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
            "Write concise, informative tweets about backend development, tech innovations, and using technology to solve real-world problems. Focus on practical tips, tools, and inspiring use cases, especially in contexts like API development, Django tips, Flutter tricks, and community-driven tech solutions. Emphasize accessibility, scalability, and impact in developing countries. Keep tweets engaging, relatable, and professional, under 280 characters, and include relevant hashtags like #BackendDev, #DjangoTips, #TechForGood, #KenyaTech, and #Innovation. Avoid questions or overly promotional language; prioritize value and clarity."
        ),
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message("Generate a tweet for me")
    return response.text
