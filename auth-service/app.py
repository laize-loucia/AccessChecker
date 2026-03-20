from flask import Flask
import ldap3



#Ça crée le serveur web

#décorateur.
#permet de modifier ou enrichir une fonction sans changer son code

#"Quand quelqu’un va sur /health → exécute la fonction health()"

#app = serveur flask

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}
