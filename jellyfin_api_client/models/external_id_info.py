from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union
from ..models.external_id_info_type import ExternalIdInfoType


T = TypeVar("T", bound="ExternalIdInfo")


@_attrs_define
class ExternalIdInfo:
    """Represents the external id information for serialization to the client.

    Attributes:
        name (Union[Unset, str]): Gets or sets the display name of the external id provider (IE: IMDB, MusicBrainz,
            etc).
        key (Union[Unset, str]): Gets or sets the unique key for this id. This key should be unique across all
            providers.
        type (Union[Unset, ExternalIdInfoType]): Gets or sets the specific media type for this id. This is used to
            distinguish between the different
            external id types for providers with multiple ids.
            A null value indicates there is no specific media type associated with the external id, or this is the
            default id for the external provider so there is no need to specify a type.
        url_format_string (Union[None, Unset, str]): Gets or sets the URL format string.
    """

    name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    type: Union[Unset, ExternalIdInfoType] = UNSET
    url_format_string: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        key = self.key

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        url_format_string: Union[None, Unset, str]
        if isinstance(self.url_format_string, Unset):
            url_format_string = UNSET
        else:
            url_format_string = self.url_format_string

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if key is not UNSET:
            field_dict["Key"] = key
        if type is not UNSET:
            field_dict["Type"] = type
        if url_format_string is not UNSET:
            field_dict["UrlFormatString"] = url_format_string

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        key = d.pop("Key", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ExternalIdInfoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ExternalIdInfoType(_type)

        def _parse_url_format_string(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url_format_string = _parse_url_format_string(d.pop("UrlFormatString", UNSET))

        external_id_info = cls(
            name=name,
            key=key,
            type=type,
            url_format_string=url_format_string,
        )

        return external_id_info
