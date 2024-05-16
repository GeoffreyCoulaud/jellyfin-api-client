from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from typing import Dict
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_source_info import MediaSourceInfo


T = TypeVar("T", bound="LiveStreamResponse")


@_attrs_define
class LiveStreamResponse:
    """
    Attributes:
        media_source (Union[Unset, MediaSourceInfo]):
    """

    media_source: Union[Unset, "MediaSourceInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.media_source_info import MediaSourceInfo

        media_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.media_source, Unset):
            media_source = self.media_source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if media_source is not UNSET:
            field_dict["MediaSource"] = media_source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_source_info import MediaSourceInfo

        d = src_dict.copy()
        _media_source = d.pop("MediaSource", UNSET)
        media_source: Union[Unset, MediaSourceInfo]
        if isinstance(_media_source, Unset):
            media_source = UNSET
        else:
            media_source = MediaSourceInfo.from_dict(_media_source)

        live_stream_response = cls(
            media_source=media_source,
        )

        return live_stream_response
