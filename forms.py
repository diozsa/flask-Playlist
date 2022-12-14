"""Forms for playlist app."""

from ast import Str
from wtforms import SelectField
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional



class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name", validators=[InputRequired()])    
    description = StringField("Playlist Description", validators=[InputRequired()])



class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title", validators=[InputRequired()])    
    artist = StringField("Artist Name", validators=[InputRequired()])



# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
