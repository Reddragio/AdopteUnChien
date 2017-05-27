import sqlite3
from random import randint

conn = sqlite3.connect('dogs.db')
c = conn.cursor()
conn2 = sqlite3.connect('names.db')
w = conn2.cursor()
#conn2.text_factory = str    
#Corrige un bug provoqué par les accents français

c.execute("""CREATE TABLE IF NOT EXISTS chien(id_chien INT, sexe INT, nom VARCHAR(30), id_race INT, age DATE, taille INT, pedigree INT, id_vendeur INT, prix DECIMAL(6,2), PRIMARY KEY(id_chien,id_race,id_vendeur),
FOREIGN KEY(id_race) REFERENCES race, FOREIGN KEY(id_vendeur) REFERENCES vendeur)""")
c.execute("""CREATE TABLE IF NOT EXISTS race(id_race INT, nom_race VARCHAR(50), taille_moyenne INT, esp_de_vie INT, long_poil VARCHAR(30), chien_chasse INT, chien_garde INT, chien_appartement INT, PRIMARY KEY(id_race))""")
c.execute("""CREATE TABLE IF NOT EXISTS vendeur(id_vendeur INT, nom_vendeur VARCHAR(70), type VARCHAR(30), id_ville INT, coord_gps VARCHAR(100), PRIMARY KEY(id_vendeur, id_ville),
FOREIGN KEY(id_ville) REFERENCES ville)""")
c.execute("""CREATE TABLE IF NOT EXISTS ville(id_ville INT, nom_ville VARCHAR(70),region VARCHAR(70), coord_gps VARCHAR(100), PRIMARY KEY(id_ville))""")

#c.execute("""INSERT INTO localisation(id_localisation, ville, coord_gps) VALUES (1,'Lyon','1234')""")
#c.execute("""INSERT INTO race(id_race, nom_race, taille, poil, caractère) VALUES (1,'Labrador','grand','soyeux','amical')""")
#c.execute("""INSERT INTO vendeur(id_vendeur, nom_vendeur, type, id_localisation) VALUES (1,'Red','Particulier','1')""")
#conn.commit()
#robes = ['noire','chocolat','beige','fauve','sable','blanche','fauve masquée','fauve charbonnée','bigarrée','grisonnée']

#Commandes création bames.db:
#CREATE TABLE IF NOT EXISTS nom(id_nom INT, nom VARCHAR(30), PRIMARY KEY(id_nom));
#CREATE TABLE IF NOT EXISTS prenom(id_prenom INT, prenom VARCHAR(30), PRIMARY KEY(id_prenom));
#CREATE TABLE IF NOT EXISTS pseudo(id_pseudo INT, pseudo VARCHAR(50), PRIMARY KEY(id_pseudo));
#CREATE TABLE IF NOT EXISTS nom_male(id_nom_male INT, nom_male VARCHAR(50), PRIMARY KEY(id_nom_male));
#CREATE TABLE IF NOT EXISTS nom_femelle(id_nom_femelle INT, nom_femelle VARCHAR(50), PRIMARY KEY(id_nom_femelle));

#Tests requêtes:
# SELECT * FROM chien WHERE age >= date("0015-01-01");
# --> Affiche tous les chiens de plus de 15 ans
# SELECT * FROM chien WHERE age <= date("0000-11-30");
# --> Affiche tous les chiots (ie les chiens de moins de 1 an)
#SELECT * FROM chien WHERE date("0005-01-01") <= age and age <= date("0010-01-01");

def random_particulier(n):
    """Génère aléatoirement n vendeurs particuliers et les ajoute à la base de données"""
    
    tabvend = []
    c.execute("""SELECT COUNT(*) FROM vendeur""")
    lenvend = (c.fetchone())[0]
    c.execute("""SELECT COUNT(*) FROM ville""")
    lenville = (c.fetchone())[0]
    w.execute("""SELECT COUNT(*) FROM nom""")
    lennom = (w.fetchone())[0]
    w.execute("""SELECT COUNT(*) FROM prenom""")
    lenprenom = (w.fetchone())[0]
    w.execute("""SELECT COUNT(*) FROM pseudo""")
    lenpseudo = (w.fetchone())[0]

    for i in range(lenvend+1,lenvend+n+1):
        vend = []

        vend.append(i)              #ID du vendeur
        hasard = randint(1,11)
        if hasard <= 10:
            w.execute("""SELECT prenom FROM prenom WHERE id_prenom = ?""", (randint(1,lenprenom),))
            nom = (w.fetchone())[0]
            if hasard <= 5:
                w.execute("""SELECT nom FROM nom WHERE id_nom = ?""", (randint(1,lennom),))
                nom = nom +' '+ (w.fetchone())[0]
        else:
            w.execute("""SELECT pseudo FROM pseudo WHERE id_pseudo = ?""", (randint(1,lenpseudo),))
            nom = (w.fetchone())[0]
        #Pour le choix du nom, il y a 10/11 chances que ce soit un prénom ou un couple prénom & nom
        #Avec 1/11 chance, le nom peut-etre un pseudo internet
        
        vend.append(nom)            #Nom du vendeur
        vend.append('Particulier')  #Type du vendeur
        id_ville = randint(1,lenville)
        vend.append(id_ville)       #ID de la ville
        c.execute("""SELECT coord_gps FROM ville WHERE id_ville = ?""", (id_ville,))
        coord_gps_ville = (c.fetchone())[0]
        #L'objectif de ce qui suit est de générer des coordonnées gps réalistes pour le particulier.
        #Pour se faire, on récupere les coordonnées GPS de la ville et on les modifie de telle sorte
        #que le particulier se trouver dans un rayon de 10~15 km autour du centre ville.
        dot1 = -1
        dot2 = -1
        virgule = -1
        for j in range(len(coord_gps_ville)):
            if coord_gps_ville[j] == '.':
                if dot1 == -1:
                    dot1 = j
                else:
                    dot2 = j
            if coord_gps_ville[j] == ',':
                virgule = j
            
        modnord = str(float(coord_gps_ville[0:dot1+2]) + randint(-15,15)*10**(-2))
        modest = str(float(coord_gps_ville[virgule+2:dot2+2]) + randint(-15,15)*10**(-2))
        for j in range(len(modnord)):
            if modnord[j] == '.':
                dot3 = j
        if len(modnord)-dot3>3:
            modnord = modnord[0:dot3+2]
        elif len(modnord)-dot3<3:
            modnord = modnord + '0'
        for j in range(len(modest)):
            if modest[j] == '.':
                dot4 = j
        if len(modest)-dot4>3:
            modest = modest[0:dot4+2]
        elif len(modest)-dot4<3:
            modest = modest + '0'
            
        coord_gps = modnord+ coord_gps_ville[dot1+3:virgule+1] +modest+ coord_gps_ville[dot2+3:]
        
        vend.append(coord_gps)   #Coordonnées GPS du vendeur
        tabvend.append(vend)
        
    c.executemany("""INSERT INTO vendeur (id_vendeur,nom_vendeur,type,id_ville,coord_gps) VALUES(?,?,?,?,?)""", tabvend)
    conn.commit()
        
    return None

def random_dog(n):
    """Génère aléatoirement n chiens et les ajoute à la base de données"""

    tabdog = []
    c.execute("""SELECT COUNT(*) FROM chien""")
    lendog = (c.fetchone())[0]
    c.execute("""SELECT COUNT(*) FROM race""")
    lenrace = (c.fetchone())[0]
    c.execute("""SELECT COUNT(*) FROM vendeur""")
    lenvendeur = (c.fetchone())[0]
    w.execute("""SELECT COUNT(*) FROM nom_male""")
    len_nom_male = (w.fetchone())[0]
    w.execute("""SELECT COUNT(*) FROM nom_femelle""")
    len_nom_femelle = (w.fetchone())[0]
    
    for i in range(lendog+1,lendog+n+1):
        dog = []
        dog.append(i)                      #ID du chien
        dog.append(randint(0,1))           #Sexe
        if dog[1] == 1:
            w.execute("""SELECT nom_male FROM nom_male WHERE id_nom_male = ?""", (randint(1,len_nom_male),))
            nom_chien = (w.fetchone())[0]
        else:
            w.execute("""SELECT nom_femelle FROM nom_femelle WHERE id_nom_femelle = ?""", (randint(1,len_nom_femelle),))
            nom_chien = (w.fetchone())[0]
        dog.append(nom_chien)
        dog.append(randint(1,lenrace))     #ID de la race
        hasard = randint(1,10)
        if hasard <= 4:
            id_vendeur = randint(1,20)
        else:
            id_vendeur = randint(21,lenvendeur)
        c.execute("""SELECT type FROM vendeur WHERE id_vendeur = ?""", (id_vendeur,))
        type_vendeur = (c.fetchone())[0]
        c.execute("""SELECT esp_de_vie FROM race WHERE id_race = ?""", (dog[3],))
        esp_de_vie = (c.fetchone())[0]
        if type_vendeur == 'Particulier':
            hasard = randint(1,10)
            if hasard <= 9:
                années = 0
            else:
                années = randint(1,esp_de_vie//2)
        else:
            années = randint(0,esp_de_vie)
        années = str(années)
        #Les chiens venant de la SPA ont plus de chance d'être vieux, ceux venant d'un particulier plus de chance d'être jeunes
        mois = randint(1,11)
        mois = str(mois)
        jour = randint(1,30)
        jour = str(jour)
        age = '0'*(4-len(années))+années+"-"+'0'*(2-len(mois))+mois+"-"+'0'*(2-len(jour))+jour
        dog.append(age)                    #Age
        c.execute("""SELECT taille_moyenne FROM race WHERE id_race = ?""", (dog[3],))
        taille = (c.fetchone())[0]+randint(-5,5)
        dog.append(taille)                 #taille
        if type_vendeur == 'Particulier':
            pedigree = randint(0,1)
        else:
            hasard = randint(1,10)
            pedigree = (hasard == 10)
        dog.append(pedigree)               #Pedigree (existant ou non)
        dog.append(id_vendeur)             #ID du vendeur
        if type_vendeur == 'Particulier':
            if pedigree == 0:
                prix = randint(80,120)*10
            else:
                prix = randint(100,150)*10
        else:
            if pedigree == 0:
                prix = randint(5,15)*10
            else:
                prix = randint(15,25)*10
        #Les chiens vendus par la SPA ne sont pas très chers, contrairement à ceux vendu par les particuliers
        #Les chiens ayant un Pedigree sont plus chers que les autres
        dog.append(prix)                   #Prix
        tabdog.append(dog)
    
    c.executemany("""INSERT INTO chien (id_chien,sexe,nom,id_race,age,taille,pedigree,id_vendeur,prix) VALUES(?,?,?,?,?,?,?,?,?)""", tabdog)
    conn.commit()
    
    return None
