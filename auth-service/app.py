from flask import Flask
import ldap3



#crée le serveur web


app = Flask(__name__)  #app = serveur flask

@app.route("/health")  #"Quand quelqu’un va sur /health → exécute la fonction health()"
def health():
    return {"status": "ok"} #réponse json

@app.route("/auth")
def auth():


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
