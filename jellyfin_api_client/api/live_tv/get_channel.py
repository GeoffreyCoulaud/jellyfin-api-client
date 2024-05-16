from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Dict
from typing import Union
from typing import cast
from ...models.base_item_dto import BaseItemDto
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    channel_id: str,
    *,
    user_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/Channels/{channel_id}".format(
            channel_id=channel_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDto, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BaseItemDto.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
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
) -> Response[Union[Any, BaseItemDto, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, BaseItemDto, ProblemDetails]]:
    """Gets a live tv channel.

    Args:
        channel_id (str):
        user_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDto, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, BaseItemDto, ProblemDetails]]:
    """Gets a live tv channel.

    Args:
        channel_id (str):
        user_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDto, ProblemDetails]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, BaseItemDto, ProblemDetails]]:
    """Gets a live tv channel.

    Args:
        channel_id (str):
        user_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDto, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, BaseItemDto, ProblemDetails]]:
    """Gets a live tv channel.

    Args:
        channel_id (str):
        user_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDto, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            user_id=user_id,
        )
    ).parsed
