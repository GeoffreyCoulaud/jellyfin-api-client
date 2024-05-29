from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_playlist_dto import CreatePlaylistDto
from ...models.playlist_creation_result import PlaylistCreationResult
from ...models.media_type import MediaType
from ...types import Unset


def _get_kwargs(
    *,
    body: Union[
        CreatePlaylistDto,
        CreatePlaylistDto,
    ],
    name: Union[Unset, str] = UNSET,
    ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    media_type: Union[Unset, MediaType] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["name"] = name

    json_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids"] = json_ids

    params["userId"] = user_id

    json_media_type: Union[Unset, str] = UNSET
    if not isinstance(media_type, Unset):
        json_media_type = media_type.value

    params["mediaType"] = json_media_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/Playlists",
        "params": params,
    }

    if isinstance(body, CreatePlaylistDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, CreatePlaylistDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PlaylistCreationResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PlaylistCreationResult.from_dict(response.json())

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
) -> Response[Union[Any, PlaylistCreationResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlaylistDto,
        CreatePlaylistDto,
    ],
    name: Union[Unset, str] = UNSET,
    ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    media_type: Union[Unset, MediaType] = UNSET,
) -> Response[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, str]):
        ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):
        media_type (Union[Unset, MediaType]): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlaylistCreationResult]]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlaylistDto,
        CreatePlaylistDto,
    ],
    name: Union[Unset, str] = UNSET,
    ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    media_type: Union[Unset, MediaType] = UNSET,
) -> Optional[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, str]):
        ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):
        media_type (Union[Unset, MediaType]): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlaylistCreationResult]
    """

    return sync_detailed(
        client=client,
        body=body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlaylistDto,
        CreatePlaylistDto,
    ],
    name: Union[Unset, str] = UNSET,
    ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    media_type: Union[Unset, MediaType] = UNSET,
) -> Response[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, str]):
        ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):
        media_type (Union[Unset, MediaType]): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlaylistCreationResult]]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlaylistDto,
        CreatePlaylistDto,
    ],
    name: Union[Unset, str] = UNSET,
    ids: Union[Unset, List[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    media_type: Union[Unset, MediaType] = UNSET,
) -> Optional[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, str]):
        ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):
        media_type (Union[Unset, MediaType]): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlaylistCreationResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            name=name,
            ids=ids,
            user_id=user_id,
            media_type=media_type,
        )
    ).parsed
