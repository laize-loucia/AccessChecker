from flask import Flask
import ldap3

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}
