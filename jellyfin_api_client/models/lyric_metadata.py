from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union


T = TypeVar("T", bound="LyricMetadata")


@_attrs_define
class LyricMetadata:
    """LyricMetadata model.

    Attributes:
        artist (Union[None, Unset, str]): Gets or sets the song artist.
        album (Union[None, Unset, str]): Gets or sets the album this song is on.
        title (Union[None, Unset, str]): Gets or sets the title of the song.
        author (Union[None, Unset, str]): Gets or sets the author of the lyric data.
        length (Union[None, Unset, int]): Gets or sets the length of the song in ticks.
        by (Union[None, Unset, str]): Gets or sets who the LRC file was created by.
        offset (Union[None, Unset, int]): Gets or sets the lyric offset compared to audio in ticks.
        creator (Union[None, Unset, str]): Gets or sets the software used to create the LRC file.
        version (Union[None, Unset, str]): Gets or sets the version of the creator used.
        is_synced (Union[None, Unset, bool]): Gets or sets a value indicating whether this lyric is synced.
    """

    artist: Union[None, Unset, str] = UNSET
    album: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    author: Union[None, Unset, str] = UNSET
    length: Union[None, Unset, int] = UNSET
    by: Union[None, Unset, str] = UNSET
    offset: Union[None, Unset, int] = UNSET
    creator: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    is_synced: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        artist: Union[None, Unset, str]
        if isinstance(self.artist, Unset):
            artist = UNSET
        else:
            artist = self.artist

        album: Union[None, Unset, str]
        if isinstance(self.album, Unset):
            album = UNSET
        else:
            album = self.album

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        author: Union[None, Unset, str]
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        length: Union[None, Unset, int]
        if isinstance(self.length, Unset):
            length = UNSET
        else:
            length = self.length

        by: Union[None, Unset, str]
        if isinstance(self.by, Unset):
            by = UNSET
        else:
            by = self.by

        offset: Union[None, Unset, int]
        if isinstance(self.offset, Unset):
            offset = UNSET
        else:
            offset = self.offset

        creator: Union[None, Unset, str]
        if isinstance(self.creator, Unset):
            creator = UNSET
        else:
            creator = self.creator

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        is_synced: Union[None, Unset, bool]
        if isinstance(self.is_synced, Unset):
            is_synced = UNSET
        else:
            is_synced = self.is_synced

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if artist is not UNSET:
            field_dict["Artist"] = artist
        if album is not UNSET:
            field_dict["Album"] = album
        if title is not UNSET:
            field_dict["Title"] = title
        if author is not UNSET:
            field_dict["Author"] = author
        if length is not UNSET:
            field_dict["Length"] = length
        if by is not UNSET:
            field_dict["By"] = by
        if offset is not UNSET:
            field_dict["Offset"] = offset
        if creator is not UNSET:
            field_dict["Creator"] = creator
        if version is not UNSET:
            field_dict["Version"] = version
        if is_synced is not UNSET:
            field_dict["IsSynced"] = is_synced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_artist(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artist = _parse_artist(d.pop("Artist", UNSET))

        def _parse_album(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album = _parse_album(d.pop("Album", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("Title", UNSET))

        def _parse_author(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        author = _parse_author(d.pop("Author", UNSET))

        def _parse_length(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        length = _parse_length(d.pop("Length", UNSET))

        def _parse_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        by = _parse_by(d.pop("By", UNSET))

        def _parse_offset(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        offset = _parse_offset(d.pop("Offset", UNSET))

        def _parse_creator(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        creator = _parse_creator(d.pop("Creator", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("Version", UNSET))

        def _parse_is_synced(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_synced = _parse_is_synced(d.pop("IsSynced", UNSET))

        lyric_metadata = cls(
            artist=artist,
            album=album,
            title=title,
            author=author,
            length=length,
            by=by,
            offset=offset,
            creator=creator,
            version=version,
            is_synced=is_synced,
        )

        return lyric_metadata
