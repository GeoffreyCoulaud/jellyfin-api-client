from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from ..models.session_message_type import SessionMessageType
from typing import Union


T = TypeVar("T", bound="InboundKeepAliveMessage")


@_attrs_define
class InboundKeepAliveMessage:
    """Keep alive websocket messages.

    Attributes:
        message_type (Union[Unset, SessionMessageType]): The different kinds of messages that are used in the WebSocket
            api. Default: SessionMessageType.KEEPALIVE.
    """

    message_type: Union[Unset, SessionMessageType] = SessionMessageType.KEEPALIVE

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

        inbound_keep_alive_message = cls(
            message_type=message_type,
        )

        return inbound_keep_alive_message
