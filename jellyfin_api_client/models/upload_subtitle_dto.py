from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="UploadSubtitleDto")


@_attrs_define
class UploadSubtitleDto:
    """Upload subtitles dto.

    Attributes:
        language (str): Gets or sets the subtitle language.
        format_ (str): Gets or sets the subtitle format.
        is_forced (bool): Gets or sets a value indicating whether the subtitle is forced.
        is_hearing_impaired (bool): Gets or sets a value indicating whether the subtitle is for hearing impaired.
        data (str): Gets or sets the subtitle data.
    """

    language: str
    format_: str
    is_forced: bool
    is_hearing_impaired: bool
    data: str

    def to_dict(self) -> Dict[str, Any]:
        language = self.language

        format_ = self.format_

        is_forced = self.is_forced

        is_hearing_impaired = self.is_hearing_impaired

        data = self.data

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Language": language,
                "Format": format_,
                "IsForced": is_forced,
                "IsHearingImpaired": is_hearing_impaired,
                "Data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("Language")

        format_ = d.pop("Format")

        is_forced = d.pop("IsForced")

        is_hearing_impaired = d.pop("IsHearingImpaired")

        data = d.pop("Data")

        upload_subtitle_dto = cls(
            language=language,
            format_=format_,
            is_forced=is_forced,
            is_hearing_impaired=is_hearing_impaired,
            data=data,
        )

        return upload_subtitle_dto
