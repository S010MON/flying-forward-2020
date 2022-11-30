CREATE DATABASE droneData;
USE droneData;

CREATE TABLE Users (
    user_id INT NOT NULL,
    age INT,
    flying_minutes INT,
    gender VARCHAR(1),
    licences VARCHAR(255),
    PRIMARY KEY (user_id)
    );

CREATE TABLE Coordinates (
    session_id INT NOT NULL,
    map VARCHAR(255) NOT NULL,
    time_ms INT NOT NULL,
    x INT NOT NULL,
    y INT NOT NULL,
    z INT NOT NULL,
    CONSTRAINT unique_coord PRIMARY KEY (session_id, time_ms)
    );

-- Sessions map Users to Coordinate sets
CREATE TABLE Sessions (
    session_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    PRIMARY KEY (session_id),
    CONSTRAINT FK_coordinate_id_to FOREIGN KEY (session_id) REFERENCES Coordinates(session_id),
    CONSTRAINT FK_user_id_to FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );