from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union
from ..models.transcoding_info_hardware_acceleration_type import (
    TranscodingInfoHardwareAccelerationType,
)
from ..models.transcoding_info_transcode_reasons import TranscodingInfoTranscodeReasons


T = TypeVar("T", bound="TranscodingInfo")


@_attrs_define
class TranscodingInfo:
    """
    Attributes:
        audio_codec (Union[None, Unset, str]):
        video_codec (Union[None, Unset, str]):
        container (Union[None, Unset, str]):
        is_video_direct (Union[Unset, bool]):
        is_audio_direct (Union[Unset, bool]):
        bitrate (Union[None, Unset, int]):
        framerate (Union[None, Unset, float]):
        completion_percentage (Union[None, Unset, float]):
        width (Union[None, Unset, int]):
        height (Union[None, Unset, int]):
        audio_channels (Union[None, Unset, int]):
        hardware_acceleration_type (Union[Unset, TranscodingInfoHardwareAccelerationType]):
        transcode_reasons (Union[Unset, TranscodingInfoTranscodeReasons]):
    """

    audio_codec: Union[None, Unset, str] = UNSET
    video_codec: Union[None, Unset, str] = UNSET
    container: Union[None, Unset, str] = UNSET
    is_video_direct: Union[Unset, bool] = UNSET
    is_audio_direct: Union[Unset, bool] = UNSET
    bitrate: Union[None, Unset, int] = UNSET
    framerate: Union[None, Unset, float] = UNSET
    completion_percentage: Union[None, Unset, float] = UNSET
    width: Union[None, Unset, int] = UNSET
    height: Union[None, Unset, int] = UNSET
    audio_channels: Union[None, Unset, int] = UNSET
    hardware_acceleration_type: Union[
        Unset, TranscodingInfoHardwareAccelerationType
    ] = UNSET
    transcode_reasons: Union[Unset, TranscodingInfoTranscodeReasons] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        audio_codec: Union[None, Unset, str]
        if isinstance(self.audio_codec, Unset):
            audio_codec = UNSET
        else:
            audio_codec = self.audio_codec

        video_codec: Union[None, Unset, str]
        if isinstance(self.video_codec, Unset):
            video_codec = UNSET
        else:
            video_codec = self.video_codec

        container: Union[None, Unset, str]
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        is_video_direct = self.is_video_direct

        is_audio_direct = self.is_audio_direct

        bitrate: Union[None, Unset, int]
        if isinstance(self.bitrate, Unset):
            bitrate = UNSET
        else:
            bitrate = self.bitrate

        framerate: Union[None, Unset, float]
        if isinstance(self.framerate, Unset):
            framerate = UNSET
        else:
            framerate = self.framerate

        completion_percentage: Union[None, Unset, float]
        if isinstance(self.completion_percentage, Unset):
            completion_percentage = UNSET
        else:
            completion_percentage = self.completion_percentage

        width: Union[None, Unset, int]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: Union[None, Unset, int]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        audio_channels: Union[None, Unset, int]
        if isinstance(self.audio_channels, Unset):
            audio_channels = UNSET
        else:
            audio_channels = self.audio_channels

        hardware_acceleration_type: Union[Unset, str] = UNSET
        if not isinstance(self.hardware_acceleration_type, Unset):
            hardware_acceleration_type = self.hardware_acceleration_type.value

        transcode_reasons: Union[Unset, str] = UNSET
        if not isinstance(self.transcode_reasons, Unset):
            transcode_reasons = self.transcode_reasons.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if audio_codec is not UNSET:
            field_dict["AudioCodec"] = audio_codec
        if video_codec is not UNSET:
            field_dict["VideoCodec"] = video_codec
        if container is not UNSET:
            field_dict["Container"] = container
        if is_video_direct is not UNSET:
            field_dict["IsVideoDirect"] = is_video_direct
        if is_audio_direct is not UNSET:
            field_dict["IsAudioDirect"] = is_audio_direct
        if bitrate is not UNSET:
            field_dict["Bitrate"] = bitrate
        if framerate is not UNSET:
            field_dict["Framerate"] = framerate
        if completion_percentage is not UNSET:
            field_dict["CompletionPercentage"] = completion_percentage
        if width is not UNSET:
            field_dict["Width"] = width
        if height is not UNSET:
            field_dict["Height"] = height
        if audio_channels is not UNSET:
            field_dict["AudioChannels"] = audio_channels
        if hardware_acceleration_type is not UNSET:
            field_dict["HardwareAccelerationType"] = hardware_acceleration_type
        if transcode_reasons is not UNSET:
            field_dict["TranscodeReasons"] = transcode_reasons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_audio_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_codec = _parse_audio_codec(d.pop("AudioCodec", UNSET))

        def _parse_video_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        video_codec = _parse_video_codec(d.pop("VideoCodec", UNSET))

        def _parse_container(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        container = _parse_container(d.pop("Container", UNSET))

        is_video_direct = d.pop("IsVideoDirect", UNSET)

        is_audio_direct = d.pop("IsAudioDirect", UNSET)

        def _parse_bitrate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bitrate = _parse_bitrate(d.pop("Bitrate", UNSET))

        def _parse_framerate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        framerate = _parse_framerate(d.pop("Framerate", UNSET))

        def _parse_completion_percentage(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        completion_percentage = _parse_completion_percentage(
            d.pop("CompletionPercentage", UNSET)
        )

        def _parse_width(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        width = _parse_width(d.pop("Width", UNSET))

        def _parse_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        height = _parse_height(d.pop("Height", UNSET))

        def _parse_audio_channels(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        audio_channels = _parse_audio_channels(d.pop("AudioChannels", UNSET))

        _hardware_acceleration_type = d.pop("HardwareAccelerationType", UNSET)
        hardware_acceleration_type: Union[
            Unset, TranscodingInfoHardwareAccelerationType
        ]
        if isinstance(_hardware_acceleration_type, Unset):
            hardware_acceleration_type = UNSET
        else:
            hardware_acceleration_type = TranscodingInfoHardwareAccelerationType(
                _hardware_acceleration_type
            )

        _transcode_reasons = d.pop("TranscodeReasons", UNSET)
        transcode_reasons: Union[Unset, TranscodingInfoTranscodeReasons]
        if isinstance(_transcode_reasons, Unset):
            transcode_reasons = UNSET
        else:
            transcode_reasons = TranscodingInfoTranscodeReasons(_transcode_reasons)

        transcoding_info = cls(
            audio_codec=audio_codec,
            video_codec=video_codec,
            container=container,
            is_video_direct=is_video_direct,
            is_audio_direct=is_audio_direct,
            bitrate=bitrate,
            framerate=framerate,
            completion_percentage=completion_percentage,
            width=width,
            height=height,
            audio_channels=audio_channels,
            hardware_acceleration_type=hardware_acceleration_type,
            transcode_reasons=transcode_reasons,
        )

        return transcoding_info
