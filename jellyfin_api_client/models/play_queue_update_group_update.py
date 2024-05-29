from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from ..models.group_update_type import GroupUpdateType
from typing import Union

if TYPE_CHECKING:
    from ..models.play_queue_update import PlayQueueUpdate


T = TypeVar("T", bound="PlayQueueUpdateGroupUpdate")


@_attrs_define
class PlayQueueUpdateGroupUpdate:
    """Class GroupUpdate.

    Attributes:
        group_id (Union[Unset, str]): Gets the group identifier.
        type (Union[Unset, GroupUpdateType]): Enum GroupUpdateType.
        data (Union[Unset, PlayQueueUpdate]): Class PlayQueueUpdate.
    """

    group_id: Union[Unset, str] = UNSET
    type: Union[Unset, GroupUpdateType] = UNSET
    data: Union[Unset, "PlayQueueUpdate"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["GroupId"] = group_id
        if type is not UNSET:
            field_dict["Type"] = type
        if data is not UNSET:
            field_dict["Data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.play_queue_update import PlayQueueUpdate

        d = src_dict.copy()
        group_id = d.pop("GroupId", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, GroupUpdateType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GroupUpdateType(_type)

        _data = d.pop("Data", UNSET)
        data: Union[Unset, PlayQueueUpdate]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PlayQueueUpdate.from_dict(_data)

        play_queue_update_group_update = cls(
            group_id=group_id,
            type=type,
            data=data,
        )

        return play_queue_update_group_update
