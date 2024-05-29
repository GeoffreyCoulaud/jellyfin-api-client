from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.playlist_user_permissions import PlaylistUserPermissions
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    playlist_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Playlists/{playlist_id}/Users".format(
            playlist_id=playlist_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["PlaylistUserPermissions"], ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PlaylistUserPermissions.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["PlaylistUserPermissions"], ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, List["PlaylistUserPermissions"], ProblemDetails]]:
    """Get a playlist's users.

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['PlaylistUserPermissions'], ProblemDetails]]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, List["PlaylistUserPermissions"], ProblemDetails]]:
    """Get a playlist's users.

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['PlaylistUserPermissions'], ProblemDetails]
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, List["PlaylistUserPermissions"], ProblemDetails]]:
    """Get a playlist's users.

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['PlaylistUserPermissions'], ProblemDetails]]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, List["PlaylistUserPermissions"], ProblemDetails]]:
    """Get a playlist's users.

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['PlaylistUserPermissions'], ProblemDetails]
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
        )
    ).parsed
