from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union
from typing import Dict
from ..types import UNSET, Unset
from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.user_dto import UserDto
    from ..models.session_info import SessionInfo


T = TypeVar("T", bound="AuthenticationResult")


@_attrs_define
class AuthenticationResult:
    """
    Attributes:
        user (Union['UserDto', None, Unset]): Class UserDto.
        session_info (Union['SessionInfo', None, Unset]): Class SessionInfo.
        access_token (Union[None, Unset, str]):
        server_id (Union[None, Unset, str]):
    """

    user: Union["UserDto", None, Unset] = UNSET
    session_info: Union["SessionInfo", None, Unset] = UNSET
    access_token: Union[None, Unset, str] = UNSET
    server_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.user_dto import UserDto
        from ..models.session_info import SessionInfo

        user: Union[Dict[str, Any], None, Unset]
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UserDto):
            user = self.user.to_dict()
        else:
            user = self.user

        session_info: Union[Dict[str, Any], None, Unset]
        if isinstance(self.session_info, Unset):
            session_info = UNSET
        elif isinstance(self.session_info, SessionInfo):
            session_info = self.session_info.to_dict()
        else:
            session_info = self.session_info

        access_token: Union[None, Unset, str]
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        server_id: Union[None, Unset, str]
        if isinstance(self.server_id, Unset):
            server_id = UNSET
        else:
            server_id = self.server_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user is not UNSET:
            field_dict["User"] = user
        if session_info is not UNSET:
            field_dict["SessionInfo"] = session_info
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_dto import UserDto
        from ..models.session_info import SessionInfo

        d = src_dict.copy()

        def _parse_user(data: object) -> Union["UserDto", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_1 = UserDto.from_dict(data)

                return user_type_1
            except:  # noqa: E722
                pass
            return cast(Union["UserDto", None, Unset], data)

        user = _parse_user(d.pop("User", UNSET))

        def _parse_session_info(data: object) -> Union["SessionInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                session_info_type_1 = SessionInfo.from_dict(data)

                return session_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SessionInfo", None, Unset], data)

        session_info = _parse_session_info(d.pop("SessionInfo", UNSET))

        def _parse_access_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        access_token = _parse_access_token(d.pop("AccessToken", UNSET))

        def _parse_server_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        server_id = _parse_server_id(d.pop("ServerId", UNSET))

        authentication_result = cls(
            user=user,
            session_info=session_info,
            access_token=access_token,
            server_id=server_id,
        )

        return authentication_result
