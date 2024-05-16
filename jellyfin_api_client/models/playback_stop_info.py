from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union
from typing import cast, List
from typing import Dict
from ..types import UNSET, Unset
from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto
    from ..models.queue_item import QueueItem


T = TypeVar("T", bound="PlaybackStopInfo")


@_attrs_define
class PlaybackStopInfo:
    """Class PlaybackStopInfo.

    Attributes:
        item (Union['BaseItemDto', None, Unset]): Gets or sets the item.
        item_id (Union[Unset, str]): Gets or sets the item identifier.
        session_id (Union[None, Unset, str]): Gets or sets the session id.
        media_source_id (Union[None, Unset, str]): Gets or sets the media version identifier.
        position_ticks (Union[None, Unset, int]): Gets or sets the position ticks.
        live_stream_id (Union[None, Unset, str]): Gets or sets the live stream identifier.
        play_session_id (Union[None, Unset, str]): Gets or sets the play session identifier.
        failed (Union[Unset, bool]): Gets or sets a value indicating whether this
            MediaBrowser.Model.Session.PlaybackStopInfo is failed.
        next_media_type (Union[None, Unset, str]):
        playlist_item_id (Union[None, Unset, str]):
        now_playing_queue (Union[List['QueueItem'], None, Unset]):
    """

    item: Union["BaseItemDto", None, Unset] = UNSET
    item_id: Union[Unset, str] = UNSET
    session_id: Union[None, Unset, str] = UNSET
    media_source_id: Union[None, Unset, str] = UNSET
    position_ticks: Union[None, Unset, int] = UNSET
    live_stream_id: Union[None, Unset, str] = UNSET
    play_session_id: Union[None, Unset, str] = UNSET
    failed: Union[Unset, bool] = UNSET
    next_media_type: Union[None, Unset, str] = UNSET
    playlist_item_id: Union[None, Unset, str] = UNSET
    now_playing_queue: Union[List["QueueItem"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.base_item_dto import BaseItemDto
        from ..models.queue_item import QueueItem

        item: Union[Dict[str, Any], None, Unset]
        if isinstance(self.item, Unset):
            item = UNSET
        elif isinstance(self.item, BaseItemDto):
            item = self.item.to_dict()
        else:
            item = self.item

        item_id = self.item_id

        session_id: Union[None, Unset, str]
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        media_source_id: Union[None, Unset, str]
        if isinstance(self.media_source_id, Unset):
            media_source_id = UNSET
        else:
            media_source_id = self.media_source_id

        position_ticks: Union[None, Unset, int]
        if isinstance(self.position_ticks, Unset):
            position_ticks = UNSET
        else:
            position_ticks = self.position_ticks

        live_stream_id: Union[None, Unset, str]
        if isinstance(self.live_stream_id, Unset):
            live_stream_id = UNSET
        else:
            live_stream_id = self.live_stream_id

        play_session_id: Union[None, Unset, str]
        if isinstance(self.play_session_id, Unset):
            play_session_id = UNSET
        else:
            play_session_id = self.play_session_id

        failed = self.failed

        next_media_type: Union[None, Unset, str]
        if isinstance(self.next_media_type, Unset):
            next_media_type = UNSET
        else:
            next_media_type = self.next_media_type

        playlist_item_id: Union[None, Unset, str]
        if isinstance(self.playlist_item_id, Unset):
            playlist_item_id = UNSET
        else:
            playlist_item_id = self.playlist_item_id

        now_playing_queue: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.now_playing_queue, Unset):
            now_playing_queue = UNSET
        elif isinstance(self.now_playing_queue, list):
            now_playing_queue = []
            for now_playing_queue_type_0_item_data in self.now_playing_queue:
                now_playing_queue_type_0_item = now_playing_queue_type_0_item_data.to_dict()
                now_playing_queue.append(now_playing_queue_type_0_item)

        else:
            now_playing_queue = self.now_playing_queue

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item is not UNSET:
            field_dict["Item"] = item
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if session_id is not UNSET:
            field_dict["SessionId"] = session_id
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if failed is not UNSET:
            field_dict["Failed"] = failed
        if next_media_type is not UNSET:
            field_dict["NextMediaType"] = next_media_type
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if now_playing_queue is not UNSET:
            field_dict["NowPlayingQueue"] = now_playing_queue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto
        from ..models.queue_item import QueueItem

        d = src_dict.copy()

        def _parse_item(data: object) -> Union["BaseItemDto", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_1 = BaseItemDto.from_dict(data)

                return item_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemDto", None, Unset], data)

        item = _parse_item(d.pop("Item", UNSET))

        item_id = d.pop("ItemId", UNSET)

        def _parse_session_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        session_id = _parse_session_id(d.pop("SessionId", UNSET))

        def _parse_media_source_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        media_source_id = _parse_media_source_id(d.pop("MediaSourceId", UNSET))

        def _parse_position_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position_ticks = _parse_position_ticks(d.pop("PositionTicks", UNSET))

        def _parse_live_stream_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        live_stream_id = _parse_live_stream_id(d.pop("LiveStreamId", UNSET))

        def _parse_play_session_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        play_session_id = _parse_play_session_id(d.pop("PlaySessionId", UNSET))

        failed = d.pop("Failed", UNSET)

        def _parse_next_media_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_media_type = _parse_next_media_type(d.pop("NextMediaType", UNSET))

        def _parse_playlist_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        playlist_item_id = _parse_playlist_item_id(d.pop("PlaylistItemId", UNSET))

        def _parse_now_playing_queue(data: object) -> Union[List["QueueItem"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                now_playing_queue_type_0 = []
                _now_playing_queue_type_0 = data
                for now_playing_queue_type_0_item_data in _now_playing_queue_type_0:
                    now_playing_queue_type_0_item = QueueItem.from_dict(now_playing_queue_type_0_item_data)

                    now_playing_queue_type_0.append(now_playing_queue_type_0_item)

                return now_playing_queue_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["QueueItem"], None, Unset], data)

        now_playing_queue = _parse_now_playing_queue(d.pop("NowPlayingQueue", UNSET))

        playback_stop_info = cls(
            item=item,
            item_id=item_id,
            session_id=session_id,
            media_source_id=media_source_id,
            position_ticks=position_ticks,
            live_stream_id=live_stream_id,
            play_session_id=play_session_id,
            failed=failed,
            next_media_type=next_media_type,
            playlist_item_id=playlist_item_id,
            now_playing_queue=now_playing_queue,
        )

        return playback_stop_info
