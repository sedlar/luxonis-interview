#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "db" <<-EOSQL
    CREATE TABLE IF NOT EXISTS flats (
        id serial PRIMARY KEY,
        title VARCHAR NOT NULL,
        image_url VARCHAR NOT NULL
    );
EOSQL
