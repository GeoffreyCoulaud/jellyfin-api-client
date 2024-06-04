from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.open_live_stream_dto import OpenLiveStreamDto
from ...models.live_stream_response import LiveStreamResponse


def _get_kwargs(
    *,
    body: Union[
        OpenLiveStreamDto,
        OpenLiveStreamDto,
    ],
    open_token: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    max_streaming_bitrate: Union[Unset, int] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    item_id: Union[Unset, str] = UNSET,
    enable_direct_play: Union[Unset, bool] = UNSET,
    enable_direct_stream: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["openToken"] = open_token

    params["userId"] = user_id

    params["playSessionId"] = play_session_id

    params["maxStreamingBitrate"] = max_streaming_bitrate

    params["startTimeTicks"] = start_time_ticks

    params["audioStreamIndex"] = audio_stream_index

    params["subtitleStreamIndex"] = subtitle_stream_index

    params["maxAudioChannels"] = max_audio_channels

    params["itemId"] = item_id

    params["enableDirectPlay"] = enable_direct_play

    params["enableDirectStream"] = enable_direct_stream

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/LiveStreams/Open",
        "params": params,
    }

    if isinstance(body, OpenLiveStreamDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, OpenLiveStreamDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LiveStreamResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LiveStreamResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, LiveStreamResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        OpenLiveStreamDto,
        OpenLiveStreamDto,
    ],
    open_token: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    max_streaming_bitrate: Union[Unset, int] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    item_id: Union[Unset, str] = UNSET,
    enable_direct_play: Union[Unset, bool] = UNSET,
    enable_direct_stream: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, LiveStreamResponse]]:
    """Opens a media source.

    Args:
        open_token (Union[Unset, str]):
        user_id (Union[Unset, str]):
        play_session_id (Union[Unset, str]):
        max_streaming_bitrate (Union[Unset, int]):
        start_time_ticks (Union[Unset, int]):
        audio_stream_index (Union[Unset, int]):
        subtitle_stream_index (Union[Unset, int]):
        max_audio_channels (Union[Unset, int]):
        item_id (Union[Unset, str]):
        enable_direct_play (Union[Unset, bool]):
        enable_direct_stream (Union[Unset, bool]):
        body (OpenLiveStreamDto): Open live stream dto.
        body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LiveStreamResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        OpenLiveStreamDto,
        OpenLiveStreamDto,
    ],
    open_token: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    max_streaming_bitrate: Union[Unset, int] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    item_id: Union[Unset, str] = UNSET,
    enable_direct_play: Union[Unset, bool] = UNSET,
    enable_direct_stream: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, LiveStreamResponse]]:
    """Opens a media source.

    Args:
        open_token (Union[Unset, str]):
        user_id (Union[Unset, str]):
        play_session_id (Union[Unset, str]):
        max_streaming_bitrate (Union[Unset, int]):
        start_time_ticks (Union[Unset, int]):
        audio_stream_index (Union[Unset, int]):
        subtitle_stream_index (Union[Unset, int]):
        max_audio_channels (Union[Unset, int]):
        item_id (Union[Unset, str]):
        enable_direct_play (Union[Unset, bool]):
        enable_direct_stream (Union[Unset, bool]):
        body (OpenLiveStreamDto): Open live stream dto.
        body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LiveStreamResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        OpenLiveStreamDto,
        OpenLiveStreamDto,
    ],
    open_token: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    max_streaming_bitrate: Union[Unset, int] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    item_id: Union[Unset, str] = UNSET,
    enable_direct_play: Union[Unset, bool] = UNSET,
    enable_direct_stream: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, LiveStreamResponse]]:
    """Opens a media source.

    Args:
        open_token (Union[Unset, str]):
        user_id (Union[Unset, str]):
        play_session_id (Union[Unset, str]):
        max_streaming_bitrate (Union[Unset, int]):
        start_time_ticks (Union[Unset, int]):
        audio_stream_index (Union[Unset, int]):
        subtitle_stream_index (Union[Unset, int]):
        max_audio_channels (Union[Unset, int]):
        item_id (Union[Unset, str]):
        enable_direct_play (Union[Unset, bool]):
        enable_direct_stream (Union[Unset, bool]):
        body (OpenLiveStreamDto): Open live stream dto.
        body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LiveStreamResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        OpenLiveStreamDto,
        OpenLiveStreamDto,
    ],
    open_token: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    max_streaming_bitrate: Union[Unset, int] = UNSET,
    start_time_ticks: Union[Unset, int] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    max_audio_channels: Union[Unset, int] = UNSET,
    item_id: Union[Unset, str] = UNSET,
    enable_direct_play: Union[Unset, bool] = UNSET,
    enable_direct_stream: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, LiveStreamResponse]]:
    """Opens a media source.

    Args:
        open_token (Union[Unset, str]):
        user_id (Union[Unset, str]):
        play_session_id (Union[Unset, str]):
        max_streaming_bitrate (Union[Unset, int]):
        start_time_ticks (Union[Unset, int]):
        audio_stream_index (Union[Unset, int]):
        subtitle_stream_index (Union[Unset, int]):
        max_audio_channels (Union[Unset, int]):
        item_id (Union[Unset, str]):
        enable_direct_play (Union[Unset, bool]):
        enable_direct_stream (Union[Unset, bool]):
        body (OpenLiveStreamDto): Open live stream dto.
        body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LiveStreamResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
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
        )
    ).parsed
