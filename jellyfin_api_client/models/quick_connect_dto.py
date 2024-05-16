from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="QuickConnectDto")


@_attrs_define
class QuickConnectDto:
    """The quick connect request body.

    Attributes:
        secret (str): Gets or sets the quick connect secret.
    """

    secret: str

    def to_dict(self) -> Dict[str, Any]:
        secret = self.secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        secret = d.pop("Secret")

        quick_connect_dto = cls(
            secret=secret,
        )

        return quick_connect_dto
