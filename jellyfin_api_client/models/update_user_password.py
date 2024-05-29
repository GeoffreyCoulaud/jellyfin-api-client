from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union


T = TypeVar("T", bound="UpdateUserPassword")


@_attrs_define
class UpdateUserPassword:
    """The update user password request body.

    Attributes:
        current_password (Union[None, Unset, str]): Gets or sets the current sha1-hashed password.
        current_pw (Union[None, Unset, str]): Gets or sets the current plain text password.
        new_pw (Union[None, Unset, str]): Gets or sets the new plain text password.
        reset_password (Union[Unset, bool]): Gets or sets a value indicating whether to reset the password.
    """

    current_password: Union[None, Unset, str] = UNSET
    current_pw: Union[None, Unset, str] = UNSET
    new_pw: Union[None, Unset, str] = UNSET
    reset_password: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        current_password: Union[None, Unset, str]
        if isinstance(self.current_password, Unset):
            current_password = UNSET
        else:
            current_password = self.current_password

        current_pw: Union[None, Unset, str]
        if isinstance(self.current_pw, Unset):
            current_pw = UNSET
        else:
            current_pw = self.current_pw

        new_pw: Union[None, Unset, str]
        if isinstance(self.new_pw, Unset):
            new_pw = UNSET
        else:
            new_pw = self.new_pw

        reset_password = self.reset_password

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if current_password is not UNSET:
            field_dict["CurrentPassword"] = current_password
        if current_pw is not UNSET:
            field_dict["CurrentPw"] = current_pw
        if new_pw is not UNSET:
            field_dict["NewPw"] = new_pw
        if reset_password is not UNSET:
            field_dict["ResetPassword"] = reset_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_current_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        current_password = _parse_current_password(d.pop("CurrentPassword", UNSET))

        def _parse_current_pw(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        current_pw = _parse_current_pw(d.pop("CurrentPw", UNSET))

        def _parse_new_pw(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        new_pw = _parse_new_pw(d.pop("NewPw", UNSET))

        reset_password = d.pop("ResetPassword", UNSET)

        update_user_password = cls(
            current_password=current_password,
            current_pw=current_pw,
            new_pw=new_pw,
            reset_password=reset_password,
        )

        return update_user_password
