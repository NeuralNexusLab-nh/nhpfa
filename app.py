from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hi/<user>")
def hi (user):
    return "hello! " + user

@app.route("/r/nh")
def nh ():
    return "<script>window.location.href='https://nethacker.onrender.com'</script>"

@app.route("/r/snh")
def snh ():
    return "<script>window.location.href='https://nethacker-nh.onrender.com'</script>"

@app.route("/r/gnh")
def gnh ():
    return "<script>window.location.href='https://neuralnexuslab-nh.github.io'</script>"

if __name__ == "__main__":
    app.run(debug=True)
