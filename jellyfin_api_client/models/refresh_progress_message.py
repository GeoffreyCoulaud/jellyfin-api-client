from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union
from ..models.session_message_type import SessionMessageType
from typing import Dict
from ..types import UNSET, Unset
from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.refresh_progress_message_data_type_0 import RefreshProgressMessageDataType0


T = TypeVar("T", bound="RefreshProgressMessage")


@_attrs_define
class RefreshProgressMessage:
    """Refresh progress message.

    Attributes:
        data (Union['RefreshProgressMessageDataType0', None, Unset]): Gets or sets the data.
        message_id (Union[Unset, str]): Gets or sets the message id.
        message_type (Union[Unset, SessionMessageType]): The different kinds of messages that are used in the WebSocket
            api. Default: SessionMessageType.REFRESHPROGRESS.
    """

    data: Union["RefreshProgressMessageDataType0", None, Unset] = UNSET
    message_id: Union[Unset, str] = UNSET
    message_type: Union[Unset, SessionMessageType] = SessionMessageType.REFRESHPROGRESS

    def to_dict(self) -> Dict[str, Any]:
        from ..models.refresh_progress_message_data_type_0 import RefreshProgressMessageDataType0

        data: Union[Dict[str, Any], None, Unset]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, RefreshProgressMessageDataType0):
            data = self.data.to_dict()
        else:
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
        from ..models.refresh_progress_message_data_type_0 import RefreshProgressMessageDataType0

        d = src_dict.copy()

        def _parse_data(data: object) -> Union["RefreshProgressMessageDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = RefreshProgressMessageDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RefreshProgressMessageDataType0", None, Unset], data)

        data = _parse_data(d.pop("Data", UNSET))

        message_id = d.pop("MessageId", UNSET)

        _message_type = d.pop("MessageType", UNSET)
        message_type: Union[Unset, SessionMessageType]
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = SessionMessageType(_message_type)

        refresh_progress_message = cls(
            data=data,
            message_id=message_id,
            message_type=message_type,
        )

        return refresh_progress_message
