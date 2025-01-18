import sqlite3
conn = sqlite3.connect("db/music.db")
cur = conn.cursor()

cur.execute("DELETE FROM music WHERE music_id='65f9ef9ee5b6ca35ba35ddde06afe12a86a39d4cfa98f36ade35cd1b14a37e65'")
conn.commit()