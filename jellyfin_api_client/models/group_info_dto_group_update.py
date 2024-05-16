from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from ..types import UNSET, Unset
from typing import Union
from ..models.group_update_type import GroupUpdateType
from typing import cast

if TYPE_CHECKING:
    from ..models.group_info_dto import GroupInfoDto


T = TypeVar("T", bound="GroupInfoDtoGroupUpdate")


@_attrs_define
class GroupInfoDtoGroupUpdate:
    """Class GroupUpdate.

    Attributes:
        group_id (Union[Unset, str]): Gets the group identifier.
        type (Union[Unset, GroupUpdateType]): Enum GroupUpdateType.
        data (Union[Unset, GroupInfoDto]): Class GroupInfoDto.
    """

    group_id: Union[Unset, str] = UNSET
    type: Union[Unset, GroupUpdateType] = UNSET
    data: Union[Unset, "GroupInfoDto"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.group_info_dto import GroupInfoDto

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
        from ..models.group_info_dto import GroupInfoDto

        d = src_dict.copy()
        group_id = d.pop("GroupId", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, GroupUpdateType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GroupUpdateType(_type)

        _data = d.pop("Data", UNSET)
        data: Union[Unset, GroupInfoDto]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GroupInfoDto.from_dict(_data)

        group_info_dto_group_update = cls(
            group_id=group_id,
            type=type,
            data=data,
        )

        return group_info_dto_group_update
