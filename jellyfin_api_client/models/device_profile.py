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
    from ..models.direct_play_profile import DirectPlayProfile
    from ..models.transcoding_profile import TranscodingProfile
    from ..models.codec_profile import CodecProfile
    from ..models.subtitle_profile import SubtitleProfile
    from ..models.container_profile import ContainerProfile


T = TypeVar("T", bound="DeviceProfile")


@_attrs_define
class DeviceProfile:
    """A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata which determines which content a certain device
    is able to play.
    <br />
    Specifically, it defines the supported <see
    cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
    <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including codec
    profiles and levels)
    the device is able to direct play (without transcoding or remuxing),
    as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
    transcode to</see> in case it isn't.

        Attributes:
            name (Union[None, Unset, str]): Gets or sets the name of this device profile.
            id (Union[None, Unset, str]): Gets or sets the Id.
            max_streaming_bitrate (Union[None, Unset, int]): Gets or sets the maximum allowed bitrate for all streamed
                content.
            max_static_bitrate (Union[None, Unset, int]): Gets or sets the maximum allowed bitrate for statically streamed
                content (= direct played files).
            music_streaming_transcoding_bitrate (Union[None, Unset, int]): Gets or sets the maximum allowed bitrate for
                transcoded music streams.
            max_static_music_bitrate (Union[None, Unset, int]): Gets or sets the maximum allowed bitrate for statically
                streamed (= direct played) music files.
            direct_play_profiles (Union[Unset, List['DirectPlayProfile']]): Gets or sets the direct play profiles.
            transcoding_profiles (Union[Unset, List['TranscodingProfile']]): Gets or sets the transcoding profiles.
            container_profiles (Union[Unset, List['ContainerProfile']]): Gets or sets the container profiles.
            codec_profiles (Union[Unset, List['CodecProfile']]): Gets or sets the codec profiles.
            subtitle_profiles (Union[Unset, List['SubtitleProfile']]): Gets or sets the subtitle profiles.
    """

    name: Union[None, Unset, str] = UNSET
    id: Union[None, Unset, str] = UNSET
    max_streaming_bitrate: Union[None, Unset, int] = UNSET
    max_static_bitrate: Union[None, Unset, int] = UNSET
    music_streaming_transcoding_bitrate: Union[None, Unset, int] = UNSET
    max_static_music_bitrate: Union[None, Unset, int] = UNSET
    direct_play_profiles: Union[Unset, List["DirectPlayProfile"]] = UNSET
    transcoding_profiles: Union[Unset, List["TranscodingProfile"]] = UNSET
    container_profiles: Union[Unset, List["ContainerProfile"]] = UNSET
    codec_profiles: Union[Unset, List["CodecProfile"]] = UNSET
    subtitle_profiles: Union[Unset, List["SubtitleProfile"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.direct_play_profile import DirectPlayProfile
        from ..models.transcoding_profile import TranscodingProfile
        from ..models.codec_profile import CodecProfile
        from ..models.subtitle_profile import SubtitleProfile
        from ..models.container_profile import ContainerProfile

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        max_streaming_bitrate: Union[None, Unset, int]
        if isinstance(self.max_streaming_bitrate, Unset):
            max_streaming_bitrate = UNSET
        else:
            max_streaming_bitrate = self.max_streaming_bitrate

        max_static_bitrate: Union[None, Unset, int]
        if isinstance(self.max_static_bitrate, Unset):
            max_static_bitrate = UNSET
        else:
            max_static_bitrate = self.max_static_bitrate

        music_streaming_transcoding_bitrate: Union[None, Unset, int]
        if isinstance(self.music_streaming_transcoding_bitrate, Unset):
            music_streaming_transcoding_bitrate = UNSET
        else:
            music_streaming_transcoding_bitrate = self.music_streaming_transcoding_bitrate

        max_static_music_bitrate: Union[None, Unset, int]
        if isinstance(self.max_static_music_bitrate, Unset):
            max_static_music_bitrate = UNSET
        else:
            max_static_music_bitrate = self.max_static_music_bitrate

        direct_play_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.direct_play_profiles, Unset):
            direct_play_profiles = []
            for direct_play_profiles_item_data in self.direct_play_profiles:
                direct_play_profiles_item = direct_play_profiles_item_data.to_dict()
                direct_play_profiles.append(direct_play_profiles_item)

        transcoding_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transcoding_profiles, Unset):
            transcoding_profiles = []
            for transcoding_profiles_item_data in self.transcoding_profiles:
                transcoding_profiles_item = transcoding_profiles_item_data.to_dict()
                transcoding_profiles.append(transcoding_profiles_item)

        container_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.container_profiles, Unset):
            container_profiles = []
            for container_profiles_item_data in self.container_profiles:
                container_profiles_item = container_profiles_item_data.to_dict()
                container_profiles.append(container_profiles_item)

        codec_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.codec_profiles, Unset):
            codec_profiles = []
            for codec_profiles_item_data in self.codec_profiles:
                codec_profiles_item = codec_profiles_item_data.to_dict()
                codec_profiles.append(codec_profiles_item)

        subtitle_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subtitle_profiles, Unset):
            subtitle_profiles = []
            for subtitle_profiles_item_data in self.subtitle_profiles:
                subtitle_profiles_item = subtitle_profiles_item_data.to_dict()
                subtitle_profiles.append(subtitle_profiles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id
        if max_streaming_bitrate is not UNSET:
            field_dict["MaxStreamingBitrate"] = max_streaming_bitrate
        if max_static_bitrate is not UNSET:
            field_dict["MaxStaticBitrate"] = max_static_bitrate
        if music_streaming_transcoding_bitrate is not UNSET:
            field_dict["MusicStreamingTranscodingBitrate"] = music_streaming_transcoding_bitrate
        if max_static_music_bitrate is not UNSET:
            field_dict["MaxStaticMusicBitrate"] = max_static_music_bitrate
        if direct_play_profiles is not UNSET:
            field_dict["DirectPlayProfiles"] = direct_play_profiles
        if transcoding_profiles is not UNSET:
            field_dict["TranscodingProfiles"] = transcoding_profiles
        if container_profiles is not UNSET:
            field_dict["ContainerProfiles"] = container_profiles
        if codec_profiles is not UNSET:
            field_dict["CodecProfiles"] = codec_profiles
        if subtitle_profiles is not UNSET:
            field_dict["SubtitleProfiles"] = subtitle_profiles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.direct_play_profile import DirectPlayProfile
        from ..models.transcoding_profile import TranscodingProfile
        from ..models.codec_profile import CodecProfile
        from ..models.subtitle_profile import SubtitleProfile
        from ..models.container_profile import ContainerProfile

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_max_streaming_bitrate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_streaming_bitrate = _parse_max_streaming_bitrate(d.pop("MaxStreamingBitrate", UNSET))

        def _parse_max_static_bitrate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_static_bitrate = _parse_max_static_bitrate(d.pop("MaxStaticBitrate", UNSET))

        def _parse_music_streaming_transcoding_bitrate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        music_streaming_transcoding_bitrate = _parse_music_streaming_transcoding_bitrate(
            d.pop("MusicStreamingTranscodingBitrate", UNSET)
        )

        def _parse_max_static_music_bitrate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_static_music_bitrate = _parse_max_static_music_bitrate(d.pop("MaxStaticMusicBitrate", UNSET))

        direct_play_profiles = []
        _direct_play_profiles = d.pop("DirectPlayProfiles", UNSET)
        for direct_play_profiles_item_data in _direct_play_profiles or []:
            direct_play_profiles_item = DirectPlayProfile.from_dict(direct_play_profiles_item_data)

            direct_play_profiles.append(direct_play_profiles_item)

        transcoding_profiles = []
        _transcoding_profiles = d.pop("TranscodingProfiles", UNSET)
        for transcoding_profiles_item_data in _transcoding_profiles or []:
            transcoding_profiles_item = TranscodingProfile.from_dict(transcoding_profiles_item_data)

            transcoding_profiles.append(transcoding_profiles_item)

        container_profiles = []
        _container_profiles = d.pop("ContainerProfiles", UNSET)
        for container_profiles_item_data in _container_profiles or []:
            container_profiles_item = ContainerProfile.from_dict(container_profiles_item_data)

            container_profiles.append(container_profiles_item)

        codec_profiles = []
        _codec_profiles = d.pop("CodecProfiles", UNSET)
        for codec_profiles_item_data in _codec_profiles or []:
            codec_profiles_item = CodecProfile.from_dict(codec_profiles_item_data)

            codec_profiles.append(codec_profiles_item)

        subtitle_profiles = []
        _subtitle_profiles = d.pop("SubtitleProfiles", UNSET)
        for subtitle_profiles_item_data in _subtitle_profiles or []:
            subtitle_profiles_item = SubtitleProfile.from_dict(subtitle_profiles_item_data)

            subtitle_profiles.append(subtitle_profiles_item)

        device_profile = cls(
            name=name,
            id=id,
            max_streaming_bitrate=max_streaming_bitrate,
            max_static_bitrate=max_static_bitrate,
            music_streaming_transcoding_bitrate=music_streaming_transcoding_bitrate,
            max_static_music_bitrate=max_static_music_bitrate,
            direct_play_profiles=direct_play_profiles,
            transcoding_profiles=transcoding_profiles,
            container_profiles=container_profiles,
            codec_profiles=codec_profiles,
            subtitle_profiles=subtitle_profiles,
        )

        return device_profile
