from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.item_fields import ItemFields
from ...models.image_type import ImageType
from ...models.sort_order import SortOrder
from ...models.base_item_kind import BaseItemKind
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_sort_by import ItemSortBy


def _get_kwargs(
    *,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, str] = UNSET,
    name_starts_with: Union[Unset, str] = UNSET,
    name_less_than: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, List[ItemSortBy]] = UNSET,
    sort_order: Union[Unset, List[SortOrder]] = UNSET,
    enable_images: Union[Unset, bool] = True,
    enable_total_record_count: Union[Unset, bool] = True,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["startIndex"] = start_index

    params["limit"] = limit

    params["searchTerm"] = search_term

    params["parentId"] = parent_id

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    json_exclude_item_types: Union[Unset, List[str]] = UNSET
    if not isinstance(exclude_item_types, Unset):
        json_exclude_item_types = []
        for exclude_item_types_item_data in exclude_item_types:
            exclude_item_types_item = exclude_item_types_item_data.value
            json_exclude_item_types.append(exclude_item_types_item)

    params["excludeItemTypes"] = json_exclude_item_types

    json_include_item_types: Union[Unset, List[str]] = UNSET
    if not isinstance(include_item_types, Unset):
        json_include_item_types = []
        for include_item_types_item_data in include_item_types:
            include_item_types_item = include_item_types_item_data.value
            json_include_item_types.append(include_item_types_item)

    params["includeItemTypes"] = json_include_item_types

    params["isFavorite"] = is_favorite

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: Union[Unset, List[str]] = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params["userId"] = user_id

    params["nameStartsWithOrGreater"] = name_starts_with_or_greater

    params["nameStartsWith"] = name_starts_with

    params["nameLessThan"] = name_less_than

    json_sort_by: Union[Unset, List[str]] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = []
        for sort_by_item_data in sort_by:
            sort_by_item = sort_by_item_data.value
            json_sort_by.append(sort_by_item)

    params["sortBy"] = json_sort_by

    json_sort_order: Union[Unset, List[str]] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = []
        for sort_order_item_data in sort_order:
            sort_order_item = sort_order_item_data.value
            json_sort_order.append(sort_order_item)

    params["sortOrder"] = json_sort_order

    params["enableImages"] = enable_images

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Genres",
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
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, str] = UNSET,
    name_starts_with: Union[Unset, str] = UNSET,
    name_less_than: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, List[ItemSortBy]] = UNSET,
    sort_order: Union[Unset, List[SortOrder]] = UNSET,
    enable_images: Union[Unset, bool] = True,
    enable_total_record_count: Union[Unset, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all genres from a given item, folder, or the entire library.

    Args:
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        search_term (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        exclude_item_types (Union[Unset, List[BaseItemKind]]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_favorite (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        user_id (Union[Unset, str]):
        name_starts_with_or_greater (Union[Unset, str]):
        name_starts_with (Union[Unset, str]):
        name_less_than (Union[Unset, str]):
        sort_by (Union[Unset, List[ItemSortBy]]):
        sort_order (Union[Unset, List[SortOrder]]):
        enable_images (Union[Unset, bool]):  Default: True.
        enable_total_record_count (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        is_favorite=is_favorite,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, str] = UNSET,
    name_starts_with: Union[Unset, str] = UNSET,
    name_less_than: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, List[ItemSortBy]] = UNSET,
    sort_order: Union[Unset, List[SortOrder]] = UNSET,
    enable_images: Union[Unset, bool] = True,
    enable_total_record_count: Union[Unset, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all genres from a given item, folder, or the entire library.

    Args:
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        search_term (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        exclude_item_types (Union[Unset, List[BaseItemKind]]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_favorite (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        user_id (Union[Unset, str]):
        name_starts_with_or_greater (Union[Unset, str]):
        name_starts_with (Union[Unset, str]):
        name_less_than (Union[Unset, str]):
        sort_by (Union[Unset, List[ItemSortBy]]):
        sort_order (Union[Unset, List[SortOrder]]):
        enable_images (Union[Unset, bool]):  Default: True.
        enable_total_record_count (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        is_favorite=is_favorite,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, str] = UNSET,
    name_starts_with: Union[Unset, str] = UNSET,
    name_less_than: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, List[ItemSortBy]] = UNSET,
    sort_order: Union[Unset, List[SortOrder]] = UNSET,
    enable_images: Union[Unset, bool] = True,
    enable_total_record_count: Union[Unset, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all genres from a given item, folder, or the entire library.

    Args:
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        search_term (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        exclude_item_types (Union[Unset, List[BaseItemKind]]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_favorite (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        user_id (Union[Unset, str]):
        name_starts_with_or_greater (Union[Unset, str]):
        name_starts_with (Union[Unset, str]):
        name_less_than (Union[Unset, str]):
        sort_by (Union[Unset, List[ItemSortBy]]):
        sort_order (Union[Unset, List[SortOrder]]):
        enable_images (Union[Unset, bool]):  Default: True.
        enable_total_record_count (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        is_favorite=is_favorite,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, str] = UNSET,
    name_starts_with: Union[Unset, str] = UNSET,
    name_less_than: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, List[ItemSortBy]] = UNSET,
    sort_order: Union[Unset, List[SortOrder]] = UNSET,
    enable_images: Union[Unset, bool] = True,
    enable_total_record_count: Union[Unset, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all genres from a given item, folder, or the entire library.

    Args:
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        search_term (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        exclude_item_types (Union[Unset, List[BaseItemKind]]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_favorite (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        user_id (Union[Unset, str]):
        name_starts_with_or_greater (Union[Unset, str]):
        name_starts_with (Union[Unset, str]):
        name_less_than (Union[Unset, str]):
        sort_by (Union[Unset, List[ItemSortBy]]):
        sort_order (Union[Unset, List[SortOrder]]):
        enable_images (Union[Unset, bool]):  Default: True.
        enable_total_record_count (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_index=start_index,
            limit=limit,
            search_term=search_term,
            parent_id=parent_id,
            fields=fields,
            exclude_item_types=exclude_item_types,
            include_item_types=include_item_types,
            is_favorite=is_favorite,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            user_id=user_id,
            name_starts_with_or_greater=name_starts_with_or_greater,
            name_starts_with=name_starts_with,
            name_less_than=name_less_than,
            sort_by=sort_by,
            sort_order=sort_order,
            enable_images=enable_images,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
