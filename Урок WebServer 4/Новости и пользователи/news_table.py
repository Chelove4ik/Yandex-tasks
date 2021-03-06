import sqlite3


class DB:
    def __init__(self):
        conn = sqlite3.connect('SQLite/news.db', check_same_thread=False)
        self.conn = conn

    def get_connection(self):
        return self.conn

    def __del__(self):
        self.conn.close()


class UsersModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_name VARCHAR(50),
                             password_hash VARCHAR(128)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (user_name, password_hash) 
                          VALUES (?,?)''', (user_name, password_hash))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id),))
        row = cursor.fetchone()
        return row

    def put(self, user_id, user_name, password):
        cursor = self.connection.cursor()
        if user_name:
            cursor.execute('''UPDATE users 
                              SET user_name = ? 
                              WHERE id = ?''', (user_name, user_id))
        if password:
            cursor.execute('''UPDATE users 
                              SET password_hash = ? 
                              WHERE id = ?''', (password, user_id))
        cursor.close()
        self.connection.commit()

    def get_all(self, only_names=False):
        cursor = self.connection.cursor()
        if only_names:
            cursor.execute("SELECT id, user_name FROM users")
        else:
            cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = ? AND password_hash = ?",
                       (user_name, password_hash))
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def delete(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', str(user_id))
        cursor.close()
        self.connection.commit()


class NewsModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS news 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             title VARCHAR(100),
                             content VARCHAR(1000),
                             user_id INTEGER
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, title, content, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO news 
                          (title, content, user_id) 
                          VALUES (?,?,?)''', (title, content, str(user_id)))
        cursor.close()
        self.connection.commit()

    def get(self, news_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM news WHERE id = ?", (str(news_id),))
        row = cursor.fetchone()
        return row

    def put(self, news_id, title, content, user_id):
        cursor = self.connection.cursor()
        if title:
            cursor.execute('''UPDATE news 
                              SET title = ? 
                              WHERE id = ? and user_id = ?''', (title, news_id, user_id))
        if content:
            cursor.execute('''UPDATE news 
                              SET content = ? 
                              WHERE id = ? and user_id = ?''', (content, news_id, user_id))
        cursor.close()
        self.connection.commit()

    def get_all(self, user_id=None, only_titles=False):
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute("SELECT * FROM news WHERE user_id = ?",
                           (str(user_id),))
        elif only_titles:
            cursor.execute("SELECT id, title FROM news")
        else:
            cursor.execute("SELECT * FROM news")
        rows = cursor.fetchall()
        return rows

    def get_len_all(self, user_id):
        return len(self.get_all(user_id[0]))

    def delete(self, news_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM news WHERE id = ?''', (str(news_id),))
        cursor.close()
        self.connection.commit()
