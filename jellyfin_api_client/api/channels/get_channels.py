from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...types import Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, str] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    supports_latest_items: Union[Unset, bool] = UNSET,
    supports_media_deletion: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["userId"] = user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    params["supportsLatestItems"] = supports_latest_items

    params["supportsMediaDeletion"] = supports_media_deletion

    params["isFavorite"] = is_favorite

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Channels",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

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
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
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
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    supports_latest_items: Union[Unset, bool] = UNSET,
    supports_media_deletion: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available channels.

    Args:
        user_id (Union[Unset, str]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        supports_latest_items (Union[Unset, bool]):
        supports_media_deletion (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        supports_latest_items=supports_latest_items,
        supports_media_deletion=supports_media_deletion,
        is_favorite=is_favorite,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    supports_latest_items: Union[Unset, bool] = UNSET,
    supports_media_deletion: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available channels.

    Args:
        user_id (Union[Unset, str]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        supports_latest_items (Union[Unset, bool]):
        supports_media_deletion (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        supports_latest_items=supports_latest_items,
        supports_media_deletion=supports_media_deletion,
        is_favorite=is_favorite,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    supports_latest_items: Union[Unset, bool] = UNSET,
    supports_media_deletion: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available channels.

    Args:
        user_id (Union[Unset, str]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        supports_latest_items (Union[Unset, bool]):
        supports_media_deletion (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        supports_latest_items=supports_latest_items,
        supports_media_deletion=supports_media_deletion,
        is_favorite=is_favorite,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    supports_latest_items: Union[Unset, bool] = UNSET,
    supports_media_deletion: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available channels.

    Args:
        user_id (Union[Unset, str]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        supports_latest_items (Union[Unset, bool]):
        supports_media_deletion (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            supports_latest_items=supports_latest_items,
            supports_media_deletion=supports_media_deletion,
            is_favorite=is_favorite,
        )
    ).parsed
