import sqlite3


def execute(command : str, arguments : tuple = tuple()) -> tuple:
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        cursor.execute(command, arguments)
        
        data = cursor.fetchall()
        
        conn.commit()
    return data


def execute_dict(command: str, arguments: tuple = tuple()) -> list[dict]:
    with sqlite3.connect("test.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(command, arguments)
        
        data = [dict(row) for row in cursor.fetchall()]
        
        conn.commit()
    return data