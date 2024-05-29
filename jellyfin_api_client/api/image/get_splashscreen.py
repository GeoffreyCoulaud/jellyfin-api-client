from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.image_format import ImageFormat


def _get_kwargs(
    *,
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    fill_width: Union[Unset, int] = UNSET,
    fill_height: Union[Unset, int] = UNSET,
    blur: Union[Unset, int] = UNSET,
    background_color: Union[Unset, str] = UNSET,
    foreground_layer: Union[Unset, str] = UNSET,
    quality: Union[Unset, int] = 90,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["tag"] = tag

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["maxWidth"] = max_width

    params["maxHeight"] = max_height

    params["width"] = width

    params["height"] = height

    params["fillWidth"] = fill_width

    params["fillHeight"] = fill_height

    params["blur"] = blur

    params["backgroundColor"] = background_color

    params["foregroundLayer"] = foreground_layer

    params["quality"] = quality

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Branding/Splashscreen",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
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
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    fill_width: Union[Unset, int] = UNSET,
    fill_height: Union[Unset, int] = UNSET,
    blur: Union[Unset, int] = UNSET,
    background_color: Union[Unset, str] = UNSET,
    foreground_layer: Union[Unset, str] = UNSET,
    quality: Union[Unset, int] = 90,
) -> Response[Any]:
    """Generates or gets the splashscreen.

    Args:
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        fill_width (Union[Unset, int]):
        fill_height (Union[Unset, int]):
        blur (Union[Unset, int]):
        background_color (Union[Unset, str]):
        foreground_layer (Union[Unset, str]):
        quality (Union[Unset, int]):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        width=width,
        height=height,
        fill_width=fill_width,
        fill_height=fill_height,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
        quality=quality,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    fill_width: Union[Unset, int] = UNSET,
    fill_height: Union[Unset, int] = UNSET,
    blur: Union[Unset, int] = UNSET,
    background_color: Union[Unset, str] = UNSET,
    foreground_layer: Union[Unset, str] = UNSET,
    quality: Union[Unset, int] = 90,
) -> Response[Any]:
    """Generates or gets the splashscreen.

    Args:
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        fill_width (Union[Unset, int]):
        fill_height (Union[Unset, int]):
        blur (Union[Unset, int]):
        background_color (Union[Unset, str]):
        foreground_layer (Union[Unset, str]):
        quality (Union[Unset, int]):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        width=width,
        height=height,
        fill_width=fill_width,
        fill_height=fill_height,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
        quality=quality,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
