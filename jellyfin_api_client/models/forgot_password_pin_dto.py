from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="ForgotPasswordPinDto")


@_attrs_define
class ForgotPasswordPinDto:
    """Forgot Password Pin enter request body DTO.

    Attributes:
        pin (str): Gets or sets the entered pin to have the password reset.
    """

    pin: str

    def to_dict(self) -> Dict[str, Any]:
        pin = self.pin

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Pin": pin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pin = d.pop("Pin")

        forgot_password_pin_dto = cls(
            pin=pin,
        )

        return forgot_password_pin_dto
