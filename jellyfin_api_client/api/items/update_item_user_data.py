from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.user_item_data_dto import UserItemDataDto
from ...models.problem_details import ProblemDetails
from ...models.update_user_item_data_dto import UpdateUserItemDataDto


def _get_kwargs(
    item_id: str,
    *,
    body: Union[
        UpdateUserItemDataDto,
        UpdateUserItemDataDto,
    ],
    user_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/UserItems/{item_id}/UserData".format(
            item_id=item_id,
        ),
        "params": params,
    }

    if isinstance(body, UpdateUserItemDataDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateUserItemDataDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails, UserItemDataDto]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserItemDataDto.from_dict(response.json())

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
) -> Response[Union[Any, ProblemDetails, UserItemDataDto]]:
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
    body: Union[
        UpdateUserItemDataDto,
        UpdateUserItemDataDto,
    ],
    user_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ProblemDetails, UserItemDataDto]]:
    """Update Item User Data.

    Args:
        item_id (str):
        user_id (Union[Unset, str]):
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, UserItemDataDto]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUserItemDataDto,
        UpdateUserItemDataDto,
    ],
    user_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails, UserItemDataDto]]:
    """Update Item User Data.

    Args:
        item_id (str):
        user_id (Union[Unset, str]):
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails, UserItemDataDto]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        body=body,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUserItemDataDto,
        UpdateUserItemDataDto,
    ],
    user_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ProblemDetails, UserItemDataDto]]:
    """Update Item User Data.

    Args:
        item_id (str):
        user_id (Union[Unset, str]):
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, UserItemDataDto]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUserItemDataDto,
        UpdateUserItemDataDto,
    ],
    user_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails, UserItemDataDto]]:
    """Update Item User Data.

    Args:
        item_id (str):
        user_id (Union[Unset, str]):
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.
        body (UpdateUserItemDataDto): This is used by the api to get information about a item user
            data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails, UserItemDataDto]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            body=body,
            user_id=user_id,
        )
    ).parsed
