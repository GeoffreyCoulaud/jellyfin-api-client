from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.series_timer_info_dto import SeriesTimerInfoDto


def _get_kwargs(
    *,
    program_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["programId"] = program_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/Timers/Defaults",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SeriesTimerInfoDto]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SeriesTimerInfoDto.from_dict(response.json())

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
) -> Response[Union[Any, SeriesTimerInfoDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    program_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, SeriesTimerInfoDto]]:
    """Gets the default values for a new timer.

    Args:
        program_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SeriesTimerInfoDto]]
    """

    kwargs = _get_kwargs(
        program_id=program_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    program_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, SeriesTimerInfoDto]]:
    """Gets the default values for a new timer.

    Args:
        program_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SeriesTimerInfoDto]
    """

    return sync_detailed(
        client=client,
        program_id=program_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    program_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, SeriesTimerInfoDto]]:
    """Gets the default values for a new timer.

    Args:
        program_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SeriesTimerInfoDto]]
    """

    kwargs = _get_kwargs(
        program_id=program_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    program_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, SeriesTimerInfoDto]]:
    """Gets the default values for a new timer.

    Args:
        program_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SeriesTimerInfoDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            program_id=program_id,
        )
    ).parsed
