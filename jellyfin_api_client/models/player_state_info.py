from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from ..models.playback_order import PlaybackOrder
from typing import cast, Union
from ..models.player_state_info_play_method import PlayerStateInfoPlayMethod
from ..models.repeat_mode import RepeatMode


T = TypeVar("T", bound="PlayerStateInfo")


@_attrs_define
class PlayerStateInfo:
    """
    Attributes:
        position_ticks (Union[None, Unset, int]): Gets or sets the now playing position ticks.
        can_seek (Union[Unset, bool]): Gets or sets a value indicating whether this instance can seek.
        is_paused (Union[Unset, bool]): Gets or sets a value indicating whether this instance is paused.
        is_muted (Union[Unset, bool]): Gets or sets a value indicating whether this instance is muted.
        volume_level (Union[None, Unset, int]): Gets or sets the volume level.
        audio_stream_index (Union[None, Unset, int]): Gets or sets the index of the now playing audio stream.
        subtitle_stream_index (Union[None, Unset, int]): Gets or sets the index of the now playing subtitle stream.
        media_source_id (Union[None, Unset, str]): Gets or sets the now playing media version identifier.
        play_method (Union[Unset, PlayerStateInfoPlayMethod]): Gets or sets the play method.
        repeat_mode (Union[Unset, RepeatMode]):
        playback_order (Union[Unset, PlaybackOrder]): Enum PlaybackOrder.
        live_stream_id (Union[None, Unset, str]): Gets or sets the now playing live stream identifier.
    """

    position_ticks: Union[None, Unset, int] = UNSET
    can_seek: Union[Unset, bool] = UNSET
    is_paused: Union[Unset, bool] = UNSET
    is_muted: Union[Unset, bool] = UNSET
    volume_level: Union[None, Unset, int] = UNSET
    audio_stream_index: Union[None, Unset, int] = UNSET
    subtitle_stream_index: Union[None, Unset, int] = UNSET
    media_source_id: Union[None, Unset, str] = UNSET
    play_method: Union[Unset, PlayerStateInfoPlayMethod] = UNSET
    repeat_mode: Union[Unset, RepeatMode] = UNSET
    playback_order: Union[Unset, PlaybackOrder] = UNSET
    live_stream_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        position_ticks: Union[None, Unset, int]
        if isinstance(self.position_ticks, Unset):
            position_ticks = UNSET
        else:
            position_ticks = self.position_ticks

        can_seek = self.can_seek

        is_paused = self.is_paused

        is_muted = self.is_muted

        volume_level: Union[None, Unset, int]
        if isinstance(self.volume_level, Unset):
            volume_level = UNSET
        else:
            volume_level = self.volume_level

        audio_stream_index: Union[None, Unset, int]
        if isinstance(self.audio_stream_index, Unset):
            audio_stream_index = UNSET
        else:
            audio_stream_index = self.audio_stream_index

        subtitle_stream_index: Union[None, Unset, int]
        if isinstance(self.subtitle_stream_index, Unset):
            subtitle_stream_index = UNSET
        else:
            subtitle_stream_index = self.subtitle_stream_index

        media_source_id: Union[None, Unset, str]
        if isinstance(self.media_source_id, Unset):
            media_source_id = UNSET
        else:
            media_source_id = self.media_source_id

        play_method: Union[Unset, str] = UNSET
        if not isinstance(self.play_method, Unset):
            play_method = self.play_method.value

        repeat_mode: Union[Unset, str] = UNSET
        if not isinstance(self.repeat_mode, Unset):
            repeat_mode = self.repeat_mode.value

        playback_order: Union[Unset, str] = UNSET
        if not isinstance(self.playback_order, Unset):
            playback_order = self.playback_order.value

        live_stream_id: Union[None, Unset, str]
        if isinstance(self.live_stream_id, Unset):
            live_stream_id = UNSET
        else:
            live_stream_id = self.live_stream_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks
        if can_seek is not UNSET:
            field_dict["CanSeek"] = can_seek
        if is_paused is not UNSET:
            field_dict["IsPaused"] = is_paused
        if is_muted is not UNSET:
            field_dict["IsMuted"] = is_muted
        if volume_level is not UNSET:
            field_dict["VolumeLevel"] = volume_level
        if audio_stream_index is not UNSET:
            field_dict["AudioStreamIndex"] = audio_stream_index
        if subtitle_stream_index is not UNSET:
            field_dict["SubtitleStreamIndex"] = subtitle_stream_index
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if play_method is not UNSET:
            field_dict["PlayMethod"] = play_method
        if repeat_mode is not UNSET:
            field_dict["RepeatMode"] = repeat_mode
        if playback_order is not UNSET:
            field_dict["PlaybackOrder"] = playback_order
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_position_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position_ticks = _parse_position_ticks(d.pop("PositionTicks", UNSET))

        can_seek = d.pop("CanSeek", UNSET)

        is_paused = d.pop("IsPaused", UNSET)

        is_muted = d.pop("IsMuted", UNSET)

        def _parse_volume_level(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        volume_level = _parse_volume_level(d.pop("VolumeLevel", UNSET))

        def _parse_audio_stream_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        audio_stream_index = _parse_audio_stream_index(d.pop("AudioStreamIndex", UNSET))

        def _parse_subtitle_stream_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        subtitle_stream_index = _parse_subtitle_stream_index(
            d.pop("SubtitleStreamIndex", UNSET)
        )

        def _parse_media_source_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        media_source_id = _parse_media_source_id(d.pop("MediaSourceId", UNSET))

        _play_method = d.pop("PlayMethod", UNSET)
        play_method: Union[Unset, PlayerStateInfoPlayMethod]
        if isinstance(_play_method, Unset):
            play_method = UNSET
        else:
            play_method = PlayerStateInfoPlayMethod(_play_method)

        _repeat_mode = d.pop("RepeatMode", UNSET)
        repeat_mode: Union[Unset, RepeatMode]
        if isinstance(_repeat_mode, Unset):
            repeat_mode = UNSET
        else:
            repeat_mode = RepeatMode(_repeat_mode)

        _playback_order = d.pop("PlaybackOrder", UNSET)
        playback_order: Union[Unset, PlaybackOrder]
        if isinstance(_playback_order, Unset):
            playback_order = UNSET
        else:
            playback_order = PlaybackOrder(_playback_order)

        def _parse_live_stream_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        live_stream_id = _parse_live_stream_id(d.pop("LiveStreamId", UNSET))

        player_state_info = cls(
            position_ticks=position_ticks,
            can_seek=can_seek,
            is_paused=is_paused,
            is_muted=is_muted,
            volume_level=volume_level,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            media_source_id=media_source_id,
            play_method=play_method,
            repeat_mode=repeat_mode,
            playback_order=playback_order,
            live_stream_id=live_stream_id,
        )

        return player_state_info
