
### Genèse du projet

Comprendre le rôle d'un reverse proxy en système est très important. 
C'est le pilier qui assure la robustesse d'une archicture.

Un **reverse proxy** est un point d’entrée unique qui :
* protège les services internes
* applique des règles de sécurité (TLS, WAF, rate-limit)
* sépare **exposition réseau** et **logique applicative**

![Aperçu Rôle Reverse Proxy](ReverseProxyNGINX.png "TRverse Proxy Role").


#NGINX

## Etapes du projet *AccessChecker*

1️⃣ **Mettre en place l’annuaire LDAP**

* Déployer OpenLDAP avec **Docker / docker-compose**
* Créer utilisateurs et groupes
* Vérifier l’authentification depuis un client

2️⃣ **Déployer le service d’authentification**

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


##Sources
 [freeCodeCamp.org](https://www.youtube.com/watch?v=9t9Mp0BGnyI)
