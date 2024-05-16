from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast, List
from typing import Dict
from typing import cast
from ...models.remote_search_result import RemoteSearchResult
from ...models.movie_info_remote_search_query import MovieInfoRemoteSearchQuery


def _get_kwargs(
    *,
    body: Union[
        MovieInfoRemoteSearchQuery,
        MovieInfoRemoteSearchQuery,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/Items/RemoteSearch/Movie",
    }

    if isinstance(body, MovieInfoRemoteSearchQuery):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, MovieInfoRemoteSearchQuery):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["RemoteSearchResult"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RemoteSearchResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, List["RemoteSearchResult"]]]:
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
        MovieInfoRemoteSearchQuery,
        MovieInfoRemoteSearchQuery,
    ],
) -> Response[Union[Any, List["RemoteSearchResult"]]]:
    """Get movie remote search.

    Args:
        body (MovieInfoRemoteSearchQuery):
        body (MovieInfoRemoteSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['RemoteSearchResult']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        MovieInfoRemoteSearchQuery,
        MovieInfoRemoteSearchQuery,
    ],
) -> Optional[Union[Any, List["RemoteSearchResult"]]]:
    """Get movie remote search.

    Args:
        body (MovieInfoRemoteSearchQuery):
        body (MovieInfoRemoteSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['RemoteSearchResult']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        MovieInfoRemoteSearchQuery,
        MovieInfoRemoteSearchQuery,
    ],
) -> Response[Union[Any, List["RemoteSearchResult"]]]:
    """Get movie remote search.

    Args:
        body (MovieInfoRemoteSearchQuery):
        body (MovieInfoRemoteSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['RemoteSearchResult']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        MovieInfoRemoteSearchQuery,
        MovieInfoRemoteSearchQuery,
    ],
) -> Optional[Union[Any, List["RemoteSearchResult"]]]:
    """Get movie remote search.

    Args:
        body (MovieInfoRemoteSearchQuery):
        body (MovieInfoRemoteSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['RemoteSearchResult']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
