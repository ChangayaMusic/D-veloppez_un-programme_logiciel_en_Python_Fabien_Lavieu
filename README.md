# Projet 4 Fabien Lavieu


[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)]

Un programme permettant de gérer des tournois d'echecs.

## Pour commencer

Le programme s'execute en local et ne nécessite ni connexion, ni base de donnée, cependant une base de données exitante créer avec ce programme pourra être utilisée.


### Pré-requis


- Python 3.11
- Une console


### Installation

- Installer l'environement virtuel avec : python3 -m venv new-env puis pour l'activer source bin/activate
- Placer si déjà générés, les fichiers tournaments.json et/ou players.json à la racine.



## Démarrage

- Dans la console : python3 main.py
- Vous serez interrogé sur les actions que vous voulez effectuer.
- Le premier menu permet de créer et charger les données.
- L'affichage des rapports et la manipulation des données se font via leurs menus respectifs accesibles à partir du menu principal (Continue an existing tournament/Show reports)
- Le main menu dispose d'une option exit pour quitter le programmes, les menus secondaires disposent d'une option de retour au menu précédant.
  
## Fonctions

- Create a new player
  Create a new tournament

- Continue an existing tournament
  - Add player(s) to a tournament
  - Start tournament
  - End tournament
- Show reports
  - Tournaments lis
  - Tournament's name and date
  - Tournament's players by name
  - All tournament's rounds and matches


## Datas

Les datas sont enregistrées suivant :

- Les tournois : /tournaments.json
- Les joueurs : /players.json


## Flake8

Pour générer les rapport flake8 en HTML , lancez les commandes suivantes:

 - python -m pip install flake8
 - python -m pip install flake8-html
 - python -m flake8 --format=html --htmldir=flake-report

Les rapport seront disponibles suivant : /flake-reports/...



## Fabriqué avec


* Vs Studio



## Auteurs

Fabien Lavieu

## License

Ce projet est open source.


