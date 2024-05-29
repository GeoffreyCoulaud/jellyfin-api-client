from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from ..models.session_message_type import SessionMessageType
from typing import cast

if TYPE_CHECKING:
    from ..models.library_update_info import LibraryUpdateInfo


T = TypeVar("T", bound="LibraryChangedMessage")


@_attrs_define
class LibraryChangedMessage:
    """Library changed message.

    Attributes:
        data (Union['LibraryUpdateInfo', None, Unset]): Class LibraryUpdateInfo.
        message_id (Union[Unset, str]): Gets or sets the message id.
        message_type (Union[Unset, SessionMessageType]): The different kinds of messages that are used in the WebSocket
            api. Default: SessionMessageType.LIBRARYCHANGED.
    """

    data: Union["LibraryUpdateInfo", None, Unset] = UNSET
    message_id: Union[Unset, str] = UNSET
    message_type: Union[Unset, SessionMessageType] = SessionMessageType.LIBRARYCHANGED

    def to_dict(self) -> Dict[str, Any]:
        from ..models.library_update_info import LibraryUpdateInfo

        data: Union[Dict[str, Any], None, Unset]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, LibraryUpdateInfo):
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
        from ..models.library_update_info import LibraryUpdateInfo

        d = src_dict.copy()

        def _parse_data(data: object) -> Union["LibraryUpdateInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = LibraryUpdateInfo.from_dict(data)

                return data_type_1
            except:  # noqa: E722
                pass
            return cast(Union["LibraryUpdateInfo", None, Unset], data)

        data = _parse_data(d.pop("Data", UNSET))

        message_id = d.pop("MessageId", UNSET)

        _message_type = d.pop("MessageType", UNSET)
        message_type: Union[Unset, SessionMessageType]
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = SessionMessageType(_message_type)

        library_changed_message = cls(
            data=data,
            message_id=message_id,
            message_type=message_type,
        )

        return library_changed_message
