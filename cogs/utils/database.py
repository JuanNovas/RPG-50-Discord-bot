import sqlite3


def execute(command, *args):
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        cursor.execute(command, (*args,))
        
        data = cursor.fetchall()
        
        conn.commit()
    return data