from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast


T = TypeVar("T", bound="MediaUpdateInfoPathDto")


@_attrs_define
class MediaUpdateInfoPathDto:
    """The media update info path.

    Attributes:
        path (Union[None, Unset, str]): Gets or sets media path.
        update_type (Union[None, Unset, str]): Gets or sets media update type.
            Created, Modified, Deleted.
    """

    path: Union[None, Unset, str] = UNSET
    update_type: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        update_type: Union[None, Unset, str]
        if isinstance(self.update_type, Unset):
            update_type = UNSET
        else:
            update_type = self.update_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if path is not UNSET:
            field_dict["Path"] = path
        if update_type is not UNSET:
            field_dict["UpdateType"] = update_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_update_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        update_type = _parse_update_type(d.pop("UpdateType", UNSET))

        media_update_info_path_dto = cls(
            path=path,
            update_type=update_type,
        )

        return media_update_info_path_dto
