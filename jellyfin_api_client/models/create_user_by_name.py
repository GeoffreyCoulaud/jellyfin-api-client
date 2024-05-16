from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="CreateUserByName")


@_attrs_define
class CreateUserByName:
    """The create user by name request body.

    Attributes:
        name (str): Gets or sets the username.
        password (Union[None, Unset, str]): Gets or sets the password.
    """

    name: str
    password: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Name": name,
            }
        )
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("Password", UNSET))

        create_user_by_name = cls(
            name=name,
            password=password,
        )

        return create_user_by_name
