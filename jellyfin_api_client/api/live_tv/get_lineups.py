from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.name_id_pair import NameIdPair


def _get_kwargs(
    *,
    id: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["id"] = id

    params["type"] = type

    params["location"] = location

    params["country"] = country

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/ListingProviders/Lineups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["NameIdPair"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = NameIdPair.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["NameIdPair"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["NameIdPair"]]]:
    """Gets available lineups.

    Args:
        id (Union[Unset, str]):
        type (Union[Unset, str]):
        location (Union[Unset, str]):
        country (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['NameIdPair']]]
    """

    kwargs = _get_kwargs(
        id=id,
        type=type,
        location=location,
        country=country,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["NameIdPair"]]]:
    """Gets available lineups.

    Args:
        id (Union[Unset, str]):
        type (Union[Unset, str]):
        location (Union[Unset, str]):
        country (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['NameIdPair']]
    """

    return sync_detailed(
        client=client,
        id=id,
        type=type,
        location=location,
        country=country,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["NameIdPair"]]]:
    """Gets available lineups.

    Args:
        id (Union[Unset, str]):
        type (Union[Unset, str]):
        location (Union[Unset, str]):
        country (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['NameIdPair']]]
    """

    kwargs = _get_kwargs(
        id=id,
        type=type,
        location=location,
        country=country,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["NameIdPair"]]]:
    """Gets available lineups.

    Args:
        id (Union[Unset, str]):
        type (Union[Unset, str]):
        location (Union[Unset, str]):
        country (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['NameIdPair']]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            type=type,
            location=location,
            country=country,
        )
    ).parsed
