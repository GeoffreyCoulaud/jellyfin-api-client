from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.item_fields import ItemFields
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult


def _get_kwargs(
    item_id: str,
    *,
    exclude_artist_ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_exclude_artist_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(exclude_artist_ids, Unset):
        json_exclude_artist_ids = exclude_artist_ids

    params["excludeArtistIds"] = json_exclude_artist_ids

    params["userId"] = user_id

    params["limit"] = limit

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Albums/{item_id}/Similar".format(
            item_id=item_id,
        ),
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
    item_id: str,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets similar items.

    Args:
        item_id (str):
        exclude_artist_ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):
        limit (Union[Unset, int]):
        fields (Union[Unset, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        exclude_artist_ids=exclude_artist_ids,
        user_id=user_id,
        limit=limit,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets similar items.

    Args:
        item_id (str):
        exclude_artist_ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):
        limit (Union[Unset, int]):
        fields (Union[Unset, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        exclude_artist_ids=exclude_artist_ids,
        user_id=user_id,
        limit=limit,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets similar items.

    Args:
        item_id (str):
        exclude_artist_ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):
        limit (Union[Unset, int]):
        fields (Union[Unset, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        exclude_artist_ids=exclude_artist_ids,
        user_id=user_id,
        limit=limit,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets similar items.

    Args:
        item_id (str):
        exclude_artist_ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):
        limit (Union[Unset, int]):
        fields (Union[Unset, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            exclude_artist_ids=exclude_artist_ids,
            user_id=user_id,
            limit=limit,
            fields=fields,
        )
    ).parsed
