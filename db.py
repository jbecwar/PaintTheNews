import sqlite3

def createSqliteConnection():
    return sqlite3.connect('paint_the_news.db')

def initDb():
    createHeadlineTable()
    return

def createHeadlineTable():
    conn = createSqliteConnection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS headlines (id INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT, title TEXT, url TEXT, date TEXT, runtime TEXT)''')
    conn.commit()
    conn.close()
    return

def insertHeadline(source, title, url, date, runtime):
    conn = createSqliteConnection()
    c = conn.cursor()
    c.execute('''INSERT INTO headlines (source, title, url, date, runtime) VALUES (?, ?, ?, ?, ?)''', (source, title, url, date, runtime))
    conn.commit()
    conn.close()
    return

def selectHeadlines(runtime):
    conn = createSqliteConnection()
    c = conn.cursor()
    c.execute('''SELECT * FROM headlines WHERE runtime = ?''', (runtime,))
    rows = c.fetchall()
    conn.close()
    return rows