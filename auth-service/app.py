from flask import Flask, request
from ldap3 import Server, Connection

app = Flask(__name__)


#/health → test
#/auth   → login LDAP

#SI quelqu’un va sur /health
#ALORS exécute la fonction health()



'''

👉 /health sert à :

vérifier que le service fonctionne

👉 /auth sert à :

vérifier un utilisateur dans LDAP

/health → “le guichet est ouvert ?”
/auth → “identifiez-vous”
'''

# 1 - Test du bon fonctionnement de l'API
@app.route("/")
def home():
    return "API is running"


# après on ajoute LDAP
#sinon si LDAP ne marche pas on ne saura pas si ça vient de Flask ou LDAP

@app.route("/health")
def health():
    return {"status": "ok"}




@app.route("/auth", methods=["POST"])
def auth():
    username = request.form.get("username")
    password = request.form.get("password")

    server = Server("ldap://localhost:389")

    # 1. Connexion admin
    conn = Connection(
        server,
        user="cn=admin,dc=access,dc=local",
        password="ad123"
    )

    if not conn.bind():
        return {"status": "ldap error"}, 500

    # 2. Recherche utilisateur
    conn.search(
        "dc=access,dc=local",
        f"(uid={username})"
    )

    if len(conn.entries) == 0:
        return {"status": "user not found"}, 404

    user_dn = conn.entries[0].entry_dn

    # 3. Test mot de passe
    user_conn = Connection(server, user=user_dn, password=password)

    if user_conn.bind():
        return {"status": "ok"}
    else:
        return {"status": "invalid credentials"}, 401


if __name__ == "__main__":
    app.run(port=5000)





#crée le serveur web
#le service python va interroger le LDAP pour interroger un login

''''
app = Flask(__name__)  #app = serveur flask

@app.route("/health")  #"Quand quelqu’un va sur /health → exécute la fonction health()"
def health():
    return {"status": "ok"} #réponse json

@app.route("/auth", methods="POST")
def auth():
    if request.method == 'POST':
        username = request.form.get("username")


'''
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
