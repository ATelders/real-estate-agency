from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='arthur', database='agence_location_python', password='*****')
cursor = cnx.cursor()


add_commune = ("INSERT INTO communes "
               "(commune, nombre_habitants, distance_agence) "
               "VALUES (%s, %s, %s)")
add_type_logement = ("INSERT INTO types_logement "
              "(type, charges) "
              "VALUES (%s, %s)")
add_locataire = ("INSERT INTO locataires "
              "(nom, prenom, date_de_naissance) "
              "VALUES (%s, %s, %s)")
add_telephone = ("INSERT INTO telephones "
              "(telephone, locataire_id) "
              "VALUES (%s, %s)")
add_logement = ("INSERT INTO logements "
              "(adresse, superficie, loyer, commune_id, type_logement_id) "
              "VALUES (%s, %s, %s, %s, %s)")
add_contrat_de_location = ("INSERT INTO types_logement "
              "(locataire_id, logement_id, date_entree, date_sortie) "
              "VALUES (%s, %s, %s, %s)")

data_commune = [
    ['Lille', 232741, 0],
    ['Paris', 10000000, 200],
    ['Dunkerque', 10000000, 200],
    ['Pékin', 10000000, 200],
    ['Armentières', 10000000, 200],
]


data_type_logement = [
    ["Studio", 30],
    ["T2", 40],
    ["T3", 50],
    ["T4", 60],
    ["Maison", 70]
]

data_locataire = [
    ["Hallyday", "Johnny", date(1943,1,8)],
    ["Presley", "Elvis", date(1935,1,8)],
    ["Zidane", "Zinedine", date(1970,1,8)],
    ["Sanson", "Véronique", date(1958,1,8)],
    ["chanteuse", "Rihanna", date(1988,1,8)]
]

data_telephone = [
    ["0123456789", 1],
    ["0223456789", 2],
    ["0323456789", 3],
    ["0423456789", 4],
    ["0523456789", 5],
]

data_logement = [
    ["1, rue de l'avenir", 30, 400, 2, "Studio"],
    ["2, rue de l'avenir", 40, 500, 3, "T4"],
    ["3, rue de l'avenir", 50, 600, 4, "T3"],
    ["4, rue de l'avenir", 60, 700, 5, "T2"],
    ["5, rue de l'avenir", 70, 800, 1, "Maison"]
]

data_contrat_de_location = [
    [1, 2, datetime(2002, 12, 4), datetime(2020,2,2)],
    [2, 3, datetime(2012, 12, 4, 20, 30, 40)],
    [3, 4, datetime(2018, 12, 4, 20, 30, 40), datetime(2020, 12, 4, 20, 30, 40)],
    [4, 5, datetime(2020, 12, 4, 20, 30, 40)],
    [5, 1, datetime(2019, 12, 4, 20, 30, 40)],
]


# Insert commune

for i in range(len(data_commune)) :
    try :
        cursor.execute(add_commune, data_commune[i])
        print("Commune créée : {}".format(data_commune[i][0]))
    except :
        print("La commune {} existe déjà".format(data_type_logement[i][0]))

# Insert type de logement

for i in range(len(data_type_logement)) :
    try :
        cursor.execute(add_type_logement, data_type_logement[i])
        print("Type créé : {}".format(data_type_logement[i][0]))
    except :
        print("Le type {} existe déjà".format(data_type_logement[i][0]))

# Insert locataire

for i in range(len(data_locataire)) :
    try :
        cursor.execute(add_locataire, data_locataire[i])
        print("Locataire créé : {}".format(data_locataire[i][0]))
    except :
        print("Le locataire {} existe déjà".format(data_locataire[i][0]))

# Insert telephone

for i in range(len(data_telephone)) :
    try :
        cursor.execute(add_telephone, data_telephone[i])
        print("Téléphone créé : {}".format(data_telephone[i][0]))
    except :
        print("Le téléphone {} existe déjà".format(data_telephone[i][0]))

# Insert logement

for i in range(len(data_logement)) :
    try :
        cursor.execute(add_logement, data_logement[i])
        print("Logement créé : {}".format(data_logement[i][0]))
    except :
        print("Le logement {} existe déjà".format(data_logement[i][0]))

# Insert contrat de location

for i in range(len(data_contrat_de_location)) :
    try :
        cursor.execute(add_contrat_de_location, data_contrat_de_location[i])
        print("Contrat créé : {}".format(data_contrat_de_location[i][0]))
    except :
        print("Le contrat {} existe déjà".format(data_contrat_de_location[i][0]))



# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()