from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.base_item_kind import BaseItemKind


def _get_kwargs(
    session_id: str,
    *,
    item_type: BaseItemKind,
    item_id: str,
    item_name: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_item_type = item_type.value
    params["itemType"] = json_item_type

    params["itemId"] = item_id

    params["itemName"] = item_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/Sessions/{session_id}/Viewing".format(
            session_id=session_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient,
    item_type: BaseItemKind,
    item_id: str,
    item_name: str,
) -> Response[Any]:
    """Instructs a session to browse to an item or view.

    Args:
        session_id (str):
        item_type (BaseItemKind): The base item kind.
        item_id (str):
        item_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        item_type=item_type,
        item_id=item_id,
        item_name=item_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient,
    item_type: BaseItemKind,
    item_id: str,
    item_name: str,
) -> Response[Any]:
    """Instructs a session to browse to an item or view.

    Args:
        session_id (str):
        item_type (BaseItemKind): The base item kind.
        item_id (str):
        item_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        item_type=item_type,
        item_id=item_id,
        item_name=item_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
