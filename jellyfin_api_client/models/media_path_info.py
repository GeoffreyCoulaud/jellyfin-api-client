from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast


T = TypeVar("T", bound="MediaPathInfo")


@_attrs_define
class MediaPathInfo:
    """
    Attributes:
        path (Union[Unset, str]):
        network_path (Union[None, Unset, str]):
    """

    path: Union[Unset, str] = UNSET
    network_path: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        path = self.path

        network_path: Union[None, Unset, str]
        if isinstance(self.network_path, Unset):
            network_path = UNSET
        else:
            network_path = self.network_path

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if path is not UNSET:
            field_dict["Path"] = path
        if network_path is not UNSET:
            field_dict["NetworkPath"] = network_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("Path", UNSET)

        def _parse_network_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        network_path = _parse_network_path(d.pop("NetworkPath", UNSET))

        media_path_info = cls(
            path=path,
            network_path=network_path,
        )

        return media_path_info
