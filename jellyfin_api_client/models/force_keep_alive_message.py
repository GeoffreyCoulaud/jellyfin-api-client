from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from ..models.session_message_type import SessionMessageType
from typing import Union


T = TypeVar("T", bound="ForceKeepAliveMessage")


@_attrs_define
class ForceKeepAliveMessage:
    """Force keep alive websocket messages.

    Attributes:
        data (Union[Unset, int]): Gets or sets the data.
        message_id (Union[Unset, str]): Gets or sets the message id.
        message_type (Union[Unset, SessionMessageType]): The different kinds of messages that are used in the WebSocket
            api. Default: SessionMessageType.FORCEKEEPALIVE.
    """

    data: Union[Unset, int] = UNSET
    message_id: Union[Unset, str] = UNSET
    message_type: Union[Unset, SessionMessageType] = SessionMessageType.FORCEKEEPALIVE

    def to_dict(self) -> Dict[str, Any]:
        data = self.data

        message_id = self.message_id

        message_type: Union[Unset, str] = UNSET
        if not isinstance(self.message_type, Unset):
            message_type = self.message_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if data is not UNSET:
            field_dict["Data"] = data
        if message_id is not UNSET:
            field_dict["MessageId"] = message_id
        if message_type is not UNSET:
            field_dict["MessageType"] = message_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = d.pop("Data", UNSET)

        message_id = d.pop("MessageId", UNSET)

        _message_type = d.pop("MessageType", UNSET)
        message_type: Union[Unset, SessionMessageType]
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = SessionMessageType(_message_type)

        force_keep_alive_message = cls(
            data=data,
            message_id=message_id,
            message_type=message_type,
        )

        return force_keep_alive_message
