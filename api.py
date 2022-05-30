from flask import Flask, render_template, request, jsonify
import jwt

app = Flask(__name__)
password = "admin"
user = "admin"

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login_page.html")


@app.route("/autenticar", methods=["POST",])
def autenticar():
    if request.form["usuario"] == user and request.form["senha"] == password:
        encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
        return jsonify({"token": encoded_jwt})
    else:
        return render_template("login_page.html",  result="Dados incorretos!Tente novamente.")

app.run(debug=True)