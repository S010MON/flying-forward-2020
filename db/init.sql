CREATE DATABASE IF NOT EXISTS drone;
USE drone;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT,
    age INT,
    flying_minutes INT,
    gender VARCHAR(1),
    licences VARCHAR(255),
    PRIMARY KEY (user_id)
    );

CREATE TABLE Coordinates (
    session_id INT NOT NULL,
    time_ms INT NOT NULL,
    x INT NOT NULL,
    y INT NOT NULL,
    z INT NOT NULL,
    PRIMARY KEY (session_id, time_ms)
    );

-- Sessions map Users to Coordinate sets
CREATE TABLE Sessions (
    session_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    map VARCHAR(255) NOT NULL,
    PRIMARY KEY (session_id),
    CONSTRAINT FK_user_id_to FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );

INSERT INTO Users (age, flying_minutes, gender, licences) VALUES (29, 10, "m", "a1 & a3"),
                                                                 (18, 0, "f", null);

INSERT INTO Sessions (user_id, map) VALUES (1, "intruder");

INSERT INTO Coordinates (session_id, time_ms, x, y, z) VALUES (1, 0, 0, 0, 0),
                                                              (1, 1, 0, 10, 1),
                                                              (1, 2, 0, 20, 2),
                                                              (1, 3, 0, 30, 4),
                                                              (1, 4, 0, 40, 8),
                                                              (1, 5, 0, 50, 16);