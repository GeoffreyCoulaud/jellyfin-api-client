from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define


T = TypeVar("T", bound="StartupRemoteAccessDto")


@_attrs_define
class StartupRemoteAccessDto:
    """Startup remote access dto.

    Attributes:
        enable_remote_access (bool): Gets or sets a value indicating whether enable remote access.
        enable_automatic_port_mapping (bool): Gets or sets a value indicating whether enable automatic port mapping.
    """

    enable_remote_access: bool
    enable_automatic_port_mapping: bool

    def to_dict(self) -> Dict[str, Any]:
        enable_remote_access = self.enable_remote_access

        enable_automatic_port_mapping = self.enable_automatic_port_mapping

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "EnableRemoteAccess": enable_remote_access,
                "EnableAutomaticPortMapping": enable_automatic_port_mapping,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable_remote_access = d.pop("EnableRemoteAccess")

        enable_automatic_port_mapping = d.pop("EnableAutomaticPortMapping")

        startup_remote_access_dto = cls(
            enable_remote_access=enable_remote_access,
            enable_automatic_port_mapping=enable_automatic_port_mapping,
        )

        return startup_remote_access_dto
