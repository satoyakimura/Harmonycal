-- DROP TABLE IF EXISTS userdata;
-- DROP TABLE IF EXISTS schedule;


-- テーブル:userdata
DROP TABLE IF EXISTS userdata;
CREATE TABLE userdata(
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- table: schedule
DROP TABLE IF EXISTS schedule;
CREATE TABLE schedule(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description VARCHAR(255),
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES userdata (id)
);

