from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.play_method import PlayMethod


def _get_kwargs(
    item_id: str,
    *,
    media_source_id: Union[Unset, str] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    play_method: Union[Unset, PlayMethod] = UNSET,
    live_stream_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    can_seek: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["mediaSourceId"] = media_source_id

    params["audioStreamIndex"] = audio_stream_index

    params["subtitleStreamIndex"] = subtitle_stream_index

    json_play_method: Union[Unset, str] = UNSET
    if not isinstance(play_method, Unset):
        json_play_method = play_method.value

    params["playMethod"] = json_play_method

    params["liveStreamId"] = live_stream_id

    params["playSessionId"] = play_session_id

    params["canSeek"] = can_seek

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/PlayingItems/{item_id}".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
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
    media_source_id: Union[Unset, str] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    play_method: Union[Unset, PlayMethod] = UNSET,
    live_stream_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    can_seek: Union[Unset, bool] = False,
) -> Response[Any]:
    """Reports that a session has begun playing an item.

    Args:
        item_id (str):
        media_source_id (Union[Unset, str]):
        audio_stream_index (Union[Unset, int]):
        subtitle_stream_index (Union[Unset, int]):
        play_method (Union[Unset, PlayMethod]):
        live_stream_id (Union[Unset, str]):
        play_session_id (Union[Unset, str]):
        can_seek (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        media_source_id=media_source_id,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        play_method=play_method,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
        can_seek=can_seek,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    media_source_id: Union[Unset, str] = UNSET,
    audio_stream_index: Union[Unset, int] = UNSET,
    subtitle_stream_index: Union[Unset, int] = UNSET,
    play_method: Union[Unset, PlayMethod] = UNSET,
    live_stream_id: Union[Unset, str] = UNSET,
    play_session_id: Union[Unset, str] = UNSET,
    can_seek: Union[Unset, bool] = False,
) -> Response[Any]:
    """Reports that a session has begun playing an item.

    Args:
        item_id (str):
        media_source_id (Union[Unset, str]):
        audio_stream_index (Union[Unset, int]):
        subtitle_stream_index (Union[Unset, int]):
        play_method (Union[Unset, PlayMethod]):
        live_stream_id (Union[Unset, str]):
        play_session_id (Union[Unset, str]):
        can_seek (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        media_source_id=media_source_id,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        play_method=play_method,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
        can_seek=can_seek,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
