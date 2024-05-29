from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union


T = TypeVar("T", bound="ItemCounts")


@_attrs_define
class ItemCounts:
    """Class LibrarySummary.

    Attributes:
        movie_count (Union[Unset, int]): Gets or sets the movie count.
        series_count (Union[Unset, int]): Gets or sets the series count.
        episode_count (Union[Unset, int]): Gets or sets the episode count.
        artist_count (Union[Unset, int]): Gets or sets the artist count.
        program_count (Union[Unset, int]): Gets or sets the program count.
        trailer_count (Union[Unset, int]): Gets or sets the trailer count.
        song_count (Union[Unset, int]): Gets or sets the song count.
        album_count (Union[Unset, int]): Gets or sets the album count.
        music_video_count (Union[Unset, int]): Gets or sets the music video count.
        box_set_count (Union[Unset, int]): Gets or sets the box set count.
        book_count (Union[Unset, int]): Gets or sets the book count.
        item_count (Union[Unset, int]): Gets or sets the item count.
    """

    movie_count: Union[Unset, int] = UNSET
    series_count: Union[Unset, int] = UNSET
    episode_count: Union[Unset, int] = UNSET
    artist_count: Union[Unset, int] = UNSET
    program_count: Union[Unset, int] = UNSET
    trailer_count: Union[Unset, int] = UNSET
    song_count: Union[Unset, int] = UNSET
    album_count: Union[Unset, int] = UNSET
    music_video_count: Union[Unset, int] = UNSET
    box_set_count: Union[Unset, int] = UNSET
    book_count: Union[Unset, int] = UNSET
    item_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        movie_count = self.movie_count

        series_count = self.series_count

        episode_count = self.episode_count

        artist_count = self.artist_count

        program_count = self.program_count

        trailer_count = self.trailer_count

        song_count = self.song_count

        album_count = self.album_count

        music_video_count = self.music_video_count

        box_set_count = self.box_set_count

        book_count = self.book_count

        item_count = self.item_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if movie_count is not UNSET:
            field_dict["MovieCount"] = movie_count
        if series_count is not UNSET:
            field_dict["SeriesCount"] = series_count
        if episode_count is not UNSET:
            field_dict["EpisodeCount"] = episode_count
        if artist_count is not UNSET:
            field_dict["ArtistCount"] = artist_count
        if program_count is not UNSET:
            field_dict["ProgramCount"] = program_count
        if trailer_count is not UNSET:
            field_dict["TrailerCount"] = trailer_count
        if song_count is not UNSET:
            field_dict["SongCount"] = song_count
        if album_count is not UNSET:
            field_dict["AlbumCount"] = album_count
        if music_video_count is not UNSET:
            field_dict["MusicVideoCount"] = music_video_count
        if box_set_count is not UNSET:
            field_dict["BoxSetCount"] = box_set_count
        if book_count is not UNSET:
            field_dict["BookCount"] = book_count
        if item_count is not UNSET:
            field_dict["ItemCount"] = item_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        movie_count = d.pop("MovieCount", UNSET)

        series_count = d.pop("SeriesCount", UNSET)

        episode_count = d.pop("EpisodeCount", UNSET)

        artist_count = d.pop("ArtistCount", UNSET)

        program_count = d.pop("ProgramCount", UNSET)

        trailer_count = d.pop("TrailerCount", UNSET)

        song_count = d.pop("SongCount", UNSET)

        album_count = d.pop("AlbumCount", UNSET)

        music_video_count = d.pop("MusicVideoCount", UNSET)

        box_set_count = d.pop("BoxSetCount", UNSET)

        book_count = d.pop("BookCount", UNSET)

        item_count = d.pop("ItemCount", UNSET)

        item_counts = cls(
            movie_count=movie_count,
            series_count=series_count,
            episode_count=episode_count,
            artist_count=artist_count,
            program_count=program_count,
            trailer_count=trailer_count,
            song_count=song_count,
            album_count=album_count,
            music_video_count=music_video_count,
            box_set_count=box_set_count,
            book_count=book_count,
            item_count=item_count,
        )

        return item_counts
