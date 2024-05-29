from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.base_item_kind import BaseItemKind
from ...types import Unset
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.media_type import MediaType


def _get_kwargs(
    *,
    user_id: Union[Unset, str] = UNSET,
    media_type: Union[Unset, List[MediaType]] = UNSET,
    type: Union[Unset, List[BaseItemKind]] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    enable_total_record_count: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["userId"] = user_id

    json_media_type: Union[Unset, List[str]] = UNSET
    if not isinstance(media_type, Unset):
        json_media_type = []
        for media_type_item_data in media_type:
            media_type_item = media_type_item_data.value
            json_media_type.append(media_type_item)

    params["mediaType"] = json_media_type

    json_type: Union[Unset, List[str]] = UNSET
    if not isinstance(type, Unset):
        json_type = []
        for type_item_data in type:
            type_item = type_item_data.value
            json_type.append(type_item)

    params["type"] = json_type

    params["startIndex"] = start_index

    params["limit"] = limit

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Items/Suggestions",
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
    media_type: Union[Unset, List[MediaType]] = UNSET,
    type: Union[Unset, List[BaseItemKind]] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    enable_total_record_count: Union[Unset, bool] = False,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets suggestions.

    Args:
        user_id (Union[Unset, str]):
        media_type (Union[Unset, List[MediaType]]):
        type (Union[Unset, List[BaseItemKind]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        enable_total_record_count (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        media_type=media_type,
        type=type,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    media_type: Union[Unset, List[MediaType]] = UNSET,
    type: Union[Unset, List[BaseItemKind]] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    enable_total_record_count: Union[Unset, bool] = False,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets suggestions.

    Args:
        user_id (Union[Unset, str]):
        media_type (Union[Unset, List[MediaType]]):
        type (Union[Unset, List[BaseItemKind]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        enable_total_record_count (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        media_type=media_type,
        type=type,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    media_type: Union[Unset, List[MediaType]] = UNSET,
    type: Union[Unset, List[BaseItemKind]] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    enable_total_record_count: Union[Unset, bool] = False,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets suggestions.

    Args:
        user_id (Union[Unset, str]):
        media_type (Union[Unset, List[MediaType]]):
        type (Union[Unset, List[BaseItemKind]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        enable_total_record_count (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        media_type=media_type,
        type=type,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    media_type: Union[Unset, List[MediaType]] = UNSET,
    type: Union[Unset, List[BaseItemKind]] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    enable_total_record_count: Union[Unset, bool] = False,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets suggestions.

    Args:
        user_id (Union[Unset, str]):
        media_type (Union[Unset, List[MediaType]]):
        type (Union[Unset, List[BaseItemKind]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        enable_total_record_count (Union[Unset, bool]):  Default: False.

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
            media_type=media_type,
            type=type,
            start_index=start_index,
            limit=limit,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
