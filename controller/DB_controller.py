import sqlite3
import os

class DB:

    """Class for database connection"""

    # dir = os.path.dirname(__file__)
    # filename = os.path.join(dir, "todo.db")

    def __init__(self):
        self.dir = os.path.dirname(__file__)
        self.filename = os.path.join(dir, "todo.db")

    def get_connection(cls):
        base = sqlite3.connect(cls.filename)
        return base

    def get_all(cls):
        database = DB.get_connection()
        task_list = []
        db_list = database.execute("SELECT * FROM products")
        for task in db_list:
            new_task = Task(task[1], task[2], task[3])
            new_task.id = task[0]
            task_list.append(new_task)
        database.close()

        return task_list
    @classmethod
    def db_reset(cls):
        conn = sqlite3.connect(cls.filename)
        curr = conn.cursor()
        curr.execute("DROP TABLE IF EXISTS todo;")
        curr.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY AUTOINCREMENT, task_name TEXT, done BOOLEAN);")
        curr.execute(
            "INSERT INTO todo (task_name, done) VALUES ('brush teeth', 1), ('speak with the duck', 0), ('code', 0);")
        conn.commit()
        conn.close()



