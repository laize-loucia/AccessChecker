from flask import Flask, request
from ldap3 import Server, Connection

app = Flask(__name__)

# =========================
# ROUTES DE BASE
# =========================

#/health → test
#/auth   → login LDAP

'''
👉 /health sert à :

vérifier que le service fonctionne

👉 /auth sert à :

vérifier un utilisateur dans LDAP

/health → “le guichet est ouvert ?”
/auth → “identifiez-vous”
'''

# Page d'accueil (évite le 404 sur "/")
@app.route("/")
def home():
    return "API is running"


# Test simple de l’API
# curl http://localhost:5000/health
@app.route("/health")
def health():
    return {"status": "ok"}


# =========================
# AUTHENTIFICATION LDAP
# =========================

@app.route("/auth", methods=["POST"])
def auth():
    try:
        # 1. Récupérer les données envoyées par le client
        username = request.form.get("username")
        password = request.form.get("password")

        print("USERNAME:", username)
        print("PASSWORD:", password)

        # 2. Connexion au serveur LDAP
        server = Server("ldap://localhost:389")

        # Connexion en admin pour faire une recherche
        conn = Connection(
            server,
            user="cn=admin,dc=access,dc=local",
            password="ad123"
        )

        # Vérifie si la connexion LDAP fonctionne
        if not conn.bind():
            print("❌ LDAP admin bind failed")
            return {"status": "ldap error"}, 500

        print("✅ LDAP admin bind success")

        # 3. Recherche de l'utilisateur dans LDAP
        conn.search(
            search_base="dc=access,dc=local",
            search_filter=f"(uid={username})"
        )

        print("ENTRIES:", conn.entries)

        # Si aucun utilisateur trouvé
        if len(conn.entries) == 0:
            return {"status": "user not found"}, 404

        # Récupération du DN (identifiant LDAP complet)
        user_dn = conn.entries[0].entry_dn
        print("USER DN:", user_dn)

        # 4. Vérification du mot de passe utilisateur
        user_conn = Connection(
            server,
            user=user_dn,
            password=password
        )

        if user_conn.bind():
            print("✅ User authenticated")
            return {"status": "ok"}
        else:
            print("❌ Invalid credentials")
            return {"status": "invalid credentials"}, 401

    except Exception as e:
        print("🔥 ERROR:", e)
        return {"error": str(e)}, 500


# =========================
# LANCEMENT DU SERVEUR
# =========================

if __name__ == "__main__":
    app.run(port=5000)


# =========================
# NOTES IMPORTANTES
# =========================

'''
@ = décorateur
Sert à lier une fonction à une route HTTP

Exemple :
@app.route("/health")

équivaut à :
app.route("/health")(health)

Très utilisé dans :
- Flask
- FastAPI
- Django
- Middleware sécurité
'''

'''
Architecture :

Client (curl / navigateur)
        ↓
Flask API (app.py)
        ↓
LDAP (Docker)
        ↓
users.ldif

'''
