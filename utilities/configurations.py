import configparser
import mysql.connector
from mysql.connector import Error


def get_config():
    cp = configparser.ConfigParser()
    cp.read("utilities/properties.ini")
    return cp


connect_details_config = {
    "host": get_config()['SQL']['host'],
    "database": get_config()['SQL']['database'],
    "user": get_config()['SQL']['user'],
    "password": get_config()['SQL']['password']
}


def get_db_connection():
    try:
        conn = mysql.connector.connect(**connect_details_config)
        if conn.is_connected():
            print("Database connection is Estalished!!!")
            return conn
    except Error as e:
        print(e)
