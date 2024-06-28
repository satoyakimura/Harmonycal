-- create role
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'harmonycal') THEN
        CREATE ROLE harmonycal WITH LOGIN PASSWORD 'password';
    END IF;
END $$;

-- create database
DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'harmonycal') THEN
        CREATE DATABASE harmonycal;
    END IF;
END $$;
