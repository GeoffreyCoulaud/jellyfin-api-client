from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.base_item_kind import BaseItemKind
from typing import cast, List
from ...types import UNSET, Unset
from typing import Dict
from typing import Union
from ...models.image_type import ImageType
from typing import cast
from ...models.base_item_dto import BaseItemDto
from ...models.item_fields import ItemFields


def _get_kwargs(
    *,
    user_id: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_played: Union[Unset, bool] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 20,
    group_items: Union[Unset, bool] = True,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["userId"] = user_id

    params["parentId"] = parent_id

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    json_include_item_types: Union[Unset, List[str]] = UNSET
    if not isinstance(include_item_types, Unset):
        json_include_item_types = []
        for include_item_types_item_data in include_item_types:
            include_item_types_item = include_item_types_item_data.value
            json_include_item_types.append(include_item_types_item)

    params["includeItemTypes"] = json_include_item_types

    params["isPlayed"] = is_played

    params["enableImages"] = enable_images

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: Union[Unset, List[str]] = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params["enableUserData"] = enable_user_data

    params["limit"] = limit

    params["groupItems"] = group_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Items/Latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["BaseItemDto"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BaseItemDto.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["BaseItemDto"]]]:
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
    fields: Union[Unset, List[ItemFields]] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_played: Union[Unset, bool] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 20,
    group_items: Union[Unset, bool] = True,
) -> Response[Union[Any, List["BaseItemDto"]]]:
    """Gets latest media.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_played (Union[Unset, bool]):
        enable_images (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        enable_user_data (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 20.
        group_items (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['BaseItemDto']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        include_item_types=include_item_types,
        is_played=is_played,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        limit=limit,
        group_items=group_items,
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
    fields: Union[Unset, List[ItemFields]] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_played: Union[Unset, bool] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 20,
    group_items: Union[Unset, bool] = True,
) -> Optional[Union[Any, List["BaseItemDto"]]]:
    """Gets latest media.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_played (Union[Unset, bool]):
        enable_images (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        enable_user_data (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 20.
        group_items (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['BaseItemDto']]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        include_item_types=include_item_types,
        is_played=is_played,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        limit=limit,
        group_items=group_items,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_played: Union[Unset, bool] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 20,
    group_items: Union[Unset, bool] = True,
) -> Response[Union[Any, List["BaseItemDto"]]]:
    """Gets latest media.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_played (Union[Unset, bool]):
        enable_images (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        enable_user_data (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 20.
        group_items (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['BaseItemDto']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        include_item_types=include_item_types,
        is_played=is_played,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        limit=limit,
        group_items=group_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    include_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    is_played: Union[Unset, bool] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 20,
    group_items: Union[Unset, bool] = True,
) -> Optional[Union[Any, List["BaseItemDto"]]]:
    """Gets latest media.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        is_played (Union[Unset, bool]):
        enable_images (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        enable_user_data (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 20.
        group_items (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['BaseItemDto']]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            parent_id=parent_id,
            fields=fields,
            include_item_types=include_item_types,
            is_played=is_played,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
            limit=limit,
            group_items=group_items,
        )
    ).parsed
