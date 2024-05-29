from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.device_profile import DeviceProfile


T = TypeVar("T", bound="PlaybackInfoDto")


@_attrs_define
class PlaybackInfoDto:
    """Plabyback info dto.

    Attributes:
        user_id (Union[None, Unset, str]): Gets or sets the playback userId.
        max_streaming_bitrate (Union[None, Unset, int]): Gets or sets the max streaming bitrate.
        start_time_ticks (Union[None, Unset, int]): Gets or sets the start time in ticks.
        audio_stream_index (Union[None, Unset, int]): Gets or sets the audio stream index.
        subtitle_stream_index (Union[None, Unset, int]): Gets or sets the subtitle stream index.
        max_audio_channels (Union[None, Unset, int]): Gets or sets the max audio channels.
        media_source_id (Union[None, Unset, str]): Gets or sets the media source id.
        live_stream_id (Union[None, Unset, str]): Gets or sets the live stream id.
        device_profile (Union['DeviceProfile', None, Unset]): A MediaBrowser.Model.Dlna.DeviceProfile represents a set
            of metadata which determines which content a certain device is able to play.
            <br />
            Specifically, it defines the supported <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
            <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including
            codec profiles and levels)
            the device is able to direct play (without transcoding or remuxing),
            as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
            transcode to</see> in case it isn't.
        enable_direct_play (Union[None, Unset, bool]): Gets or sets a value indicating whether to enable direct play.
        enable_direct_stream (Union[None, Unset, bool]): Gets or sets a value indicating whether to enable direct
            stream.
        enable_transcoding (Union[None, Unset, bool]): Gets or sets a value indicating whether to enable transcoding.
        allow_video_stream_copy (Union[None, Unset, bool]): Gets or sets a value indicating whether to enable video
            stream copy.
        allow_audio_stream_copy (Union[None, Unset, bool]): Gets or sets a value indicating whether to allow audio
            stream copy.
        auto_open_live_stream (Union[None, Unset, bool]): Gets or sets a value indicating whether to auto open the live
            stream.
    """

    user_id: Union[None, Unset, str] = UNSET
    max_streaming_bitrate: Union[None, Unset, int] = UNSET
    start_time_ticks: Union[None, Unset, int] = UNSET
    audio_stream_index: Union[None, Unset, int] = UNSET
    subtitle_stream_index: Union[None, Unset, int] = UNSET
    max_audio_channels: Union[None, Unset, int] = UNSET
    media_source_id: Union[None, Unset, str] = UNSET
    live_stream_id: Union[None, Unset, str] = UNSET
    device_profile: Union["DeviceProfile", None, Unset] = UNSET
    enable_direct_play: Union[None, Unset, bool] = UNSET
    enable_direct_stream: Union[None, Unset, bool] = UNSET
    enable_transcoding: Union[None, Unset, bool] = UNSET
    allow_video_stream_copy: Union[None, Unset, bool] = UNSET
    allow_audio_stream_copy: Union[None, Unset, bool] = UNSET
    auto_open_live_stream: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.device_profile import DeviceProfile

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

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

        media_source_id: Union[None, Unset, str]
        if isinstance(self.media_source_id, Unset):
            media_source_id = UNSET
        else:
            media_source_id = self.media_source_id

        live_stream_id: Union[None, Unset, str]
        if isinstance(self.live_stream_id, Unset):
            live_stream_id = UNSET
        else:
            live_stream_id = self.live_stream_id

        device_profile: Union[Dict[str, Any], None, Unset]
        if isinstance(self.device_profile, Unset):
            device_profile = UNSET
        elif isinstance(self.device_profile, DeviceProfile):
            device_profile = self.device_profile.to_dict()
        else:
            device_profile = self.device_profile

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

        enable_transcoding: Union[None, Unset, bool]
        if isinstance(self.enable_transcoding, Unset):
            enable_transcoding = UNSET
        else:
            enable_transcoding = self.enable_transcoding

        allow_video_stream_copy: Union[None, Unset, bool]
        if isinstance(self.allow_video_stream_copy, Unset):
            allow_video_stream_copy = UNSET
        else:
            allow_video_stream_copy = self.allow_video_stream_copy

        allow_audio_stream_copy: Union[None, Unset, bool]
        if isinstance(self.allow_audio_stream_copy, Unset):
            allow_audio_stream_copy = UNSET
        else:
            allow_audio_stream_copy = self.allow_audio_stream_copy

        auto_open_live_stream: Union[None, Unset, bool]
        if isinstance(self.auto_open_live_stream, Unset):
            auto_open_live_stream = UNSET
        else:
            auto_open_live_stream = self.auto_open_live_stream

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
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
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id
        if device_profile is not UNSET:
            field_dict["DeviceProfile"] = device_profile
        if enable_direct_play is not UNSET:
            field_dict["EnableDirectPlay"] = enable_direct_play
        if enable_direct_stream is not UNSET:
            field_dict["EnableDirectStream"] = enable_direct_stream
        if enable_transcoding is not UNSET:
            field_dict["EnableTranscoding"] = enable_transcoding
        if allow_video_stream_copy is not UNSET:
            field_dict["AllowVideoStreamCopy"] = allow_video_stream_copy
        if allow_audio_stream_copy is not UNSET:
            field_dict["AllowAudioStreamCopy"] = allow_audio_stream_copy
        if auto_open_live_stream is not UNSET:
            field_dict["AutoOpenLiveStream"] = auto_open_live_stream

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_profile import DeviceProfile

        d = src_dict.copy()

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("UserId", UNSET))

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

        def _parse_media_source_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        media_source_id = _parse_media_source_id(d.pop("MediaSourceId", UNSET))

        def _parse_live_stream_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        live_stream_id = _parse_live_stream_id(d.pop("LiveStreamId", UNSET))

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

        def _parse_enable_transcoding(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_transcoding = _parse_enable_transcoding(
            d.pop("EnableTranscoding", UNSET)
        )

        def _parse_allow_video_stream_copy(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        allow_video_stream_copy = _parse_allow_video_stream_copy(
            d.pop("AllowVideoStreamCopy", UNSET)
        )

        def _parse_allow_audio_stream_copy(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        allow_audio_stream_copy = _parse_allow_audio_stream_copy(
            d.pop("AllowAudioStreamCopy", UNSET)
        )

        def _parse_auto_open_live_stream(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        auto_open_live_stream = _parse_auto_open_live_stream(
            d.pop("AutoOpenLiveStream", UNSET)
        )

        playback_info_dto = cls(
            user_id=user_id,
            max_streaming_bitrate=max_streaming_bitrate,
            start_time_ticks=start_time_ticks,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            max_audio_channels=max_audio_channels,
            media_source_id=media_source_id,
            live_stream_id=live_stream_id,
            device_profile=device_profile,
            enable_direct_play=enable_direct_play,
            enable_direct_stream=enable_direct_stream,
            enable_transcoding=enable_transcoding,
            allow_video_stream_copy=allow_video_stream_copy,
            allow_audio_stream_copy=allow_audio_stream_copy,
            auto_open_live_stream=auto_open_live_stream,
        )

        return playback_info_dto
