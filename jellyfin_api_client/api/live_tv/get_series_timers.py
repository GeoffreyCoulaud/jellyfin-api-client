from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Dict
from typing import Union
from ...models.sort_order import SortOrder
from typing import cast
from ...models.series_timer_info_dto_query_result import SeriesTimerInfoDtoQueryResult


def _get_kwargs(
    *,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, SortOrder] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["sortBy"] = sort_by

    json_sort_order: Union[Unset, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/SeriesTimers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SeriesTimerInfoDtoQueryResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SeriesTimerInfoDtoQueryResult.from_dict(response.json())

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
) -> Response[Union[Any, SeriesTimerInfoDtoQueryResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, SortOrder] = UNSET,
) -> Response[Union[Any, SeriesTimerInfoDtoQueryResult]]:
    """Gets live tv series timers.

    Args:
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, SortOrder]): An enum representing the sorting order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SeriesTimerInfoDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, SortOrder] = UNSET,
) -> Optional[Union[Any, SeriesTimerInfoDtoQueryResult]]:
    """Gets live tv series timers.

    Args:
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, SortOrder]): An enum representing the sorting order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SeriesTimerInfoDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, SortOrder] = UNSET,
) -> Response[Union[Any, SeriesTimerInfoDtoQueryResult]]:
    """Gets live tv series timers.

    Args:
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, SortOrder]): An enum representing the sorting order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SeriesTimerInfoDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, SortOrder] = UNSET,
) -> Optional[Union[Any, SeriesTimerInfoDtoQueryResult]]:
    """Gets live tv series timers.

    Args:
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, SortOrder]): An enum representing the sorting order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SeriesTimerInfoDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
