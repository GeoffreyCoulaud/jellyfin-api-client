from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union


T = TypeVar("T", bound="SyncPlayQueueItem")


@_attrs_define
class SyncPlayQueueItem:
    """Class QueueItem.

    Attributes:
        item_id (Union[Unset, str]): Gets the item identifier.
        playlist_item_id (Union[Unset, str]): Gets the playlist identifier of the item.
    """

    item_id: Union[Unset, str] = UNSET
    playlist_item_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_id = self.item_id

        playlist_item_id = self.playlist_item_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_id = d.pop("ItemId", UNSET)

        playlist_item_id = d.pop("PlaylistItemId", UNSET)

        sync_play_queue_item = cls(
            item_id=item_id,
            playlist_item_id=playlist_item_id,
        )

        return sync_play_queue_item
