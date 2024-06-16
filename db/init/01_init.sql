DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'harmonycal') THEN
        CREATE DATABASE harmonycal;
    END IF;
END $$;
