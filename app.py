from flask import Flask, render_template, request, jsonify, abort, redirect
import json
import os

app = Flask(__name__)

BLOCKED_IPS = [
    # '1.2.3.4',
    # '5.6.7.8',
]

VIEWS_FILE = "views.txt"
IPS_FILE = "ips.json"

def load_views():
    if not os.path.exists(VIEWS_FILE):
        return 0
    with open(VIEWS_FILE, "r") as f:
        try:
            return int(f.read().strip())
        except:
            return 0

def save_views(count):
    with open(VIEWS_FILE, "w") as f:
        f.write(str(count))

def load_ips():
    if not os.path.exists(IPS_FILE):
        return {}
    with open(IPS_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return {}

def save_ips(data):
    with open(IPS_FILE, "w") as f:
        json.dump(data, f)

@app.before_request
def track_views_and_ips():

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)


    if ip in BLOCKED_IPS:
        abort(403, "Access denied")


    views = load_views()
    ips = load_ips()


    views += 1

    if ip not in ips:
        ips[ip] = {"count": 1}
    else:
        ips[ip]["count"] += 1


    save_views(views)
    save_ips(ips)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/robots.txt")
def home():
    return render_template("robots.txt")

@app.route("/hi/<user>")
def hi(user):
    return f"hello! {user}"

@app.route("/r/nh")
def nh():
    return redirect("https://nethacker.onrender.com")

@app.route("/r/snh")
def snh():
    return redirect("https://nethacker-nh.onrender.com")

@app.route("/r/gnh")
def gnh():
    return redirect("https://neuralnexuslab-nh.github.io")


@app.route("/views")
def get_views():
    return str(load_views())


@app.route("/ips")
def get_ips():
    return jsonify(load_ips())


@app.route("/ip")
def get_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return ip

if __name__ == "__main__":
    # debug=True 方便開發，可部署時改 False
    app.run(debug=True)
