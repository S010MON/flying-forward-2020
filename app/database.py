from mysql.connector import (connection)
import mysql.connector

from app.models import DataDump, Vector

# Database config
config = {'user': 'root',
          'password': 'password',
          'host': 'db',
          'port': '3306',
          'database': 'drone'
          }

# Setup SQL connector
cnx = mysql.connector.connect(**config)


def add_new_admin():


def add_new_user(d: DataDump):
    """
    Add a new user and return the integer user_id from the new user
    """
    # Fetch new user_id
    cursor = cnx.cursor()
    query = f"""INSERT INTO Users (age, flying_minutes, gender, licences,  time_overflying_people_ms,
            number_overflown_people, min_dist_to_nearest_structure, min_dist_to_nearest_person, avg_dist_to_intruder,
            max_dist_to_start, gated_vul_points, map) VALUES
            ({d.user_data.age},
            {d.user_data.flying_exp_mins},
            \"{d.user_data.gender}\",
            \"{d.user_data.license}\",
            {d.summary.time_overflying_people_ms},
            {d.summary.number_overflown_people},
            {d.summary.min_dist_to_nearest_structure},
            {d.summary.min_dist_to_nearest_person},
            {d.summary.avg_dist_to_intruder},
            {d.summary.max_dist_to_start},
            {d.summary.gated_vul_points},
            \"{d.map}\");"""
    cursor.execute(query)
    cnx.commit()

    cursor.execute("SELECT LAST_INSERT_ID();")
    result = cursor.fetchone()
    cursor.close()
    return result[0]


def get_one_user(user_id: int):
    query = f"SELECT * FROM Users WHERE user_id = {user_id}"

    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result


def get_multiple_users():
    query = "SELECT user_id FROM Users;"
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def add_vector(user_id: int, vector: Vector):
    query = f"INSERT INTO Vectors (user_id, time_ms, px, py, pz, vx, vy, vz) VALUES (" \
            f"{user_id}," \
            f"{vector.time_ms}," \
            f"{vector.px}," \
            f"{vector.py}," \
            f"{vector.pz}," \
            f"{vector.vx}," \
            f"{vector.vy}," \
            f"{vector.vz});"
    try:
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        return True
    except:
        return False


def get_multiple_vectors(user_id: int):
    query = f"SELECT time_ms, px, py, px, vx, vy, vz FROM Vectors WHERE user_id = {user_id}"
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    i = 0
    response = {}
    for line in result:
        p = {'x': line[1], 'y': line[2], 'z': line[3]}
        v = {'x': line[4], 'y': line[5], 'z': line[6]}
        response[i] = {'time_ms': line[0], 'p': p, 'v': v}
        i += 1

    return response
