#AdopteUnChien
#Version console

import sqlite3
from random import randint
from copy import deepcopy

conn = sqlite3.connect('dogs.db')
c = conn.cursor()

sexe_off = 1
race_off = 1
age_off = 1
taille_off = 1
carac_off = 1
pedigree_off = 1
prix_off = 1
ville_off = 1
region_off = 1
typevend_off = 1

sexe = 0
race = ''
age_inf = 0
age_inf_int = 0
age_sup = 0
age_sup_int = 0
taille_inf = 0
taille_sup = 0
carac = [0,0,0]
pedigree = 0
prix = 0
ville = ''
region = ''
typevend = 0

def affiche_data(legende,données_original,mise_en_forme,separator,mod):
    """Affiche de facon élégante les données issues d'une recherche dans la base de données.
    - 'Legende' est un table contenant les titres de chaque colonne
    - 'données' contient l'ensemble des données
    - 'mise_en_forme' est un tableau de fonctions de mise_en_forme à applique aux colonnes
    - 'separator' est le separateur des colonnes ('|' conseillé)
    - active le mod alternatif d'application de la mise_en_forme
      (nécessaire pour l'utilisation de la fonction pour le menu)"""
    
    données = deepcopy(données_original)
    longvert = len(données)
    longhori = len(données[0])
    
    if mod == 0:
        for j in range(longvert):
            for i in range(longhori-1):
                données[j][i] = mise_en_forme[i](données[j][i])
    else:
        for j in range(longvert):
            données[j][2] = mise_en_forme[j](données[j][2])
    
    maxtab = []
    for i in range(longhori):
        maximum = len(legende[i])
        for j in range(longvert):
            longdata = len(str(données[j][i]))
            if  longdata > maximum:
                maximum = longdata
        maxtab.append(maximum)
        
    buffer = '\n'
    for i in range(longhori-1):
        buffer = buffer + legende[i] + ' '*(maxtab[i]-len(legende[i])) + ' '+separator+' '
    before_end = len(buffer)
    buffer = buffer + legende[longhori-1]
    print(buffer)
    print('-'*(before_end+maxtab[longhori-1]))
    
    for j in range(longvert):
        buffer = ''
        for i in range(longhori-1):
            data = str(données[j][i])
            buffer = buffer + data + ' '*(maxtab[i]-len(data))+' '+separator+' '
        data = str(données[j][longhori-1])
        buffer = buffer + data
        print(buffer)
        
def critère_corres(x):
    """Fait correspondre son numéro à chaque critère en toute lettre"""
    if x.lower() == 'sexe':
        return 1
    elif x.lower() == 'race':
        return 2
    elif x.lower() == 'age' or x.lower() == 'âge':
        return 3
    elif x.lower() == 'taille':
        return 4
    elif x.lower() == 'type du chien':
        return 5
    elif x.lower() == 'pedigree':
        return 6
    elif x.lower() == 'prix':
        return 7
    elif x.lower() == 'ville':
        return 8
    elif x.lower() == 'region' or x.lower() == 'région':
        return 9
    elif x.lower() == 'type de vendeur' or x.lower() == 'type du vendeur':
        return 10
    else:
        return x
    
def identité(x):
    return x

def sexe_text(x):
    if x==0:
        return 'femelle'
    else:
        return 'mâle'

def age_simplify(x):
    year = int(x[0:4])
    month = int(x[5:7])
    if year >= 1:
        return str(year)+' ans'
    else:
        return str(month)+' mois'
    
def taille_cm(x):
    return str(x)+' cm'

def pedigree_text(x):
    if x ==1:
        return 'chien de race'
    else:
        return 'sans'

def euro(x):
    return str(x)+'€'
 
#[sexe_text,identité,identité,age_simplify,taille_cm,pedigree_text,euro,identité,identité,identité]

def sexe_text_mod(x):
    if sexe_off == 1:
        return 'Ø'
    else:
        if x==0:
            return 'femelle'
        else:
            return 'mâle'
        
