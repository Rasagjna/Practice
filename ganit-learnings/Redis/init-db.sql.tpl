-- init-db.sql.tpl


-- AI APP setup
DO
$$
BEGIN
    IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE rolname = 'treux_admin'
    ) THEN
        CREATE USER treux_admin WITH PASSWORD 'admin';
   END IF;
END
$$;

CREATE DATABASE treux_ai_db OWNER treux_admin;
GRANT ALL PRIVILEGES ON DATABASE treux_ai_db TO treux_admin;

\connect treux_ai_db;
CREATE SCHEMA IF NOT EXISTS dev AUTHORIZATION treux_admin;
