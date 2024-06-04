from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from ..models.group_state_type import GroupStateType
from ..models.playback_request_type import PlaybackRequestType


T = TypeVar("T", bound="GroupStateUpdate")


@_attrs_define
class GroupStateUpdate:
    """Class GroupStateUpdate.

    Attributes:
        state (Union[Unset, GroupStateType]): Enum GroupState.
        reason (Union[Unset, PlaybackRequestType]): Enum PlaybackRequestType.
    """

    state: Union[Unset, GroupStateType] = UNSET
    reason: Union[Unset, PlaybackRequestType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if state is not UNSET:
            field_dict["State"] = state
        if reason is not UNSET:
            field_dict["Reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("State", UNSET)
        state: Union[Unset, GroupStateType]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = GroupStateType(_state)

        _reason = d.pop("Reason", UNSET)
        reason: Union[Unset, PlaybackRequestType]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = PlaybackRequestType(_reason)

        group_state_update = cls(
            state=state,
            reason=reason,
        )

        return group_state_update
