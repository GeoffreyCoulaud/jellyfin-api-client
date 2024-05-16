from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="WakeOnLanInfo")


@_attrs_define
class WakeOnLanInfo:
    """Provides the MAC address and port for wake-on-LAN functionality.

    Attributes:
        mac_address (Union[None, Unset, str]): Gets the MAC address of the device.
        port (Union[Unset, int]): Gets or sets the wake-on-LAN port.
    """

    mac_address: Union[None, Unset, str] = UNSET
    port: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        mac_address: Union[None, Unset, str]
        if isinstance(self.mac_address, Unset):
            mac_address = UNSET
        else:
            mac_address = self.mac_address

        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if mac_address is not UNSET:
            field_dict["MacAddress"] = mac_address
        if port is not UNSET:
            field_dict["Port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_mac_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mac_address = _parse_mac_address(d.pop("MacAddress", UNSET))

        port = d.pop("Port", UNSET)

        wake_on_lan_info = cls(
            mac_address=mac_address,
            port=port,
        )

        return wake_on_lan_info
