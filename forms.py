"""Forms for playlist app."""

from wtforms import StringField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional


class PlaylistForm(FlaskForm):
    name = StringField("Playlist Name", validators=[InputRequired()])
    description = StringField("Description", validators=[InputRequired()])
    """Form for adding playlists."""

    # Add the necessary code to use this form


class SongForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    artist = StringField("Artist", validators=[InputRequired()])
    
    """Form for adding songs."""

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    songs = SelectField('Song To Add', coerce=int)
