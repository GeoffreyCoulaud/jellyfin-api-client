from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="DeviceOptions")


@_attrs_define
class DeviceOptions:
    """An entity representing custom options for a device.

    Attributes:
        id (Union[Unset, int]): Gets the id.
        device_id (Union[Unset, str]): Gets the device id.
        custom_name (Union[None, Unset, str]): Gets or sets the custom name.
    """

    id: Union[Unset, int] = UNSET
    device_id: Union[Unset, str] = UNSET
    custom_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        device_id = self.device_id

        custom_name: Union[None, Unset, str]
        if isinstance(self.custom_name, Unset):
            custom_name = UNSET
        else:
            custom_name = self.custom_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if custom_name is not UNSET:
            field_dict["CustomName"] = custom_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        device_id = d.pop("DeviceId", UNSET)

        def _parse_custom_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_name = _parse_custom_name(d.pop("CustomName", UNSET))

        device_options = cls(
            id=id,
            device_id=device_id,
            custom_name=custom_name,
        )

        return device_options
