from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast


T = TypeVar("T", bound="ValidatePathDto")


@_attrs_define
class ValidatePathDto:
    """Validate path object.

    Attributes:
        validate_writable (Union[Unset, bool]): Gets or sets a value indicating whether validate if path is writable.
        path (Union[None, Unset, str]): Gets or sets the path.
        is_file (Union[None, Unset, bool]): Gets or sets is path file.
    """

    validate_writable: Union[Unset, bool] = UNSET
    path: Union[None, Unset, str] = UNSET
    is_file: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        validate_writable = self.validate_writable

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        is_file: Union[None, Unset, bool]
        if isinstance(self.is_file, Unset):
            is_file = UNSET
        else:
            is_file = self.is_file

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if validate_writable is not UNSET:
            field_dict["ValidateWritable"] = validate_writable
        if path is not UNSET:
            field_dict["Path"] = path
        if is_file is not UNSET:
            field_dict["IsFile"] = is_file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        validate_writable = d.pop("ValidateWritable", UNSET)

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_is_file(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_file = _parse_is_file(d.pop("IsFile", UNSET))

        validate_path_dto = cls(
            validate_writable=validate_writable,
            path=path,
            is_file=is_file,
        )

        return validate_path_dto
