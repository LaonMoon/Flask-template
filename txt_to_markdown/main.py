from flask import Flask, render_template
import markdown

app = Flask(__name__)

@app.route("/")
def index():
    with open("kakao_after.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()

    return render_template("index.html", lines=lines)

if __name__ == "__main__":
    app.run()