from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import List
from typing import Union

if TYPE_CHECKING:
    from ..models.lyric_metadata import LyricMetadata
    from ..models.lyric_line import LyricLine


T = TypeVar("T", bound="LyricDto")


@_attrs_define
class LyricDto:
    """LyricResponse model.

    Attributes:
        metadata (Union[Unset, LyricMetadata]): LyricMetadata model.
        lyrics (Union[Unset, List['LyricLine']]): Gets or sets a collection of individual lyric lines.
    """

    metadata: Union[Unset, "LyricMetadata"] = UNSET
    lyrics: Union[Unset, List["LyricLine"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        lyrics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lyrics, Unset):
            lyrics = []
            for lyrics_item_data in self.lyrics:
                lyrics_item = lyrics_item_data.to_dict()
                lyrics.append(lyrics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata
        if lyrics is not UNSET:
            field_dict["Lyrics"] = lyrics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lyric_metadata import LyricMetadata
        from ..models.lyric_line import LyricLine

        d = src_dict.copy()
        _metadata = d.pop("Metadata", UNSET)
        metadata: Union[Unset, LyricMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = LyricMetadata.from_dict(_metadata)

        lyrics = []
        _lyrics = d.pop("Lyrics", UNSET)
        for lyrics_item_data in _lyrics or []:
            lyrics_item = LyricLine.from_dict(lyrics_item_data)

            lyrics.append(lyrics_item)

        lyric_dto = cls(
            metadata=metadata,
            lyrics=lyrics,
        )

        return lyric_dto
