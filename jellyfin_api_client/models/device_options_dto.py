from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast


T = TypeVar("T", bound="DeviceOptionsDto")


@_attrs_define
class DeviceOptionsDto:
    """A dto representing custom options for a device.

    Attributes:
        id (Union[Unset, int]): Gets or sets the id.
        device_id (Union[None, Unset, str]): Gets or sets the device id.
        custom_name (Union[None, Unset, str]): Gets or sets the custom name.
    """

    id: Union[Unset, int] = UNSET
    device_id: Union[None, Unset, str] = UNSET
    custom_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        device_id: Union[None, Unset, str]
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
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

        def _parse_device_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_id = _parse_device_id(d.pop("DeviceId", UNSET))

        def _parse_custom_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_name = _parse_custom_name(d.pop("CustomName", UNSET))

        device_options_dto = cls(
            id=id,
            device_id=device_id,
            custom_name=custom_name,
        )

        return device_options_dto
