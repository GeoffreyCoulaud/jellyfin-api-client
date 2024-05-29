from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast
from typing import Union

if TYPE_CHECKING:
    from ..models.library_options import LibraryOptions


T = TypeVar("T", bound="AddVirtualFolderDto")


@_attrs_define
class AddVirtualFolderDto:
    """Add virtual folder dto.

    Attributes:
        library_options (Union['LibraryOptions', None, Unset]): Gets or sets library options.
    """

    library_options: Union["LibraryOptions", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.library_options import LibraryOptions

        library_options: Union[Dict[str, Any], None, Unset]
        if isinstance(self.library_options, Unset):
            library_options = UNSET
        elif isinstance(self.library_options, LibraryOptions):
            library_options = self.library_options.to_dict()
        else:
            library_options = self.library_options

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if library_options is not UNSET:
            field_dict["LibraryOptions"] = library_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.library_options import LibraryOptions

        d = src_dict.copy()

        def _parse_library_options(
            data: object,
        ) -> Union["LibraryOptions", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                library_options_type_1 = LibraryOptions.from_dict(data)

                return library_options_type_1
            except:  # noqa: E722
                pass
            return cast(Union["LibraryOptions", None, Unset], data)

        library_options = _parse_library_options(d.pop("LibraryOptions", UNSET))

        add_virtual_folder_dto = cls(
            library_options=library_options,
        )

        return add_virtual_folder_dto
