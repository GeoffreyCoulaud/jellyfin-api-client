from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="BasePluginConfiguration")


@_attrs_define
class BasePluginConfiguration:
    """Class BasePluginConfiguration."""

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        base_plugin_configuration = cls()

        return base_plugin_configuration
