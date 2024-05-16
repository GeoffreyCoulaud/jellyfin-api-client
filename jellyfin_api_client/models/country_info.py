from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="CountryInfo")


@_attrs_define
class CountryInfo:
    """Class CountryInfo.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        display_name (Union[None, Unset, str]): Gets or sets the display name.
        two_letter_iso_region_name (Union[None, Unset, str]): Gets or sets the name of the two letter ISO region.
        three_letter_iso_region_name (Union[None, Unset, str]): Gets or sets the name of the three letter ISO region.
    """

    name: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    two_letter_iso_region_name: Union[None, Unset, str] = UNSET
    three_letter_iso_region_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        two_letter_iso_region_name: Union[None, Unset, str]
        if isinstance(self.two_letter_iso_region_name, Unset):
            two_letter_iso_region_name = UNSET
        else:
            two_letter_iso_region_name = self.two_letter_iso_region_name

        three_letter_iso_region_name: Union[None, Unset, str]
        if isinstance(self.three_letter_iso_region_name, Unset):
            three_letter_iso_region_name = UNSET
        else:
            three_letter_iso_region_name = self.three_letter_iso_region_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if two_letter_iso_region_name is not UNSET:
            field_dict["TwoLetterISORegionName"] = two_letter_iso_region_name
        if three_letter_iso_region_name is not UNSET:
            field_dict["ThreeLetterISORegionName"] = three_letter_iso_region_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("DisplayName", UNSET))

        def _parse_two_letter_iso_region_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        two_letter_iso_region_name = _parse_two_letter_iso_region_name(d.pop("TwoLetterISORegionName", UNSET))

        def _parse_three_letter_iso_region_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        three_letter_iso_region_name = _parse_three_letter_iso_region_name(d.pop("ThreeLetterISORegionName", UNSET))

        country_info = cls(
            name=name,
            display_name=display_name,
            two_letter_iso_region_name=two_letter_iso_region_name,
            three_letter_iso_region_name=three_letter_iso_region_name,
        )

        return country_info
