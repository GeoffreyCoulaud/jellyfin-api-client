from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.add_virtual_folder_dto import AddVirtualFolderDto
from ...models.collection_type_options import CollectionTypeOptions
from ...types import Unset


def _get_kwargs(
    *,
    body: Union[
        AddVirtualFolderDto,
        AddVirtualFolderDto,
    ],
    name: Union[Unset, str] = UNSET,
    collection_type: Union[Unset, CollectionTypeOptions] = UNSET,
    paths: Union[Unset, List[str]] = UNSET,
    refresh_library: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["name"] = name

    json_collection_type: Union[Unset, str] = UNSET
    if not isinstance(collection_type, Unset):
        json_collection_type = collection_type.value

    params["collectionType"] = json_collection_type

    json_paths: Union[Unset, List[str]] = UNSET
    if not isinstance(paths, Unset):
        json_paths = paths

    params["paths"] = json_paths

    params["refreshLibrary"] = refresh_library

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/Library/VirtualFolders",
        "params": params,
    }

    if isinstance(body, AddVirtualFolderDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, AddVirtualFolderDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
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
    body: Union[
        AddVirtualFolderDto,
        AddVirtualFolderDto,
    ],
    name: Union[Unset, str] = UNSET,
    collection_type: Union[Unset, CollectionTypeOptions] = UNSET,
    paths: Union[Unset, List[str]] = UNSET,
    refresh_library: Union[Unset, bool] = False,
) -> Response[Any]:
    """Adds a virtual folder.

    Args:
        name (Union[Unset, str]):
        collection_type (Union[Unset, CollectionTypeOptions]): The collection type options.
        paths (Union[Unset, List[str]]):
        refresh_library (Union[Unset, bool]):  Default: False.
        body (AddVirtualFolderDto): Add virtual folder dto.
        body (AddVirtualFolderDto): Add virtual folder dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
        collection_type=collection_type,
        paths=paths,
        refresh_library=refresh_library,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        AddVirtualFolderDto,
        AddVirtualFolderDto,
    ],
    name: Union[Unset, str] = UNSET,
    collection_type: Union[Unset, CollectionTypeOptions] = UNSET,
    paths: Union[Unset, List[str]] = UNSET,
    refresh_library: Union[Unset, bool] = False,
) -> Response[Any]:
    """Adds a virtual folder.

    Args:
        name (Union[Unset, str]):
        collection_type (Union[Unset, CollectionTypeOptions]): The collection type options.
        paths (Union[Unset, List[str]]):
        refresh_library (Union[Unset, bool]):  Default: False.
        body (AddVirtualFolderDto): Add virtual folder dto.
        body (AddVirtualFolderDto): Add virtual folder dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
        collection_type=collection_type,
        paths=paths,
        refresh_library=refresh_library,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
