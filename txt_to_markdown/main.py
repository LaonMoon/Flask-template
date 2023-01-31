from flask import Flask, render_template
import markdown

app = Flask(__name__)

@app.route("/")
def index():
    with open("kakao_after.txt", "r", encoding="UTF-8") as file:
        content = file.read()

    html = markdown.markdown(content)
    return render_template("index.html", content=html)

if __name__ == "__main__":
    app.run()