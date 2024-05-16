from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Dict
from ...models.subtitle_delivery_method import SubtitleDeliveryMethod
from typing import Union
from typing import cast
from ...models.encoding_context import EncodingContext
from ...models.get_variant_hls_video_playlist_stream_options import GetVariantHlsVideoPlaylistStreamOptions


def _get_kwargs(
    item_id: str,
    *,
    static: Union[Unset, bool] = UNSET,
    params: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    device_profile_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    segment_container: Union[Unset, str] = UNSET,
    segment_length: Union[Unset, int] = UNSET,
    min_segments: Union[Unset, int] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    audio_codec: Union[Unset, str] = UNSET,
    enable_auto_stream_copy: Union[Unset, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, bool] = UNSET,
    audio_sample_rate: Union[Unset, int] = UNSET,
    max_audio_bit_depth: Union[Unset, int] = UNSET,
    audio_bit_rate: Union[Unset, int] = UNSET,
    audio_channels: Union[Unset, int] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    profile: Union[Unset, str] = UNSET,
    level: Union[Unset, str] = UNSET,
    framerate: Union[Unset, float] = UNSET,
    max_framerate: Union[Unset, float] = UNSET,
    copy_timestamps: Union[Unset, bool] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    video_bit_rate: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    subtitle_method: Union[Unset, SubtitleDeliveryMethod] = UNSET,
    max_ref_frames: Union[Unset, int] = UNSET,
    max_video_bit_depth: Union[Unset, int] = UNSET,
    require_avc: Union[Unset, bool] = UNSET,
    de_interlace: Union[Unset, bool] = UNSET,
    require_non_anamorphic: Union[Unset, bool] = UNSET,
    transcoding_max_audio_channels: Union[Unset, int] = UNSET,
    cpu_core_limit: Union[Unset, int] = UNSET,
    live_stream_id: Union[Unset, str] = UNSET,
    enable_mpegts_m2_ts_mode: Union[Unset, bool] = UNSET,
    video_codec: Union[Unset, str] = UNSET,
    subtitle_codec: Union[Unset, str] = UNSET,
    transcode_reasons: Union[Unset, str] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    video_stream_index: Union[Unset, int] = UNSET,
    context: Union[Unset, EncodingContext] = UNSET,
    stream_options: Union[Unset, "GetVariantHlsVideoPlaylistStreamOptions"] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["static"] = static

    params["params"] = params

    params["tag"] = tag

    params["deviceProfileId"] = device_profile_id

    params["playSessionId"] = play_session_id

    params["segmentContainer"] = segment_container

    params["segmentLength"] = segment_length

    params["minSegments"] = min_segments

    params["mediaSourceId"] = media_source_id

    params["deviceId"] = device_id

    params["audioCodec"] = audio_codec

    params["enableAutoStreamCopy"] = enable_auto_stream_copy

    params["allowVideoStreamCopy"] = allow_video_stream_copy

    params["allowAudioStreamCopy"] = allow_audio_stream_copy

    params["breakOnNonKeyFrames"] = break_on_non_key_frames

    params["audioSampleRate"] = audio_sample_rate

    params["maxAudioBitDepth"] = max_audio_bit_depth

    params["audioBitRate"] = audio_bit_rate

    params["audioChannels"] = audio_channels

    params["maxAudioChannels"] = max_audio_channels

    params["profile"] = profile

    params["level"] = level

    params["framerate"] = framerate

    params["maxFramerate"] = max_framerate

    params["copyTimestamps"] = copy_timestamps

    params["startTimeTicks"] = start_time_ticks

    params["width"] = width

    params["height"] = height

    params["maxWidth"] = max_width

    params["maxHeight"] = max_height

    params["videoBitRate"] = video_bit_rate

    params["subtitleStreamIndex"] = subtitle_stream_index

    json_subtitle_method: Union[Unset, str] = UNSET
    if not isinstance(subtitle_method, Unset):
        json_subtitle_method = subtitle_method.value

    params["subtitleMethod"] = json_subtitle_method

    params["maxRefFrames"] = max_ref_frames

    params["maxVideoBitDepth"] = max_video_bit_depth

    params["requireAvc"] = require_avc

    params["deInterlace"] = de_interlace

    params["requireNonAnamorphic"] = require_non_anamorphic

    params["transcodingMaxAudioChannels"] = transcoding_max_audio_channels

    params["cpuCoreLimit"] = cpu_core_limit

    params["liveStreamId"] = live_stream_id

    params["enableMpegtsM2TsMode"] = enable_mpegts_m2_ts_mode

    params["videoCodec"] = video_codec

    params["subtitleCodec"] = subtitle_codec

    params["transcodeReasons"] = transcode_reasons

    params["audioStreamIndex"] = audio_stream_index

    params["videoStreamIndex"] = video_stream_index

    json_context: Union[Unset, str] = UNSET
    if not isinstance(context, Unset):
        json_context = context.value

    params["context"] = json_context

    json_stream_options: Union[Unset, Dict[str, Any]] = UNSET
    if not isinstance(stream_options, Unset):
        json_stream_options = stream_options.to_dict()
    if not isinstance(json_stream_options, Unset):
        params.update(json_stream_options)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Videos/{item_id}/main.m3u8".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    static: Union[Unset, bool] = UNSET,
    params: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    device_profile_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    segment_container: Union[Unset, str] = UNSET,
    segment_length: Union[Unset, int] = UNSET,
    min_segments: Union[Unset, int] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    audio_codec: Union[Unset, str] = UNSET,
    enable_auto_stream_copy: Union[Unset, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, bool] = UNSET,
    audio_sample_rate: Union[Unset, int] = UNSET,
    max_audio_bit_depth: Union[Unset, int] = UNSET,
    audio_bit_rate: Union[Unset, int] = UNSET,
    audio_channels: Union[Unset, int] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    profile: Union[Unset, str] = UNSET,
    level: Union[Unset, str] = UNSET,
    framerate: Union[Unset, float] = UNSET,
    max_framerate: Union[Unset, float] = UNSET,
    copy_timestamps: Union[Unset, bool] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    video_bit_rate: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    subtitle_method: Union[Unset, SubtitleDeliveryMethod] = UNSET,
    max_ref_frames: Union[Unset, int] = UNSET,
    max_video_bit_depth: Union[Unset, int] = UNSET,
    require_avc: Union[Unset, bool] = UNSET,
    de_interlace: Union[Unset, bool] = UNSET,
    require_non_anamorphic: Union[Unset, bool] = UNSET,
    transcoding_max_audio_channels: Union[Unset, int] = UNSET,
    cpu_core_limit: Union[Unset, int] = UNSET,
    live_stream_id: Union[Unset, str] = UNSET,
    enable_mpegts_m2_ts_mode: Union[Unset, bool] = UNSET,
    video_codec: Union[Unset, str] = UNSET,
    subtitle_codec: Union[Unset, str] = UNSET,
    transcode_reasons: Union[Unset, str] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    video_stream_index: Union[Unset, int] = UNSET,
    context: Union[Unset, EncodingContext] = UNSET,
    stream_options: Union[Unset, "GetVariantHlsVideoPlaylistStreamOptions"] = UNSET,
) -> Response[Any]:
    """Gets a video stream using HTTP live streaming.

    Args:
        item_id (str):
        static (Union[Unset, bool]):
        params (Union[Unset, str]):
        tag (Union[Unset, str]):
        device_profile_id (Union[Unset, str]):
        play_session_id (Union[Unset, str]):
        segment_container (Union[Unset, str]):
        segment_length (Union[Unset, int]):
        min_segments (Union[Unset, int]):
        media_source_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        audio_codec (Union[Unset, str]):
        enable_auto_stream_copy (Union[Unset, bool]):
        allow_video_stream_copy (Union[Unset, bool]):
        allow_audio_stream_copy (Union[Unset, bool]):
        break_on_non_key_frames (Union[Unset, bool]):
        audio_sample_rate (Union[Unset, int]):
        max_audio_bit_depth (Union[Unset, int]):
        audio_bit_rate (Union[Unset, int]):
        audio_channels (Union[Unset, int]):
        max_audio_channels (Union[Unset, int]):
        profile (Union[Unset, str]):
        level (Union[Unset, str]):
        framerate (Union[Unset, float]):
        max_framerate (Union[Unset, float]):
        copy_timestamps (Union[Unset, bool]):
        start_time_ticks (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        video_bit_rate (Union[Unset, int]):
        subtitle_stream_index (Union[Unset, int]):
        subtitle_method (Union[Unset, SubtitleDeliveryMethod]): Delivery method to use during
            playback of a specific subtitle format.
        max_ref_frames (Union[Unset, int]):
        max_video_bit_depth (Union[Unset, int]):
        require_avc (Union[Unset, bool]):
        de_interlace (Union[Unset, bool]):
        require_non_anamorphic (Union[Unset, bool]):
        transcoding_max_audio_channels (Union[Unset, int]):
        cpu_core_limit (Union[Unset, int]):
        live_stream_id (Union[Unset, str]):
        enable_mpegts_m2_ts_mode (Union[Unset, bool]):
        video_codec (Union[Unset, str]):
        subtitle_codec (Union[Unset, str]):
        transcode_reasons (Union[Unset, str]):
        audio_stream_index (Union[Unset, int]):
        video_stream_index (Union[Unset, int]):
        context (Union[Unset, EncodingContext]):
        stream_options (Union[Unset, GetVariantHlsVideoPlaylistStreamOptions]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        static=static,
        params=params,
        tag=tag,
        device_profile_id=device_profile_id,
        play_session_id=play_session_id,
        segment_container=segment_container,
        segment_length=segment_length,
        min_segments=min_segments,
        media_source_id=media_source_id,
        device_id=device_id,
        audio_codec=audio_codec,
        enable_auto_stream_copy=enable_auto_stream_copy,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
        break_on_non_key_frames=break_on_non_key_frames,
        audio_sample_rate=audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        audio_bit_rate=audio_bit_rate,
        audio_channels=audio_channels,
        max_audio_channels=max_audio_channels,
        profile=profile,
        level=level,
        framerate=framerate,
        max_framerate=max_framerate,
        copy_timestamps=copy_timestamps,
        start_time_ticks=start_time_ticks,
        width=width,
        height=height,
        max_width=max_width,
        max_height=max_height,
        video_bit_rate=video_bit_rate,
        subtitle_stream_index=subtitle_stream_index,
        subtitle_method=subtitle_method,
        max_ref_frames=max_ref_frames,
        max_video_bit_depth=max_video_bit_depth,
        require_avc=require_avc,
        de_interlace=de_interlace,
        require_non_anamorphic=require_non_anamorphic,
        transcoding_max_audio_channels=transcoding_max_audio_channels,
        cpu_core_limit=cpu_core_limit,
        live_stream_id=live_stream_id,
        enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode,
        video_codec=video_codec,
        subtitle_codec=subtitle_codec,
        transcode_reasons=transcode_reasons,
        audio_stream_index=audio_stream_index,
        video_stream_index=video_stream_index,
        context=context,
        stream_options=stream_options,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    static: Union[Unset, bool] = UNSET,
    params: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    device_profile_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    segment_container: Union[Unset, str] = UNSET,
    segment_length: Union[Unset, int] = UNSET,
    min_segments: Union[Unset, int] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    audio_codec: Union[Unset, str] = UNSET,
    enable_auto_stream_copy: Union[Unset, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, bool] = UNSET,
    audio_sample_rate: Union[Unset, int] = UNSET,
    max_audio_bit_depth: Union[Unset, int] = UNSET,
    audio_bit_rate: Union[Unset, int] = UNSET,
    audio_channels: Union[Unset, int] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    profile: Union[Unset, str] = UNSET,
    level: Union[Unset, str] = UNSET,
    framerate: Union[Unset, float] = UNSET,
    max_framerate: Union[Unset, float] = UNSET,
    copy_timestamps: Union[Unset, bool] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    video_bit_rate: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    subtitle_method: Union[Unset, SubtitleDeliveryMethod] = UNSET,
    max_ref_frames: Union[Unset, int] = UNSET,
    max_video_bit_depth: Union[Unset, int] = UNSET,
    require_avc: Union[Unset, bool] = UNSET,
    de_interlace: Union[Unset, bool] = UNSET,
    require_non_anamorphic: Union[Unset, bool] = UNSET,
    transcoding_max_audio_channels: Union[Unset, int] = UNSET,
    cpu_core_limit: Union[Unset, int] = UNSET,
    live_stream_id: Union[Unset, str] = UNSET,
    enable_mpegts_m2_ts_mode: Union[Unset, bool] = UNSET,
    video_codec: Union[Unset, str] = UNSET,
    subtitle_codec: Union[Unset, str] = UNSET,
    transcode_reasons: Union[Unset, str] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    video_stream_index: Union[Unset, int] = UNSET,
    context: Union[Unset, EncodingContext] = UNSET,
    stream_options: Union[Unset, "GetVariantHlsVideoPlaylistStreamOptions"] = UNSET,
) -> Response[Any]:
    """Gets a video stream using HTTP live streaming.

    Args:
        item_id (str):
        static (Union[Unset, bool]):
        params (Union[Unset, str]):
        tag (Union[Unset, str]):
        device_profile_id (Union[Unset, str]):
        play_session_id (Union[Unset, str]):
        segment_container (Union[Unset, str]):
        segment_length (Union[Unset, int]):
        min_segments (Union[Unset, int]):
        media_source_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        audio_codec (Union[Unset, str]):
        enable_auto_stream_copy (Union[Unset, bool]):
        allow_video_stream_copy (Union[Unset, bool]):
        allow_audio_stream_copy (Union[Unset, bool]):
        break_on_non_key_frames (Union[Unset, bool]):
        audio_sample_rate (Union[Unset, int]):
        max_audio_bit_depth (Union[Unset, int]):
        audio_bit_rate (Union[Unset, int]):
        audio_channels (Union[Unset, int]):
        max_audio_channels (Union[Unset, int]):
        profile (Union[Unset, str]):
        level (Union[Unset, str]):
        framerate (Union[Unset, float]):
        max_framerate (Union[Unset, float]):
        copy_timestamps (Union[Unset, bool]):
        start_time_ticks (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        video_bit_rate (Union[Unset, int]):
        subtitle_stream_index (Union[Unset, int]):
        subtitle_method (Union[Unset, SubtitleDeliveryMethod]): Delivery method to use during
            playback of a specific subtitle format.
        max_ref_frames (Union[Unset, int]):
        max_video_bit_depth (Union[Unset, int]):
        require_avc (Union[Unset, bool]):
        de_interlace (Union[Unset, bool]):
        require_non_anamorphic (Union[Unset, bool]):
        transcoding_max_audio_channels (Union[Unset, int]):
        cpu_core_limit (Union[Unset, int]):
        live_stream_id (Union[Unset, str]):
        enable_mpegts_m2_ts_mode (Union[Unset, bool]):
        video_codec (Union[Unset, str]):
        subtitle_codec (Union[Unset, str]):
        transcode_reasons (Union[Unset, str]):
        audio_stream_index (Union[Unset, int]):
        video_stream_index (Union[Unset, int]):
        context (Union[Unset, EncodingContext]):
        stream_options (Union[Unset, GetVariantHlsVideoPlaylistStreamOptions]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        static=static,
        params=params,
        tag=tag,
        device_profile_id=device_profile_id,
        play_session_id=play_session_id,
        segment_container=segment_container,
        segment_length=segment_length,
        min_segments=min_segments,
        media_source_id=media_source_id,
        device_id=device_id,
        audio_codec=audio_codec,
        enable_auto_stream_copy=enable_auto_stream_copy,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
        break_on_non_key_frames=break_on_non_key_frames,
        audio_sample_rate=audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        audio_bit_rate=audio_bit_rate,
        audio_channels=audio_channels,
        max_audio_channels=max_audio_channels,
        profile=profile,
        level=level,
        framerate=framerate,
        max_framerate=max_framerate,
        copy_timestamps=copy_timestamps,
        start_time_ticks=start_time_ticks,
        width=width,
        height=height,
        max_width=max_width,
        max_height=max_height,
        video_bit_rate=video_bit_rate,
        subtitle_stream_index=subtitle_stream_index,
        subtitle_method=subtitle_method,
        max_ref_frames=max_ref_frames,
        max_video_bit_depth=max_video_bit_depth,
        require_avc=require_avc,
        de_interlace=de_interlace,
        require_non_anamorphic=require_non_anamorphic,
        transcoding_max_audio_channels=transcoding_max_audio_channels,
        cpu_core_limit=cpu_core_limit,
        live_stream_id=live_stream_id,
        enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode,
        video_codec=video_codec,
        subtitle_codec=subtitle_codec,
        transcode_reasons=transcode_reasons,
        audio_stream_index=audio_stream_index,
        video_stream_index=video_stream_index,
        context=context,
        stream_options=stream_options,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
