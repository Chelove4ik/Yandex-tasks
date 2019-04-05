class AdminsModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS admins 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_name VARCHAR(50),
                             password_hash VARCHAR(128)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, admin_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO admins 
                          (user_name, password_hash) 
                          VALUES (?,?)''', (admin_name, password_hash))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM admins WHERE id = ?", (str(user_id),))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM admins")
        rows = cursor.fetchall()
        return rows

    def exists(self, admin_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM admins WHERE user_name = ? AND password_hash = ?",
                       (admin_name, password_hash))
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)
