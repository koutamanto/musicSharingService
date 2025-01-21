from hashlib import sha256
from uuid import uuid4
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3
import traceback

import requests
conn = sqlite3.connect("db/music.db", check_same_thread=False)
cur = conn.cursor()

app = Flask(__name__)

@app.route("/")
def index_page():
    cur.execute('SELECT * FROM music')
    musics = []
    for music_id, title, artist, description, url, upload_at, tags in cur.fetchall():
        try:
            oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
            oembed = requests.get(oembed_url).json()
            thumbnail_url = oembed["thumbnail_url"]
            musics.append([music_id, title, artist, description, url, upload_at, tags, thumbnail_url])
        except Exception as e:
            traceback.print_exc()
    return render_template("index.html", musics=musics)

@app.route("/music/<string:music_id>")
def music_page(music_id: str):
    cur.execute('SELECT * FROM music')
    musics = []
    for _music_id, _title, _artist, _description, _url, _upload_at, _tags in cur.fetchall():
        try:
            oembed_url = f"https://www.youtube.com/oembed?url={_url}&format=json"
            oembed = requests.get(oembed_url).json()
            _thumbnail_url = oembed["thumbnail_url"]
            musics.append([_music_id, _title, _artist, _description, _url, _upload_at, _tags, _thumbnail_url])
        except Exception as e:
            traceback.print_exc()
    cur.execute('SELECT * FROM music WHERE music_id=?', [music_id])
    music_id, title, artist, description, url, upload_at, tags = cur.fetchone()
    oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
    oembed = requests.get(oembed_url).json()
    thumbnail_url = oembed["thumbnail_url"]
    print(oembed["html"])
    embed_html = oembed["html"].replace("200", "800").replace("150", "450").replace("113", "450")
    return render_template("music.html", music_id=music_id, title=title, artist=artist, description=description, url=url, upload_at=upload_at, thumbnail_url=thumbnail_url, embed_html=embed_html, tags=tags, musics=musics)

@app.route("/search")
def search_page():
    search_query = request.args.get("q", "")
    if search_query == "":
        return redirect(url_for("index_page"))
    else:
        print(search_query)
        cur.execute(f'SELECT * FROM music WHERE title LIKE "%{search_query}%" OR artist LIKE "%{search_query}%" OR description LIKE "%{search_query}" OR tags LIKE "%{search_query}%"')
        musics = []
        for music_id, title, artist, description, url, upload_at, tags in cur.fetchall():
            oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
            oembed = requests.get(oembed_url).json()
            thumbnail_url = oembed["thumbnail_url"]
            musics.append([music_id, title, artist, description, url, upload_at, tags, thumbnail_url])
        return render_template("index.html", musics=musics)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        url = request.form["url"]
        title = request.form["title"]
        artist = request.form["artist"]
        description = request.form["description"]
        tags = request.form["tags"].rstrip(",").replace("NaN", "")
        print(tags)
        upload_at = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        music_id = sha256(str(upload_at).encode("utf-8")).hexdigest()
        cur.execute("""INSERT INTO music VALUES(?, ?, ?, ?, ?, ?, ?)""", (music_id, title, artist, description, url, upload_at, tags))
        conn.commit()
        return redirect(f"/music/{music_id}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)