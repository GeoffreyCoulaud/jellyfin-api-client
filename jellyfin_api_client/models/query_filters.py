from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast
from typing import List
from typing import Union

if TYPE_CHECKING:
    from ..models.name_guid_pair import NameGuidPair


T = TypeVar("T", bound="QueryFilters")


@_attrs_define
class QueryFilters:
    """
    Attributes:
        genres (Union[List['NameGuidPair'], None, Unset]):
        tags (Union[List[str], None, Unset]):
    """

    genres: Union[List["NameGuidPair"], None, Unset] = UNSET
    tags: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        genres: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = []
            for genres_type_0_item_data in self.genres:
                genres_type_0_item = genres_type_0_item_data.to_dict()
                genres.append(genres_type_0_item)

        else:
            genres = self.genres

        tags: Union[List[str], None, Unset]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if tags is not UNSET:
            field_dict["Tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.name_guid_pair import NameGuidPair

        d = src_dict.copy()

        def _parse_genres(data: object) -> Union[List["NameGuidPair"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genres_type_0 = []
                _genres_type_0 = data
                for genres_type_0_item_data in _genres_type_0:
                    genres_type_0_item = NameGuidPair.from_dict(genres_type_0_item_data)

                    genres_type_0.append(genres_type_0_item)

                return genres_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["NameGuidPair"], None, Unset], data)

        genres = _parse_genres(d.pop("Genres", UNSET))

        def _parse_tags(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(List[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        tags = _parse_tags(d.pop("Tags", UNSET))

        query_filters = cls(
            genres=genres,
            tags=tags,
        )

        return query_filters
