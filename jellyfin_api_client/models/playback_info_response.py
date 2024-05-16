from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from typing import cast, Union
from typing import Dict
from ..models.playback_info_response_error_code import PlaybackInfoResponseErrorCode
from ..types import UNSET, Unset
from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.media_source_info import MediaSourceInfo


T = TypeVar("T", bound="PlaybackInfoResponse")


@_attrs_define
class PlaybackInfoResponse:
    """Class PlaybackInfoResponse.

    Attributes:
        media_sources (Union[Unset, List['MediaSourceInfo']]): Gets or sets the media sources.
        play_session_id (Union[None, Unset, str]): Gets or sets the play session identifier.
        error_code (Union[Unset, PlaybackInfoResponseErrorCode]): Gets or sets the error code.
    """

    media_sources: Union[Unset, List["MediaSourceInfo"]] = UNSET
    play_session_id: Union[None, Unset, str] = UNSET
    error_code: Union[Unset, PlaybackInfoResponseErrorCode] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.media_source_info import MediaSourceInfo

        media_sources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media_sources, Unset):
            media_sources = []
            for media_sources_item_data in self.media_sources:
                media_sources_item = media_sources_item_data.to_dict()
                media_sources.append(media_sources_item)

        play_session_id: Union[None, Unset, str]
        if isinstance(self.play_session_id, Unset):
            play_session_id = UNSET
        else:
            play_session_id = self.play_session_id

        error_code: Union[Unset, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if media_sources is not UNSET:
            field_dict["MediaSources"] = media_sources
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if error_code is not UNSET:
            field_dict["ErrorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_source_info import MediaSourceInfo

        d = src_dict.copy()
        media_sources = []
        _media_sources = d.pop("MediaSources", UNSET)
        for media_sources_item_data in _media_sources or []:
            media_sources_item = MediaSourceInfo.from_dict(media_sources_item_data)

            media_sources.append(media_sources_item)

        def _parse_play_session_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        play_session_id = _parse_play_session_id(d.pop("PlaySessionId", UNSET))

        _error_code = d.pop("ErrorCode", UNSET)
        error_code: Union[Unset, PlaybackInfoResponseErrorCode]
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = PlaybackInfoResponseErrorCode(_error_code)

        playback_info_response = cls(
            media_sources=media_sources,
            play_session_id=play_session_id,
            error_code=error_code,
        )

        return playback_info_response
