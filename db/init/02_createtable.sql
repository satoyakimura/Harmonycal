-- テーブル:userdata
DROP TABLE IF EXISTS userdata;
CREATE TABLE userdata(
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- table: member
DROP TABLE IF EXISTS member;
CREATE TABLE member(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);
-- table: lognote
DROP TABLE IF EXISTS lognote;
CREATE TABLE lognote(
    id SERIAL PRIMARY KEY,
    member_id INT,
    content TEXT,
    FOREIGN KEY (member_id) REFERENCES member (id)
);

-- table: agenda
DROP TABLE IF EXISTS agenda;
CREATE TABLE agenda(
    id SERIAL PRIMARY KEY,
    topic VARCHAR(255) UNIQUE,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP
);

-- table: view
DROP TABLE IF EXISTS opinion;
CREATE TABLE opinion(
    id SERIAL PRIMARY KEY,
    member_id INT NOT NULL,
    is_approve BOOLEAN,
    topic_id INT NOT NULL,
    FOREIGN KEY (topic_id) REFERENCES agenda (id),
    FOREIGN KEY (member_id) REFERENCES member (id)
);
