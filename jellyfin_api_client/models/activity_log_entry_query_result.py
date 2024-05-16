from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from typing import cast, Union
from typing import Dict
from ..types import UNSET, Unset
from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.activity_log_entry import ActivityLogEntry


T = TypeVar("T", bound="ActivityLogEntryQueryResult")


@_attrs_define
class ActivityLogEntryQueryResult:
    """
    Attributes:
        items (Union[List['ActivityLogEntry'], None, Unset]): Gets or sets the items.
        total_record_count (Union[Unset, int]): Gets or sets the total number of records available.
        start_index (Union[Unset, int]): Gets or sets the index of the first record in Items.
    """

    items: Union[List["ActivityLogEntry"], None, Unset] = UNSET
    total_record_count: Union[Unset, int] = UNSET
    start_index: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.activity_log_entry import ActivityLogEntry

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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if items is not UNSET:
            field_dict["Items"] = items
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity_log_entry import ActivityLogEntry

        d = src_dict.copy()

        def _parse_items(data: object) -> Union[List["ActivityLogEntry"], None, Unset]:
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
                    items_type_0_item = ActivityLogEntry.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ActivityLogEntry"], None, Unset], data)

        items = _parse_items(d.pop("Items", UNSET))

        total_record_count = d.pop("TotalRecordCount", UNSET)

        start_index = d.pop("StartIndex", UNSET)

        activity_log_entry_query_result = cls(
            items=items,
            total_record_count=total_record_count,
            start_index=start_index,
        )

        return activity_log_entry_query_result
