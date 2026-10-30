CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
INSERT INTO items (name) VALUES ('Item 1'), ('Item 2'), ('Item 3');
