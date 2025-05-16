# PensionPit




DESCARGAR POSGRES
sudo apt update
sudo apt install postgresql postgresql-contrib

Instalar el conector de PostgreSQL para Django

pip install psycopg2-binary

Acceder a posgres:
sudo -u postgres psql


CREATE DATABASE buyandblood_db;
CREATE USER admin WITH PASSWORD 'admin';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE buyandblood_db TO admin;