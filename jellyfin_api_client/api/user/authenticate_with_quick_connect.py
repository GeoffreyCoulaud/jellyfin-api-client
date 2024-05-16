from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.authentication_result import AuthenticationResult
from typing import cast
from ...models.quick_connect_dto import QuickConnectDto
from typing import Dict


def _get_kwargs(
    *,
    body: Union[
        QuickConnectDto,
        QuickConnectDto,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/Users/AuthenticateWithQuickConnect",
    }

    if isinstance(body, QuickConnectDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, QuickConnectDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AuthenticationResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuthenticationResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, AuthenticationResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        QuickConnectDto,
        QuickConnectDto,
    ],
) -> Response[Union[Any, AuthenticationResult]]:
    """Authenticates a user with quick connect.

    Args:
        body (QuickConnectDto): The quick connect request body.
        body (QuickConnectDto): The quick connect request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuthenticationResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        QuickConnectDto,
        QuickConnectDto,
    ],
) -> Optional[Union[Any, AuthenticationResult]]:
    """Authenticates a user with quick connect.

    Args:
        body (QuickConnectDto): The quick connect request body.
        body (QuickConnectDto): The quick connect request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuthenticationResult]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        QuickConnectDto,
        QuickConnectDto,
    ],
) -> Response[Union[Any, AuthenticationResult]]:
    """Authenticates a user with quick connect.

    Args:
        body (QuickConnectDto): The quick connect request body.
        body (QuickConnectDto): The quick connect request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuthenticationResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        QuickConnectDto,
        QuickConnectDto,
    ],
) -> Optional[Union[Any, AuthenticationResult]]:
    """Authenticates a user with quick connect.

    Args:
        body (QuickConnectDto): The quick connect request body.
        body (QuickConnectDto): The quick connect request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuthenticationResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
