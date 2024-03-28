from flask import Flask, render_template, request, jsonify
from generate_text import TextGenerator

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_response():
    prompt = request.form["prompt"]
    text_generator = TextGenerator()
    generated_text = text_generator.generate_text(prompt)
    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run(debug=True)
