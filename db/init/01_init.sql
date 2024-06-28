-- create role
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'minnatoseizi') THEN
        CREATE ROLE minnatoseizi WITH LOGIN PASSWORD 'password';
    END IF;
END $$;

-- create database
DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'minnatoseizi') THEN
        CREATE DATABASE minnatoseizi;
    END IF;
END $$;
