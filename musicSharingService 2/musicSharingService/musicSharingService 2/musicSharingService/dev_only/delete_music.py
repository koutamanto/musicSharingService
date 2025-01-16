import sqlite3
conn = sqlite3.connect("db/music.db")
cur = conn.cursor()

cur.execute("DELETE FROM music WHERE music_id='9e550166c3c2305163b1df0f9b4645bbb42076be0cc5fcb33f646dc2c780e025'")
conn.commit()