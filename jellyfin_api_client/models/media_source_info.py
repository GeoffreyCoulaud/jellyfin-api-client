from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.media_protocol import MediaProtocol
from typing import cast, Union
from typing import cast, List
from typing import Dict
from ..models.media_source_type import MediaSourceType
from ..models.media_source_info_video_type import MediaSourceInfoVideoType
from ..models.media_stream_protocol import MediaStreamProtocol
from ..types import UNSET, Unset
from typing import Union
from ..models.media_source_info_encoder_protocol import MediaSourceInfoEncoderProtocol
from typing import cast
from ..models.media_source_info_video_3d_format import MediaSourceInfoVideo3DFormat
from ..models.media_source_info_iso_type import MediaSourceInfoIsoType
from ..models.media_source_info_timestamp import MediaSourceInfoTimestamp

if TYPE_CHECKING:
    from ..models.media_attachment import MediaAttachment
    from ..models.media_source_info_required_http_headers_type_0 import MediaSourceInfoRequiredHttpHeadersType0
    from ..models.media_stream import MediaStream


T = TypeVar("T", bound="MediaSourceInfo")


@_attrs_define
class MediaSourceInfo:
    """
    Attributes:
        protocol (Union[Unset, MediaProtocol]):
        id (Union[None, Unset, str]):
        path (Union[None, Unset, str]):
        encoder_path (Union[None, Unset, str]):
        encoder_protocol (Union[Unset, MediaSourceInfoEncoderProtocol]):
        type (Union[Unset, MediaSourceType]):
        container (Union[None, Unset, str]):
        size (Union[None, Unset, int]):
        name (Union[None, Unset, str]):
        is_remote (Union[Unset, bool]): Gets or sets a value indicating whether the media is remote.
            Differentiate internet url vs local network.
        e_tag (Union[None, Unset, str]):
        run_time_ticks (Union[None, Unset, int]):
        read_at_native_framerate (Union[Unset, bool]):
        ignore_dts (Union[Unset, bool]):
        ignore_index (Union[Unset, bool]):
        gen_pts_input (Union[Unset, bool]):
        supports_transcoding (Union[Unset, bool]):
        supports_direct_stream (Union[Unset, bool]):
        supports_direct_play (Union[Unset, bool]):
        is_infinite_stream (Union[Unset, bool]):
        requires_opening (Union[Unset, bool]):
        open_token (Union[None, Unset, str]):
        requires_closing (Union[Unset, bool]):
        live_stream_id (Union[None, Unset, str]):
        buffer_ms (Union[None, Unset, int]):
        requires_looping (Union[Unset, bool]):
        supports_probing (Union[Unset, bool]):
        video_type (Union[Unset, MediaSourceInfoVideoType]):
        iso_type (Union[Unset, MediaSourceInfoIsoType]):
        video_3d_format (Union[Unset, MediaSourceInfoVideo3DFormat]):
        media_streams (Union[List['MediaStream'], None, Unset]):
        media_attachments (Union[List['MediaAttachment'], None, Unset]):
        formats (Union[List[str], None, Unset]):
        bitrate (Union[None, Unset, int]):
        timestamp (Union[Unset, MediaSourceInfoTimestamp]):
        required_http_headers (Union['MediaSourceInfoRequiredHttpHeadersType0', None, Unset]):
        transcoding_url (Union[None, Unset, str]):
        transcoding_sub_protocol (Union[Unset, MediaStreamProtocol]): Media streaming protocol.
            Lowercase for backwards compatibility.
        transcoding_container (Union[None, Unset, str]):
        analyze_duration_ms (Union[None, Unset, int]):
        default_audio_stream_index (Union[None, Unset, int]):
        default_subtitle_stream_index (Union[None, Unset, int]):
    """

    protocol: Union[Unset, MediaProtocol] = UNSET
    id: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    encoder_path: Union[None, Unset, str] = UNSET
    encoder_protocol: Union[Unset, MediaSourceInfoEncoderProtocol] = UNSET
    type: Union[Unset, MediaSourceType] = UNSET
    container: Union[None, Unset, str] = UNSET
    size: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    is_remote: Union[Unset, bool] = UNSET
    e_tag: Union[None, Unset, str] = UNSET
    run_time_ticks: Union[None, Unset, int] = UNSET
    read_at_native_framerate: Union[Unset, bool] = UNSET
    ignore_dts: Union[Unset, bool] = UNSET
    ignore_index: Union[Unset, bool] = UNSET
    gen_pts_input: Union[Unset, bool] = UNSET
    supports_transcoding: Union[Unset, bool] = UNSET
    supports_direct_stream: Union[Unset, bool] = UNSET
    supports_direct_play: Union[Unset, bool] = UNSET
    is_infinite_stream: Union[Unset, bool] = UNSET
    requires_opening: Union[Unset, bool] = UNSET
    open_token: Union[None, Unset, str] = UNSET
    requires_closing: Union[Unset, bool] = UNSET
    live_stream_id: Union[None, Unset, str] = UNSET
    buffer_ms: Union[None, Unset, int] = UNSET
    requires_looping: Union[Unset, bool] = UNSET
    supports_probing: Union[Unset, bool] = UNSET
    video_type: Union[Unset, MediaSourceInfoVideoType] = UNSET
    iso_type: Union[Unset, MediaSourceInfoIsoType] = UNSET
    video_3d_format: Union[Unset, MediaSourceInfoVideo3DFormat] = UNSET
    media_streams: Union[List["MediaStream"], None, Unset] = UNSET
    media_attachments: Union[List["MediaAttachment"], None, Unset] = UNSET
    formats: Union[List[str], None, Unset] = UNSET
    bitrate: Union[None, Unset, int] = UNSET
    timestamp: Union[Unset, MediaSourceInfoTimestamp] = UNSET
    required_http_headers: Union["MediaSourceInfoRequiredHttpHeadersType0", None, Unset] = UNSET
    transcoding_url: Union[None, Unset, str] = UNSET
    transcoding_sub_protocol: Union[Unset, MediaStreamProtocol] = UNSET
    transcoding_container: Union[None, Unset, str] = UNSET
    analyze_duration_ms: Union[None, Unset, int] = UNSET
    default_audio_stream_index: Union[None, Unset, int] = UNSET
    default_subtitle_stream_index: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.media_attachment import MediaAttachment
        from ..models.media_source_info_required_http_headers_type_0 import MediaSourceInfoRequiredHttpHeadersType0
        from ..models.media_stream import MediaStream

        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        encoder_path: Union[None, Unset, str]
        if isinstance(self.encoder_path, Unset):
            encoder_path = UNSET
        else:
            encoder_path = self.encoder_path

        encoder_protocol: Union[Unset, str] = UNSET
        if not isinstance(self.encoder_protocol, Unset):
            encoder_protocol = self.encoder_protocol.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        container: Union[None, Unset, str]
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_remote = self.is_remote

        e_tag: Union[None, Unset, str]
        if isinstance(self.e_tag, Unset):
            e_tag = UNSET
        else:
            e_tag = self.e_tag

        run_time_ticks: Union[None, Unset, int]
        if isinstance(self.run_time_ticks, Unset):
            run_time_ticks = UNSET
        else:
            run_time_ticks = self.run_time_ticks

        read_at_native_framerate = self.read_at_native_framerate

        ignore_dts = self.ignore_dts

        ignore_index = self.ignore_index

        gen_pts_input = self.gen_pts_input

        supports_transcoding = self.supports_transcoding

        supports_direct_stream = self.supports_direct_stream

        supports_direct_play = self.supports_direct_play

        is_infinite_stream = self.is_infinite_stream

        requires_opening = self.requires_opening

        open_token: Union[None, Unset, str]
        if isinstance(self.open_token, Unset):
            open_token = UNSET
        else:
            open_token = self.open_token

        requires_closing = self.requires_closing

        live_stream_id: Union[None, Unset, str]
        if isinstance(self.live_stream_id, Unset):
            live_stream_id = UNSET
        else:
            live_stream_id = self.live_stream_id

        buffer_ms: Union[None, Unset, int]
        if isinstance(self.buffer_ms, Unset):
            buffer_ms = UNSET
        else:
            buffer_ms = self.buffer_ms

        requires_looping = self.requires_looping

        supports_probing = self.supports_probing

        video_type: Union[Unset, str] = UNSET
        if not isinstance(self.video_type, Unset):
            video_type = self.video_type.value

        iso_type: Union[Unset, str] = UNSET
        if not isinstance(self.iso_type, Unset):
            iso_type = self.iso_type.value

        video_3d_format: Union[Unset, str] = UNSET
        if not isinstance(self.video_3d_format, Unset):
            video_3d_format = self.video_3d_format.value

        media_streams: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.media_streams, Unset):
            media_streams = UNSET
        elif isinstance(self.media_streams, list):
            media_streams = []
            for media_streams_type_0_item_data in self.media_streams:
                media_streams_type_0_item = media_streams_type_0_item_data.to_dict()
                media_streams.append(media_streams_type_0_item)

        else:
            media_streams = self.media_streams

        media_attachments: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.media_attachments, Unset):
            media_attachments = UNSET
        elif isinstance(self.media_attachments, list):
            media_attachments = []
            for media_attachments_type_0_item_data in self.media_attachments:
                media_attachments_type_0_item = media_attachments_type_0_item_data.to_dict()
                media_attachments.append(media_attachments_type_0_item)

        else:
            media_attachments = self.media_attachments

        formats: Union[List[str], None, Unset]
        if isinstance(self.formats, Unset):
            formats = UNSET
        elif isinstance(self.formats, list):
            formats = self.formats

        else:
            formats = self.formats

        bitrate: Union[None, Unset, int]
        if isinstance(self.bitrate, Unset):
            bitrate = UNSET
        else:
            bitrate = self.bitrate

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.value

        required_http_headers: Union[Dict[str, Any], None, Unset]
        if isinstance(self.required_http_headers, Unset):
            required_http_headers = UNSET
        elif isinstance(self.required_http_headers, MediaSourceInfoRequiredHttpHeadersType0):
            required_http_headers = self.required_http_headers.to_dict()
        else:
            required_http_headers = self.required_http_headers

        transcoding_url: Union[None, Unset, str]
        if isinstance(self.transcoding_url, Unset):
            transcoding_url = UNSET
        else:
            transcoding_url = self.transcoding_url

        transcoding_sub_protocol: Union[Unset, str] = UNSET
        if not isinstance(self.transcoding_sub_protocol, Unset):
            transcoding_sub_protocol = self.transcoding_sub_protocol.value

        transcoding_container: Union[None, Unset, str]
        if isinstance(self.transcoding_container, Unset):
            transcoding_container = UNSET
        else:
            transcoding_container = self.transcoding_container

        analyze_duration_ms: Union[None, Unset, int]
        if isinstance(self.analyze_duration_ms, Unset):
            analyze_duration_ms = UNSET
        else:
            analyze_duration_ms = self.analyze_duration_ms

        default_audio_stream_index: Union[None, Unset, int]
        if isinstance(self.default_audio_stream_index, Unset):
            default_audio_stream_index = UNSET
        else:
            default_audio_stream_index = self.default_audio_stream_index

        default_subtitle_stream_index: Union[None, Unset, int]
        if isinstance(self.default_subtitle_stream_index, Unset):
            default_subtitle_stream_index = UNSET
        else:
            default_subtitle_stream_index = self.default_subtitle_stream_index

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if protocol is not UNSET:
            field_dict["Protocol"] = protocol
        if id is not UNSET:
            field_dict["Id"] = id
        if path is not UNSET:
            field_dict["Path"] = path
        if encoder_path is not UNSET:
            field_dict["EncoderPath"] = encoder_path
        if encoder_protocol is not UNSET:
            field_dict["EncoderProtocol"] = encoder_protocol
        if type is not UNSET:
            field_dict["Type"] = type
        if container is not UNSET:
            field_dict["Container"] = container
        if size is not UNSET:
            field_dict["Size"] = size
        if name is not UNSET:
            field_dict["Name"] = name
        if is_remote is not UNSET:
            field_dict["IsRemote"] = is_remote
        if e_tag is not UNSET:
            field_dict["ETag"] = e_tag
        if run_time_ticks is not UNSET:
            field_dict["RunTimeTicks"] = run_time_ticks
        if read_at_native_framerate is not UNSET:
            field_dict["ReadAtNativeFramerate"] = read_at_native_framerate
        if ignore_dts is not UNSET:
            field_dict["IgnoreDts"] = ignore_dts
        if ignore_index is not UNSET:
            field_dict["IgnoreIndex"] = ignore_index
        if gen_pts_input is not UNSET:
            field_dict["GenPtsInput"] = gen_pts_input
        if supports_transcoding is not UNSET:
            field_dict["SupportsTranscoding"] = supports_transcoding
        if supports_direct_stream is not UNSET:
            field_dict["SupportsDirectStream"] = supports_direct_stream
        if supports_direct_play is not UNSET:
            field_dict["SupportsDirectPlay"] = supports_direct_play
        if is_infinite_stream is not UNSET:
            field_dict["IsInfiniteStream"] = is_infinite_stream
        if requires_opening is not UNSET:
            field_dict["RequiresOpening"] = requires_opening
        if open_token is not UNSET:
            field_dict["OpenToken"] = open_token
        if requires_closing is not UNSET:
            field_dict["RequiresClosing"] = requires_closing
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id
        if buffer_ms is not UNSET:
            field_dict["BufferMs"] = buffer_ms
        if requires_looping is not UNSET:
            field_dict["RequiresLooping"] = requires_looping
        if supports_probing is not UNSET:
            field_dict["SupportsProbing"] = supports_probing
        if video_type is not UNSET:
            field_dict["VideoType"] = video_type
        if iso_type is not UNSET:
            field_dict["IsoType"] = iso_type
        if video_3d_format is not UNSET:
            field_dict["Video3DFormat"] = video_3d_format
        if media_streams is not UNSET:
            field_dict["MediaStreams"] = media_streams
        if media_attachments is not UNSET:
            field_dict["MediaAttachments"] = media_attachments
        if formats is not UNSET:
            field_dict["Formats"] = formats
        if bitrate is not UNSET:
            field_dict["Bitrate"] = bitrate
        if timestamp is not UNSET:
            field_dict["Timestamp"] = timestamp
        if required_http_headers is not UNSET:
            field_dict["RequiredHttpHeaders"] = required_http_headers
        if transcoding_url is not UNSET:
            field_dict["TranscodingUrl"] = transcoding_url
        if transcoding_sub_protocol is not UNSET:
            field_dict["TranscodingSubProtocol"] = transcoding_sub_protocol
        if transcoding_container is not UNSET:
            field_dict["TranscodingContainer"] = transcoding_container
        if analyze_duration_ms is not UNSET:
            field_dict["AnalyzeDurationMs"] = analyze_duration_ms
        if default_audio_stream_index is not UNSET:
            field_dict["DefaultAudioStreamIndex"] = default_audio_stream_index
        if default_subtitle_stream_index is not UNSET:
            field_dict["DefaultSubtitleStreamIndex"] = default_subtitle_stream_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_attachment import MediaAttachment
        from ..models.media_source_info_required_http_headers_type_0 import MediaSourceInfoRequiredHttpHeadersType0
        from ..models.media_stream import MediaStream

        d = src_dict.copy()
        _protocol = d.pop("Protocol", UNSET)
        protocol: Union[Unset, MediaProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = MediaProtocol(_protocol)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_encoder_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        encoder_path = _parse_encoder_path(d.pop("EncoderPath", UNSET))

        _encoder_protocol = d.pop("EncoderProtocol", UNSET)
        encoder_protocol: Union[Unset, MediaSourceInfoEncoderProtocol]
        if isinstance(_encoder_protocol, Unset):
            encoder_protocol = UNSET
        else:
            encoder_protocol = MediaSourceInfoEncoderProtocol(_encoder_protocol)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, MediaSourceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = MediaSourceType(_type)

        def _parse_container(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        container = _parse_container(d.pop("Container", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("Size", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        is_remote = d.pop("IsRemote", UNSET)

        def _parse_e_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        e_tag = _parse_e_tag(d.pop("ETag", UNSET))

        def _parse_run_time_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        run_time_ticks = _parse_run_time_ticks(d.pop("RunTimeTicks", UNSET))

        read_at_native_framerate = d.pop("ReadAtNativeFramerate", UNSET)

        ignore_dts = d.pop("IgnoreDts", UNSET)

        ignore_index = d.pop("IgnoreIndex", UNSET)

        gen_pts_input = d.pop("GenPtsInput", UNSET)

        supports_transcoding = d.pop("SupportsTranscoding", UNSET)

        supports_direct_stream = d.pop("SupportsDirectStream", UNSET)

        supports_direct_play = d.pop("SupportsDirectPlay", UNSET)

        is_infinite_stream = d.pop("IsInfiniteStream", UNSET)

        requires_opening = d.pop("RequiresOpening", UNSET)

        def _parse_open_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        open_token = _parse_open_token(d.pop("OpenToken", UNSET))

        requires_closing = d.pop("RequiresClosing", UNSET)

        def _parse_live_stream_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        live_stream_id = _parse_live_stream_id(d.pop("LiveStreamId", UNSET))

        def _parse_buffer_ms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        buffer_ms = _parse_buffer_ms(d.pop("BufferMs", UNSET))

        requires_looping = d.pop("RequiresLooping", UNSET)

        supports_probing = d.pop("SupportsProbing", UNSET)

        _video_type = d.pop("VideoType", UNSET)
        video_type: Union[Unset, MediaSourceInfoVideoType]
        if isinstance(_video_type, Unset):
            video_type = UNSET
        else:
            video_type = MediaSourceInfoVideoType(_video_type)

        _iso_type = d.pop("IsoType", UNSET)
        iso_type: Union[Unset, MediaSourceInfoIsoType]
        if isinstance(_iso_type, Unset):
            iso_type = UNSET
        else:
            iso_type = MediaSourceInfoIsoType(_iso_type)

        _video_3d_format = d.pop("Video3DFormat", UNSET)
        video_3d_format: Union[Unset, MediaSourceInfoVideo3DFormat]
        if isinstance(_video_3d_format, Unset):
            video_3d_format = UNSET
        else:
            video_3d_format = MediaSourceInfoVideo3DFormat(_video_3d_format)

        def _parse_media_streams(data: object) -> Union[List["MediaStream"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_streams_type_0 = []
                _media_streams_type_0 = data
                for media_streams_type_0_item_data in _media_streams_type_0:
                    media_streams_type_0_item = MediaStream.from_dict(media_streams_type_0_item_data)

                    media_streams_type_0.append(media_streams_type_0_item)

                return media_streams_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["MediaStream"], None, Unset], data)

        media_streams = _parse_media_streams(d.pop("MediaStreams", UNSET))

        def _parse_media_attachments(data: object) -> Union[List["MediaAttachment"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_attachments_type_0 = []
                _media_attachments_type_0 = data
                for media_attachments_type_0_item_data in _media_attachments_type_0:
                    media_attachments_type_0_item = MediaAttachment.from_dict(media_attachments_type_0_item_data)

                    media_attachments_type_0.append(media_attachments_type_0_item)

                return media_attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["MediaAttachment"], None, Unset], data)

        media_attachments = _parse_media_attachments(d.pop("MediaAttachments", UNSET))

        def _parse_formats(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                formats_type_0 = cast(List[str], data)

                return formats_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        formats = _parse_formats(d.pop("Formats", UNSET))

        def _parse_bitrate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bitrate = _parse_bitrate(d.pop("Bitrate", UNSET))

        _timestamp = d.pop("Timestamp", UNSET)
        timestamp: Union[Unset, MediaSourceInfoTimestamp]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = MediaSourceInfoTimestamp(_timestamp)

        def _parse_required_http_headers(data: object) -> Union["MediaSourceInfoRequiredHttpHeadersType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                required_http_headers_type_0 = MediaSourceInfoRequiredHttpHeadersType0.from_dict(data)

                return required_http_headers_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MediaSourceInfoRequiredHttpHeadersType0", None, Unset], data)

        required_http_headers = _parse_required_http_headers(d.pop("RequiredHttpHeaders", UNSET))

        def _parse_transcoding_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        transcoding_url = _parse_transcoding_url(d.pop("TranscodingUrl", UNSET))

        _transcoding_sub_protocol = d.pop("TranscodingSubProtocol", UNSET)
        transcoding_sub_protocol: Union[Unset, MediaStreamProtocol]
        if isinstance(_transcoding_sub_protocol, Unset):
            transcoding_sub_protocol = UNSET
        else:
            transcoding_sub_protocol = MediaStreamProtocol(_transcoding_sub_protocol)

        def _parse_transcoding_container(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        transcoding_container = _parse_transcoding_container(d.pop("TranscodingContainer", UNSET))

        def _parse_analyze_duration_ms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        analyze_duration_ms = _parse_analyze_duration_ms(d.pop("AnalyzeDurationMs", UNSET))

        def _parse_default_audio_stream_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        default_audio_stream_index = _parse_default_audio_stream_index(d.pop("DefaultAudioStreamIndex", UNSET))

        def _parse_default_subtitle_stream_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        default_subtitle_stream_index = _parse_default_subtitle_stream_index(d.pop("DefaultSubtitleStreamIndex", UNSET))

        media_source_info = cls(
            protocol=protocol,
            id=id,
            path=path,
            encoder_path=encoder_path,
            encoder_protocol=encoder_protocol,
            type=type,
            container=container,
            size=size,
            name=name,
            is_remote=is_remote,
            e_tag=e_tag,
            run_time_ticks=run_time_ticks,
            read_at_native_framerate=read_at_native_framerate,
            ignore_dts=ignore_dts,
            ignore_index=ignore_index,
            gen_pts_input=gen_pts_input,
            supports_transcoding=supports_transcoding,
            supports_direct_stream=supports_direct_stream,
            supports_direct_play=supports_direct_play,
            is_infinite_stream=is_infinite_stream,
            requires_opening=requires_opening,
            open_token=open_token,
            requires_closing=requires_closing,
            live_stream_id=live_stream_id,
            buffer_ms=buffer_ms,
            requires_looping=requires_looping,
            supports_probing=supports_probing,
            video_type=video_type,
            iso_type=iso_type,
            video_3d_format=video_3d_format,
            media_streams=media_streams,
            media_attachments=media_attachments,
            formats=formats,
            bitrate=bitrate,
            timestamp=timestamp,
            required_http_headers=required_http_headers,
            transcoding_url=transcoding_url,
            transcoding_sub_protocol=transcoding_sub_protocol,
            transcoding_container=transcoding_container,
            analyze_duration_ms=analyze_duration_ms,
            default_audio_stream_index=default_audio_stream_index,
            default_subtitle_stream_index=default_subtitle_stream_index,
        )

        return media_source_info
