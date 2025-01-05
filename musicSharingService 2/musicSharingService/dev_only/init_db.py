import sqlite3
conn = sqlite3.connect("db/music.db")
cur = conn.cursor()

cur.execute("DROP TABLE music")
cur.execute("CREATE TABLE music(music_id TEXT, title TEXT, artist TEXT, description TEXT, url TEXT, uploaded_at datetime)")
conn.commit()