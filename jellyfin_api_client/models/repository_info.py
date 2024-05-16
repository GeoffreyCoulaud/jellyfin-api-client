from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="RepositoryInfo")


@_attrs_define
class RepositoryInfo:
    """Class RepositoryInfo.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        url (Union[None, Unset, str]): Gets or sets the URL.
        enabled (Union[Unset, bool]): Gets or sets a value indicating whether the repository is enabled.
    """

    name: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if url is not UNSET:
            field_dict["Url"] = url
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("Url", UNSET))

        enabled = d.pop("Enabled", UNSET)

        repository_info = cls(
            name=name,
            url=url,
            enabled=enabled,
        )

        return repository_info
