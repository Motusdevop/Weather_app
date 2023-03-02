import sqlite3

def create():
    db = sqlite3.connect('users.db')
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
	    'login' text(10),
	    'password' text(20),
		'city' text(20)
        )""")

def register(login: str, password: str) -> tuple:
	db = sqlite3.connect('users.db')
	cursor = db.cursor()
	try:
		cursor.execute("SELECT login FROM users WHERE login = ?", [login])
		if cursor.fetchone() == None:
			cursor.execute("INSERT INTO users VALUES (?, ?, ?)", [login, password, "Москва"])
			db.commit()
			return("Успешная регистрация", True, True)
		else:
			return ("Такой пользователь уже есть", False, True)
	except sqlite3.Error as e:
		return (f"Error {e}", False, False)
	finally:
		cursor.close()
		db.close()

def login(login: str, password: str) -> tuple:
	db = sqlite3.connect('users.db')
	cursor = db.cursor()
	try:
		cursor.execute("SELECT login FROM users WHERE login = ?", [login])
		if cursor.fetchone() == None:
			return ("Такого пользователя нету", False, True)
		else:
			cursor.execute("SELECT password FROM users WHERE login = ?", [login])
			if cursor.fetchone()[0] == password:
				return ("Успешный вход", True, True)
			else:
				return ('Не правильный пароль', True, False)
	except sqlite3.Error as e:
		return (f"Error {e}", False, False)
	finally:
		cursor.close()
		db.close()

def SetCity(city: str, login: str) -> tuple:
	db = sqlite3.connect('users.db')
	cursor = db.cursor()
	try:
		cursor.execute(f"UPDATE users SET 'city' = '{city}' WHERE login = '{login}'")
		db.commit()
		return (f"Успешно", True)
	except sqlite3.Error as e:
		return (f"Error {e}", False)
	finally:
		cursor.close()
		db.close()

def EnterCity(login: str) -> str:
	db = sqlite3.connect('users.db')
	cursor = db.cursor()
	try:
		cursor.execute(f"SELECT city FROM users WHERE login = '{login}'")
		return cursor.fetchone()[0]
	except sqlite3.Error as e:
		return f"Error {e}"
	finally:
		cursor.close()
		db.close()