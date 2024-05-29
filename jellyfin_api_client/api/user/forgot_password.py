from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.forgot_password_dto import ForgotPasswordDto
from ...models.forgot_password_result import ForgotPasswordResult


def _get_kwargs(
    *,
    body: Union[
        ForgotPasswordDto,
        ForgotPasswordDto,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/Users/ForgotPassword",
    }

    if isinstance(body, ForgotPasswordDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ForgotPasswordDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ForgotPasswordResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ForgotPasswordResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ForgotPasswordResult]:
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
        ForgotPasswordDto,
        ForgotPasswordDto,
    ],
) -> Response[ForgotPasswordResult]:
    """Initiates the forgot password process for a local user.

    Args:
        body (ForgotPasswordDto): Forgot Password request body DTO.
        body (ForgotPasswordDto): Forgot Password request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForgotPasswordResult]
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
        ForgotPasswordDto,
        ForgotPasswordDto,
    ],
) -> Optional[ForgotPasswordResult]:
    """Initiates the forgot password process for a local user.

    Args:
        body (ForgotPasswordDto): Forgot Password request body DTO.
        body (ForgotPasswordDto): Forgot Password request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForgotPasswordResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ForgotPasswordDto,
        ForgotPasswordDto,
    ],
) -> Response[ForgotPasswordResult]:
    """Initiates the forgot password process for a local user.

    Args:
        body (ForgotPasswordDto): Forgot Password request body DTO.
        body (ForgotPasswordDto): Forgot Password request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForgotPasswordResult]
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
        ForgotPasswordDto,
        ForgotPasswordDto,
    ],
) -> Optional[ForgotPasswordResult]:
    """Initiates the forgot password process for a local user.

    Args:
        body (ForgotPasswordDto): Forgot Password request body DTO.
        body (ForgotPasswordDto): Forgot Password request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForgotPasswordResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
