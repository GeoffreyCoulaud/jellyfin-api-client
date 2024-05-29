from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast
from typing import List
from ..models.media_protocol import MediaProtocol
from typing import Union

if TYPE_CHECKING:
    from ..models.device_profile import DeviceProfile


T = TypeVar("T", bound="OpenLiveStreamDto")


@_attrs_define
class OpenLiveStreamDto:
    """Open live stream dto.

    Attributes:
        open_token (Union[None, Unset, str]): Gets or sets the open token.
        user_id (Union[None, Unset, str]): Gets or sets the user id.
        play_session_id (Union[None, Unset, str]): Gets or sets the play session id.
        max_streaming_bitrate (Union[None, Unset, int]): Gets or sets the max streaming bitrate.
        start_time_ticks (Union[None, Unset, int]): Gets or sets the start time in ticks.
        audio_stream_index (Union[None, Unset, int]): Gets or sets the audio stream index.
        subtitle_stream_index (Union[None, Unset, int]): Gets or sets the subtitle stream index.
        max_audio_channels (Union[None, Unset, int]): Gets or sets the max audio channels.
        item_id (Union[None, Unset, str]): Gets or sets the item id.
        enable_direct_play (Union[None, Unset, bool]): Gets or sets a value indicating whether to enable direct play.
        enable_direct_stream (Union[None, Unset, bool]): Gets or sets a value indicating whether to enale direct stream.
        device_profile (Union['DeviceProfile', None, Unset]): Gets or sets the device profile.
        direct_play_protocols (Union[Unset, List[MediaProtocol]]): Gets or sets the device play protocols.
    """

    open_token: Union[None, Unset, str] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    play_session_id: Union[None, Unset, str] = UNSET
    max_streaming_bitrate: Union[None, Unset, int] = UNSET
    start_time_ticks: Union[None, Unset, int] = UNSET
    audio_stream_index: Union[None, Unset, int] = UNSET
    subtitle_stream_index: Union[None, Unset, int] = UNSET
    max_audio_channels: Union[None, Unset, int] = UNSET
    item_id: Union[None, Unset, str] = UNSET
    enable_direct_play: Union[None, Unset, bool] = UNSET
    enable_direct_stream: Union[None, Unset, bool] = UNSET
    device_profile: Union["DeviceProfile", None, Unset] = UNSET
    direct_play_protocols: Union[Unset, List[MediaProtocol]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.device_profile import DeviceProfile

        open_token: Union[None, Unset, str]
        if isinstance(self.open_token, Unset):
            open_token = UNSET
        else:
            open_token = self.open_token

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        play_session_id: Union[None, Unset, str]
        if isinstance(self.play_session_id, Unset):
            play_session_id = UNSET
        else:
            play_session_id = self.play_session_id

        max_streaming_bitrate: Union[None, Unset, int]
        if isinstance(self.max_streaming_bitrate, Unset):
            max_streaming_bitrate = UNSET
        else:
            max_streaming_bitrate = self.max_streaming_bitrate

        start_time_ticks: Union[None, Unset, int]
        if isinstance(self.start_time_ticks, Unset):
            start_time_ticks = UNSET
        else:
            start_time_ticks = self.start_time_ticks

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

        max_audio_channels: Union[None, Unset, int]
        if isinstance(self.max_audio_channels, Unset):
            max_audio_channels = UNSET
        else:
            max_audio_channels = self.max_audio_channels

        item_id: Union[None, Unset, str]
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        else:
            item_id = self.item_id

        enable_direct_play: Union[None, Unset, bool]
        if isinstance(self.enable_direct_play, Unset):
            enable_direct_play = UNSET
        else:
            enable_direct_play = self.enable_direct_play

        enable_direct_stream: Union[None, Unset, bool]
        if isinstance(self.enable_direct_stream, Unset):
            enable_direct_stream = UNSET
        else:
            enable_direct_stream = self.enable_direct_stream

        device_profile: Union[Dict[str, Any], None, Unset]
        if isinstance(self.device_profile, Unset):
            device_profile = UNSET
        elif isinstance(self.device_profile, DeviceProfile):
            device_profile = self.device_profile.to_dict()
        else:
            device_profile = self.device_profile

        direct_play_protocols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.direct_play_protocols, Unset):
            direct_play_protocols = []
            for direct_play_protocols_item_data in self.direct_play_protocols:
                direct_play_protocols_item = direct_play_protocols_item_data.value
                direct_play_protocols.append(direct_play_protocols_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if open_token is not UNSET:
            field_dict["OpenToken"] = open_token
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if max_streaming_bitrate is not UNSET:
            field_dict["MaxStreamingBitrate"] = max_streaming_bitrate
        if start_time_ticks is not UNSET:
            field_dict["StartTimeTicks"] = start_time_ticks
        if audio_stream_index is not UNSET:
            field_dict["AudioStreamIndex"] = audio_stream_index
        if subtitle_stream_index is not UNSET:
            field_dict["SubtitleStreamIndex"] = subtitle_stream_index
        if max_audio_channels is not UNSET:
            field_dict["MaxAudioChannels"] = max_audio_channels
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if enable_direct_play is not UNSET:
            field_dict["EnableDirectPlay"] = enable_direct_play
        if enable_direct_stream is not UNSET:
            field_dict["EnableDirectStream"] = enable_direct_stream
        if device_profile is not UNSET:
            field_dict["DeviceProfile"] = device_profile
        if direct_play_protocols is not UNSET:
            field_dict["DirectPlayProtocols"] = direct_play_protocols

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_profile import DeviceProfile

        d = src_dict.copy()

        def _parse_open_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        open_token = _parse_open_token(d.pop("OpenToken", UNSET))

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("UserId", UNSET))

        def _parse_play_session_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        play_session_id = _parse_play_session_id(d.pop("PlaySessionId", UNSET))

        def _parse_max_streaming_bitrate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_streaming_bitrate = _parse_max_streaming_bitrate(
            d.pop("MaxStreamingBitrate", UNSET)
        )

        def _parse_start_time_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        start_time_ticks = _parse_start_time_ticks(d.pop("StartTimeTicks", UNSET))

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

        def _parse_max_audio_channels(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_audio_channels = _parse_max_audio_channels(d.pop("MaxAudioChannels", UNSET))

        def _parse_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_id = _parse_item_id(d.pop("ItemId", UNSET))

        def _parse_enable_direct_play(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_direct_play = _parse_enable_direct_play(d.pop("EnableDirectPlay", UNSET))

        def _parse_enable_direct_stream(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_direct_stream = _parse_enable_direct_stream(
            d.pop("EnableDirectStream", UNSET)
        )

        def _parse_device_profile(data: object) -> Union["DeviceProfile", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_profile_type_1 = DeviceProfile.from_dict(data)

                return device_profile_type_1
            except:  # noqa: E722
                pass
            return cast(Union["DeviceProfile", None, Unset], data)

        device_profile = _parse_device_profile(d.pop("DeviceProfile", UNSET))

        direct_play_protocols = []
        _direct_play_protocols = d.pop("DirectPlayProtocols", UNSET)
        for direct_play_protocols_item_data in _direct_play_protocols or []:
            direct_play_protocols_item = MediaProtocol(direct_play_protocols_item_data)

            direct_play_protocols.append(direct_play_protocols_item)

        open_live_stream_dto = cls(
            open_token=open_token,
            user_id=user_id,
            play_session_id=play_session_id,
            max_streaming_bitrate=max_streaming_bitrate,
            start_time_ticks=start_time_ticks,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            max_audio_channels=max_audio_channels,
            item_id=item_id,
            enable_direct_play=enable_direct_play,
            enable_direct_stream=enable_direct_stream,
            device_profile=device_profile,
            direct_play_protocols=direct_play_protocols,
        )

        return open_live_stream_dto
