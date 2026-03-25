from flask import Flask
import ldap3


@app.route("/auth", methods=["POST"])
def auth():
    username = request.form.get("username")
    password = request.form.get("password")

    server = Server("ldap://localhost:389")

    conn = Connection (
        server,
        user="cn=admin, dc=access, dc=local",
        password="admin"
        )
        conn.bind()

        conn.search(
            "dc=access, dc=local",
            f"(uid={username})"
            )
        if len(conn.entries) == 0:
                return {"status": "user not fund"}, 404


#crée le serveur web
#le service python va interroger le LDAP pour interroger un login


app = Flask(__name__)  #app = serveur flask

@app.route("/health")  #"Quand quelqu’un va sur /health → exécute la fonction health()"
def health():
    return {"status": "ok"} #réponse json

@app.route("/auth", methods="POST")
def auth():
    if request.method == 'POST':
        username = request.form.get("username")


'''

@ = décorateur
Sert à lier une fonction à un comportement
Très utilisé dans  *Flask (API)  *FastAPI  *Django *sécurité / middlewares

@ est juste une écriture plus propre

Version sans décorateur (pour comprendre)

Le décorateur fait en réalité quelque chose comme ça :

def health():
    return {"status": "ok"}

app.route("/health")(health)
'''
