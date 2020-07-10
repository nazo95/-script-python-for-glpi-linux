# Script d'installation GLPI pour Linux
Installation de glpi sur une machine linux via un script python 

# Conditions d'utilisation
  - Debian
  - python3.8
  - pip3
  - Sudo sans mot de passe 
  
### Sudo sans password : 
- $user = utilisateur avec lequel on va se connecter et éxécuter le script
éditer le fichier en root:
```
$ /etc/sudoers 
```
et y ajouter :
>$user ALL=(ALL) NOPASSWD: ALL
## Installations
#### python
Pré-requis
```sh
 $ sudo apt update
 $ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```
Téléchargement de python
```sh
$ cd /tmp
$ wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
```
Extraction du .tgz et initiilisation de l'installation
```sh
$ tar -xf Python-3.8.0.tgz
$ cd Python-3.8.0
$ ./configure --enable-optimizations
```
Ensuite on lance ces commandes ( on remplace 1 par le nombre de Cores de son cpu)
```
$ make -j 1
$ sudo make altinstall
````
#### pip3
```
$ sudo apt install python3-pip
```
#### yaml
```
$ pip3 install yaml-1.3
$ pip3 install pyyaml
```

# lancement du script
  -Le fichier glpi1.py et packages.yaml doivent être dans le même dossier
  - A executer avec l'user qui les droit sudo sans password 
  ```
  
$ python3 glpi1.py
```

 
### fonctionnement
Le script permet d'installer GLPI sur la machine locale il automatise:
 - le télechargement et l'installation d'apache2, mariadb, php7.3 (package.yml)
 - téléchargement de glpi et installation
 - création base de donnée 
 - installation silencieuse de glpi
 - Modifier le fichier yaml par rapport a votre configuration
 
 
 ### Renvoi d'erreur
 Si le programme renvoi l'erreur:
- 1: La mise à jour n'a pas été faite
- 2: Apache n'a pas pu redemmarer 
- 3: glpi n'a pas pu se télécharger
- 4: l'extraction de glpi n'a pas pu aboutir 
- 5: les droit n'ont pas pu étre modifier sur le fichier html
- 6: La base de donné n'a pas été créé
- 7: la configuration de glpi a echoué 
- 8: le  fichier install n'a pas été supprimé 
 
 # Script réalisé dans le cadre d'un projet de parcours de formation avec Openclassrooms
 [![N|Solid](https://blog.openclassrooms.com/wp-content/uploads/2018/05/OC.png)](https://openclassrooms.com/)
 
 ### License GNU General Public License v3.0
Vous pouvez disposer du script librement.
