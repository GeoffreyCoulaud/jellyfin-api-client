from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from ..models.session_message_type import SessionMessageType
from typing import cast


T = TypeVar("T", bound="ScheduledTasksInfoStartMessage")


@_attrs_define
class ScheduledTasksInfoStartMessage:
    """Scheduled tasks info start message.
    Data is the timing data encoded as "$initialDelay,$interval" in ms.

        Attributes:
            data (Union[None, Unset, str]): Gets or sets the data.
            message_type (Union[Unset, SessionMessageType]): The different kinds of messages that are used in the WebSocket
                api. Default: SessionMessageType.SCHEDULEDTASKSINFOSTART.
    """

    data: Union[None, Unset, str] = UNSET
    message_type: Union[Unset, SessionMessageType] = (
        SessionMessageType.SCHEDULEDTASKSINFOSTART
    )

    def to_dict(self) -> Dict[str, Any]:
        data: Union[None, Unset, str]
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data

        message_type: Union[Unset, str] = UNSET
        if not isinstance(self.message_type, Unset):
            message_type = self.message_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if data is not UNSET:
            field_dict["Data"] = data
        if message_type is not UNSET:
            field_dict["MessageType"] = message_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_data(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        data = _parse_data(d.pop("Data", UNSET))

        _message_type = d.pop("MessageType", UNSET)
        message_type: Union[Unset, SessionMessageType]
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = SessionMessageType(_message_type)

        scheduled_tasks_info_start_message = cls(
            data=data,
            message_type=message_type,
        )

        return scheduled_tasks_info_start_message
