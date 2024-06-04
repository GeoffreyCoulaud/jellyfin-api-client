from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.problem_details import ProblemDetails
from ...models.lyric_dto import LyricDto


def _get_kwargs(
    lyric_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Providers/Lyrics/{lyric_id}".format(
            lyric_id=lyric_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LyricDto, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LyricDto.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, LyricDto, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    lyric_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, LyricDto, ProblemDetails]]:
    """Gets the remote lyrics.

    Args:
        lyric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LyricDto, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        lyric_id=lyric_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    lyric_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, LyricDto, ProblemDetails]]:
    """Gets the remote lyrics.

    Args:
        lyric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LyricDto, ProblemDetails]
    """

    return sync_detailed(
        lyric_id=lyric_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    lyric_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, LyricDto, ProblemDetails]]:
    """Gets the remote lyrics.

    Args:
        lyric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LyricDto, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        lyric_id=lyric_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    lyric_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, LyricDto, ProblemDetails]]:
    """Gets the remote lyrics.

    Args:
        lyric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LyricDto, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            lyric_id=lyric_id,
            client=client,
        )
    ).parsed
