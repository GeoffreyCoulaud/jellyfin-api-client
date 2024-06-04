from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast


T = TypeVar("T", bound="ServerDiscoveryInfo")


@_attrs_define
class ServerDiscoveryInfo:
    """The server discovery info model.

    Attributes:
        address (Union[Unset, str]): Gets the address.
        id (Union[Unset, str]): Gets the server identifier.
        name (Union[Unset, str]): Gets the name.
        endpoint_address (Union[None, Unset, str]): Gets the endpoint address.
    """

    address: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    endpoint_address: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        address = self.address

        id = self.id

        name = self.name

        endpoint_address: Union[None, Unset, str]
        if isinstance(self.endpoint_address, Unset):
            endpoint_address = UNSET
        else:
            endpoint_address = self.endpoint_address

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if endpoint_address is not UNSET:
            field_dict["EndpointAddress"] = endpoint_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("Address", UNSET)

        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        def _parse_endpoint_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        endpoint_address = _parse_endpoint_address(d.pop("EndpointAddress", UNSET))

        server_discovery_info = cls(
            address=address,
            id=id,
            name=name,
            endpoint_address=endpoint_address,
        )

        return server_discovery_info
