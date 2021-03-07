# Inspiré de l'exemple de la documentation mySQL
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

#from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode


pw = str(input("Entrez le mot de passe: "))

# Initialisation du nom de la base de données

DB_NAME = 'agence_location_python'


# Initialisation du dictionnaire de tables

TABLES = {}

TABLES['types_logement'] = (
    '''
    CREATE TABLE types_logement (
       type varchar(20) NOT NULL,
       charges decimal(6,2) DEFAULT NULL,
       PRIMARY KEY (type)
    )  ENGINE=InnoDB
    '''
)

TABLES['communes'] = (
    '''
    CREATE TABLE communes (
        id smallint unsigned NOT NULL AUTO_INCREMENT,
        commune VARCHAR(60) NOT NULL,
        nombre_habitants int unsigned DEFAULT NULL,
        distance_agence decimal(6,2) DEFAULT NULL,
        PRIMARY KEY (id)
    )   ENGINE=InnoDB
    '''
)

TABLES['logements'] = (
    '''
    CREATE TABLE logements (
        id mediumint unsigned NOT NULL AUTO_INCREMENT,
        adresse varchar(200) NOT NULL,
        superficie decimal(6,2),
        loyer decimal(7,2),
        commune_id smallint unsigned DEFAULT NULL,
        type_logement_id varchar(20) DEFAULT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (commune_id)
           REFERENCES communes (id)
           ON DELETE SET NULL
           ON UPDATE CASCADE,
        FOREIGN KEY (type_logement_id)
           REFERENCES types_logement(type)
           ON DELETE SET NULL
           ON UPDATE CASCADE
    )   ENGINE=InnoDB
    '''
)

TABLES['locataires'] = (
    '''
    CREATE TABLE locataires (
       id mediumint unsigned NOT NULL AUTO_INCREMENT,
       nom varchar(100) DEFAULT NULL,
       prenom varchar(60) DEFAULT NULL,
       date_de_naissance date DEFAULT NULL,
       PRIMARY KEY (id)
    )  ENGINE=InnoDB
    '''
)

TABLES['telephones'] = (
    '''
    CREATE TABLE telephones (
        telephone varchar(16) NOT NULL,
        locataire_id mediumint unsigned NOT NULL,
        PRIMARY KEY (telephone),
        FOREIGN KEY (locataire_id)
            REFERENCES locataires(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )   ENGINE=InnoDB
    '''
)

TABLES['contrats_de_location'] = (
    '''
    CREATE TABLE contrats_de_location (
        id mediumint unsigned NOT NULL AUTO_INCREMENT,
        locataire_id mediumint unsigned DEFAULT NULL,
        logement_id mediumint unsigned DEFAULT NULL,
        date_entree datetime DEFAULT NULL,
        date_sortie datetime DEFAULT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (locataire_id)
            REFERENCES locataires (id) ON DELETE SET NULL,
        FOREIGN KEY (logement_id)
            REFERENCES logements (id) ON DELETE SET NULL
    )   ENGINE=InnoDB
    '''
)

# Connexion à mySQL

cnx = mysql.connector.connect(user='arthur', password=pw)
cursor = cnx.cursor()

# Fonction de création de la base de données

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


# Créer la base de données si elle n'existe pas déjà

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


# Créer les tables du dictionnaire TABLES

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
