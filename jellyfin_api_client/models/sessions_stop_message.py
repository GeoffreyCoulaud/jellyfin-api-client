from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..models.session_message_type import SessionMessageType
from ..types import UNSET, Unset


T = TypeVar("T", bound="SessionsStopMessage")


@_attrs_define
class SessionsStopMessage:
    """Sessions stop message.

    Attributes:
        message_type (Union[Unset, SessionMessageType]): The different kinds of messages that are used in the WebSocket
            api. Default: SessionMessageType.SESSIONSSTOP.
    """

    message_type: Union[Unset, SessionMessageType] = SessionMessageType.SESSIONSSTOP

    def to_dict(self) -> Dict[str, Any]:
        message_type: Union[Unset, str] = UNSET
        if not isinstance(self.message_type, Unset):
            message_type = self.message_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if message_type is not UNSET:
            field_dict["MessageType"] = message_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _message_type = d.pop("MessageType", UNSET)
        message_type: Union[Unset, SessionMessageType]
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = SessionMessageType(_message_type)

        sessions_stop_message = cls(
            message_type=message_type,
        )

        return sessions_stop_message
