
# Projet 

J'ai fait un système d'authentification avec un service API , qui agit comme le point d'entrée intermédiaire à l'authentification d'un utilisateur quelconque et une base utilisateurs avec LDAP.


J'ai réalisé ce 1er projet en local qui implémente un Reverse proxy, autre point d'entrée et le pilier d'une archicture.

Il permet de :

* protèger les services internes
* appliquer des règles de sécurité (TLS, WAF, rate-limit)
* séparer **exposition réseau** et **logique applicative**

![Aperçu Rôle Reverse Proxy](ReverseProxyNGINX.png "TRverse Proxy Role").



L'application AccessChecker vérifie ce qui rentre, l'authentification et l'autorisation.



# Architecture

```mermaid

flowchart TD
    Client["Client"]
    Flask["Flask API"]
    LDAP["OpenLDAP (Docker)"]
    LDIF["users.ldif"]

    Client --> Flask
    Flask --> LDAP
    LDAP --> LDIF
```


##Sources
 [freeCodeCamp.org](https://www.youtube.com/watch?v=9t9Mp0BGnyI)
