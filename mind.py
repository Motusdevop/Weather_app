import sqlite3

def create():
    db = sqlite3.connect('users.db')
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
	    login text(10),
	    password text(20)
        )""")

def register(login, password):
	db = sqlite3.connect('users.db')
	cursor = db.cursor()
	try:
		cursor.execute("SELECT login FROM users WHERE login = ?", [login])
		if cursor.fetchone() == None:
			cursor.execute("INSERT INTO users VALUES (?, ?)", [login, password])
			db.commit()
			return("Успешная регистрация", True, True, True)
		else:
			return ("Такой пользователь уже есть", False, False, True)
	except sqlite3.Error as e:
		return (f"Error {e}", False, False, False)
	finally:
		cursor.close()
		db.close()

def login(login, password):
	db = sqlite3.connect('users.db')
	cursor = db.cursor()
	try:
		cursor.execute("SELECT login FROM users WHERE login = ?", [login])
		if cursor.fetchone() == None:
			return ("Такого пользователя нету", False, False, True)
		else:
			cursor.execute("SELECT password FROM users WHERE login = ?", [login])
			if cursor.fetchone()[0] == password:
				return ("Успешный вход", True, True, True)
			else:
				return ('Не правильный пароль', False, True, False)
	except sqlite3.Error as e:
		return (f"Error {e}", False, False, False)
	finally:
		cursor.close()
		db.close()