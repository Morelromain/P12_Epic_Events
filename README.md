# P12_Epic_Events
Secure back-end architecture using Django ORM

[Readme in French](#français)  

## Installation

Python Version : 3.8.3  

- Clone this repository using :  
`> git clone https://github.com/Morelromain/P12_epic_events.git`

- Move to the P12_epic_events root folder with :  
`> cd P12_epic_events`

- Create a virtual environment for the project with :  
`> python -m venv env` on windows or `> python3 -m venv env` on macos or linux.

- Activate the virtual environment with :  
`> env\Scripts\activate` on windows or `> source env/bin/activate` on macos or linux.

- Install project dependencies with :  
`> pip install -r requirements.txt`

- Install PostgreSQL locally if it is not done :  
[https://www.postgresql.org/download/](https://www.postgresql.org/download/)

## Create the PostgreSQL database

- Run PostgreSQL text interface: SQL Shell (psql)  

- Create the SQL Database : `postgres=# CREATE DATABASE epic_events;` 

## Start

- Move to the folder epic_events : `> cd epic_events`  

- The first time, migrate BDD :  
`> python manage.py makemigrations`  
`> python manage.py migrate`

- The first time, load groups data and users exemples :  
`> manage.py loaddata start_data.json`  

- Run the server : `> python manage.py runserver`

## Use admin manager 

To access admin API management : [http://127.0.0.1:8000/admin-secure/](http://127.0.0.1:8000/admin-secure/)

__Pre-existing administrator account__

- Username : `Admin1`
- Password : : `86Ibra86`  
once connected, remember to change this admin password for security

__Permission__

Only administrator and management users can access
- administrator users have all permission
- management users have permissions reduced :  
go to group's managament tab for see them in detail

## Browsable API

To access browsable API : [http://127.0.0.1:8000](http://127.0.0.1:8000/)

Only sales and support users can access data

POSTMAN documentation link of the OC_P12 collection :  
[https://documenter.getpostman.com/view/14076898/TzeTHow3]
(https://documenter.getpostman.com/view/14076898/TzeTHow3)

Follow the documentation to access API endpoints, 
see all methode allow per groups, restriction, filter and more.

## Error management

An error log file can be viewed at the root of the application :  
`error.log`  
the errors identified are classified by their dates.

---

<a name="français"></a>*En Français*

## Installation

Python Version : 3.8.3  

- Clonez ce dépôt de code à l'aide de la commande :   
`> git clone https://github.com/Morelromain/P12_epic_events.git`

- Rendez-vous depuis un terminal à la racine du répertoire P12_epic_events avec la commande :  
`> cd P12_epic_events`

- Créez un environnement virtuel pour le projet :  
`> python -m venv env` on windows or `> python3 -m venv env` on macos or linux.

- Activez l'environnement virtuel :  
`> env\Scripts\activate` on windows or `> source env/bin/activate` on macos or linux.

- Installez les dépendances du projet avec la commande :  
`> pip install -r requirements.txt`

- Installez PostgreSQL localement si ce n'est pas fait:  
[https://www.postgresql.org/download/](https://www.postgresql.org/download/)

## Créer la base de donnée PostgreSQL

- Lancez PostgreSQL en interface texte: SQL Shell (psql)  

- Créez la base de donnée SQL : `postgres=# CREATE DATABASE epic_events;` 

## Exécution

- Démarrez le serveur avec `$ python manage.py runserver`

## Start

- Allez le dossier epic_events : `> cd epic_events`  

- Au 1er lancement, migrez la base de donnée :  
`> python manage.py makemigrations`  
`> python manage.py migrate`

- Au 1er lancement, chargez les données de groupes et exemples d'utilisateurs :  
`> manage.py loaddata start_data.json`  

- Démarrez le serveur : `> python manage.py runserver`


## Utilisation du gestionnaire admin

Pour accéder à la gestion API admin : [http://127.0.0.1:8000/admin-secure/](http://127.0.0.1:8000/admin-secure/)

__Compte administrateur pré-existant__

- Nom d’utilisateur : `Admin1`  
- Mot de passe : : `86Ibra86`  
une fois connecté, pensez à changer ce mot de passe pour plus de sécurité

__Permission__

- Seuls les administrateurs et les utilisateurs "management" peuvent y accéder  
- les administrateurs ont toutes les autorisations  
- les utilisateurs de gestion ont des permissions réduites :  
allez dans l'onglet du groupe "management" pour les voir en détail

## API web

Pour accéder à l'API  : [http://127.0.0.1:8000](http://127.0.0.1:8000/)

Seuls les utilisateurs "sales" et "support" peuvent accéder aux données  

Lien de la documentation POSTMAN de la collection OC_P12 :  
[https://documenter.getpostman.com/view/14076898/TzeTHow3]
(https://documenter.getpostman.com/view/14076898/TzeTHow3)

Suivez la documentation pour accéder aux points de terminaison de l'API, 
voir toutes les méthodes autorisées par groupe, restriction, filtre et autre.

## Gestion des erreurs

Un fichier journal des erreurs peut être consulté à la racine de l'application :  
`error.log`  
les erreurs identifiées sont classées par leurs dates.
