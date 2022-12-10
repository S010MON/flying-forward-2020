CREATE DATABASE IF NOT EXISTS drone;
USE drone;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT,
    age INT,
    flying_minutes INT,
    gender VARCHAR(1),
    licences VARCHAR(255),
    map VARCHAR(255),
    time_overflying_people_ms INT,
    number_overflown_people INT,
    min_dist_to_nearest_structure DOUBLE,
    min_dist_to_nearest_person DOUBLE,
    avg_dist_to_intruder DOUBLE,
    max_dist_to_start DOUBLE,
    gated_vul_points INT,
    PRIMARY KEY (user_id)
    );

CREATE TABLE Vectors (
    user_id INT NOT NULL,
    time_ms INT NOT NULL,
    px DOUBLE NOT NULL,
    py DOUBLE NOT NULL,
    pz DOUBLE NOT NULL,
    vx DOUBLE NOT NULL,
    vy DOUBLE NOT NULL,
    vz DOUBLE NOT NULL,
    PRIMARY KEY (user_id, time_ms)
    );

INSERT INTO Users (age, flying_minutes, gender, licences, map) VALUES
        (29, 10, "m", "a1 & a3", "intruder"),
        (18, 0, "f", null, null);

INSERT INTO Vectors (user_id, time_ms, px, py, pz, vx, vy, vz) VALUES
        (1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        (1, 1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7),
        (1, 2, 0.4, 0.6, 0.8, 0.10, 0.12, 0.14),
        (1, 3, 0.6, 0.9, 0.16, 0.15, 0.18, 0.21),
        (1, 4, 0.8, 0.12, 0.20, 0.20, 0.24, 0.28);


