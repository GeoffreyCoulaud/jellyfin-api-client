from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.problem_details import ProblemDetails
from ...models.media_stream_protocol import MediaStreamProtocol


def _get_kwargs(
    item_id: str,
    *,
    container: Union[Unset, List[str]] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    audio_codec: Union[Unset, str] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    transcoding_audio_channels: Union[Unset, int] = UNSET,
    max_streaming_bitrate: Union[Unset, int] = UNSET,
    audio_bit_rate: Union[Unset, int] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    transcoding_container: Union[Unset, str] = UNSET,
    transcoding_protocol: Union[Unset, MediaStreamProtocol] = UNSET,
    max_audio_sample_rate: Union[Unset, int] = UNSET,
    max_audio_bit_depth: Union[Unset, int] = UNSET,
    enable_remote_media: Union[Unset, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, bool] = False,
    enable_redirection: Union[Unset, bool] = True,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_container: Union[Unset, List[str]] = UNSET
    if not isinstance(container, Unset):
        json_container = container

    params["container"] = json_container

    params["mediaSourceId"] = media_source_id

    params["deviceId"] = device_id

    params["userId"] = user_id

    params["audioCodec"] = audio_codec

    params["maxAudioChannels"] = max_audio_channels

    params["transcodingAudioChannels"] = transcoding_audio_channels

    params["maxStreamingBitrate"] = max_streaming_bitrate

    params["audioBitRate"] = audio_bit_rate

    params["startTimeTicks"] = start_time_ticks

    params["transcodingContainer"] = transcoding_container

    json_transcoding_protocol: Union[Unset, str] = UNSET
    if not isinstance(transcoding_protocol, Unset):
        json_transcoding_protocol = transcoding_protocol.value

    params["transcodingProtocol"] = json_transcoding_protocol

    params["maxAudioSampleRate"] = max_audio_sample_rate

    params["maxAudioBitDepth"] = max_audio_bit_depth

    params["enableRemoteMedia"] = enable_remote_media

    params["breakOnNonKeyFrames"] = break_on_non_key_frames

    params["enableRedirection"] = enable_redirection

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Audio/{item_id}/universal".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.FOUND:
        response_302 = cast(Any, None)
        return response_302
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProblemDetails]]:
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
    container: Union[Unset, List[str]] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    audio_codec: Union[Unset, str] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    transcoding_audio_channels: Union[Unset, int] = UNSET,
    max_streaming_bitrate: Union[Unset, int] = UNSET,
    audio_bit_rate: Union[Unset, int] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    transcoding_container: Union[Unset, str] = UNSET,
    transcoding_protocol: Union[Unset, MediaStreamProtocol] = UNSET,
    max_audio_sample_rate: Union[Unset, int] = UNSET,
    max_audio_bit_depth: Union[Unset, int] = UNSET,
    enable_remote_media: Union[Unset, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, bool] = False,
    enable_redirection: Union[Unset, bool] = True,
) -> Response[Union[Any, ProblemDetails]]:
    """Gets an audio stream.

    Args:
        item_id (str):
        container (Union[Unset, List[str]]):
        media_source_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        audio_codec (Union[Unset, str]):
        max_audio_channels (Union[Unset, int]):
        transcoding_audio_channels (Union[Unset, int]):
        max_streaming_bitrate (Union[Unset, int]):
        audio_bit_rate (Union[Unset, int]):
        start_time_ticks (Union[Unset, int]):
        transcoding_container (Union[Unset, str]):
        transcoding_protocol (Union[Unset, MediaStreamProtocol]): Media streaming protocol.
            Lowercase for backwards compatibility.
        max_audio_sample_rate (Union[Unset, int]):
        max_audio_bit_depth (Union[Unset, int]):
        enable_remote_media (Union[Unset, bool]):
        break_on_non_key_frames (Union[Unset, bool]):  Default: False.
        enable_redirection (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        container=container,
        media_source_id=media_source_id,
        device_id=device_id,
        user_id=user_id,
        audio_codec=audio_codec,
        max_audio_channels=max_audio_channels,
        transcoding_audio_channels=transcoding_audio_channels,
        max_streaming_bitrate=max_streaming_bitrate,
        audio_bit_rate=audio_bit_rate,
        start_time_ticks=start_time_ticks,
        transcoding_container=transcoding_container,
        transcoding_protocol=transcoding_protocol,
        max_audio_sample_rate=max_audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        enable_remote_media=enable_remote_media,
        break_on_non_key_frames=break_on_non_key_frames,
        enable_redirection=enable_redirection,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    container: Union[Unset, List[str]] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    audio_codec: Union[Unset, str] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    transcoding_audio_channels: Union[Unset, int] = UNSET,
    max_streaming_bitrate: Union[Unset, int] = UNSET,
    audio_bit_rate: Union[Unset, int] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    transcoding_container: Union[Unset, str] = UNSET,
    transcoding_protocol: Union[Unset, MediaStreamProtocol] = UNSET,
    max_audio_sample_rate: Union[Unset, int] = UNSET,
    max_audio_bit_depth: Union[Unset, int] = UNSET,
    enable_remote_media: Union[Unset, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, bool] = False,
    enable_redirection: Union[Unset, bool] = True,
) -> Optional[Union[Any, ProblemDetails]]:
    """Gets an audio stream.

    Args:
        item_id (str):
        container (Union[Unset, List[str]]):
        media_source_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        audio_codec (Union[Unset, str]):
        max_audio_channels (Union[Unset, int]):
        transcoding_audio_channels (Union[Unset, int]):
        max_streaming_bitrate (Union[Unset, int]):
        audio_bit_rate (Union[Unset, int]):
        start_time_ticks (Union[Unset, int]):
        transcoding_container (Union[Unset, str]):
        transcoding_protocol (Union[Unset, MediaStreamProtocol]): Media streaming protocol.
            Lowercase for backwards compatibility.
        max_audio_sample_rate (Union[Unset, int]):
        max_audio_bit_depth (Union[Unset, int]):
        enable_remote_media (Union[Unset, bool]):
        break_on_non_key_frames (Union[Unset, bool]):  Default: False.
        enable_redirection (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        container=container,
        media_source_id=media_source_id,
        device_id=device_id,
        user_id=user_id,
        audio_codec=audio_codec,
        max_audio_channels=max_audio_channels,
        transcoding_audio_channels=transcoding_audio_channels,
        max_streaming_bitrate=max_streaming_bitrate,
        audio_bit_rate=audio_bit_rate,
        start_time_ticks=start_time_ticks,
        transcoding_container=transcoding_container,
        transcoding_protocol=transcoding_protocol,
        max_audio_sample_rate=max_audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        enable_remote_media=enable_remote_media,
        break_on_non_key_frames=break_on_non_key_frames,
        enable_redirection=enable_redirection,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    container: Union[Unset, List[str]] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    audio_codec: Union[Unset, str] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    transcoding_audio_channels: Union[Unset, int] = UNSET,
    max_streaming_bitrate: Union[Unset, int] = UNSET,
    audio_bit_rate: Union[Unset, int] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    transcoding_container: Union[Unset, str] = UNSET,
    transcoding_protocol: Union[Unset, MediaStreamProtocol] = UNSET,
    max_audio_sample_rate: Union[Unset, int] = UNSET,
    max_audio_bit_depth: Union[Unset, int] = UNSET,
    enable_remote_media: Union[Unset, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, bool] = False,
    enable_redirection: Union[Unset, bool] = True,
) -> Response[Union[Any, ProblemDetails]]:
    """Gets an audio stream.

    Args:
        item_id (str):
        container (Union[Unset, List[str]]):
        media_source_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        audio_codec (Union[Unset, str]):
        max_audio_channels (Union[Unset, int]):
        transcoding_audio_channels (Union[Unset, int]):
        max_streaming_bitrate (Union[Unset, int]):
        audio_bit_rate (Union[Unset, int]):
        start_time_ticks (Union[Unset, int]):
        transcoding_container (Union[Unset, str]):
        transcoding_protocol (Union[Unset, MediaStreamProtocol]): Media streaming protocol.
            Lowercase for backwards compatibility.
        max_audio_sample_rate (Union[Unset, int]):
        max_audio_bit_depth (Union[Unset, int]):
        enable_remote_media (Union[Unset, bool]):
        break_on_non_key_frames (Union[Unset, bool]):  Default: False.
        enable_redirection (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        container=container,
        media_source_id=media_source_id,
        device_id=device_id,
        user_id=user_id,
        audio_codec=audio_codec,
        max_audio_channels=max_audio_channels,
        transcoding_audio_channels=transcoding_audio_channels,
        max_streaming_bitrate=max_streaming_bitrate,
        audio_bit_rate=audio_bit_rate,
        start_time_ticks=start_time_ticks,
        transcoding_container=transcoding_container,
        transcoding_protocol=transcoding_protocol,
        max_audio_sample_rate=max_audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        enable_remote_media=enable_remote_media,
        break_on_non_key_frames=break_on_non_key_frames,
        enable_redirection=enable_redirection,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    container: Union[Unset, List[str]] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    audio_codec: Union[Unset, str] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    transcoding_audio_channels: Union[Unset, int] = UNSET,
    max_streaming_bitrate: Union[Unset, int] = UNSET,
    audio_bit_rate: Union[Unset, int] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    transcoding_container: Union[Unset, str] = UNSET,
    transcoding_protocol: Union[Unset, MediaStreamProtocol] = UNSET,
    max_audio_sample_rate: Union[Unset, int] = UNSET,
    max_audio_bit_depth: Union[Unset, int] = UNSET,
    enable_remote_media: Union[Unset, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, bool] = False,
    enable_redirection: Union[Unset, bool] = True,
) -> Optional[Union[Any, ProblemDetails]]:
    """Gets an audio stream.

    Args:
        item_id (str):
        container (Union[Unset, List[str]]):
        media_source_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        audio_codec (Union[Unset, str]):
        max_audio_channels (Union[Unset, int]):
        transcoding_audio_channels (Union[Unset, int]):
        max_streaming_bitrate (Union[Unset, int]):
        audio_bit_rate (Union[Unset, int]):
        start_time_ticks (Union[Unset, int]):
        transcoding_container (Union[Unset, str]):
        transcoding_protocol (Union[Unset, MediaStreamProtocol]): Media streaming protocol.
            Lowercase for backwards compatibility.
        max_audio_sample_rate (Union[Unset, int]):
        max_audio_bit_depth (Union[Unset, int]):
        enable_remote_media (Union[Unset, bool]):
        break_on_non_key_frames (Union[Unset, bool]):  Default: False.
        enable_redirection (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            container=container,
            media_source_id=media_source_id,
            device_id=device_id,
            user_id=user_id,
            audio_codec=audio_codec,
            max_audio_channels=max_audio_channels,
            transcoding_audio_channels=transcoding_audio_channels,
            max_streaming_bitrate=max_streaming_bitrate,
            audio_bit_rate=audio_bit_rate,
            start_time_ticks=start_time_ticks,
            transcoding_container=transcoding_container,
            transcoding_protocol=transcoding_protocol,
            max_audio_sample_rate=max_audio_sample_rate,
            max_audio_bit_depth=max_audio_bit_depth,
            enable_remote_media=enable_remote_media,
            break_on_non_key_frames=break_on_non_key_frames,
            enable_redirection=enable_redirection,
        )
    ).parsed
