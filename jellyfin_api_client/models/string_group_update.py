from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from ..models.group_update_type import GroupUpdateType


T = TypeVar("T", bound="StringGroupUpdate")


@_attrs_define
class StringGroupUpdate:
    """Class GroupUpdate.

    Attributes:
        group_id (Union[Unset, str]): Gets the group identifier.
        type (Union[Unset, GroupUpdateType]): Enum GroupUpdateType.
        data (Union[Unset, str]): Gets the update data.
    """

    group_id: Union[Unset, str] = UNSET
    type: Union[Unset, GroupUpdateType] = UNSET
    data: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        data = self.data

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
        d = src_dict.copy()
        group_id = d.pop("GroupId", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, GroupUpdateType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GroupUpdateType(_type)

        data = d.pop("Data", UNSET)

        string_group_update = cls(
            group_id=group_id,
            type=type,
            data=data,
        )

        return string_group_update
