from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union
from typing import List


T = TypeVar("T", bound="QueryFiltersLegacy")


@_attrs_define
class QueryFiltersLegacy:
    """
    Attributes:
        genres (Union[List[str], None, Unset]):
        tags (Union[List[str], None, Unset]):
        official_ratings (Union[List[str], None, Unset]):
        years (Union[List[int], None, Unset]):
    """

    genres: Union[List[str], None, Unset] = UNSET
    tags: Union[List[str], None, Unset] = UNSET
    official_ratings: Union[List[str], None, Unset] = UNSET
    years: Union[List[int], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        genres: Union[List[str], None, Unset]
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        tags: Union[List[str], None, Unset]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        official_ratings: Union[List[str], None, Unset]
        if isinstance(self.official_ratings, Unset):
            official_ratings = UNSET
        elif isinstance(self.official_ratings, list):
            official_ratings = self.official_ratings

        else:
            official_ratings = self.official_ratings

        years: Union[List[int], None, Unset]
        if isinstance(self.years, Unset):
            years = UNSET
        elif isinstance(self.years, list):
            years = self.years

        else:
            years = self.years

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if tags is not UNSET:
            field_dict["Tags"] = tags
        if official_ratings is not UNSET:
            field_dict["OfficialRatings"] = official_ratings
        if years is not UNSET:
            field_dict["Years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_genres(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genres_type_0 = cast(List[str], data)

                return genres_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

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

        def _parse_official_ratings(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                official_ratings_type_0 = cast(List[str], data)

                return official_ratings_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        official_ratings = _parse_official_ratings(d.pop("OfficialRatings", UNSET))

        def _parse_years(data: object) -> Union[List[int], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                years_type_0 = cast(List[int], data)

                return years_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[int], None, Unset], data)

        years = _parse_years(d.pop("Years", UNSET))

        query_filters_legacy = cls(
            genres=genres,
            tags=tags,
            official_ratings=official_ratings,
            years=years,
        )

        return query_filters_legacy
