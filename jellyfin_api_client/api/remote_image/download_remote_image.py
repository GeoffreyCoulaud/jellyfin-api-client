from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.problem_details import ProblemDetails
from ...models.image_type import ImageType


def _get_kwargs(
    item_id: str,
    *,
    type: ImageType,
    image_url: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_type = type.value
    params["type"] = json_type

    params["imageUrl"] = image_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/Items/{item_id}/RemoteImages/Download".format(
            item_id=item_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, ProblemDetails]]:
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
    type: ImageType,
    image_url: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Downloads a remote image for an item.

    Args:
        item_id (str):
        type (ImageType): Enum ImageType.
        image_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        type=type,
        image_url=image_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    type: ImageType,
    image_url: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Downloads a remote image for an item.

    Args:
        item_id (str):
        type (ImageType): Enum ImageType.
        image_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        type=type,
        image_url=image_url,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    type: ImageType,
    image_url: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Downloads a remote image for an item.

    Args:
        item_id (str):
        type (ImageType): Enum ImageType.
        image_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        type=type,
        image_url=image_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    type: ImageType,
    image_url: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Downloads a remote image for an item.

    Args:
        item_id (str):
        type (ImageType): Enum ImageType.
        image_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            type=type,
            image_url=image_url,
        )
    ).parsed
