"""Seed file to make sample data for db."""

from models import Playlist, Song, PlaylistSong, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Make a couple playlists

p1 = Playlist(name="First Playlist", description="This is my first playlist.")
p2 = Playlist(name="Second Playlist", description="This is my second playlist.")

# Add some songs

s1 = Song(title="Sloth", artist="Neal Morse")
s2 = Song(title="Erotomania", artist="DreamTheater")
s3 = Song(title="Parachutes", artist="Cold Play")

db.session.add_all([p1, p2, s1, s2, s3])

db.session.commit()


