from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem_details import ProblemDetails
from ...types import Unset
from ...models.image_format import ImageFormat
from ...models.image_type import ImageType


def _get_kwargs(
    name: str,
    image_type: ImageType,
    *,
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    percent_played: Union[Unset, float] = UNSET,
    unplayed_count: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    quality: Union[Unset, int] = UNSET,
    fill_width: Union[Unset, int] = UNSET,
    fill_height: Union[Unset, int] = UNSET,
    blur: Union[Unset, int] = UNSET,
    background_color: Union[Unset, str] = UNSET,
    foreground_layer: Union[Unset, str] = UNSET,
    image_index: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["tag"] = tag

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["maxWidth"] = max_width

    params["maxHeight"] = max_height

    params["percentPlayed"] = percent_played

    params["unplayedCount"] = unplayed_count

    params["width"] = width

    params["height"] = height

    params["quality"] = quality

    params["fillWidth"] = fill_width

    params["fillHeight"] = fill_height

    params["blur"] = blur

    params["backgroundColor"] = background_color

    params["foregroundLayer"] = foreground_layer

    params["imageIndex"] = image_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "head",
        "url": "/Studios/{name}/Images/{image_type}".format(
            name=name,
            image_type=image_type,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProblemDetails]:
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    image_type: ImageType,
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    percent_played: Union[Unset, float] = UNSET,
    unplayed_count: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    quality: Union[Unset, int] = UNSET,
    fill_width: Union[Unset, int] = UNSET,
    fill_height: Union[Unset, int] = UNSET,
    blur: Union[Unset, int] = UNSET,
    background_color: Union[Unset, str] = UNSET,
    foreground_layer: Union[Unset, str] = UNSET,
    image_index: Union[Unset, int] = UNSET,
) -> Response[ProblemDetails]:
    """Get studio image by name.

    Args:
        name (str):
        image_type (ImageType): Enum ImageType.
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        percent_played (Union[Unset, float]):
        unplayed_count (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        quality (Union[Unset, int]):
        fill_width (Union[Unset, int]):
        fill_height (Union[Unset, int]):
        blur (Union[Unset, int]):
        background_color (Union[Unset, str]):
        foreground_layer (Union[Unset, str]):
        image_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        image_type=image_type,
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
        image_index=image_index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    image_type: ImageType,
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    percent_played: Union[Unset, float] = UNSET,
    unplayed_count: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    quality: Union[Unset, int] = UNSET,
    fill_width: Union[Unset, int] = UNSET,
    fill_height: Union[Unset, int] = UNSET,
    blur: Union[Unset, int] = UNSET,
    background_color: Union[Unset, str] = UNSET,
    foreground_layer: Union[Unset, str] = UNSET,
    image_index: Union[Unset, int] = UNSET,
) -> Optional[ProblemDetails]:
    """Get studio image by name.

    Args:
        name (str):
        image_type (ImageType): Enum ImageType.
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        percent_played (Union[Unset, float]):
        unplayed_count (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        quality (Union[Unset, int]):
        fill_width (Union[Unset, int]):
        fill_height (Union[Unset, int]):
        blur (Union[Unset, int]):
        background_color (Union[Unset, str]):
        foreground_layer (Union[Unset, str]):
        image_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails
    """

    return sync_detailed(
        name=name,
        image_type=image_type,
        client=client,
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
        image_index=image_index,
    ).parsed


async def asyncio_detailed(
    name: str,
    image_type: ImageType,
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    percent_played: Union[Unset, float] = UNSET,
    unplayed_count: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    quality: Union[Unset, int] = UNSET,
    fill_width: Union[Unset, int] = UNSET,
    fill_height: Union[Unset, int] = UNSET,
    blur: Union[Unset, int] = UNSET,
    background_color: Union[Unset, str] = UNSET,
    foreground_layer: Union[Unset, str] = UNSET,
    image_index: Union[Unset, int] = UNSET,
) -> Response[ProblemDetails]:
    """Get studio image by name.

    Args:
        name (str):
        image_type (ImageType): Enum ImageType.
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        percent_played (Union[Unset, float]):
        unplayed_count (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        quality (Union[Unset, int]):
        fill_width (Union[Unset, int]):
        fill_height (Union[Unset, int]):
        blur (Union[Unset, int]):
        background_color (Union[Unset, str]):
        foreground_layer (Union[Unset, str]):
        image_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        image_type=image_type,
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
        image_index=image_index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    image_type: ImageType,
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    percent_played: Union[Unset, float] = UNSET,
    unplayed_count: Union[Unset, int] = UNSET,
    width: Union[Unset, int] = UNSET,
    height: Union[Unset, int] = UNSET,
    quality: Union[Unset, int] = UNSET,
    fill_width: Union[Unset, int] = UNSET,
    fill_height: Union[Unset, int] = UNSET,
    blur: Union[Unset, int] = UNSET,
    background_color: Union[Unset, str] = UNSET,
    foreground_layer: Union[Unset, str] = UNSET,
    image_index: Union[Unset, int] = UNSET,
) -> Optional[ProblemDetails]:
    """Get studio image by name.

    Args:
        name (str):
        image_type (ImageType): Enum ImageType.
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        percent_played (Union[Unset, float]):
        unplayed_count (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        quality (Union[Unset, int]):
        fill_width (Union[Unset, int]):
        fill_height (Union[Unset, int]):
        blur (Union[Unset, int]):
        background_color (Union[Unset, str]):
        foreground_layer (Union[Unset, str]):
        image_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails
    """

    return (
        await asyncio_detailed(
            name=name,
            image_type=image_type,
            client=client,
            tag=tag,
            format_=format_,
            max_width=max_width,
            max_height=max_height,
            percent_played=percent_played,
            unplayed_count=unplayed_count,
            width=width,
            height=height,
            quality=quality,
            fill_width=fill_width,
            fill_height=fill_height,
            blur=blur,
            background_color=background_color,
            foreground_layer=foreground_layer,
            image_index=image_index,
        )
    ).parsed
