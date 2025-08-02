from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyBaEj-GS-_xQSQ7Q9fSHWJntalc1FadjRU")

def chatbot_response(message, language):
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    
    prompt = f"Respond in {language}: {message}"
    response = model.generate_content(prompt)
    
    return response.text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    lang = request.form.get("lang", "en")  # Default to English if no language is selected
    return chatbot_response(user_text, lang)

if __name__ == "__main__":
    app.run(debug=True)
