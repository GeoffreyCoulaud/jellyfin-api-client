from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.media_stream_delivery_method import MediaStreamDeliveryMethod
from typing import cast, Union
from ..models.media_stream_type import MediaStreamType
from ..types import UNSET, Unset
from typing import Union
from ..models.audio_spatial_format import AudioSpatialFormat
from ..models.video_range import VideoRange
from ..models.video_range_type import VideoRangeType


T = TypeVar("T", bound="MediaStream")


@_attrs_define
class MediaStream:
    """Class MediaStream.

    Attributes:
        codec (Union[None, Unset, str]): Gets or sets the codec.
        codec_tag (Union[None, Unset, str]): Gets or sets the codec tag.
        language (Union[None, Unset, str]): Gets or sets the language.
        color_range (Union[None, Unset, str]): Gets or sets the color range.
        color_space (Union[None, Unset, str]): Gets or sets the color space.
        color_transfer (Union[None, Unset, str]): Gets or sets the color transfer.
        color_primaries (Union[None, Unset, str]): Gets or sets the color primaries.
        dv_version_major (Union[None, Unset, int]): Gets or sets the Dolby Vision version major.
        dv_version_minor (Union[None, Unset, int]): Gets or sets the Dolby Vision version minor.
        dv_profile (Union[None, Unset, int]): Gets or sets the Dolby Vision profile.
        dv_level (Union[None, Unset, int]): Gets or sets the Dolby Vision level.
        rpu_present_flag (Union[None, Unset, int]): Gets or sets the Dolby Vision rpu present flag.
        el_present_flag (Union[None, Unset, int]): Gets or sets the Dolby Vision el present flag.
        bl_present_flag (Union[None, Unset, int]): Gets or sets the Dolby Vision bl present flag.
        dv_bl_signal_compatibility_id (Union[None, Unset, int]): Gets or sets the Dolby Vision bl signal compatibility
            id.
        comment (Union[None, Unset, str]): Gets or sets the comment.
        time_base (Union[None, Unset, str]): Gets or sets the time base.
        codec_time_base (Union[None, Unset, str]): Gets or sets the codec time base.
        title (Union[None, Unset, str]): Gets or sets the title.
        video_range (Union[Unset, VideoRange]): An enum representing video ranges.
        video_range_type (Union[Unset, VideoRangeType]): An enum representing types of video ranges.
        video_do_vi_title (Union[None, Unset, str]): Gets the video dovi title.
        audio_spatial_format (Union[Unset, AudioSpatialFormat]): An enum representing formats of spatial audio. Default:
            AudioSpatialFormat.NONE.
        localized_undefined (Union[None, Unset, str]):
        localized_default (Union[None, Unset, str]):
        localized_forced (Union[None, Unset, str]):
        localized_external (Union[None, Unset, str]):
        localized_hearing_impaired (Union[None, Unset, str]):
        display_title (Union[None, Unset, str]):
        nal_length_size (Union[None, Unset, str]):
        is_interlaced (Union[Unset, bool]): Gets or sets a value indicating whether this instance is interlaced.
        is_avc (Union[None, Unset, bool]):
        channel_layout (Union[None, Unset, str]): Gets or sets the channel layout.
        bit_rate (Union[None, Unset, int]): Gets or sets the bit rate.
        bit_depth (Union[None, Unset, int]): Gets or sets the bit depth.
        ref_frames (Union[None, Unset, int]): Gets or sets the reference frames.
        packet_length (Union[None, Unset, int]): Gets or sets the length of the packet.
        channels (Union[None, Unset, int]): Gets or sets the channels.
        sample_rate (Union[None, Unset, int]): Gets or sets the sample rate.
        is_default (Union[Unset, bool]): Gets or sets a value indicating whether this instance is default.
        is_forced (Union[Unset, bool]): Gets or sets a value indicating whether this instance is forced.
        is_hearing_impaired (Union[Unset, bool]): Gets or sets a value indicating whether this instance is for the
            hearing impaired.
        height (Union[None, Unset, int]): Gets or sets the height.
        width (Union[None, Unset, int]): Gets or sets the width.
        average_frame_rate (Union[None, Unset, float]): Gets or sets the average frame rate.
        real_frame_rate (Union[None, Unset, float]): Gets or sets the real frame rate.
        profile (Union[None, Unset, str]): Gets or sets the profile.
        type (Union[Unset, MediaStreamType]): Enum MediaStreamType.
        aspect_ratio (Union[None, Unset, str]): Gets or sets the aspect ratio.
        index (Union[Unset, int]): Gets or sets the index.
        score (Union[None, Unset, int]): Gets or sets the score.
        is_external (Union[Unset, bool]): Gets or sets a value indicating whether this instance is external.
        delivery_method (Union[Unset, MediaStreamDeliveryMethod]): Gets or sets the method.
        delivery_url (Union[None, Unset, str]): Gets or sets the delivery URL.
        is_external_url (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is external
            URL.
        is_text_subtitle_stream (Union[Unset, bool]):
        supports_external_stream (Union[Unset, bool]): Gets or sets a value indicating whether [supports external
            stream].
        path (Union[None, Unset, str]): Gets or sets the filename.
        pixel_format (Union[None, Unset, str]): Gets or sets the pixel format.
        level (Union[None, Unset, float]): Gets or sets the level.
        is_anamorphic (Union[None, Unset, bool]): Gets or sets whether this instance is anamorphic.
    """

    codec: Union[None, Unset, str] = UNSET
    codec_tag: Union[None, Unset, str] = UNSET
    language: Union[None, Unset, str] = UNSET
    color_range: Union[None, Unset, str] = UNSET
    color_space: Union[None, Unset, str] = UNSET
    color_transfer: Union[None, Unset, str] = UNSET
    color_primaries: Union[None, Unset, str] = UNSET
    dv_version_major: Union[None, Unset, int] = UNSET
    dv_version_minor: Union[None, Unset, int] = UNSET
    dv_profile: Union[None, Unset, int] = UNSET
    dv_level: Union[None, Unset, int] = UNSET
    rpu_present_flag: Union[None, Unset, int] = UNSET
    el_present_flag: Union[None, Unset, int] = UNSET
    bl_present_flag: Union[None, Unset, int] = UNSET
    dv_bl_signal_compatibility_id: Union[None, Unset, int] = UNSET
    comment: Union[None, Unset, str] = UNSET
    time_base: Union[None, Unset, str] = UNSET
    codec_time_base: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    video_range: Union[Unset, VideoRange] = UNSET
    video_range_type: Union[Unset, VideoRangeType] = UNSET
    video_do_vi_title: Union[None, Unset, str] = UNSET
    audio_spatial_format: Union[Unset, AudioSpatialFormat] = AudioSpatialFormat.NONE
    localized_undefined: Union[None, Unset, str] = UNSET
    localized_default: Union[None, Unset, str] = UNSET
    localized_forced: Union[None, Unset, str] = UNSET
    localized_external: Union[None, Unset, str] = UNSET
    localized_hearing_impaired: Union[None, Unset, str] = UNSET
    display_title: Union[None, Unset, str] = UNSET
    nal_length_size: Union[None, Unset, str] = UNSET
    is_interlaced: Union[Unset, bool] = UNSET
    is_avc: Union[None, Unset, bool] = UNSET
    channel_layout: Union[None, Unset, str] = UNSET
    bit_rate: Union[None, Unset, int] = UNSET
    bit_depth: Union[None, Unset, int] = UNSET
    ref_frames: Union[None, Unset, int] = UNSET
    packet_length: Union[None, Unset, int] = UNSET
    channels: Union[None, Unset, int] = UNSET
    sample_rate: Union[None, Unset, int] = UNSET
    is_default: Union[Unset, bool] = UNSET
    is_forced: Union[Unset, bool] = UNSET
    is_hearing_impaired: Union[Unset, bool] = UNSET
    height: Union[None, Unset, int] = UNSET
    width: Union[None, Unset, int] = UNSET
    average_frame_rate: Union[None, Unset, float] = UNSET
    real_frame_rate: Union[None, Unset, float] = UNSET
    profile: Union[None, Unset, str] = UNSET
    type: Union[Unset, MediaStreamType] = UNSET
    aspect_ratio: Union[None, Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    score: Union[None, Unset, int] = UNSET
    is_external: Union[Unset, bool] = UNSET
    delivery_method: Union[Unset, MediaStreamDeliveryMethod] = UNSET
    delivery_url: Union[None, Unset, str] = UNSET
    is_external_url: Union[None, Unset, bool] = UNSET
    is_text_subtitle_stream: Union[Unset, bool] = UNSET
    supports_external_stream: Union[Unset, bool] = UNSET
    path: Union[None, Unset, str] = UNSET
    pixel_format: Union[None, Unset, str] = UNSET
    level: Union[None, Unset, float] = UNSET
    is_anamorphic: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        codec: Union[None, Unset, str]
        if isinstance(self.codec, Unset):
            codec = UNSET
        else:
            codec = self.codec

        codec_tag: Union[None, Unset, str]
        if isinstance(self.codec_tag, Unset):
            codec_tag = UNSET
        else:
            codec_tag = self.codec_tag

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        color_range: Union[None, Unset, str]
        if isinstance(self.color_range, Unset):
            color_range = UNSET
        else:
            color_range = self.color_range

        color_space: Union[None, Unset, str]
        if isinstance(self.color_space, Unset):
            color_space = UNSET
        else:
            color_space = self.color_space

        color_transfer: Union[None, Unset, str]
        if isinstance(self.color_transfer, Unset):
            color_transfer = UNSET
        else:
            color_transfer = self.color_transfer

        color_primaries: Union[None, Unset, str]
        if isinstance(self.color_primaries, Unset):
            color_primaries = UNSET
        else:
            color_primaries = self.color_primaries

        dv_version_major: Union[None, Unset, int]
        if isinstance(self.dv_version_major, Unset):
            dv_version_major = UNSET
        else:
            dv_version_major = self.dv_version_major

        dv_version_minor: Union[None, Unset, int]
        if isinstance(self.dv_version_minor, Unset):
            dv_version_minor = UNSET
        else:
            dv_version_minor = self.dv_version_minor

        dv_profile: Union[None, Unset, int]
        if isinstance(self.dv_profile, Unset):
            dv_profile = UNSET
        else:
            dv_profile = self.dv_profile

        dv_level: Union[None, Unset, int]
        if isinstance(self.dv_level, Unset):
            dv_level = UNSET
        else:
            dv_level = self.dv_level

        rpu_present_flag: Union[None, Unset, int]
        if isinstance(self.rpu_present_flag, Unset):
            rpu_present_flag = UNSET
        else:
            rpu_present_flag = self.rpu_present_flag

        el_present_flag: Union[None, Unset, int]
        if isinstance(self.el_present_flag, Unset):
            el_present_flag = UNSET
        else:
            el_present_flag = self.el_present_flag

        bl_present_flag: Union[None, Unset, int]
        if isinstance(self.bl_present_flag, Unset):
            bl_present_flag = UNSET
        else:
            bl_present_flag = self.bl_present_flag

        dv_bl_signal_compatibility_id: Union[None, Unset, int]
        if isinstance(self.dv_bl_signal_compatibility_id, Unset):
            dv_bl_signal_compatibility_id = UNSET
        else:
            dv_bl_signal_compatibility_id = self.dv_bl_signal_compatibility_id

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        time_base: Union[None, Unset, str]
        if isinstance(self.time_base, Unset):
            time_base = UNSET
        else:
            time_base = self.time_base

        codec_time_base: Union[None, Unset, str]
        if isinstance(self.codec_time_base, Unset):
            codec_time_base = UNSET
        else:
            codec_time_base = self.codec_time_base

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        video_range: Union[Unset, str] = UNSET
        if not isinstance(self.video_range, Unset):
            video_range = self.video_range.value

        video_range_type: Union[Unset, str] = UNSET
        if not isinstance(self.video_range_type, Unset):
            video_range_type = self.video_range_type.value

        video_do_vi_title: Union[None, Unset, str]
        if isinstance(self.video_do_vi_title, Unset):
            video_do_vi_title = UNSET
        else:
            video_do_vi_title = self.video_do_vi_title

        audio_spatial_format: Union[Unset, str] = UNSET
        if not isinstance(self.audio_spatial_format, Unset):
            audio_spatial_format = self.audio_spatial_format.value

        localized_undefined: Union[None, Unset, str]
        if isinstance(self.localized_undefined, Unset):
            localized_undefined = UNSET
        else:
            localized_undefined = self.localized_undefined

        localized_default: Union[None, Unset, str]
        if isinstance(self.localized_default, Unset):
            localized_default = UNSET
        else:
            localized_default = self.localized_default

        localized_forced: Union[None, Unset, str]
        if isinstance(self.localized_forced, Unset):
            localized_forced = UNSET
        else:
            localized_forced = self.localized_forced

        localized_external: Union[None, Unset, str]
        if isinstance(self.localized_external, Unset):
            localized_external = UNSET
        else:
            localized_external = self.localized_external

        localized_hearing_impaired: Union[None, Unset, str]
        if isinstance(self.localized_hearing_impaired, Unset):
            localized_hearing_impaired = UNSET
        else:
            localized_hearing_impaired = self.localized_hearing_impaired

        display_title: Union[None, Unset, str]
        if isinstance(self.display_title, Unset):
            display_title = UNSET
        else:
            display_title = self.display_title

        nal_length_size: Union[None, Unset, str]
        if isinstance(self.nal_length_size, Unset):
            nal_length_size = UNSET
        else:
            nal_length_size = self.nal_length_size

        is_interlaced = self.is_interlaced

        is_avc: Union[None, Unset, bool]
        if isinstance(self.is_avc, Unset):
            is_avc = UNSET
        else:
            is_avc = self.is_avc

        channel_layout: Union[None, Unset, str]
        if isinstance(self.channel_layout, Unset):
            channel_layout = UNSET
        else:
            channel_layout = self.channel_layout

        bit_rate: Union[None, Unset, int]
        if isinstance(self.bit_rate, Unset):
            bit_rate = UNSET
        else:
            bit_rate = self.bit_rate

        bit_depth: Union[None, Unset, int]
        if isinstance(self.bit_depth, Unset):
            bit_depth = UNSET
        else:
            bit_depth = self.bit_depth

        ref_frames: Union[None, Unset, int]
        if isinstance(self.ref_frames, Unset):
            ref_frames = UNSET
        else:
            ref_frames = self.ref_frames

        packet_length: Union[None, Unset, int]
        if isinstance(self.packet_length, Unset):
            packet_length = UNSET
        else:
            packet_length = self.packet_length

        channels: Union[None, Unset, int]
        if isinstance(self.channels, Unset):
            channels = UNSET
        else:
            channels = self.channels

        sample_rate: Union[None, Unset, int]
        if isinstance(self.sample_rate, Unset):
            sample_rate = UNSET
        else:
            sample_rate = self.sample_rate

        is_default = self.is_default

        is_forced = self.is_forced

        is_hearing_impaired = self.is_hearing_impaired

        height: Union[None, Unset, int]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        width: Union[None, Unset, int]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        average_frame_rate: Union[None, Unset, float]
        if isinstance(self.average_frame_rate, Unset):
            average_frame_rate = UNSET
        else:
            average_frame_rate = self.average_frame_rate

        real_frame_rate: Union[None, Unset, float]
        if isinstance(self.real_frame_rate, Unset):
            real_frame_rate = UNSET
        else:
            real_frame_rate = self.real_frame_rate

        profile: Union[None, Unset, str]
        if isinstance(self.profile, Unset):
            profile = UNSET
        else:
            profile = self.profile

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        aspect_ratio: Union[None, Unset, str]
        if isinstance(self.aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = self.aspect_ratio

        index = self.index

        score: Union[None, Unset, int]
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        is_external = self.is_external

        delivery_method: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_method, Unset):
            delivery_method = self.delivery_method.value

        delivery_url: Union[None, Unset, str]
        if isinstance(self.delivery_url, Unset):
            delivery_url = UNSET
        else:
            delivery_url = self.delivery_url

        is_external_url: Union[None, Unset, bool]
        if isinstance(self.is_external_url, Unset):
            is_external_url = UNSET
        else:
            is_external_url = self.is_external_url

        is_text_subtitle_stream = self.is_text_subtitle_stream

        supports_external_stream = self.supports_external_stream

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        pixel_format: Union[None, Unset, str]
        if isinstance(self.pixel_format, Unset):
            pixel_format = UNSET
        else:
            pixel_format = self.pixel_format

        level: Union[None, Unset, float]
        if isinstance(self.level, Unset):
            level = UNSET
        else:
            level = self.level

        is_anamorphic: Union[None, Unset, bool]
        if isinstance(self.is_anamorphic, Unset):
            is_anamorphic = UNSET
        else:
            is_anamorphic = self.is_anamorphic

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if codec is not UNSET:
            field_dict["Codec"] = codec
        if codec_tag is not UNSET:
            field_dict["CodecTag"] = codec_tag
        if language is not UNSET:
            field_dict["Language"] = language
        if color_range is not UNSET:
            field_dict["ColorRange"] = color_range
        if color_space is not UNSET:
            field_dict["ColorSpace"] = color_space
        if color_transfer is not UNSET:
            field_dict["ColorTransfer"] = color_transfer
        if color_primaries is not UNSET:
            field_dict["ColorPrimaries"] = color_primaries
        if dv_version_major is not UNSET:
            field_dict["DvVersionMajor"] = dv_version_major
        if dv_version_minor is not UNSET:
            field_dict["DvVersionMinor"] = dv_version_minor
        if dv_profile is not UNSET:
            field_dict["DvProfile"] = dv_profile
        if dv_level is not UNSET:
            field_dict["DvLevel"] = dv_level
        if rpu_present_flag is not UNSET:
            field_dict["RpuPresentFlag"] = rpu_present_flag
        if el_present_flag is not UNSET:
            field_dict["ElPresentFlag"] = el_present_flag
        if bl_present_flag is not UNSET:
            field_dict["BlPresentFlag"] = bl_present_flag
        if dv_bl_signal_compatibility_id is not UNSET:
            field_dict["DvBlSignalCompatibilityId"] = dv_bl_signal_compatibility_id
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if time_base is not UNSET:
            field_dict["TimeBase"] = time_base
        if codec_time_base is not UNSET:
            field_dict["CodecTimeBase"] = codec_time_base
        if title is not UNSET:
            field_dict["Title"] = title
        if video_range is not UNSET:
            field_dict["VideoRange"] = video_range
        if video_range_type is not UNSET:
            field_dict["VideoRangeType"] = video_range_type
        if video_do_vi_title is not UNSET:
            field_dict["VideoDoViTitle"] = video_do_vi_title
        if audio_spatial_format is not UNSET:
            field_dict["AudioSpatialFormat"] = audio_spatial_format
        if localized_undefined is not UNSET:
            field_dict["LocalizedUndefined"] = localized_undefined
        if localized_default is not UNSET:
            field_dict["LocalizedDefault"] = localized_default
        if localized_forced is not UNSET:
            field_dict["LocalizedForced"] = localized_forced
        if localized_external is not UNSET:
            field_dict["LocalizedExternal"] = localized_external
        if localized_hearing_impaired is not UNSET:
            field_dict["LocalizedHearingImpaired"] = localized_hearing_impaired
        if display_title is not UNSET:
            field_dict["DisplayTitle"] = display_title
        if nal_length_size is not UNSET:
            field_dict["NalLengthSize"] = nal_length_size
        if is_interlaced is not UNSET:
            field_dict["IsInterlaced"] = is_interlaced
        if is_avc is not UNSET:
            field_dict["IsAVC"] = is_avc
        if channel_layout is not UNSET:
            field_dict["ChannelLayout"] = channel_layout
        if bit_rate is not UNSET:
            field_dict["BitRate"] = bit_rate
        if bit_depth is not UNSET:
            field_dict["BitDepth"] = bit_depth
        if ref_frames is not UNSET:
            field_dict["RefFrames"] = ref_frames
        if packet_length is not UNSET:
            field_dict["PacketLength"] = packet_length
        if channels is not UNSET:
            field_dict["Channels"] = channels
        if sample_rate is not UNSET:
            field_dict["SampleRate"] = sample_rate
        if is_default is not UNSET:
            field_dict["IsDefault"] = is_default
        if is_forced is not UNSET:
            field_dict["IsForced"] = is_forced
        if is_hearing_impaired is not UNSET:
            field_dict["IsHearingImpaired"] = is_hearing_impaired
        if height is not UNSET:
            field_dict["Height"] = height
        if width is not UNSET:
            field_dict["Width"] = width
        if average_frame_rate is not UNSET:
            field_dict["AverageFrameRate"] = average_frame_rate
        if real_frame_rate is not UNSET:
            field_dict["RealFrameRate"] = real_frame_rate
        if profile is not UNSET:
            field_dict["Profile"] = profile
        if type is not UNSET:
            field_dict["Type"] = type
        if aspect_ratio is not UNSET:
            field_dict["AspectRatio"] = aspect_ratio
        if index is not UNSET:
            field_dict["Index"] = index
        if score is not UNSET:
            field_dict["Score"] = score
        if is_external is not UNSET:
            field_dict["IsExternal"] = is_external
        if delivery_method is not UNSET:
            field_dict["DeliveryMethod"] = delivery_method
        if delivery_url is not UNSET:
            field_dict["DeliveryUrl"] = delivery_url
        if is_external_url is not UNSET:
            field_dict["IsExternalUrl"] = is_external_url
        if is_text_subtitle_stream is not UNSET:
            field_dict["IsTextSubtitleStream"] = is_text_subtitle_stream
        if supports_external_stream is not UNSET:
            field_dict["SupportsExternalStream"] = supports_external_stream
        if path is not UNSET:
            field_dict["Path"] = path
        if pixel_format is not UNSET:
            field_dict["PixelFormat"] = pixel_format
        if level is not UNSET:
            field_dict["Level"] = level
        if is_anamorphic is not UNSET:
            field_dict["IsAnamorphic"] = is_anamorphic

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        codec = _parse_codec(d.pop("Codec", UNSET))

        def _parse_codec_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        codec_tag = _parse_codec_tag(d.pop("CodecTag", UNSET))

        def _parse_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language = _parse_language(d.pop("Language", UNSET))

        def _parse_color_range(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        color_range = _parse_color_range(d.pop("ColorRange", UNSET))

        def _parse_color_space(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        color_space = _parse_color_space(d.pop("ColorSpace", UNSET))

        def _parse_color_transfer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        color_transfer = _parse_color_transfer(d.pop("ColorTransfer", UNSET))

        def _parse_color_primaries(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        color_primaries = _parse_color_primaries(d.pop("ColorPrimaries", UNSET))

        def _parse_dv_version_major(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dv_version_major = _parse_dv_version_major(d.pop("DvVersionMajor", UNSET))

        def _parse_dv_version_minor(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dv_version_minor = _parse_dv_version_minor(d.pop("DvVersionMinor", UNSET))

        def _parse_dv_profile(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dv_profile = _parse_dv_profile(d.pop("DvProfile", UNSET))

        def _parse_dv_level(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dv_level = _parse_dv_level(d.pop("DvLevel", UNSET))

        def _parse_rpu_present_flag(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rpu_present_flag = _parse_rpu_present_flag(d.pop("RpuPresentFlag", UNSET))

        def _parse_el_present_flag(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        el_present_flag = _parse_el_present_flag(d.pop("ElPresentFlag", UNSET))

        def _parse_bl_present_flag(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bl_present_flag = _parse_bl_present_flag(d.pop("BlPresentFlag", UNSET))

        def _parse_dv_bl_signal_compatibility_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dv_bl_signal_compatibility_id = _parse_dv_bl_signal_compatibility_id(d.pop("DvBlSignalCompatibilityId", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("Comment", UNSET))

        def _parse_time_base(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_base = _parse_time_base(d.pop("TimeBase", UNSET))

        def _parse_codec_time_base(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        codec_time_base = _parse_codec_time_base(d.pop("CodecTimeBase", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("Title", UNSET))

        _video_range = d.pop("VideoRange", UNSET)
        video_range: Union[Unset, VideoRange]
        if isinstance(_video_range, Unset):
            video_range = UNSET
        else:
            video_range = VideoRange(_video_range)

        _video_range_type = d.pop("VideoRangeType", UNSET)
        video_range_type: Union[Unset, VideoRangeType]
        if isinstance(_video_range_type, Unset):
            video_range_type = UNSET
        else:
            video_range_type = VideoRangeType(_video_range_type)

        def _parse_video_do_vi_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        video_do_vi_title = _parse_video_do_vi_title(d.pop("VideoDoViTitle", UNSET))

        _audio_spatial_format = d.pop("AudioSpatialFormat", UNSET)
        audio_spatial_format: Union[Unset, AudioSpatialFormat]
        if isinstance(_audio_spatial_format, Unset):
            audio_spatial_format = UNSET
        else:
            audio_spatial_format = AudioSpatialFormat(_audio_spatial_format)

        def _parse_localized_undefined(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        localized_undefined = _parse_localized_undefined(d.pop("LocalizedUndefined", UNSET))

        def _parse_localized_default(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        localized_default = _parse_localized_default(d.pop("LocalizedDefault", UNSET))

        def _parse_localized_forced(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        localized_forced = _parse_localized_forced(d.pop("LocalizedForced", UNSET))

        def _parse_localized_external(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        localized_external = _parse_localized_external(d.pop("LocalizedExternal", UNSET))

        def _parse_localized_hearing_impaired(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        localized_hearing_impaired = _parse_localized_hearing_impaired(d.pop("LocalizedHearingImpaired", UNSET))

        def _parse_display_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_title = _parse_display_title(d.pop("DisplayTitle", UNSET))

        def _parse_nal_length_size(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nal_length_size = _parse_nal_length_size(d.pop("NalLengthSize", UNSET))

        is_interlaced = d.pop("IsInterlaced", UNSET)

        def _parse_is_avc(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_avc = _parse_is_avc(d.pop("IsAVC", UNSET))

        def _parse_channel_layout(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_layout = _parse_channel_layout(d.pop("ChannelLayout", UNSET))

        def _parse_bit_rate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bit_rate = _parse_bit_rate(d.pop("BitRate", UNSET))

        def _parse_bit_depth(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bit_depth = _parse_bit_depth(d.pop("BitDepth", UNSET))

        def _parse_ref_frames(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ref_frames = _parse_ref_frames(d.pop("RefFrames", UNSET))

        def _parse_packet_length(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        packet_length = _parse_packet_length(d.pop("PacketLength", UNSET))

        def _parse_channels(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        channels = _parse_channels(d.pop("Channels", UNSET))

        def _parse_sample_rate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sample_rate = _parse_sample_rate(d.pop("SampleRate", UNSET))

        is_default = d.pop("IsDefault", UNSET)

        is_forced = d.pop("IsForced", UNSET)

        is_hearing_impaired = d.pop("IsHearingImpaired", UNSET)

        def _parse_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        height = _parse_height(d.pop("Height", UNSET))

        def _parse_width(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        width = _parse_width(d.pop("Width", UNSET))

        def _parse_average_frame_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        average_frame_rate = _parse_average_frame_rate(d.pop("AverageFrameRate", UNSET))

        def _parse_real_frame_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        real_frame_rate = _parse_real_frame_rate(d.pop("RealFrameRate", UNSET))

        def _parse_profile(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        profile = _parse_profile(d.pop("Profile", UNSET))

        _type = d.pop("Type", UNSET)
        type: Union[Unset, MediaStreamType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = MediaStreamType(_type)

        def _parse_aspect_ratio(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aspect_ratio = _parse_aspect_ratio(d.pop("AspectRatio", UNSET))

        index = d.pop("Index", UNSET)

        def _parse_score(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        score = _parse_score(d.pop("Score", UNSET))

        is_external = d.pop("IsExternal", UNSET)

        _delivery_method = d.pop("DeliveryMethod", UNSET)
        delivery_method: Union[Unset, MediaStreamDeliveryMethod]
        if isinstance(_delivery_method, Unset):
            delivery_method = UNSET
        else:
            delivery_method = MediaStreamDeliveryMethod(_delivery_method)

        def _parse_delivery_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_url = _parse_delivery_url(d.pop("DeliveryUrl", UNSET))

        def _parse_is_external_url(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_external_url = _parse_is_external_url(d.pop("IsExternalUrl", UNSET))

        is_text_subtitle_stream = d.pop("IsTextSubtitleStream", UNSET)

        supports_external_stream = d.pop("SupportsExternalStream", UNSET)

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_pixel_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pixel_format = _parse_pixel_format(d.pop("PixelFormat", UNSET))

        def _parse_level(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        level = _parse_level(d.pop("Level", UNSET))

        def _parse_is_anamorphic(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_anamorphic = _parse_is_anamorphic(d.pop("IsAnamorphic", UNSET))

        media_stream = cls(
            codec=codec,
            codec_tag=codec_tag,
            language=language,
            color_range=color_range,
            color_space=color_space,
            color_transfer=color_transfer,
            color_primaries=color_primaries,
            dv_version_major=dv_version_major,
            dv_version_minor=dv_version_minor,
            dv_profile=dv_profile,
            dv_level=dv_level,
            rpu_present_flag=rpu_present_flag,
            el_present_flag=el_present_flag,
            bl_present_flag=bl_present_flag,
            dv_bl_signal_compatibility_id=dv_bl_signal_compatibility_id,
            comment=comment,
            time_base=time_base,
            codec_time_base=codec_time_base,
            title=title,
            video_range=video_range,
            video_range_type=video_range_type,
            video_do_vi_title=video_do_vi_title,
            audio_spatial_format=audio_spatial_format,
            localized_undefined=localized_undefined,
            localized_default=localized_default,
            localized_forced=localized_forced,
            localized_external=localized_external,
            localized_hearing_impaired=localized_hearing_impaired,
            display_title=display_title,
            nal_length_size=nal_length_size,
            is_interlaced=is_interlaced,
            is_avc=is_avc,
            channel_layout=channel_layout,
            bit_rate=bit_rate,
            bit_depth=bit_depth,
            ref_frames=ref_frames,
            packet_length=packet_length,
            channels=channels,
            sample_rate=sample_rate,
            is_default=is_default,
            is_forced=is_forced,
            is_hearing_impaired=is_hearing_impaired,
            height=height,
            width=width,
            average_frame_rate=average_frame_rate,
            real_frame_rate=real_frame_rate,
            profile=profile,
            type=type,
            aspect_ratio=aspect_ratio,
            index=index,
            score=score,
            is_external=is_external,
            delivery_method=delivery_method,
            delivery_url=delivery_url,
            is_external_url=is_external_url,
            is_text_subtitle_stream=is_text_subtitle_stream,
            supports_external_stream=supports_external_stream,
            path=path,
            pixel_format=pixel_format,
            level=level,
            is_anamorphic=is_anamorphic,
        )

        return media_stream
