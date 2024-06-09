import sqlite3


def execute(command : str, arguments : tuple = tuple()) -> tuple:
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        cursor.execute(command, arguments)
        
        data = cursor.fetchall()
        
        conn.commit()
    return data