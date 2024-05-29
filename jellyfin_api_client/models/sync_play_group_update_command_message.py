from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast
from ..models.session_message_type import SessionMessageType
from typing import Union

if TYPE_CHECKING:
    from ..models.play_queue_update_group_update import PlayQueueUpdateGroupUpdate
    from ..models.group_state_update_group_update import GroupStateUpdateGroupUpdate
    from ..models.string_group_update import StringGroupUpdate
    from ..models.group_info_dto_group_update import GroupInfoDtoGroupUpdate


T = TypeVar("T", bound="SyncPlayGroupUpdateCommandMessage")


@_attrs_define
class SyncPlayGroupUpdateCommandMessage:
    """Untyped sync play command.

    Attributes:
        data (Union['GroupInfoDtoGroupUpdate', 'GroupStateUpdateGroupUpdate', 'PlayQueueUpdateGroupUpdate',
            'StringGroupUpdate', None, Unset]): Gets or sets the data.
        message_id (Union[Unset, str]): Gets or sets the message id.
        message_type (Union[Unset, SessionMessageType]): The different kinds of messages that are used in the WebSocket
            api. Default: SessionMessageType.SYNCPLAYGROUPUPDATE.
    """

    data: Union[
        "GroupInfoDtoGroupUpdate",
        "GroupStateUpdateGroupUpdate",
        "PlayQueueUpdateGroupUpdate",
        "StringGroupUpdate",
        None,
        Unset,
    ] = UNSET
    message_id: Union[Unset, str] = UNSET
    message_type: Union[Unset, SessionMessageType] = (
        SessionMessageType.SYNCPLAYGROUPUPDATE
    )

    def to_dict(self) -> Dict[str, Any]:
        from ..models.play_queue_update_group_update import PlayQueueUpdateGroupUpdate
        from ..models.group_state_update_group_update import GroupStateUpdateGroupUpdate
        from ..models.string_group_update import StringGroupUpdate
        from ..models.group_info_dto_group_update import GroupInfoDtoGroupUpdate

        data: Union[Dict[str, Any], None, Unset]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, GroupInfoDtoGroupUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, GroupStateUpdateGroupUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, StringGroupUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, PlayQueueUpdateGroupUpdate):
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
        from ..models.play_queue_update_group_update import PlayQueueUpdateGroupUpdate
        from ..models.group_state_update_group_update import GroupStateUpdateGroupUpdate
        from ..models.string_group_update import StringGroupUpdate
        from ..models.group_info_dto_group_update import GroupInfoDtoGroupUpdate

        d = src_dict.copy()

        def _parse_data(
            data: object,
        ) -> Union[
            "GroupInfoDtoGroupUpdate",
            "GroupStateUpdateGroupUpdate",
            "PlayQueueUpdateGroupUpdate",
            "StringGroupUpdate",
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_0 = (
                    GroupInfoDtoGroupUpdate.from_dict(data)
                )

                return componentsschemas_group_update_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_1 = (
                    GroupStateUpdateGroupUpdate.from_dict(data)
                )

                return componentsschemas_group_update_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_2 = StringGroupUpdate.from_dict(
                    data
                )

                return componentsschemas_group_update_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_group_update_type_3 = (
                    PlayQueueUpdateGroupUpdate.from_dict(data)
                )

                return componentsschemas_group_update_type_3
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "GroupInfoDtoGroupUpdate",
                    "GroupStateUpdateGroupUpdate",
                    "PlayQueueUpdateGroupUpdate",
                    "StringGroupUpdate",
                    None,
                    Unset,
                ],
                data,
            )

        data = _parse_data(d.pop("Data", UNSET))

        message_id = d.pop("MessageId", UNSET)

        _message_type = d.pop("MessageType", UNSET)
        message_type: Union[Unset, SessionMessageType]
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = SessionMessageType(_message_type)

        sync_play_group_update_command_message = cls(
            data=data,
            message_id=message_id,
            message_type=message_type,
        )

        return sync_play_group_update_command_message
