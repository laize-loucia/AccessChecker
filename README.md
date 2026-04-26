

/!\ Projet en cours

# Projet 

J'ai fait un système d'authentification avec un service API , qui agit comme le point d'entrée intermédiaire à l'authentification d'un utilisateur quelconque et une base utilisateurs avec LDAP.


L'application AccessChecker permet de vérifier ce qui rentre, l'authentification et l'autorisation.


```mermaid
gantt
    title Profil de Charge Révisé (Lissage des Ressources)
    dateFormat  YYYY-MM-DD
    axisFormat  Jour %j
    
    section PILOTE (Dispo 1)
    A (Audit)           :active, p1, 2026-01-01, 4d
    C (Normalisation)   :active, p2, 2026-01-08, 4d
    D (Maquettage)      :active, p3, 2026-01-12, 5d
    H (Script KPI)      :active, p4, 2026-01-18, 4d
    I (Affichage)       :active, p5, 2026-01-22, 3d
    J (Graphes)         :active, p6, 2026-01-25, 2d
    L (Guide)           :active, p7, 2026-01-29, 3d
    M (Doc Tech)        :active, p8, 2026-02-01, 2d
    N (Formation)       :active, p9, 2026-02-03, 1d

    section DEV (Dispo 1)
    G (Script Flux)     :crit, d1, 2026-01-12, 6d
    E (Règles Excel)    :crit, d2, 2026-01-18, 2d
    F (Dév VBA)         :crit, d3, 2026-01-20, 2d
    K (Recette)         :crit, d4, 2026-01-27, 2d

    section PPO (Dispo 2)
    A (Audit)           : 2026-01-01, 4d
    B (Structure)       : 2026-01-05, 3d
```


# Architecture


J'ai réalisé ce 1er projet en local qui implémente un Reverse proxy, point d'entrée et pilier de l'archicture.

Il permet de :

* protèger les services internes
* appliquer des règles de sécurité (TLS, WAF...)
* séparer **exposition réseau**

![Aperçu Rôle Reverse Proxy](ReverseProxyNGINX.png "TRverse Proxy Role").


 Dans ce cas précis, le client fait une requête, qui passe par le service Flask que le proxy redirige vers l'annuaire.


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
