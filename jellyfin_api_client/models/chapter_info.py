from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union
import datetime
from dateutil.parser import isoparse


T = TypeVar("T", bound="ChapterInfo")


@_attrs_define
class ChapterInfo:
    """Class ChapterInfo.

    Attributes:
        start_position_ticks (Union[Unset, int]): Gets or sets the start position ticks.
        name (Union[None, Unset, str]): Gets or sets the name.
        image_path (Union[None, Unset, str]): Gets or sets the image path.
        image_date_modified (Union[Unset, datetime.datetime]):
        image_tag (Union[None, Unset, str]):
    """

    start_position_ticks: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    image_path: Union[None, Unset, str] = UNSET
    image_date_modified: Union[Unset, datetime.datetime] = UNSET
    image_tag: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start_position_ticks = self.start_position_ticks

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        image_path: Union[None, Unset, str]
        if isinstance(self.image_path, Unset):
            image_path = UNSET
        else:
            image_path = self.image_path

        image_date_modified: Union[Unset, str] = UNSET
        if not isinstance(self.image_date_modified, Unset):
            image_date_modified = self.image_date_modified.isoformat()

        image_tag: Union[None, Unset, str]
        if isinstance(self.image_tag, Unset):
            image_tag = UNSET
        else:
            image_tag = self.image_tag

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if start_position_ticks is not UNSET:
            field_dict["StartPositionTicks"] = start_position_ticks
        if name is not UNSET:
            field_dict["Name"] = name
        if image_path is not UNSET:
            field_dict["ImagePath"] = image_path
        if image_date_modified is not UNSET:
            field_dict["ImageDateModified"] = image_date_modified
        if image_tag is not UNSET:
            field_dict["ImageTag"] = image_tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_position_ticks = d.pop("StartPositionTicks", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_image_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_path = _parse_image_path(d.pop("ImagePath", UNSET))

        _image_date_modified = d.pop("ImageDateModified", UNSET)
        image_date_modified: Union[Unset, datetime.datetime]
        if isinstance(_image_date_modified, Unset):
            image_date_modified = UNSET
        else:
            image_date_modified = isoparse(_image_date_modified)

        def _parse_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_tag = _parse_image_tag(d.pop("ImageTag", UNSET))

        chapter_info = cls(
            start_position_ticks=start_position_ticks,
            name=name,
            image_path=image_path,
            image_date_modified=image_date_modified,
            image_tag=image_tag,
        )

        return chapter_info
