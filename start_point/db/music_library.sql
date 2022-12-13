-- write your tables in here. 

DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist_id INT NOT NULL REFERENCES artists(id)
);

INSERT INTO artists (name)
VALUES ('Sonata Arctica');

INSERT INTO artists (name)
VALUES ('Muse');

INSERT INTO albums (title, artist_id)
VALUES ('Absolution', 2);