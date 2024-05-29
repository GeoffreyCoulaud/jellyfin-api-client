from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.tuner_channel_mapping import TunerChannelMapping
from ...models.set_channel_mapping_dto import SetChannelMappingDto


def _get_kwargs(
    *,
    body: Union[
        SetChannelMappingDto,
        SetChannelMappingDto,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/LiveTv/ChannelMappings",
    }

    if isinstance(body, SetChannelMappingDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, SetChannelMappingDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TunerChannelMapping]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TunerChannelMapping.from_dict(response.json())

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
) -> Response[Union[Any, TunerChannelMapping]]:
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
        SetChannelMappingDto,
        SetChannelMappingDto,
    ],
) -> Response[Union[Any, TunerChannelMapping]]:
    """Set channel mappings.

    Args:
        body (SetChannelMappingDto): Set channel mapping dto.
        body (SetChannelMappingDto): Set channel mapping dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TunerChannelMapping]]
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
    client: AuthenticatedClient,
    body: Union[
        SetChannelMappingDto,
        SetChannelMappingDto,
    ],
) -> Optional[Union[Any, TunerChannelMapping]]:
    """Set channel mappings.

    Args:
        body (SetChannelMappingDto): Set channel mapping dto.
        body (SetChannelMappingDto): Set channel mapping dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TunerChannelMapping]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        SetChannelMappingDto,
        SetChannelMappingDto,
    ],
) -> Response[Union[Any, TunerChannelMapping]]:
    """Set channel mappings.

    Args:
        body (SetChannelMappingDto): Set channel mapping dto.
        body (SetChannelMappingDto): Set channel mapping dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TunerChannelMapping]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        SetChannelMappingDto,
        SetChannelMappingDto,
    ],
) -> Optional[Union[Any, TunerChannelMapping]]:
    """Set channel mappings.

    Args:
        body (SetChannelMappingDto): Set channel mapping dto.
        body (SetChannelMappingDto): Set channel mapping dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TunerChannelMapping]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
