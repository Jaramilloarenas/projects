import mysql.connector

DB_HOST = "database-1.cyvzlpyrzxvu.us-east-2.rds.amazonaws.com"
DB_USER = "m4dm1n1str4t0r"
DB_PASS = "administrator"
Db_NAME = "general"

def execute_insert(query = "") -> None:
    print(query)
    connection = mysql.connector.connect()
    try:
        connection = mysql.connector.connect( host = DB_HOST, user = DB_USER, passwd = DB_PASS, db = Db_NAME)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
    except Exception as ex:
        connection.rollback()
        raise ex

def execute_select(query = "") -> list:
    print(query)
    connection = mysql.connector.connect()
    try:
        connection = mysql.connector.connect( host = DB_HOST, user = DB_USER, passwd = DB_PASS, db = Db_NAME)
        cursor = connection.cursor()
        cursor.execute(query)
        regs = []
        for message, timestamp, qos, topic in cursor.fetchall():
            regs.append([message, "false", timestamp, 0, qos, topic])
        connection.close()
        return regs
    except Exception as ex:
        connection.rollback()
        raise ex


def write_file(topic, msg, qos, stamptime) -> None:
    try:
        file = open("topic_messages.txt", mode = "a")
        line = f"{topic} {msg} {qos} {stamptime} \n"
        file.write(line)
        file.close()
    except Exception as ex:
        print("Se ha generado ub error", ex)
    

