from enum import Enum


class ExternalIdMediaType(str, Enum):
    ALBUM = "Album"
    ALBUMARTIST = "AlbumArtist"
    ARTIST = "Artist"
    BOOK = "Book"
    BOXSET = "BoxSet"
    EPISODE = "Episode"
    MOVIE = "Movie"
    OTHERARTIST = "OtherArtist"
    PERSON = "Person"
    RELEASEGROUP = "ReleaseGroup"
    SEASON = "Season"
    SERIES = "Series"
    TRACK = "Track"

    def __str__(self) -> str:
        return str(self.value)
