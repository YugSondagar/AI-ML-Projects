from flask import Flask, render_template, request, jsonify
from MarketInsight.components.agents import agent
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "").strip()

        if not message:
            return jsonify({"error": "Message cannot be empty"}), 400

        thread_id = data.get("threadId", "default-session")

        config = {"configurable": {"thread_id": thread_id}}
        result = agent.invoke(
            {"messages": [("user", message)]},
            config
        )

        return jsonify({
            "response": result["messages"][-1].content
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
