from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast, List
from ...types import UNSET, Unset
from typing import Dict
from typing import Union
from typing import cast
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    playlist_id: str,
    *,
    ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids"] = json_ids

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/Playlists/{playlist_id}/Items".format(
            playlist_id=playlist_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, ProblemDetails]]:
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
    ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Adds items to a playlist.

    Args:
        playlist_id (str):
        ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        ids=ids,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Adds items to a playlist.

    Args:
        playlist_id (str):
        ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
        ids=ids,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Adds items to a playlist.

    Args:
        playlist_id (str):
        ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        ids=ids,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Adds items to a playlist.

    Args:
        playlist_id (str):
        ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
            ids=ids,
            user_id=user_id,
        )
    ).parsed
