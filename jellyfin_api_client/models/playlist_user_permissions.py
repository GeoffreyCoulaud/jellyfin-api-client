from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="PlaylistUserPermissions")


@_attrs_define
class PlaylistUserPermissions:
    """Class to hold data on user permissions for playlists.

    Attributes:
        user_id (Union[Unset, str]): Gets or sets the user id.
        can_edit (Union[Unset, bool]): Gets or sets a value indicating whether the user has edit permissions.
    """

    user_id: Union[Unset, str] = UNSET
    can_edit: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        can_edit = self.can_edit

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if can_edit is not UNSET:
            field_dict["CanEdit"] = can_edit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("UserId", UNSET)

        can_edit = d.pop("CanEdit", UNSET)

        playlist_user_permissions = cls(
            user_id=user_id,
            can_edit=can_edit,
        )

        return playlist_user_permissions
