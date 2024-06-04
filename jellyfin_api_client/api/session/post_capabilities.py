from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.general_command_type import GeneralCommandType
from ...models.media_type import MediaType


def _get_kwargs(
    *,
    id: Union[Unset, str] = UNSET,
    playable_media_types: Union[Unset, List[MediaType]] = UNSET,
    supported_commands: Union[Unset, List[GeneralCommandType]] = UNSET,
    supports_media_control: Union[Unset, bool] = False,
    supports_persistent_identifier: Union[Unset, bool] = True,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["id"] = id

    json_playable_media_types: Union[Unset, List[str]] = UNSET
    if not isinstance(playable_media_types, Unset):
        json_playable_media_types = []
        for playable_media_types_item_data in playable_media_types:
            playable_media_types_item = playable_media_types_item_data.value
            json_playable_media_types.append(playable_media_types_item)

    params["playableMediaTypes"] = json_playable_media_types

    json_supported_commands: Union[Unset, List[str]] = UNSET
    if not isinstance(supported_commands, Unset):
        json_supported_commands = []
        for supported_commands_item_data in supported_commands:
            supported_commands_item = supported_commands_item_data.value
            json_supported_commands.append(supported_commands_item)

    params["supportedCommands"] = json_supported_commands

    params["supportsMediaControl"] = supports_media_control

    params["supportsPersistentIdentifier"] = supports_persistent_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/Sessions/Capabilities",
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
    *,
    client: AuthenticatedClient,
    id: Union[Unset, str] = UNSET,
    playable_media_types: Union[Unset, List[MediaType]] = UNSET,
    supported_commands: Union[Unset, List[GeneralCommandType]] = UNSET,
    supports_media_control: Union[Unset, bool] = False,
    supports_persistent_identifier: Union[Unset, bool] = True,
) -> Response[Any]:
    """Updates capabilities for a device.

    Args:
        id (Union[Unset, str]):
        playable_media_types (Union[Unset, List[MediaType]]):
        supported_commands (Union[Unset, List[GeneralCommandType]]):
        supports_media_control (Union[Unset, bool]):  Default: False.
        supports_persistent_identifier (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        playable_media_types=playable_media_types,
        supported_commands=supported_commands,
        supports_media_control=supports_media_control,
        supports_persistent_identifier=supports_persistent_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, str] = UNSET,
    playable_media_types: Union[Unset, List[MediaType]] = UNSET,
    supported_commands: Union[Unset, List[GeneralCommandType]] = UNSET,
    supports_media_control: Union[Unset, bool] = False,
    supports_persistent_identifier: Union[Unset, bool] = True,
) -> Response[Any]:
    """Updates capabilities for a device.

    Args:
        id (Union[Unset, str]):
        playable_media_types (Union[Unset, List[MediaType]]):
        supported_commands (Union[Unset, List[GeneralCommandType]]):
        supports_media_control (Union[Unset, bool]):  Default: False.
        supports_persistent_identifier (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        playable_media_types=playable_media_types,
        supported_commands=supported_commands,
        supports_media_control=supports_media_control,
        supports_persistent_identifier=supports_persistent_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
