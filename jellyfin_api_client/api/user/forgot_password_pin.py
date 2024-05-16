from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.pin_redeem_result import PinRedeemResult
from typing import cast
from typing import Dict
from ...models.forgot_password_pin_dto import ForgotPasswordPinDto


def _get_kwargs(
    *,
    body: Union[
        ForgotPasswordPinDto,
        ForgotPasswordPinDto,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/Users/ForgotPassword/Pin",
    }

    if isinstance(body, ForgotPasswordPinDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ForgotPasswordPinDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PinRedeemResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PinRedeemResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PinRedeemResult]:
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
        ForgotPasswordPinDto,
        ForgotPasswordPinDto,
    ],
) -> Response[PinRedeemResult]:
    """Redeems a forgot password pin.

    Args:
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PinRedeemResult]
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
        ForgotPasswordPinDto,
        ForgotPasswordPinDto,
    ],
) -> Optional[PinRedeemResult]:
    """Redeems a forgot password pin.

    Args:
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PinRedeemResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ForgotPasswordPinDto,
        ForgotPasswordPinDto,
    ],
) -> Response[PinRedeemResult]:
    """Redeems a forgot password pin.

    Args:
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PinRedeemResult]
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
        ForgotPasswordPinDto,
        ForgotPasswordPinDto,
    ],
) -> Optional[PinRedeemResult]:
    """Redeems a forgot password pin.

    Args:
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.
        body (ForgotPasswordPinDto): Forgot Password Pin enter request body DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PinRedeemResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
