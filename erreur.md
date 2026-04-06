
une architecture = plusieurs services → ils doivent TOUS être lancés

[Client] ↓ [Flask API] ↓ [LDAP Docker]

💥 ❗ Ton erreur
curl -k https://localhost:8443/auth ...

👉 ça donne :

405 Method Not Allowed
🧠 🔍 Traduction
La route existe MAIS
tu n’utilises pas la bonne méthode HTTP
⚠️ Pourquoi ?

Dans ton code Flask :

@app.route("/auth", methods=["POST"])

👉 donc :

/auth accepte UNIQUEMENT POST
❌ Ce que tu as fait
curl https://localhost:8443/auth

👉 ça envoie :

GET
✅ Ce qu’il faut faire

👉 refaire avec POST :

curl -k -X POST https://localhost:8443/auth \
-d "username=jdoe" \
-d "password=password"
🎯 Résultat attendu
{"status":"ok"}
💡 Deuxième petite erreur
curl: (6) Could not resolve host: ...

👉 parce que tu as laissé :

...

👉 dans la commande 😄

🧠 Résumé mental (important)
405 = mauvaise méthode HTTP
404 = route inexistante
502 = backend down

👉 ça c’est des réflexes de dev/sec
