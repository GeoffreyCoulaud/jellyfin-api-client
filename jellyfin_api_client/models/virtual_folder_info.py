from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast
from typing import List
from typing import Union
from ..models.virtual_folder_info_collection_type import VirtualFolderInfoCollectionType

if TYPE_CHECKING:
    from ..models.library_options import LibraryOptions


T = TypeVar("T", bound="VirtualFolderInfo")


@_attrs_define
class VirtualFolderInfo:
    """Used to hold information about a user's list of configured virtual folders.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        locations (Union[List[str], None, Unset]): Gets or sets the locations.
        collection_type (Union[Unset, VirtualFolderInfoCollectionType]): Gets or sets the type of the collection.
        library_options (Union['LibraryOptions', None, Unset]):
        item_id (Union[None, Unset, str]): Gets or sets the item identifier.
        primary_image_item_id (Union[None, Unset, str]): Gets or sets the primary image item identifier.
        refresh_progress (Union[None, Unset, float]):
        refresh_status (Union[None, Unset, str]):
    """

    name: Union[None, Unset, str] = UNSET
    locations: Union[List[str], None, Unset] = UNSET
    collection_type: Union[Unset, VirtualFolderInfoCollectionType] = UNSET
    library_options: Union["LibraryOptions", None, Unset] = UNSET
    item_id: Union[None, Unset, str] = UNSET
    primary_image_item_id: Union[None, Unset, str] = UNSET
    refresh_progress: Union[None, Unset, float] = UNSET
    refresh_status: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.library_options import LibraryOptions

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        locations: Union[List[str], None, Unset]
        if isinstance(self.locations, Unset):
            locations = UNSET
        elif isinstance(self.locations, list):
            locations = self.locations

        else:
            locations = self.locations

        collection_type: Union[Unset, str] = UNSET
        if not isinstance(self.collection_type, Unset):
            collection_type = self.collection_type.value

        library_options: Union[Dict[str, Any], None, Unset]
        if isinstance(self.library_options, Unset):
            library_options = UNSET
        elif isinstance(self.library_options, LibraryOptions):
            library_options = self.library_options.to_dict()
        else:
            library_options = self.library_options

        item_id: Union[None, Unset, str]
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        else:
            item_id = self.item_id

        primary_image_item_id: Union[None, Unset, str]
        if isinstance(self.primary_image_item_id, Unset):
            primary_image_item_id = UNSET
        else:
            primary_image_item_id = self.primary_image_item_id

        refresh_progress: Union[None, Unset, float]
        if isinstance(self.refresh_progress, Unset):
            refresh_progress = UNSET
        else:
            refresh_progress = self.refresh_progress

        refresh_status: Union[None, Unset, str]
        if isinstance(self.refresh_status, Unset):
            refresh_status = UNSET
        else:
            refresh_status = self.refresh_status

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if locations is not UNSET:
            field_dict["Locations"] = locations
        if collection_type is not UNSET:
            field_dict["CollectionType"] = collection_type
        if library_options is not UNSET:
            field_dict["LibraryOptions"] = library_options
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if primary_image_item_id is not UNSET:
            field_dict["PrimaryImageItemId"] = primary_image_item_id
        if refresh_progress is not UNSET:
            field_dict["RefreshProgress"] = refresh_progress
        if refresh_status is not UNSET:
            field_dict["RefreshStatus"] = refresh_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.library_options import LibraryOptions

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_locations(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locations_type_0 = cast(List[str], data)

                return locations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        locations = _parse_locations(d.pop("Locations", UNSET))

        _collection_type = d.pop("CollectionType", UNSET)
        collection_type: Union[Unset, VirtualFolderInfoCollectionType]
        if isinstance(_collection_type, Unset):
            collection_type = UNSET
        else:
            collection_type = VirtualFolderInfoCollectionType(_collection_type)

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

        def _parse_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_id = _parse_item_id(d.pop("ItemId", UNSET))

        def _parse_primary_image_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_image_item_id = _parse_primary_image_item_id(
            d.pop("PrimaryImageItemId", UNSET)
        )

        def _parse_refresh_progress(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        refresh_progress = _parse_refresh_progress(d.pop("RefreshProgress", UNSET))

        def _parse_refresh_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        refresh_status = _parse_refresh_status(d.pop("RefreshStatus", UNSET))

        virtual_folder_info = cls(
            name=name,
            locations=locations,
            collection_type=collection_type,
            library_options=library_options,
            item_id=item_id,
            primary_image_item_id=primary_image_item_id,
            refresh_progress=refresh_progress,
            refresh_status=refresh_status,
        )

        return virtual_folder_info
