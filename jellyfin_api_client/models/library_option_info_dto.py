from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast


T = TypeVar("T", bound="LibraryOptionInfoDto")


@_attrs_define
class LibraryOptionInfoDto:
    """Library option info dto.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets name.
        default_enabled (Union[Unset, bool]): Gets or sets a value indicating whether default enabled.
    """

    name: Union[None, Unset, str] = UNSET
    default_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        default_enabled = self.default_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if default_enabled is not UNSET:
            field_dict["DefaultEnabled"] = default_enabled

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

        default_enabled = d.pop("DefaultEnabled", UNSET)

        library_option_info_dto = cls(
            name=name,
            default_enabled=default_enabled,
        )

        return library_option_info_dto
