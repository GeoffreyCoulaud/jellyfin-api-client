from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast
import datetime
from typing import List
from ..models.media_type import MediaType
from dateutil.parser import isoparse
from ..models.base_item_kind import BaseItemKind


T = TypeVar("T", bound="SearchHint")


@_attrs_define
class SearchHint:
    """Class SearchHintResult.

    Attributes:
        item_id (Union[Unset, str]): Gets or sets the item id.
        id (Union[Unset, str]): Gets or sets the item id.
        name (Union[Unset, str]): Gets or sets the name.
        matched_term (Union[Unset, str]): Gets or sets the matched term.
        index_number (Union[None, Unset, int]): Gets or sets the index number.
        production_year (Union[None, Unset, int]): Gets or sets the production year.
        parent_index_number (Union[None, Unset, int]): Gets or sets the parent index number.
        primary_image_tag (Union[None, Unset, str]): Gets or sets the image tag.
        thumb_image_tag (Union[None, Unset, str]): Gets or sets the thumb image tag.
        thumb_image_item_id (Union[None, Unset, str]): Gets or sets the thumb image item identifier.
        backdrop_image_tag (Union[None, Unset, str]): Gets or sets the backdrop image tag.
        backdrop_image_item_id (Union[None, Unset, str]): Gets or sets the backdrop image item identifier.
        type (Union[Unset, BaseItemKind]): The base item kind.
        is_folder (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is folder.
        run_time_ticks (Union[None, Unset, int]): Gets or sets the run time ticks.
        media_type (Union[Unset, MediaType]): Media types.
        start_date (Union[None, Unset, datetime.datetime]): Gets or sets the start date.
        end_date (Union[None, Unset, datetime.datetime]): Gets or sets the end date.
        series (Union[None, Unset, str]): Gets or sets the series.
        status (Union[None, Unset, str]): Gets or sets the status.
        album (Union[None, Unset, str]): Gets or sets the album.
        album_id (Union[None, Unset, str]): Gets or sets the album id.
        album_artist (Union[None, Unset, str]): Gets or sets the album artist.
        artists (Union[Unset, List[str]]): Gets or sets the artists.
        song_count (Union[None, Unset, int]): Gets or sets the song count.
        episode_count (Union[None, Unset, int]): Gets or sets the episode count.
        channel_id (Union[None, Unset, str]): Gets or sets the channel identifier.
        channel_name (Union[None, Unset, str]): Gets or sets the name of the channel.
        primary_image_aspect_ratio (Union[None, Unset, float]): Gets or sets the primary image aspect ratio.
    """

    item_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    matched_term: Union[Unset, str] = UNSET
    index_number: Union[None, Unset, int] = UNSET
    production_year: Union[None, Unset, int] = UNSET
    parent_index_number: Union[None, Unset, int] = UNSET
    primary_image_tag: Union[None, Unset, str] = UNSET
    thumb_image_tag: Union[None, Unset, str] = UNSET
    thumb_image_item_id: Union[None, Unset, str] = UNSET
    backdrop_image_tag: Union[None, Unset, str] = UNSET
    backdrop_image_item_id: Union[None, Unset, str] = UNSET
    type: Union[Unset, BaseItemKind] = UNSET
    is_folder: Union[None, Unset, bool] = UNSET
    run_time_ticks: Union[None, Unset, int] = UNSET
    media_type: Union[Unset, MediaType] = UNSET
    start_date: Union[None, Unset, datetime.datetime] = UNSET
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    series: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    album: Union[None, Unset, str] = UNSET
    album_id: Union[None, Unset, str] = UNSET
    album_artist: Union[None, Unset, str] = UNSET
    artists: Union[Unset, List[str]] = UNSET
    song_count: Union[None, Unset, int] = UNSET
    episode_count: Union[None, Unset, int] = UNSET
    channel_id: Union[None, Unset, str] = UNSET
    channel_name: Union[None, Unset, str] = UNSET
    primary_image_aspect_ratio: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_id = self.item_id

        id = self.id

        name = self.name

        matched_term = self.matched_term

        index_number: Union[None, Unset, int]
        if isinstance(self.index_number, Unset):
            index_number = UNSET
        else:
            index_number = self.index_number

        production_year: Union[None, Unset, int]
        if isinstance(self.production_year, Unset):
            production_year = UNSET
        else:
            production_year = self.production_year

        parent_index_number: Union[None, Unset, int]
        if isinstance(self.parent_index_number, Unset):
            parent_index_number = UNSET
        else:
            parent_index_number = self.parent_index_number

        primary_image_tag: Union[None, Unset, str]
        if isinstance(self.primary_image_tag, Unset):
            primary_image_tag = UNSET
        else:
            primary_image_tag = self.primary_image_tag

        thumb_image_tag: Union[None, Unset, str]
        if isinstance(self.thumb_image_tag, Unset):
            thumb_image_tag = UNSET
        else:
            thumb_image_tag = self.thumb_image_tag

        thumb_image_item_id: Union[None, Unset, str]
        if isinstance(self.thumb_image_item_id, Unset):
            thumb_image_item_id = UNSET
        else:
            thumb_image_item_id = self.thumb_image_item_id

        backdrop_image_tag: Union[None, Unset, str]
        if isinstance(self.backdrop_image_tag, Unset):
            backdrop_image_tag = UNSET
        else:
            backdrop_image_tag = self.backdrop_image_tag

        backdrop_image_item_id: Union[None, Unset, str]
        if isinstance(self.backdrop_image_item_id, Unset):
            backdrop_image_item_id = UNSET
        else:
            backdrop_image_item_id = self.backdrop_image_item_id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        is_folder: Union[None, Unset, bool]
        if isinstance(self.is_folder, Unset):
            is_folder = UNSET
        else:
            is_folder = self.is_folder

        run_time_ticks: Union[None, Unset, int]
        if isinstance(self.run_time_ticks, Unset):
            run_time_ticks = UNSET
        else:
            run_time_ticks = self.run_time_ticks

        media_type: Union[Unset, str] = UNSET
        if not isinstance(self.media_type, Unset):
            media_type = self.media_type.value

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        series: Union[None, Unset, str]
        if isinstance(self.series, Unset):
            series = UNSET
        else:
            series = self.series

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        album: Union[None, Unset, str]
        if isinstance(self.album, Unset):
            album = UNSET
        else:
            album = self.album

        album_id: Union[None, Unset, str]
        if isinstance(self.album_id, Unset):
            album_id = UNSET
        else:
            album_id = self.album_id

        album_artist: Union[None, Unset, str]
        if isinstance(self.album_artist, Unset):
            album_artist = UNSET
        else:
            album_artist = self.album_artist

        artists: Union[Unset, List[str]] = UNSET
        if not isinstance(self.artists, Unset):
            artists = self.artists

        song_count: Union[None, Unset, int]
        if isinstance(self.song_count, Unset):
            song_count = UNSET
        else:
            song_count = self.song_count

        episode_count: Union[None, Unset, int]
        if isinstance(self.episode_count, Unset):
            episode_count = UNSET
        else:
            episode_count = self.episode_count

        channel_id: Union[None, Unset, str]
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        else:
            channel_id = self.channel_id

        channel_name: Union[None, Unset, str]
        if isinstance(self.channel_name, Unset):
            channel_name = UNSET
        else:
            channel_name = self.channel_name

        primary_image_aspect_ratio: Union[None, Unset, float]
        if isinstance(self.primary_image_aspect_ratio, Unset):
            primary_image_aspect_ratio = UNSET
        else:
            primary_image_aspect_ratio = self.primary_image_aspect_ratio

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if matched_term is not UNSET:
            field_dict["MatchedTerm"] = matched_term
        if index_number is not UNSET:
            field_dict["IndexNumber"] = index_number
        if production_year is not UNSET:
            field_dict["ProductionYear"] = production_year
        if parent_index_number is not UNSET:
            field_dict["ParentIndexNumber"] = parent_index_number
        if primary_image_tag is not UNSET:
            field_dict["PrimaryImageTag"] = primary_image_tag
        if thumb_image_tag is not UNSET:
            field_dict["ThumbImageTag"] = thumb_image_tag
        if thumb_image_item_id is not UNSET:
            field_dict["ThumbImageItemId"] = thumb_image_item_id
        if backdrop_image_tag is not UNSET:
            field_dict["BackdropImageTag"] = backdrop_image_tag
        if backdrop_image_item_id is not UNSET:
            field_dict["BackdropImageItemId"] = backdrop_image_item_id
        if type is not UNSET:
            field_dict["Type"] = type
        if is_folder is not UNSET:
            field_dict["IsFolder"] = is_folder
        if run_time_ticks is not UNSET:
            field_dict["RunTimeTicks"] = run_time_ticks
        if media_type is not UNSET:
            field_dict["MediaType"] = media_type
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if series is not UNSET:
            field_dict["Series"] = series
        if status is not UNSET:
            field_dict["Status"] = status
        if album is not UNSET:
            field_dict["Album"] = album
        if album_id is not UNSET:
            field_dict["AlbumId"] = album_id
        if album_artist is not UNSET:
            field_dict["AlbumArtist"] = album_artist
        if artists is not UNSET:
            field_dict["Artists"] = artists
        if song_count is not UNSET:
            field_dict["SongCount"] = song_count
        if episode_count is not UNSET:
            field_dict["EpisodeCount"] = episode_count
        if channel_id is not UNSET:
            field_dict["ChannelId"] = channel_id
        if channel_name is not UNSET:
            field_dict["ChannelName"] = channel_name
        if primary_image_aspect_ratio is not UNSET:
            field_dict["PrimaryImageAspectRatio"] = primary_image_aspect_ratio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_id = d.pop("ItemId", UNSET)

        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        matched_term = d.pop("MatchedTerm", UNSET)

        def _parse_index_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        index_number = _parse_index_number(d.pop("IndexNumber", UNSET))

        def _parse_production_year(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        production_year = _parse_production_year(d.pop("ProductionYear", UNSET))

        def _parse_parent_index_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_index_number = _parse_parent_index_number(
            d.pop("ParentIndexNumber", UNSET)
        )

        def _parse_primary_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_image_tag = _parse_primary_image_tag(d.pop("PrimaryImageTag", UNSET))

        def _parse_thumb_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumb_image_tag = _parse_thumb_image_tag(d.pop("ThumbImageTag", UNSET))

        def _parse_thumb_image_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumb_image_item_id = _parse_thumb_image_item_id(
            d.pop("ThumbImageItemId", UNSET)
        )

        def _parse_backdrop_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backdrop_image_tag = _parse_backdrop_image_tag(d.pop("BackdropImageTag", UNSET))

        def _parse_backdrop_image_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backdrop_image_item_id = _parse_backdrop_image_item_id(
            d.pop("BackdropImageItemId", UNSET)
        )

        _type = d.pop("Type", UNSET)
        type: Union[Unset, BaseItemKind]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = BaseItemKind(_type)

        def _parse_is_folder(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_folder = _parse_is_folder(d.pop("IsFolder", UNSET))

        def _parse_run_time_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        run_time_ticks = _parse_run_time_ticks(d.pop("RunTimeTicks", UNSET))

        _media_type = d.pop("MediaType", UNSET)
        media_type: Union[Unset, MediaType]
        if isinstance(_media_type, Unset):
            media_type = UNSET
        else:
            media_type = MediaType(_media_type)

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_date = _parse_start_date(d.pop("StartDate", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_date = _parse_end_date(d.pop("EndDate", UNSET))

        def _parse_series(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series = _parse_series(d.pop("Series", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("Status", UNSET))

        def _parse_album(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album = _parse_album(d.pop("Album", UNSET))

        def _parse_album_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album_id = _parse_album_id(d.pop("AlbumId", UNSET))

        def _parse_album_artist(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album_artist = _parse_album_artist(d.pop("AlbumArtist", UNSET))

        artists = cast(List[str], d.pop("Artists", UNSET))

        def _parse_song_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        song_count = _parse_song_count(d.pop("SongCount", UNSET))

        def _parse_episode_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        episode_count = _parse_episode_count(d.pop("EpisodeCount", UNSET))

        def _parse_channel_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_id = _parse_channel_id(d.pop("ChannelId", UNSET))

        def _parse_channel_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_name = _parse_channel_name(d.pop("ChannelName", UNSET))

        def _parse_primary_image_aspect_ratio(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        primary_image_aspect_ratio = _parse_primary_image_aspect_ratio(
            d.pop("PrimaryImageAspectRatio", UNSET)
        )

        search_hint = cls(
            item_id=item_id,
            id=id,
            name=name,
            matched_term=matched_term,
            index_number=index_number,
            production_year=production_year,
            parent_index_number=parent_index_number,
            primary_image_tag=primary_image_tag,
            thumb_image_tag=thumb_image_tag,
            thumb_image_item_id=thumb_image_item_id,
            backdrop_image_tag=backdrop_image_tag,
            backdrop_image_item_id=backdrop_image_item_id,
            type=type,
            is_folder=is_folder,
            run_time_ticks=run_time_ticks,
            media_type=media_type,
            start_date=start_date,
            end_date=end_date,
            series=series,
            status=status,
            album=album,
            album_id=album_id,
            album_artist=album_artist,
            artists=artists,
            song_count=song_count,
            episode_count=episode_count,
            channel_id=channel_id,
            channel_name=channel_name,
            primary_image_aspect_ratio=primary_image_aspect_ratio,
        )

        return search_hint
