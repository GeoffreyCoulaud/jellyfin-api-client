from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.tuner_host_info import TunerHostInfo


def _get_kwargs(
    *,
    new_devices_only: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["newDevicesOnly"] = new_devices_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/LiveTv/Tuners/Discover",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["TunerHostInfo"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TunerHostInfo.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["TunerHostInfo"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    new_devices_only: Union[Unset, bool] = False,
) -> Response[Union[Any, List["TunerHostInfo"]]]:
    """Discover tuners.

    Args:
        new_devices_only (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['TunerHostInfo']]]
    """

    kwargs = _get_kwargs(
        new_devices_only=new_devices_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    new_devices_only: Union[Unset, bool] = False,
) -> Optional[Union[Any, List["TunerHostInfo"]]]:
    """Discover tuners.

    Args:
        new_devices_only (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['TunerHostInfo']]
    """

    return sync_detailed(
        client=client,
        new_devices_only=new_devices_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    new_devices_only: Union[Unset, bool] = False,
) -> Response[Union[Any, List["TunerHostInfo"]]]:
    """Discover tuners.

    Args:
        new_devices_only (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['TunerHostInfo']]]
    """

    kwargs = _get_kwargs(
        new_devices_only=new_devices_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    new_devices_only: Union[Unset, bool] = False,
) -> Optional[Union[Any, List["TunerHostInfo"]]]:
    """Discover tuners.

    Args:
        new_devices_only (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['TunerHostInfo']]
    """

    return (
        await asyncio_detailed(
            client=client,
            new_devices_only=new_devices_only,
        )
    ).parsed
