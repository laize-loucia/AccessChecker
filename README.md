
# Projet 

J'ai fait un système d'authentification avec un service API , qui agit comme le point d'entrée intermédiaire à l'authentification d'un utilisateur quelconque et une base utilisateurs avec LDAP.


J'ai réalisé ce 1er projet en local qui implémente un Reverse proxy, autre point d'entrée et le pilier d'une archicture.

Il permet de :

* protèger les services internes
* appliquer des règles de sécurité (TLS, WAF, rate-limit)
* séparer **exposition réseau** et **logique applicative**

![Aperçu Rôle Reverse Proxy](ReverseProxyNGINX.png "TRverse Proxy Role").



L'application AccessChecker vérifie ce qui est entrée et qui rentre, l'authentification et l'autorisation.



# Architecture

```mermaid

flowchart TD
    Client["Client (curl / navigateur)"]
    Flask["Flask API (app.py)"]
    LDAP["OpenLDAP (Docker)"]
    LDIF["users.ldif"]

    Client --> Flask
    Flask --> LDAP
    LDAP --> LDIF
```



curl = client
Flask = serveur web (API) en Python app.py 
LDAP = serveur d’authentification

app.py = le cerveau
LDAP = la base d’utilisateurs
curl = le test


👉 /health sert à :

vérifier que le service fonctionne

👉 /auth sert à :

vérifier un utilisateur dans LDAP

client réel (utilisateur)
   
NGINX
   
API Flask
   
LDAP

## installation

pip3 install ldap3 flask


## fichier de service applicatif

Création du fichier app.py, pour établir une connexion au serveur LDAP, faire une recherche utilisateur, et une récupération du DN et vérification du mot de passe.



## client
Le client qui envoie la requête dans ce cas, curl et le navigateur http://localhost:5000/health

curl -X POST http://localhost:5000/auth \
-d "username=jdoe" \
-d "password=password"





## Erreur :

- curl: (7) Failed to connect to localhost port 5000
Le serveur Flask n’est pas lancé (ou pas accessible)


#  1 - Mise en place du LDAP

* Déployer OpenLDAP avec **Docker / docker-compose**
* Créer utilisateurs et groupes
* Vérifier l’authentification depuis un client


# 2 - Déployer le service d’authentification**

* Service applicatif (ex : Python)
* Vérification des identifiants via LDAP
* Exposition d’une API simple (`/auth`, `/health`)

3️⃣ **Installer et configurer NGINX**

* NGINX agit comme **reverse proxy** devant le service
* Redirection du trafic vers le backend
* Centralisation des accès et des logs

4️⃣ **Activer le chiffrement TLS**

* Générer des certificats (self-signed)
* Forcer HTTPS
* Vérifier la protection des échanges

5️⃣ **Ajouter OWASP ModSecurity**

* Intégrer ModSecurity à NGINX
* Activer les règles **OWASP CRS**
* Tester des attaques simples (XSS, injections)

6️⃣ **Tester et documenter**

* Cas normal / cas attaque
* Schéma d’architecture
* README clair + limites + perspectives


# Conclusion

Ce que tu as construit
Client → API Flask → LDAP → données utilisateurs

👉 donc oui :

✔ Flask = service intermédiaire (API)
✔ LDAP = base d’identités
✔ /auth = point d’entrée d’authentification

👉 ton API fait :

"Donne-moi username/password → je vérifie dans LDAP → je réponds OK/KO"

👉 ça s’appelle :

un service d’authentification

💡 → EXACTEMENT ce qu’on trouve dans les systèmes réels


##Sources
 [freeCodeCamp.org](https://www.youtube.com/watch?v=9t9Mp0BGnyI)
