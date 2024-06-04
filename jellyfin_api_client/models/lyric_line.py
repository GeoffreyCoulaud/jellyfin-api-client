from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast


T = TypeVar("T", bound="LyricLine")


@_attrs_define
class LyricLine:
    """Lyric model.

    Attributes:
        text (Union[Unset, str]): Gets the text of this lyric line.
        start (Union[None, Unset, int]): Gets the start time in ticks.
    """

    text: Union[Unset, str] = UNSET
    start: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        start: Union[None, Unset, int]
        if isinstance(self.start, Unset):
            start = UNSET
        else:
            start = self.start

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if text is not UNSET:
            field_dict["Text"] = text
        if start is not UNSET:
            field_dict["Start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("Text", UNSET)

        def _parse_start(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        start = _parse_start(d.pop("Start", UNSET))

        lyric_line = cls(
            text=text,
            start=start,
        )

        return lyric_line
