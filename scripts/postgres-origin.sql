CREATE USER username WITH PASSWORD 'password';
ALTER ROLE username SET client_encoding TO 'utf8';
ALTER ROLE username SET default_transaction_isolation TO 'read committed';
ALTER ROLE username SET timezone TO 'UTC';
ALTER USER username CREATEDB;


CREATE DATABASE database;
GRANT ALL PRIVILEGES ON DATABASE database TO username;