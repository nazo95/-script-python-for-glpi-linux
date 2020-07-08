#!/usr/bin/python3

import sys
import  os 
import  yaml


def lectureyaml():
	with open("packages.yaml", 'r') as stream:
		try:	
			return(yaml.safe_load(stream)) 
		except yaml.YAMLError as exc:
			print(exc)

lecture = lectureyaml()
s = ' '
s = s.join(lecture["lamp"])

try:
	os.system("sudo apt-get update -y && sudo apt-get upgrade -y")
except:	
	print("Erreur de mise à jours")
	sys.exit(1)


#Installation des prérequis 
try:
	os.system("sudo apt-get install " + s + ' -y')
except: 
	print("les prérequis ne se sont pas bien installé")
	sys.exit(1)

rebootapache = 'sudo service apache2 restart'

try:
	os.system(rebootapache)
except:
	print("apache n'a pas reboot")
	sys.exit(1)
 
#Telechargement de glpi
try:
	os.system("sudo wget -P /var/tmp " + lecture["glpi"]["tele"])
	print("Téléchargement de GLPI effectué")
except:
	print("Erreur de téléchargement")
	sys.exit(1)

#Extraction du fichier .tgz vers le dossier apache

try:
	os.system("sudo tar xvzf /var/tmp/glpi-9.4.5.tgz -C " + lecture["glpi"]["chemin"])
except:
	print("le fichier ne c'est pas extrait correctement")
	sys.exit(1)


# modification des droit sur le fichier /var/www/html 

r = " && "
r = r.join(lecture["cmd"])
try:
	os.system(r)
except:
	print("Echec de la modification des droit du fichier html")
	sys.exit(1)

#creation de la base de donnée 
try:
	os.system('sudo mysql -e "create database ' + lecture["connexion"]["basedb"]+'"' )
	os.system('sudo mysql -e "create user \'' + lecture["connexion"]["userdb"] + '\'@\'localhost\' identified by \'' + lecture["connexion"]["pwddb"] + '\'"')
	os.system('sudo mysql -e "grant all privileges on ' + lecture["connexion"]["basedb"] + '.* to \'' + lecture["connexion"]["userdb"] + '\'@\'localhost\'"' )
except:
	print("Echec de la création de la base de donnée")
	sys.exit(1)



#configuration de glpi
print("configuration de glpi")
try:
	os.system("sudo su && cd /var/www/html/glpi")
	os.system('sudo php ' + lecture["glpi"]["chemin"] + '/glpi/bin/console db:install -f -n -L fr_FR -H ' + lecture["connexion"]["hostname"] + ' -d ' + lecture["connexion"]["basedb"] + ' -u ' + lecture["connexion"]["userdb"] + ' -p ' + lecture["connexion"]["pwddb"])  
except:
	print("Erreur de configuration glpi")
	sys.exit(1)

#suppression du fichier install.php
#try:
	#os.system("sudo rm /var/www/html/glpi/install/install.php")
#except:
#	print("le fichier install ne c'est pas supprimé")
#	sys.exit(1)



