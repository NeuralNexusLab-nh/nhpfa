from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hi/<user>")
def hi (user):
    return "hello! " + user

if __name__ == "__main__":
    app.run(port=443, target='0.0.0.0', debug=True)
