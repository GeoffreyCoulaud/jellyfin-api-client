from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

import datetime
from typing import cast
from typing import List
from typing import Union
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.remote_search_result_provider_ids_type_0 import (
        RemoteSearchResultProviderIdsType0,
    )


T = TypeVar("T", bound="RemoteSearchResult")


@_attrs_define
class RemoteSearchResult:
    """
    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        provider_ids (Union['RemoteSearchResultProviderIdsType0', None, Unset]): Gets or sets the provider ids.
        production_year (Union[None, Unset, int]): Gets or sets the year.
        index_number (Union[None, Unset, int]):
        index_number_end (Union[None, Unset, int]):
        parent_index_number (Union[None, Unset, int]):
        premiere_date (Union[None, Unset, datetime.datetime]):
        image_url (Union[None, Unset, str]):
        search_provider_name (Union[None, Unset, str]):
        overview (Union[None, Unset, str]):
        album_artist (Union['RemoteSearchResult', None, Unset]):
        artists (Union[List['RemoteSearchResult'], None, Unset]):
    """

    name: Union[None, Unset, str] = UNSET
    provider_ids: Union["RemoteSearchResultProviderIdsType0", None, Unset] = UNSET
    production_year: Union[None, Unset, int] = UNSET
    index_number: Union[None, Unset, int] = UNSET
    index_number_end: Union[None, Unset, int] = UNSET
    parent_index_number: Union[None, Unset, int] = UNSET
    premiere_date: Union[None, Unset, datetime.datetime] = UNSET
    image_url: Union[None, Unset, str] = UNSET
    search_provider_name: Union[None, Unset, str] = UNSET
    overview: Union[None, Unset, str] = UNSET
    album_artist: Union["RemoteSearchResult", None, Unset] = UNSET
    artists: Union[List["RemoteSearchResult"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.remote_search_result_provider_ids_type_0 import (
            RemoteSearchResultProviderIdsType0,
        )

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        provider_ids: Union[Dict[str, Any], None, Unset]
        if isinstance(self.provider_ids, Unset):
            provider_ids = UNSET
        elif isinstance(self.provider_ids, RemoteSearchResultProviderIdsType0):
            provider_ids = self.provider_ids.to_dict()
        else:
            provider_ids = self.provider_ids

        production_year: Union[None, Unset, int]
        if isinstance(self.production_year, Unset):
            production_year = UNSET
        else:
            production_year = self.production_year

        index_number: Union[None, Unset, int]
        if isinstance(self.index_number, Unset):
            index_number = UNSET
        else:
            index_number = self.index_number

        index_number_end: Union[None, Unset, int]
        if isinstance(self.index_number_end, Unset):
            index_number_end = UNSET
        else:
            index_number_end = self.index_number_end

        parent_index_number: Union[None, Unset, int]
        if isinstance(self.parent_index_number, Unset):
            parent_index_number = UNSET
        else:
            parent_index_number = self.parent_index_number

        premiere_date: Union[None, Unset, str]
        if isinstance(self.premiere_date, Unset):
            premiere_date = UNSET
        elif isinstance(self.premiere_date, datetime.datetime):
            premiere_date = self.premiere_date.isoformat()
        else:
            premiere_date = self.premiere_date

        image_url: Union[None, Unset, str]
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        search_provider_name: Union[None, Unset, str]
        if isinstance(self.search_provider_name, Unset):
            search_provider_name = UNSET
        else:
            search_provider_name = self.search_provider_name

        overview: Union[None, Unset, str]
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        album_artist: Union[Dict[str, Any], None, Unset]
        if isinstance(self.album_artist, Unset):
            album_artist = UNSET
        elif isinstance(self.album_artist, RemoteSearchResult):
            album_artist = self.album_artist.to_dict()
        else:
            album_artist = self.album_artist

        artists: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.artists, Unset):
            artists = UNSET
        elif isinstance(self.artists, list):
            artists = []
            for artists_type_0_item_data in self.artists:
                artists_type_0_item = artists_type_0_item_data.to_dict()
                artists.append(artists_type_0_item)

        else:
            artists = self.artists

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if provider_ids is not UNSET:
            field_dict["ProviderIds"] = provider_ids
        if production_year is not UNSET:
            field_dict["ProductionYear"] = production_year
        if index_number is not UNSET:
            field_dict["IndexNumber"] = index_number
        if index_number_end is not UNSET:
            field_dict["IndexNumberEnd"] = index_number_end
        if parent_index_number is not UNSET:
            field_dict["ParentIndexNumber"] = parent_index_number
        if premiere_date is not UNSET:
            field_dict["PremiereDate"] = premiere_date
        if image_url is not UNSET:
            field_dict["ImageUrl"] = image_url
        if search_provider_name is not UNSET:
            field_dict["SearchProviderName"] = search_provider_name
        if overview is not UNSET:
            field_dict["Overview"] = overview
        if album_artist is not UNSET:
            field_dict["AlbumArtist"] = album_artist
        if artists is not UNSET:
            field_dict["Artists"] = artists

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.remote_search_result_provider_ids_type_0 import (
            RemoteSearchResultProviderIdsType0,
        )

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_provider_ids(
            data: object,
        ) -> Union["RemoteSearchResultProviderIdsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_ids_type_0 = RemoteSearchResultProviderIdsType0.from_dict(data)

                return provider_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RemoteSearchResultProviderIdsType0", None, Unset], data)

        provider_ids = _parse_provider_ids(d.pop("ProviderIds", UNSET))

        def _parse_production_year(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        production_year = _parse_production_year(d.pop("ProductionYear", UNSET))

        def _parse_index_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        index_number = _parse_index_number(d.pop("IndexNumber", UNSET))

        def _parse_index_number_end(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        index_number_end = _parse_index_number_end(d.pop("IndexNumberEnd", UNSET))

        def _parse_parent_index_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_index_number = _parse_parent_index_number(
            d.pop("ParentIndexNumber", UNSET)
        )

        def _parse_premiere_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                premiere_date_type_0 = isoparse(data)

                return premiere_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        premiere_date = _parse_premiere_date(d.pop("PremiereDate", UNSET))

        def _parse_image_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_url = _parse_image_url(d.pop("ImageUrl", UNSET))

        def _parse_search_provider_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        search_provider_name = _parse_search_provider_name(
            d.pop("SearchProviderName", UNSET)
        )

        def _parse_overview(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        overview = _parse_overview(d.pop("Overview", UNSET))

        def _parse_album_artist(
            data: object,
        ) -> Union["RemoteSearchResult", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                album_artist_type_1 = RemoteSearchResult.from_dict(data)

                return album_artist_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RemoteSearchResult", None, Unset], data)

        album_artist = _parse_album_artist(d.pop("AlbumArtist", UNSET))

        def _parse_artists(
            data: object,
        ) -> Union[List["RemoteSearchResult"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                artists_type_0 = []
                _artists_type_0 = data
                for artists_type_0_item_data in _artists_type_0:
                    artists_type_0_item = RemoteSearchResult.from_dict(
                        artists_type_0_item_data
                    )

                    artists_type_0.append(artists_type_0_item)

                return artists_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["RemoteSearchResult"], None, Unset], data)

        artists = _parse_artists(d.pop("Artists", UNSET))

        remote_search_result = cls(
            name=name,
            provider_ids=provider_ids,
            production_year=production_year,
            index_number=index_number,
            index_number_end=index_number_end,
            parent_index_number=parent_index_number,
            premiere_date=premiere_date,
            image_url=image_url,
            search_provider_name=search_provider_name,
            overview=overview,
            album_artist=album_artist,
            artists=artists,
        )

        return remote_search_result
