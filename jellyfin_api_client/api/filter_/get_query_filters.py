from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.base_item_kind import BaseItemKind
from ...models.query_filters import QueryFilters


def _get_kwargs(
    *,
    user_id: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_airing: Union[Unset, bool] = UNSET,
    is_movie: Union[Unset, bool] = UNSET,
    is_sports: Union[Unset, bool] = UNSET,
    is_kids: Union[Unset, bool] = UNSET,
    is_news: Union[Unset, bool] = UNSET,
    is_series: Union[Unset, bool] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["userId"] = user_id

    params["parentId"] = parent_id

    json_include_item_types: Union[Unset, List[str]] = UNSET
    if not isinstance(include_item_types, Unset):
        json_include_item_types = []
        for include_item_types_item_data in include_item_types:
            include_item_types_item = include_item_types_item_data.value
            json_include_item_types.append(include_item_types_item)

    params["includeItemTypes"] = json_include_item_types

    params["isAiring"] = is_airing

    params["isMovie"] = is_movie

    params["isSports"] = is_sports

    params["isKids"] = is_kids

    params["isNews"] = is_news

    params["isSeries"] = is_series

    params["recursive"] = recursive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Items/Filters2",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, QueryFilters]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryFilters.from_dict(response.json())

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
) -> Response[Union[Any, QueryFilters]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_airing: Union[Unset, bool] = UNSET,
    is_movie: Union[Unset, bool] = UNSET,
    is_sports: Union[Unset, bool] = UNSET,
    is_kids: Union[Unset, bool] = UNSET,
    is_news: Union[Unset, bool] = UNSET,
    is_series: Union[Unset, bool] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, QueryFilters]]:
    """Gets query filters.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_airing (Union[Unset, bool]):
        is_movie (Union[Unset, bool]):
        is_sports (Union[Unset, bool]):
        is_kids (Union[Unset, bool]):
        is_news (Union[Unset, bool]):
        is_series (Union[Unset, bool]):
        recursive (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QueryFilters]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        include_item_types=include_item_types,
        is_airing=is_airing,
        is_movie=is_movie,
        is_sports=is_sports,
        is_kids=is_kids,
        is_news=is_news,
        is_series=is_series,
        recursive=recursive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_airing: Union[Unset, bool] = UNSET,
    is_movie: Union[Unset, bool] = UNSET,
    is_sports: Union[Unset, bool] = UNSET,
    is_kids: Union[Unset, bool] = UNSET,
    is_news: Union[Unset, bool] = UNSET,
    is_series: Union[Unset, bool] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, QueryFilters]]:
    """Gets query filters.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_airing (Union[Unset, bool]):
        is_movie (Union[Unset, bool]):
        is_sports (Union[Unset, bool]):
        is_kids (Union[Unset, bool]):
        is_news (Union[Unset, bool]):
        is_series (Union[Unset, bool]):
        recursive (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QueryFilters]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        parent_id=parent_id,
        include_item_types=include_item_types,
        is_airing=is_airing,
        is_movie=is_movie,
        is_sports=is_sports,
        is_kids=is_kids,
        is_news=is_news,
        is_series=is_series,
        recursive=recursive,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_airing: Union[Unset, bool] = UNSET,
    is_movie: Union[Unset, bool] = UNSET,
    is_sports: Union[Unset, bool] = UNSET,
    is_kids: Union[Unset, bool] = UNSET,
    is_news: Union[Unset, bool] = UNSET,
    is_series: Union[Unset, bool] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, QueryFilters]]:
    """Gets query filters.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_airing (Union[Unset, bool]):
        is_movie (Union[Unset, bool]):
        is_sports (Union[Unset, bool]):
        is_kids (Union[Unset, bool]):
        is_news (Union[Unset, bool]):
        is_series (Union[Unset, bool]):
        recursive (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QueryFilters]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        include_item_types=include_item_types,
        is_airing=is_airing,
        is_movie=is_movie,
        is_sports=is_sports,
        is_kids=is_kids,
        is_news=is_news,
        is_series=is_series,
        recursive=recursive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_airing: Union[Unset, bool] = UNSET,
    is_movie: Union[Unset, bool] = UNSET,
    is_sports: Union[Unset, bool] = UNSET,
    is_kids: Union[Unset, bool] = UNSET,
    is_news: Union[Unset, bool] = UNSET,
    is_series: Union[Unset, bool] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, QueryFilters]]:
    """Gets query filters.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_airing (Union[Unset, bool]):
        is_movie (Union[Unset, bool]):
        is_sports (Union[Unset, bool]):
        is_kids (Union[Unset, bool]):
        is_news (Union[Unset, bool]):
        is_series (Union[Unset, bool]):
        recursive (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QueryFilters]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            parent_id=parent_id,
            include_item_types=include_item_types,
            is_airing=is_airing,
            is_movie=is_movie,
            is_sports=is_sports,
            is_kids=is_kids,
            is_news=is_news,
            is_series=is_series,
            recursive=recursive,
        )
    ).parsed
