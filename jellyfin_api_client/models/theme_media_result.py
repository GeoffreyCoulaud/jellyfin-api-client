from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast
from typing import List
from typing import Union

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto


T = TypeVar("T", bound="ThemeMediaResult")


@_attrs_define
class ThemeMediaResult:
    """Class ThemeMediaResult.

    Attributes:
        items (Union[List['BaseItemDto'], None, Unset]): Gets or sets the items.
        total_record_count (Union[Unset, int]): Gets or sets the total number of records available.
        start_index (Union[Unset, int]): Gets or sets the index of the first record in Items.
        owner_id (Union[Unset, str]): Gets or sets the owner id.
    """

    items: Union[List["BaseItemDto"], None, Unset] = UNSET
    total_record_count: Union[Unset, int] = UNSET
    start_index: Union[Unset, int] = UNSET
    owner_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        items: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        total_record_count = self.total_record_count

        start_index = self.start_index

        owner_id = self.owner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if items is not UNSET:
            field_dict["Items"] = items
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index
        if owner_id is not UNSET:
            field_dict["OwnerId"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto

        d = src_dict.copy()

        def _parse_items(data: object) -> Union[List["BaseItemDto"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = BaseItemDto.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["BaseItemDto"], None, Unset], data)

        items = _parse_items(d.pop("Items", UNSET))

        total_record_count = d.pop("TotalRecordCount", UNSET)

        start_index = d.pop("StartIndex", UNSET)

        owner_id = d.pop("OwnerId", UNSET)

        theme_media_result = cls(
            items=items,
            total_record_count=total_record_count,
            start_index=start_index,
            owner_id=owner_id,
        )

        return theme_media_result
