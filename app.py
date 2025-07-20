from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Rule-based chatbot logic
def get_bot_response(message):
    message = message.lower()

    if re.search(r"\b(hi|hello|hey)\b", message):
        return "Hello! Welcome to FoodBot 🍕. How can I assist you today?"

    elif "menu" in message:
        return "We offer 🍕 Pizza, 🍔 Burgers, 🥪 Sandwiches, and 🥤 Beverages."

    elif "order" in message and "place" in message:
        return "Sure! Please tell me what you'd like to order."

    elif "track" in message or "status" in message:
        return "Please provide your order ID so I can check the status for you."

    elif "cancel" in message:
        return "Sorry to hear that. Please share your order ID to proceed with cancellation."

    elif "open" in message or "timing" in message:
        return "We are open every day from 10 AM to 11 PM. ⏰"

    elif "location" in message or "address" in message:
        return "We are located at 123 Food Street, Flavor Town 🌍"

    elif "talk to agent" in message or "human" in message:
        return "Connecting you to a live support agent... 👨‍💻"

    elif "bye" in message:
        return "Thank you for visiting FoodBot! Have a tasty day! 🍽️"

    else:
        return "I'm not sure I understand that. Could you please rephrase?"

# Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]
    response = get_bot_response(user_message)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
