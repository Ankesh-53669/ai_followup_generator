import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from openai import AzureOpenAI

load_dotenv()
# Initialize OpenAI client with Azure endpoint
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
)

app = Flask(__name__)


# Function to analyze context and generate follow-up prompts
def generate_followups(user_prompt, ai_response):
    prompt = f"""
    Analyze the following conversation:
    User: {user_prompt}
    AI: {ai_response}
    Identify gaps, missing details, and suggest 2-3 concise follow-up questions to clarify or expand the conversation.
    """

    response = client.chat.completions.create(
        model="gpt4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant for refining AI conversations.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
        max_tokens=200,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
    )

    raw_followups = response.choices[0].message.content
    followups = [q.strip() for q in raw_followups.split("\n") if q.strip()]
    return followups


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_prompt = request.form.get("user_prompt", "").strip()
        ai_response = request.form.get("ai_response", "").strip()

        if not user_prompt or not ai_response:
            return render_template("index.html", error="Both fields are required.")

        followups = generate_followups(user_prompt, ai_response)
        print(followups)
        return render_template(
            "index.html",
            followups=followups,
            user_prompt=user_prompt,
            ai_response=ai_response,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
