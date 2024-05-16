from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="UpdatePlaylistUserDto")


@_attrs_define
class UpdatePlaylistUserDto:
    """Update existing playlist user dto. Fields set to `null` will not be updated and keep their current values.

    Attributes:
        can_edit (Union[None, Unset, bool]): Gets or sets a value indicating whether the user can edit the playlist.
    """

    can_edit: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_edit: Union[None, Unset, bool]
        if isinstance(self.can_edit, Unset):
            can_edit = UNSET
        else:
            can_edit = self.can_edit

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_edit is not UNSET:
            field_dict["CanEdit"] = can_edit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_can_edit(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        can_edit = _parse_can_edit(d.pop("CanEdit", UNSET))

        update_playlist_user_dto = cls(
            can_edit=can_edit,
        )

        return update_playlist_user_dto
