import sqlite3
import xml.etree.ElementTree as ET
conn=sqlite3.connect('tracksdb.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname=input('Enter file name:')
if(len(fname)<1):fname='Library.xml'

def lookup(d,key):
    found=False
    for chd in d:
        if found: return chd.text
        if chd.tag== 'key' and chd.text==key:
            found=True
        return None
stuff=ET.parse(fname)
all=stuff.findall('dict/dict/dict/')
print('Dictcount=',len(all))

for entry in all:
    if (lookup(entry,'Track ID') is None): continue

    name=lookup(entry,' Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre= lookup(entry,'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue


    print (name,artist,album,genre,count,rating,length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES( ? )''',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name= ? ',(genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id,genre_id, len, rating, count)
        VALUES ( ?, ?, ?,?, ?, ? )''',
        ( name, album_id,genre, length, rating, count ) )

    conn.commit()
