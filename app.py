from flask import Flask, render_template, json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/services", methods=["GET"])
def services():
    with open("services.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        services_data = data.get("services", [])
    return render_template("services.html", services=services_data)


if __name__ == '__main__':
    app.run(debug=True)
