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
from ...models.display_preferences_dto import DisplayPreferencesDto


def _get_kwargs(
    display_preferences_id: str,
    *,
    body: Union[
        DisplayPreferencesDto,
        DisplayPreferencesDto,
    ],
    user_id: Union[Unset, str] = UNSET,
    client_query: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["userId"] = user_id

    params["client"] = client_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/DisplayPreferences/{display_preferences_id}".format(
            display_preferences_id=display_preferences_id,
        ),
        "params": params,
    }

    if isinstance(body, DisplayPreferencesDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, DisplayPreferencesDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        DisplayPreferencesDto,
        DisplayPreferencesDto,
    ],
    user_id: Union[Unset, str] = UNSET,
    client_query: str,
) -> Response[Any]:
    """Update Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (Union[Unset, str]):
        client_query (str):
        body (DisplayPreferencesDto): Defines the display preferences for any item that supports
            them (usually Folders).
        body (DisplayPreferencesDto): Defines the display preferences for any item that supports
            them (usually Folders).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_preferences_id=display_preferences_id,
        body=body,
        user_id=user_id,
        client_query=client_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        DisplayPreferencesDto,
        DisplayPreferencesDto,
    ],
    user_id: Union[Unset, str] = UNSET,
    client_query: str,
) -> Response[Any]:
    """Update Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (Union[Unset, str]):
        client_query (str):
        body (DisplayPreferencesDto): Defines the display preferences for any item that supports
            them (usually Folders).
        body (DisplayPreferencesDto): Defines the display preferences for any item that supports
            them (usually Folders).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_preferences_id=display_preferences_id,
        body=body,
        user_id=user_id,
        client_query=client_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
