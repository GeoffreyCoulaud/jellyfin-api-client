from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union

if TYPE_CHECKING:
    from ..models.media_path_info import MediaPathInfo


T = TypeVar("T", bound="MediaPathDto")


@_attrs_define
class MediaPathDto:
    """Media Path dto.

    Attributes:
        name (str): Gets or sets the name of the library.
        path (Union[None, Unset, str]): Gets or sets the path to add.
        path_info (Union['MediaPathInfo', None, Unset]): Gets or sets the path info.
    """

    name: str
    path: Union[None, Unset, str] = UNSET
    path_info: Union["MediaPathInfo", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.media_path_info import MediaPathInfo

        name = self.name

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        path_info: Union[Dict[str, Any], None, Unset]
        if isinstance(self.path_info, Unset):
            path_info = UNSET
        elif isinstance(self.path_info, MediaPathInfo):
            path_info = self.path_info.to_dict()
        else:
            path_info = self.path_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Name": name,
            }
        )
        if path is not UNSET:
            field_dict["Path"] = path
        if path_info is not UNSET:
            field_dict["PathInfo"] = path_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_path_info import MediaPathInfo

        d = src_dict.copy()
        name = d.pop("Name")

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_path_info(data: object) -> Union["MediaPathInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                path_info_type_1 = MediaPathInfo.from_dict(data)

                return path_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MediaPathInfo", None, Unset], data)

        path_info = _parse_path_info(d.pop("PathInfo", UNSET))

        media_path_dto = cls(
            name=name,
            path=path,
            path_info=path_info,
        )

        return media_path_dto
