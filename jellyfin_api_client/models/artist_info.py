from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

import datetime
from typing import cast
from typing import List
from typing import Union
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.artist_info_provider_ids_type_0 import ArtistInfoProviderIdsType0
    from ..models.song_info import SongInfo


T = TypeVar("T", bound="ArtistInfo")


@_attrs_define
class ArtistInfo:
    """
    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        original_title (Union[None, Unset, str]): Gets or sets the original title.
        path (Union[None, Unset, str]): Gets or sets the path.
        metadata_language (Union[None, Unset, str]): Gets or sets the metadata language.
        metadata_country_code (Union[None, Unset, str]): Gets or sets the metadata country code.
        provider_ids (Union['ArtistInfoProviderIdsType0', None, Unset]): Gets or sets the provider ids.
        year (Union[None, Unset, int]): Gets or sets the year.
        index_number (Union[None, Unset, int]):
        parent_index_number (Union[None, Unset, int]):
        premiere_date (Union[None, Unset, datetime.datetime]):
        is_automated (Union[Unset, bool]):
        song_infos (Union[Unset, List['SongInfo']]):
    """

    name: Union[None, Unset, str] = UNSET
    original_title: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    metadata_language: Union[None, Unset, str] = UNSET
    metadata_country_code: Union[None, Unset, str] = UNSET
    provider_ids: Union["ArtistInfoProviderIdsType0", None, Unset] = UNSET
    year: Union[None, Unset, int] = UNSET
    index_number: Union[None, Unset, int] = UNSET
    parent_index_number: Union[None, Unset, int] = UNSET
    premiere_date: Union[None, Unset, datetime.datetime] = UNSET
    is_automated: Union[Unset, bool] = UNSET
    song_infos: Union[Unset, List["SongInfo"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.artist_info_provider_ids_type_0 import ArtistInfoProviderIdsType0

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        original_title: Union[None, Unset, str]
        if isinstance(self.original_title, Unset):
            original_title = UNSET
        else:
            original_title = self.original_title

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        metadata_language: Union[None, Unset, str]
        if isinstance(self.metadata_language, Unset):
            metadata_language = UNSET
        else:
            metadata_language = self.metadata_language

        metadata_country_code: Union[None, Unset, str]
        if isinstance(self.metadata_country_code, Unset):
            metadata_country_code = UNSET
        else:
            metadata_country_code = self.metadata_country_code

        provider_ids: Union[Dict[str, Any], None, Unset]
        if isinstance(self.provider_ids, Unset):
            provider_ids = UNSET
        elif isinstance(self.provider_ids, ArtistInfoProviderIdsType0):
            provider_ids = self.provider_ids.to_dict()
        else:
            provider_ids = self.provider_ids

        year: Union[None, Unset, int]
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        index_number: Union[None, Unset, int]
        if isinstance(self.index_number, Unset):
            index_number = UNSET
        else:
            index_number = self.index_number

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

        is_automated = self.is_automated

        song_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.song_infos, Unset):
            song_infos = []
            for song_infos_item_data in self.song_infos:
                song_infos_item = song_infos_item_data.to_dict()
                song_infos.append(song_infos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if original_title is not UNSET:
            field_dict["OriginalTitle"] = original_title
        if path is not UNSET:
            field_dict["Path"] = path
        if metadata_language is not UNSET:
            field_dict["MetadataLanguage"] = metadata_language
        if metadata_country_code is not UNSET:
            field_dict["MetadataCountryCode"] = metadata_country_code
        if provider_ids is not UNSET:
            field_dict["ProviderIds"] = provider_ids
        if year is not UNSET:
            field_dict["Year"] = year
        if index_number is not UNSET:
            field_dict["IndexNumber"] = index_number
        if parent_index_number is not UNSET:
            field_dict["ParentIndexNumber"] = parent_index_number
        if premiere_date is not UNSET:
            field_dict["PremiereDate"] = premiere_date
        if is_automated is not UNSET:
            field_dict["IsAutomated"] = is_automated
        if song_infos is not UNSET:
            field_dict["SongInfos"] = song_infos

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.artist_info_provider_ids_type_0 import ArtistInfoProviderIdsType0
        from ..models.song_info import SongInfo

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_original_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        original_title = _parse_original_title(d.pop("OriginalTitle", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_metadata_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        metadata_language = _parse_metadata_language(d.pop("MetadataLanguage", UNSET))

        def _parse_metadata_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        metadata_country_code = _parse_metadata_country_code(
            d.pop("MetadataCountryCode", UNSET)
        )

        def _parse_provider_ids(
            data: object,
        ) -> Union["ArtistInfoProviderIdsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_ids_type_0 = ArtistInfoProviderIdsType0.from_dict(data)

                return provider_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ArtistInfoProviderIdsType0", None, Unset], data)

        provider_ids = _parse_provider_ids(d.pop("ProviderIds", UNSET))

        def _parse_year(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        year = _parse_year(d.pop("Year", UNSET))

        def _parse_index_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        index_number = _parse_index_number(d.pop("IndexNumber", UNSET))

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

        is_automated = d.pop("IsAutomated", UNSET)

        song_infos = []
        _song_infos = d.pop("SongInfos", UNSET)
        for song_infos_item_data in _song_infos or []:
            song_infos_item = SongInfo.from_dict(song_infos_item_data)

            song_infos.append(song_infos_item)

        artist_info = cls(
            name=name,
            original_title=original_title,
            path=path,
            metadata_language=metadata_language,
            metadata_country_code=metadata_country_code,
            provider_ids=provider_ids,
            year=year,
            index_number=index_number,
            parent_index_number=parent_index_number,
            premiere_date=premiere_date,
            is_automated=is_automated,
            song_infos=song_infos,
        )

        return artist_info
