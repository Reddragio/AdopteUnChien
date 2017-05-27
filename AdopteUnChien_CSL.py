#AdopteUnChien
#Version console

import sqlite3

conn = sqlite3.connect('dogs.db')
c = conn.cursor()

sexe_off = 1
race_off = 1
age_off = 1
taille_off = 1
carac_off = 1
pedigree_off = 1
prix_off = 1

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

def affiche_data(legende,données,mise_en_forme,separator,mod):
    """Affiche de facon élégante les données issues d'une recherche dans la base de données.
    - 'Legende' est un table contenant les titres de chaque colonne
    - 'données' contient l'ensemble des données
    - 'mise_en_forme' est un tableau de fonctions de mise_en_forme à applique aux colonnes
    - 'separator' est le separateur des colonnes ('|' conseillé)
    - active le mod alternatif d'application de la mise_en_forme
      (nécessaire pour l'utilisation de la fonction pour le menu)"""
    
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
    else:
        return 'entre '+str(a)+' et '+str(b)+' ans'
    
def encadrement_taille_text(x):
    a = x[0]
    b = x[1]
    if taille_off == 1:
        return 'Ø'
    if a==0:
        return '<= '+str(b)+' cm'
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

#[sexe_text_mod,identité,encadrement_age_text,encadrement_taille_text,type_du_chien_text,pedigree_text_mod,prix_text]

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

appli_on = 1

critères = ['Sexe','Race','Age','Taille','Type du chien','pedigree','prix']
menu = []
for i in range(1,8):
    menu.append([i,critères[i-1],0])

while appli_on:
    
    valeurs = [sexe,race,(age_inf_int,age_sup_int),(taille_inf,taille_sup),carac,pedigree,prix]
    for i in range(7):
        menu[i][2] = valeurs[i]
    
    print("\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■■■ AdopteUnChien - Menu Principal ■■■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    affiche_data(['','Critères','Valeur choisie'],menu,\
                 [sexe_text_mod,identité_race,encadrement_age_text,encadrement_taille_text,type_du_chien_text,pedigree_text_mod,prix_text],\
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
            except ValueError:
                print("ERREUR ! l'argument de 'del' n'est pas un entier !")
                
        elif enter.lower() == 'go':
            enter_exit = 0
            c.execute("""SELECT sexe, nom, nom_race, age, taille, pedigree, prix, nom_vendeur, type, nom_ville FROM chien, \
                      race, vendeur, ville WHERE (sexe = ? OR ?) AND chien.id_race = race.id_race AND \
                      chien.id_vendeur =  vendeur.id_vendeur AND vendeur.id_ville = ville.id_ville AND \
                      (lower(nom_race) = lower(?) OR ?)AND ((date(?) <= age AND age <= date(?)) OR ?) AND (pedigree = ? or ?)AND(prix <= ? OR ?) AND \
                      ((? <= taille AND taille <= ?)OR ?) AND \
                      (((chien_chasse = ? AND ?) OR (chien_garde = ? AND ?) OR (chien_appartement = ? AND ?)) or ?)""", \
                      (sexe,sexe_off,race,race_off,age_inf,age_sup,age_off,pedigree,pedigree_off,prix,prix_off,taille_inf,\
                       taille_sup,taille_off,carac[0],carac[0],carac[1],carac[1],carac[2],carac[2],carac_off))

            tabres = []
            for r in c:
                tabres.append(list(r))

            if len(tabres) == 0:
                print("\nMalheuresement, aucun chien ne correspond à vos critères :( ...")
            else:
                print("\nVoici les chiens disponibles à l'adoption correspondants à vos critères:")
                affiche_data(['Sexe','Nom','Race','Age','Taille','Pedigree','prix','Nom du vendeur','Type','Ville'],\
                             tabres,\
                             [sexe_text,identité,identité,age_simplify,taille_cm,pedigree_text,euro,identité,identité,identité],\
                             '|',0)
            sexe_off = 1
            race_off = 1
            age_off = 1
            taille_off = 1
            carac_off = 1
            pedigree_off = 1
            prix_off = 1
            print("\nSi vous souhaitez faire une autre recherche, cliquez sur entrée.")
            print("Pour quitter, tapez 'exit'")
            end_enter = input()
            if end_enter.lower() == 'exit':
                appli_on = 0
        
        else:
            enter = critère_corres(enter)
            try:
                num = int(enter)
                if num>7 or num<=0:
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
            race = input()
            c.execute("""SELECT COUNT(*) FROM race where lower(nom_race) = lower(?)""", (race,))
            if (c.fetchone())[0] == 0:
                print("ERREUR ! La race précisée ne fait pas partie de notre base de données, ou est incorrecte !")
            else:
                cond = False
                
    elif num == 3:
        age_off = 0
        c.execute("""SELECT max(esp_de_vie) FROM race""")
        max_age = (c.fetchone())[0]

        cond = True
        while cond:
            print("\nVeuillez rentrer la limite d'age inferieure:")
            print("(entier positif, en années; pour un chiot, tapez 0)")
            age_inf = input()
            try:
                age_inf = int(age_inf)
                if age_inf < 0:
                    print("ERREUR ! L'age entré est strictement négatif !")
                elif age_inf > max_age:
                    print("ERREUR ! L'age entré est trop grand pour être réaliste pour un chien !")
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
                elif age_sup > max_age:
                    print("ERREUR ! L'age entré est trop grand pour être réaliste pour un chien !")
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
                elif taille_inf > 112:
                    print("ERREUR ! Meme le plus grand chien du monde ne fait pas cette taille !")
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
                elif taille_sup > 112:
                    print("ERREUR ! Meme le plus grand chien du monde ne fait pas cette taille !")
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
                print("ERREUR ! Le type de chien ne peut valoir que 1, 2 ou 3 !")
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
        
print("\nA bientot :) !")
