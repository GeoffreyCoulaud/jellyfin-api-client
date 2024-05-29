from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from ..models.rating_type import RatingType
from ..models.image_type import ImageType


T = TypeVar("T", bound="RemoteImageInfo")


@_attrs_define
class RemoteImageInfo:
    """Class RemoteImageInfo.

    Attributes:
        provider_name (Union[None, Unset, str]): Gets or sets the name of the provider.
        url (Union[None, Unset, str]): Gets or sets the URL.
        thumbnail_url (Union[None, Unset, str]): Gets or sets a url used for previewing a smaller version.
        height (Union[None, Unset, int]): Gets or sets the height.
        width (Union[None, Unset, int]): Gets or sets the width.
        community_rating (Union[None, Unset, float]): Gets or sets the community rating.
        vote_count (Union[None, Unset, int]): Gets or sets the vote count.
        language (Union[None, Unset, str]): Gets or sets the language.
        type (Union[Unset, ImageType]): Enum ImageType.
        rating_type (Union[Unset, RatingType]):
    """

    provider_name: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    thumbnail_url: Union[None, Unset, str] = UNSET
    height: Union[None, Unset, int] = UNSET
    width: Union[None, Unset, int] = UNSET
    community_rating: Union[None, Unset, float] = UNSET
    vote_count: Union[None, Unset, int] = UNSET
    language: Union[None, Unset, str] = UNSET
    type: Union[Unset, ImageType] = UNSET
    rating_type: Union[Unset, RatingType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        provider_name: Union[None, Unset, str]
        if isinstance(self.provider_name, Unset):
            provider_name = UNSET
        else:
            provider_name = self.provider_name

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        thumbnail_url: Union[None, Unset, str]
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        height: Union[None, Unset, int]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        width: Union[None, Unset, int]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        community_rating: Union[None, Unset, float]
        if isinstance(self.community_rating, Unset):
            community_rating = UNSET
        else:
            community_rating = self.community_rating

        vote_count: Union[None, Unset, int]
        if isinstance(self.vote_count, Unset):
            vote_count = UNSET
        else:
            vote_count = self.vote_count

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        rating_type: Union[Unset, str] = UNSET
        if not isinstance(self.rating_type, Unset):
            rating_type = self.rating_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name
        if url is not UNSET:
            field_dict["Url"] = url
        if thumbnail_url is not UNSET:
            field_dict["ThumbnailUrl"] = thumbnail_url
        if height is not UNSET:
            field_dict["Height"] = height
        if width is not UNSET:
            field_dict["Width"] = width
        if community_rating is not UNSET:
            field_dict["CommunityRating"] = community_rating
        if vote_count is not UNSET:
            field_dict["VoteCount"] = vote_count
        if language is not UNSET:
            field_dict["Language"] = language
        if type is not UNSET:
            field_dict["Type"] = type
        if rating_type is not UNSET:
            field_dict["RatingType"] = rating_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_provider_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_name = _parse_provider_name(d.pop("ProviderName", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("Url", UNSET))

        def _parse_thumbnail_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbnail_url = _parse_thumbnail_url(d.pop("ThumbnailUrl", UNSET))

        def _parse_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        height = _parse_height(d.pop("Height", UNSET))

        def _parse_width(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        width = _parse_width(d.pop("Width", UNSET))

        def _parse_community_rating(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        community_rating = _parse_community_rating(d.pop("CommunityRating", UNSET))

        def _parse_vote_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        vote_count = _parse_vote_count(d.pop("VoteCount", UNSET))

        def _parse_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language = _parse_language(d.pop("Language", UNSET))

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ImageType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ImageType(_type)

        _rating_type = d.pop("RatingType", UNSET)
        rating_type: Union[Unset, RatingType]
        if isinstance(_rating_type, Unset):
            rating_type = UNSET
        else:
            rating_type = RatingType(_rating_type)

        remote_image_info = cls(
            provider_name=provider_name,
            url=url,
            thumbnail_url=thumbnail_url,
            height=height,
            width=width,
            community_rating=community_rating,
            vote_count=vote_count,
            language=language,
            type=type,
            rating_type=rating_type,
        )

        return remote_image_info
