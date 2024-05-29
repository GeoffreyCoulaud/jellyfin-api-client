from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem_details import ProblemDetails


def _get_kwargs(
    item_id: str,
    media_source_id: str,
    index: int,
    *,
    segment_length: int,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["segmentLength"] = segment_length

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Videos/{item_id}/{media_source_id}/Subtitles/{index}/subtitles.m3u8".format(
            item_id=item_id,
            media_source_id=media_source_id,
            index=index,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
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
    media_source_id: str,
    index: int,
    *,
    client: AuthenticatedClient,
    segment_length: int,
) -> Response[Union[Any, ProblemDetails]]:
    """Gets an HLS subtitle playlist.

    Args:
        item_id (str):
        media_source_id (str):
        index (int):
        segment_length (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        segment_length=segment_length,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    media_source_id: str,
    index: int,
    *,
    client: AuthenticatedClient,
    segment_length: int,
) -> Optional[Union[Any, ProblemDetails]]:
    """Gets an HLS subtitle playlist.

    Args:
        item_id (str):
        media_source_id (str):
        index (int):
        segment_length (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        client=client,
        segment_length=segment_length,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    media_source_id: str,
    index: int,
    *,
    client: AuthenticatedClient,
    segment_length: int,
) -> Response[Union[Any, ProblemDetails]]:
    """Gets an HLS subtitle playlist.

    Args:
        item_id (str):
        media_source_id (str):
        index (int):
        segment_length (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        segment_length=segment_length,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    media_source_id: str,
    index: int,
    *,
    client: AuthenticatedClient,
    segment_length: int,
) -> Optional[Union[Any, ProblemDetails]]:
    """Gets an HLS subtitle playlist.

    Args:
        item_id (str):
        media_source_id (str):
        index (int):
        segment_length (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            media_source_id=media_source_id,
            index=index,
            client=client,
            segment_length=segment_length,
        )
    ).parsed
