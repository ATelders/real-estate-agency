# real-estate-agency

Before running create_database_tables.py

execute : sudo mysql


Replace 'arthur' by your username and 'mot_de_passe' by a password in the two commands below.
Also replace username and password in create_data_base_tables.py (line 95) and CRUD.py (line5)

CREATE USER 'arthur'@'localhost' IDENTIFIED BY 'mot_de_passe';
GRANT ALL PRIVILEGES ON agence_location_python.* TO 'arthur'@'localhost';

disconnect sudo




running create_database_tables.py will connect to mysql and create 1 database and 6 tables for the real estate agency.

CRUD.py will create rows (OK, TO FIX) in each database and show an example of reading, updating and deleting rows. (TODO)