def identité_race(x):
    if race_off == 1:
        return 'Ø'
    else:
        return x
        
def encadrement_age_text(x):
    a = x[0]
    b = x[1]
    if age_off == 1:
        return 'Ø'
    if a==0 and b==0:
        return 'chiot'
    elif a==0:
        return '<= '+str(b)+' ans'
    elif b>28: #Record du monde de longevité d'un chien (RIP Beagle)
        return '>= '+str(a)+' ans'
    else:
        return 'entre '+str(a)+' et '+str(b)+' ans'
    
def encadrement_taille_text(x):
    a = x[0]
    b = x[1]
    if taille_off == 1:
        return 'Ø'
    if a==0:
        return '<= '+str(b)+' cm'
    elif b>112: #Record du monde de taille d'un chien (RIP Zeus)
        return '>= '+str(a)+' cm'
    else:
        return 'entre '+str(a)+' et '+str(b)+' cm'
    
def type_du_chien_text(x):
    if carac_off == 1:
        return 'Ø'
    if x[0] == 1:
        return 'Chien de chasse'
    elif x[1] == 1:
        return 'Chien de garde'
    else:
        return "Chien d'appartement"
    
def pedigree_text_mod(x):
    if pedigree_off == 1:
        return 'Ø' 
    if pedigree == 1:
        return 'Chien de race'
    else:
        return 'sans'
    
def prix_text(x):
    if prix_off ==1:
        return 'Ø'
    return '<= '+str(x)+'€'

def identité_ville(x):
    if ville_off == 1:
        return 'Ø'
    else:
        return x
    
def identité_region(x):
    if region_off == 1:
        return 'Ø'
    else:
        return x
    
def typevend_text(x):
    if typevend_off == 1:
        return 'Ø'
    elif typevend == 0:
        return 'SPA'
    else:
        return 'Particulier'

#[sexe_text_mod,identité,encadrement_age_text,encadrement_taille_text,type_du_chien_text,pedigree_text_mod,prix_text]

critères = ['Sexe','Race','Age','Taille','Type du chien','Pedigree','Prix','Ville','Région','Type de vendeur']
menu = []
for i in range(1,11):
    menu.append([i,critères[i-1],0])

print("■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print("◀◀◀◀◀◀ AdopteUnChien ▶▶▶▶▶▶")
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■")

print("\nUn projet d'informatique réalisé par")
print("Jacques Charnay & Valentin Patillon")

print("\n■■■■■■■■■■■■■■■■■■■■■■■■■■■")

print("\nCette application vous permet de trouver et d'adopter un chien")
print("correspondant à tous les critères que vous pourriez avoir")

print("\nATTENTION !")
print("Pour un affichage optimal du programme, merci de passer votre")
print("console en pleine écran")

main_appli_on = 1
while main_appli_on:
    
    cond_main = 1
    while cond_main:
        print("\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("■■■ AdopteUnChien - Menu principal ■■■")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("\nVous pouvez:")
        print("\n1 ► Chercher un chien à adopter ◄")
        print("2 ► Proposer votre chien à l'adoption ◄")
        print("3 ► Acceder aux Records d'AdopteUnChien ◄")
        print("\n(Tapez le numéro correspondant à votre choix)")
        print("Vous pouvez quitter l'application en tapant 'exit'")
        main_choix=input()
        if not main_choix in ['1','2','3','exit','Exit']:
            print("ERREUR ! L'entrée est incorrecte !")
        else:
            cond_main = False
            
    if main_choix =='1':
        appli_on = 1
        
        sexe_off = 1
        race_off = 1
        age_off = 1
        taille_off = 1
        carac_off = 1
        pedigree_off = 1
        prix_off = 1
        ville_off = 1
        region_off = 1
        typevend_off = 1
        
        sexe = 0
        race = ''
        age_inf = 0
        age_inf_int = 0
        age_sup = 0
        age_sup_int = 0
        taille_inf = 0
        taille_sup = 0
        carac = [0,0,0]
        pedigree = 0
        prix = 0
        ville = ''
        region = ''
        typevend = 0
        
        while appli_on:
            
            valeurs = [sexe,race,(age_inf_int,age_sup_int),(taille_inf,taille_sup),carac,pedigree,prix,ville,region,typevend]
            for i in range(10):
                menu[i][2] = valeurs[i]
            
            print("\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            print("■■■ AdopteUnChien - Choix des critères ■■■")
            print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            affiche_data(['','Critères','Valeur choisie'],menu,\
                         [sexe_text_mod,identité_race,encadrement_age_text,encadrement_taille_text,type_du_chien_text,pedigree_text_mod,prix_text,identité_ville,identité_region,typevend_text],\
                         '|',1)
            print("\nVous pouvez:")
            print("- modifier un critère en tapant son numéro ou son libellé")
            print("- supprimer une valeur choisie en tapant 'del ' suivi du numéro ou du libellé")
            print("--> lancer une recherche en tapant 'go'")
            
            enter_exit = 1
            while enter_exit:
                num = -1
                enter = input()
                if enter[0:4].lower() == 'del ':
                    delete = enter[4:]
                    delete = critère_corres(delete)
                    try:
                        delete = int(delete)
                        enter_exit = 0
                        if delete == 1:
                            sexe_off = 1
                        elif delete == 2:
                            race_off = 1
                        elif delete == 3:
                            age_off = 1
                        elif delete == 4:
                            taille_off = 1
                        elif delete == 5:
                            carac_off = 1
                        elif delete == 6:
                            pedigree_off = 1
                        elif delete == 7:
                            prix_off = 1
                        elif delete == 8:
                            ville_off = 1
                        elif delete == 9:
                            region_off = 1
                        elif delete == 10:
                            typevend_off = 1
                        else:
                            print("ERREUR ! L'entier en argument ne correspond à aucun critère !")
                    except ValueError:
                        print("ERREUR ! L'argument de 'del' n'est pas un entier !")
                        
                elif enter.lower() == 'go':
                    enter_exit = 0
                    c.execute("""SELECT sexe, nom, nom_race, age, taille, pedigree, prix, nom_vendeur, type, nom_ville FROM chien, \
                              race, vendeur, ville WHERE (sexe = ? OR ?) AND chien.id_race = race.id_race AND \
                              chien.id_vendeur =  vendeur.id_vendeur AND vendeur.id_ville = ville.id_ville AND \
                              (lower(nom_race) = lower(?) OR ?)AND ((date(?) <= age AND age <= date(?)) OR ?) AND (pedigree = ? OR ?)AND(prix <= ? OR ?) AND \
                              ((? <= taille AND taille <= ?)OR ?) AND \
                              (((chien_chasse = ? AND ?) OR (chien_garde = ? AND ?) OR (chien_appartement = ? AND ?)) OR ?) AND \
                              (lower(nom_ville) = lower(?) OR ?) AND (lower(region) = lower(?) OR ?) AND (lower(type) = lower(?) OR ?)""", \
                              (sexe,sexe_off,race,race_off,age_inf,age_sup,age_off,pedigree,pedigree_off,prix,prix_off,taille_inf,\
                               taille_sup,taille_off,carac[0],carac[0],carac[1],carac[1],carac[2],carac[2],carac_off,ville,ville_off,region,region_off,typevend_text(typevend),typevend_off))
        
                    tabres = []
                    for r in c:
                        tabres.append(list(r))
                    nombre_res = len(tabres)
                    if nombre_res == 0:
                        print("\nMalheuresement, aucun chien ne correspond à vos critères :( ...")
                    else:
                        print("\nVoici les "+str(nombre_res)+" chiens disponibles à l'adoption correspondants à vos critères:")
                        affiche_data(['Sexe','Nom','Race','Age','Taille','Pedigree','prix','Nom du vendeur','Type','Ville'],\
                                     tabres,\
                                     [sexe_text,identité,identité,age_simplify,taille_cm,pedigree_text,euro,identité,identité,identité],\
                                     '|',0)
                    
                    print("\nSi vous souhaitez faire une autre recherche...")
                    print("- en conservant vos critères, cliquez sur entrée.")
                    print("- en supprimant vos critères, tapez 'delete'")
                    print("Pour quitter, tapez 'exit'")
                    end_enter = input()
                    if end_enter.lower() == 'exit':
                        appli_on = 0
                    elif end_enter.lower() == 'delete':
                        sexe_off = 1
                        race_off = 1
                        age_off = 1
                        taille_off = 1
                        carac_off = 1
                        pedigree_off = 1
                        prix_off = 1
                        ville_off = 1
                        region_off = 1
                        typevend_off = 1
                
                else:
                    enter = critère_corres(enter)
                    try:
                        num = int(enter)
                        if num>10 or num<=0:
                            print("ERREUR ! Le numéro entrée n'existe pas !")
                        else:
                            enter_exit = 0
                    except ValueError:
                        print("ERREUR ! L'entrée est incorrecte !")
            
            if num == 1:
                sexe_off = 0
                cond = True
                while cond:
                    print("\nVeuillez rentrer le sexe desiré:")
                    print("(1 pour un male, 0 pour une femelle)")
                    sexe = input()
                    if sexe != '0' and sexe !='1':
                        print("ERREUR ! Le sexe ne peut valoir que 0 ou 1 !")
                    else:
                        cond = False
                sexe = int(sexe)
                
            elif num == 2:
                race_off = 0
                cond = True
                while cond:
                    print("\nVeuillez rentrer la race desirée:")
                    print("(en toute lettre)")
                    print("(Vous pouvez taper 'liste' pour obtenir la liste des races disponibles)")
                    race = input()
                    if race.lower() == 'liste' or race.lower() == 'list':
                        c.execute("""SELECT nom_race FROM race""")
                        print("\n")
                        for r in c:
                            print(r[0])
                    else:
                        c.execute("""SELECT COUNT(*) FROM race where lower(nom_race) = lower(?)""", (race,))
                        if (c.fetchone())[0] == 0:
                            print("ERREUR ! La race précisée ne fait pas partie de notre base de données, ou est incorrecte !")
                        else:
                            cond = False
                        
            elif num == 3:
                age_off = 0
                cond = True
                while cond:
                    print("\nVeuillez rentrer la limite d'age inferieure:")
                    print("(entier positif, en années; pour un chiot, tapez 0)")
                    age_inf = input()
                    try:
                        age_inf = int(age_inf)
                        if age_inf < 0:
                            print("ERREUR ! L'age entré est strictement négatif !")
                        elif age_inf > 9999:
                            print("ERREUR ! Vous etes serieux ? Un chien de plus de 10000 ans ?!")
                        else:
                            cond = False
                    except ValueError:
                        print("ERREUR ! L'age entré n'est pas un entier !")
        
                cond = True        
                while cond:
                    print("\nVeuillez rentrer la limite d'age superieure:")
                    print("(entier positif)")
                    age_sup = input()
                    try:
                        age_sup = int(age_sup)
                        if age_sup < 0:
                            print("ERREUR ! L'age entré est strictement négatif !")
                        elif age_sup > 9999:
                            print("ERREUR ! Vous etes serieux ? Un chien de plus de 10000 ans ?!")
                        elif age_sup < age_inf:
                            print("ERREUR ! L'age entré est strictement inferieur à la limite inferieure !")
                        else:
                            cond = False
                    except ValueError:
                        print("ERREUR ! L'age entré n'est pas un entier !")
                age_inf_int = age_inf
                age_inf = str(age_inf)        
                age_inf = '0'*(4-len(age_inf))+age_inf+'-01-01'
                age_sup_int = age_sup
                age_sup = str(age_sup)
                age_sup = '0'*(4-len(age_sup))+age_sup+'-12-31'
                
            elif num  == 4:
                taille_off = 0
                cond = True
                while cond:
                    print("\nVeuillez indiquer la taille au garrot inférieure souhaitée:")
                    print("(entier positif, en centimètre)")
                    taille_inf= input()
                    try:
                        taille_inf = int(taille_inf)
                        if taille_inf < 0:
                            print("ERREUR ! La taille entrée est strictement négative !")
                        else:
                            cond = False
                    except ValueError:
                        print("ERREUR ! La taille entrée n'est pas un entier !")
                cond = True
                while cond:
                    print("\nVeuillez indiquer la taille au garrot supérieure souhaitée:")
                    print("(entier positif, en centimètre)")
                    taille_sup= input()
                    try:
                        taille_sup = int(taille_sup)
                        if taille_sup <= 0:
                            print("ERREUR ! La taille entrée est négative ou nulle !")
                        elif taille_sup < taille_inf:
                            print("ERREUR ! La taille entrée est strictement inferieur à la limite inferieure !")
                        else:
                            cond = False
                    except ValueError:
                        print("ERREUR ! La taille entrée n'est pas un entier !")
                        
            elif num == 5:
                carac_off = 0
                cond = True
                while cond:
                    print("\nSouhaitez vous un chien de chasse (tapez 1), de garde (tapez 2) ou d'apppartement (tapez 3) ?")
                    carac = input()
                    if carac != '1' and carac != '2'  and carac != '3':
                        print("ERREUR ! Le type du chien ne peut valoir que 1, 2 ou 3 !")
                    else:
                        cond = False
        
                if carac == '1':
                    carac =[1,0,0]
                elif carac == '2':
                    carac = [0,1,0]
                elif carac == '3':
                    carac = [0,0,1]
                    
            elif num == 6:
                pedigree_off = 0
                cond = True
                while cond:
                    print("\nSouhaitez vous un chien avec un Pedigree ?")
                    print("(1 si oui, 0 sinon)")
                    pedigree = input()
                    if pedigree != '0' and pedigree !='1':
                        print("ERREUR ! Le pedigree ne peut valoir que 0 ou 1 !")
                    else:
                        cond = False
                pedigree = int(pedigree)
                
            elif num == 7:
                prix_off = 0
                cond = True        
                while cond:
                    print("\nVeuillez rentrer le prix maximum")
                    print("(entier positif, en Euro)")
                    prix = input()
                    try:
                        prix = int(prix)
                        if prix < 0:
                            print("ERREUR ! Le prix entré est strictement négatif !")
                        elif prix == 0:
                            print("ERREUR ! Frais de veterinaire et nourriture oblige, aucun chien n'est malheuresement gratuit !")
                        else:
                            cond = False
                    except ValueError:
                        print("ERREUR ! Le prix entré n'est pas un entier !")
                        
            elif num == 8:
                ville_off = 0
                cond = True
                while cond:
                    print("\nVeuillez rentrer une ville:")
                    print("(Vous pouvez taper 'liste' pour obtenir la liste des villes disponibles)")
                    ville = input()
                    if ville.lower() == 'liste' or ville.lower() == 'list':
                        c.execute("""SELECT nom_ville FROM ville""")
                        print("\n")
                        for r in c:
                            print(r[0])
                    else:
                        c.execute("""SELECT COUNT(*) FROM ville where lower(nom_ville) = lower(?)""", (ville,))
                        res_ville_1 = (c.fetchone())[0]
                        c.execute("""SELECT COUNT(*) FROM ville where lower(nom_ville) = lower(?) AND (lower(region) = lower(?) OR ?)""", (ville,region,region_off))
                        res_ville_2 = (c.fetchone())[0]
                        if res_ville_1 == 0:
                            print("ERREUR ! La ville indiquée ne fait pas partie de notre base de données, ou est incorrecte !")
                        elif res_ville_2 == 0:
                            print("ERREUR ! Il y incohérence entre vos critères !")
                            print("La ville n'appartient pas à la région indiquée précedemment !")
                        else:
                            cond = False
                        
            elif num == 9:
                region_off = 0
                cond = True
                while cond:
                    print("\nVeuillez rentrer une région:")
                    print("(Nouvelles régions)")
                    print("(Vous pouvez taper 'liste' pour obtenir la liste des régions disponibles)")
                    region = input()
                    if region.lower() == 'liste' or region.lower() == 'list':
                        c.execute("""SELECT DISTINCT region FROM ville""")
                        print("\n")
                        for r in c:
                            print(r[0])
                    else:
                        c.execute("""SELECT COUNT(*) FROM ville where lower(region) = lower(?)""", (region,))
                        res_region_1 = (c.fetchone())[0]
                        c.execute("""SELECT COUNT(*) FROM ville where lower(region) = lower(?) AND (lower(nom_ville) = lower(?) OR ?)""", (region,ville,ville_off))
                        res_region_2 = (c.fetchone())[0]
                        if res_region_1 == 0:
                            print("ERREUR ! La région indiquée ne fait pas partie de notre base de données, ou est incorrecte !")
                        elif res_region_2 == 0:
                            print("ERREUR ! Il y incohérence entre vos critères !")
                            print("La ville indiquée précedemment n'appartient pas à cette région !")
                        else:
                            cond = False
                            
            elif num == 10:
                typevend_off = 0
                cond = True
                while cond:
                    print("\nVeuillez rentrer le type de vendeur souhaité:")
                    print("(0 pour une SPA, 1 pour un particulier)")
                    typevend = input()
                    if typevend != '0' and typevend !='1':
                        print("ERREUR ! Le type de vendeur ne peut valoir que 0 ou 1 !")
                    else:
                        cond = False
                typevend = int(typevend)
            
    elif main_choix == '2':
        cond = True
        while cond:
            print("\nVeuillez rentrer le sexe de votre chien:")
            print("(1 pour un male, 0 pour une femelle)")
            sexe = input()
            if sexe != '0' and sexe !='1':
                print("ERREUR ! Le sexe ne peut valoir que 0 ou 1 !")
            else:
                cond = False
        sexe = int(sexe)
        
        cond = True
        while cond:
            print("\nVeuillez rentrer le nom de votre chien:")
            nom_chien = input()
            if nom_chien == '':
                print("ERREUR ! Votre chien a forcement un nom !")
            elif len(nom_chien)>30:
                print("ERREUR ! Le nom de votre chien est trop long !")
            else:
                cond = False
        
        cond_sup = True
        while cond_sup:
            print("\nVeuillez rentrer la race de votre chien:")
            print("(en toute lettre)")
            race = input()
            c.execute("""SELECT COUNT(*) FROM race where lower(nom_race) = lower(?)""", (race,))
            if race == '':
                print("ERREUR ! Votre chien a forcement une race !")
            elif (c.fetchone())[0] == 0:
                cond = True
                while cond:
                    print("Cette race ne semble pas faire partie de notre base de données.")
                    print("Etes vous sur de ne pas avoir fait de fautes d'orthographe ?")
                    print("(1 si oui, 0 sinon)")
                    erreur_check = input()
                    if erreur_check != '0' and erreur_check !='1':
                        print("ERREUR ! Vous ne pouvez répondre que par 0 ou 1 !")
                    else:
                        cond = False
                        
                if erreur_check == '0':
                    print("Veuillez réessayer en utilisant une orthographe légèrement differente.")
                else:
                    print("Veuillez rentrer ses caractéristiques pour que nous puissions l'ajouter.")
                    
                    cond = True
                    while cond:
                        print("\nVeuillez rentrer la taille moyenne de la race:")
                        print("(entier positif, en centimètre)")
                        taille_moy= input()
                        try:
                            taille_moy = int(taille_moy)
                            if taille_moy <= 10 or taille_moy >100:
                                print("ERREUR ! La taille moyenne entrée n'est pas réaliste !")
                            else:
                                cond = False
                        except ValueError:
                            print("ERREUR ! La taille moyenne entrée n'est pas un entier !")
                            
                    cond = True
                    while cond:
                        print("\nVeuillez rentrer l'esperance de vie de la race:")
                        print("(entier positif, en années)")
                        esp_de_vie = input()
                        try:
                            esp_de_vie = int(esp_de_vie)
                            if esp_de_vie <= 0 or esp_de_vie > 28:
                                print("ERREUR ! L'esperance de vie entrée n'est pas réaliste !")
                            else:
                                cond = False
                        except ValueError:
                            print("ERREUR ! L'esperance de vie entrée n'est pas un entier !")
            
                    cond = True
                    while cond:
                        print("\nS'agit il de chiens de chasse ?")
                        print("(1 si oui, 0 sinon)")
                        chien_chasse = input()
                        if chien_chasse != '0' and chien_chasse !='1':
                            print("ERREUR ! Vous ne pouvez répondre que par 0 ou 1 !")
                        else:
                            cond = False
                    chien_chasse = int(chien_chasse)
            
                    cond = True
                    while cond:
                        print("\nS'agit il de chiens de garde ?")
                        print("(1 si oui, 0 sinon)")
                        chien_garde = input()
                        if chien_garde != '0' and chien_garde !='1':
                            print("ERREUR ! Vous ne pouvez répondre que par 0 ou 1 !")
                        else:
                            cond = False
                    chien_garde = int(chien_garde)
            
                    cond = True
                    while cond:
                        print("\nS'agit il de chiens d'appartemment ?")
                        print("(1 si oui, 0 sinon)")
                        chien_appartement = input()
                        if chien_appartement != '0' and chien_appartement !='1':
                            print("ERREUR ! Vous ne pouvez répondre que par 0 ou 1 !")
                        else:
                            cond = False
                    chien_chasse = int(chien_chasse)
                    
                    c.execute("""SELECT count(*) FROM race""")
                    id_race = (c.fetchone())[0] + 1
                    c.execute("""INSERT INTO race(id_race,nom_race,taille_moyenne,esp_de_vie,\
                long_poil,chien_chasse,chien_garde,chien_appartement) VALUES(?,?,?,?,?,?,?,?)""",\
                              (id_race,race,taille_moy,esp_de_vie,'court',chien_chasse,chien_garde,chien_appartement))
                    conn.commit()
            
                    print("\nMerci pour ces informations ! La race vient d'être ajoutée à la base !")
                    cond_sup = False
            else:
                cond_sup = False
                c.execute("""SELECT id_race FROM race where lower(nom_race) = lower(?)""", (race,))
                id_race = (c.fetchone())[0]
        
        cond_sup = True        
        while cond_sup:
            print("\nVeuillez rentrer l'age de votre chien:")
            print("(entier positif, en années; tapez 0 s'il s'agit d'un chiot)")
            age = input()
            try:
                age = int(age)
                if age < 0:
                    print("ERREUR ! L'age entré est strictement négatif !")
                elif age > 9999:
                    print("ERREUR ! Vous etes serieux ? Un chien de plus de 10000 ans ?!")
                elif age == 0:
                    print("C'est un chiot ?")
                    cond = True
                    while cond:
                        print("Quel est son âge en mois ?")
                        print("(Entier positif)")
                        mois = input()
                        try:
                            mois = int(mois)
                            if mois <=0 or mois > 11:
                                print("ERREUR ! Le nombre de mois entré est incorrecte !")
                            else:
                                cond = False
                        except ValueError:
                            print("ERREUR ! Le mois entré n'est pas un entier !")
                    cond_sup= False
                else:
                    mois = randint(1,11)
                    cond_sup = False
            except ValueError:
                print("ERREUR ! L'age entré n'est pas un entier !")
        
        age = str(age)
        mois = str(mois)
        jour = str(randint(1,30))
        
        age = '0'*(4-len(age))+age+"-"+'0'*(2-len(mois))+mois+"-"+'0'*(2-len(jour))+jour
        
        cond = True
        while cond:
            print("\nVeuillez indiquer la taille au garrot de votre chien:")
            print("(entier positif, en centimètre)")
            taille= input()
            try:
                taille = int(taille)
                if taille <= 0 or taille > 112:
                    print("ERREUR ! La taille entrée n'est pas réaliste !")
                else:
                    cond = False
            except ValueError:
                print("ERREUR ! La taille entrée n'est pas un entier !")
        
        cond = True
        while cond:
            print("\nVotre chien a t-il un Pedigree ?")
            print("(1 si oui, 0 sinon)")
            pedigree = input()
            if pedigree != '0' and pedigree !='1':
                print("ERREUR ! Le pedigree ne peut valoir que 0 ou 1 !")
            else:
                cond = False
            pedigree = int(pedigree)
            
        cond = True        
        while cond:
            print("\nA quel prix souhaitez vous vendre votre chien ?")
            print("(entier positif, en Euro)")
            prix = input()
            try:
                prix = int(prix)
                if prix < 0:
                    print("ERREUR ! Le prix entré est strictement négatif !")
                elif prix == 0:
                    print("ERREUR ! Votre chien ne peut être gratuit !")
                elif prix > 9999:
                    print("ERREUR ! Votre prix est abusif !")
                else:
                    cond = False
            except ValueError:
                print("ERREUR ! Le prix entré n'est pas un entier !")
        
        print("\nNous souhaitons maintenant en savoir plus sur vous.")
        
        cond = True
        while cond:
            print("\nQuel est votre nom ?")
            nom_vendeur = input()
            if nom_vendeur == '':
                print("ERREUR ! Vous avez forcement un nom !")
            elif len(nom_vendeur)>70:
                print("ERREUR ! Votre nom est trop long !")
            else:
                cond = False
        
        cond = True
        while cond:
            print("\nA proximité de quelle grande ville habitez vous ?")
            print("(Vous pouvez taper 'liste' pour obtenir la liste des villes disponibles)")
            ville = input()
            if ville.lower() == 'liste' or ville.lower() == 'list':
                c.execute("""SELECT nom_ville FROM ville""")
                print("\n")
                for r in c:
                    print(r[0])
            else:
                c.execute("""SELECT COUNT(*) FROM ville where lower(nom_ville) = lower(?)""", (ville,))
                res_ville = (c.fetchone())[0]
                if res_ville == 0:
                    print("ERREUR ! La ville indiquée ne fait pas partie de notre base de données, ou est incorrecte !")
                else:
                    c.execute("""SELECT id_ville FROM ville where lower(nom_ville) = lower(?)""", (ville,))
                    id_ville = (c.fetchone())[0]
                    cond = False
        
        c.execute("""SELECT count(*) FROM vendeur""")
        id_vendeur = (c.fetchone())[0] + 1
        c.execute("""INSERT INTO vendeur(id_vendeur,nom_vendeur,type,id_ville,coord_gps) VALUES(?,?,?,?,?)""",\
                          (id_vendeur,nom_vendeur,'Particulier',id_ville,'49.509777, 0.177923'))
        conn.commit()
        
        c.execute("""SELECT count(*) FROM chien""")
        id_chien = (c.fetchone())[0] + 1
        c.execute("""INSERT INTO chien(id_chien,sexe,nom,id_race,age,taille,pedigree,id_vendeur,prix) VALUES(?,?,?,?,?,?,?,?,?)""",\
                          (id_chien,sexe,nom_chien,id_race,age,taille,pedigree,id_vendeur,prix))
        conn.commit()
        
        print("\nFelicitation ! Votre chien est dès à présent disponible à l'adoption sur AdopteUnChien !")
    
    elif main_choix =='3':
        print("WORK IN PROGRESS !")
    
    else:   
        main_appli_on = 0
        
print("\nA bientot :) !")
conn.close()