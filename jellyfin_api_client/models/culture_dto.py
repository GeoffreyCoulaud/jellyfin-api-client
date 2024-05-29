from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from typing import List


T = TypeVar("T", bound="CultureDto")


@_attrs_define
class CultureDto:
    """Class CultureDto.

    Attributes:
        name (Union[Unset, str]): Gets the name.
        display_name (Union[Unset, str]): Gets the display name.
        two_letter_iso_language_name (Union[Unset, str]): Gets the name of the two letter ISO language.
        three_letter_iso_language_name (Union[None, Unset, str]): Gets the name of the three letter ISO language.
        three_letter_iso_language_names (Union[Unset, List[str]]):
    """

    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    two_letter_iso_language_name: Union[Unset, str] = UNSET
    three_letter_iso_language_name: Union[None, Unset, str] = UNSET
    three_letter_iso_language_names: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        two_letter_iso_language_name = self.two_letter_iso_language_name

        three_letter_iso_language_name: Union[None, Unset, str]
        if isinstance(self.three_letter_iso_language_name, Unset):
            three_letter_iso_language_name = UNSET
        else:
            three_letter_iso_language_name = self.three_letter_iso_language_name

        three_letter_iso_language_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.three_letter_iso_language_names, Unset):
            three_letter_iso_language_names = self.three_letter_iso_language_names

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if two_letter_iso_language_name is not UNSET:
            field_dict["TwoLetterISOLanguageName"] = two_letter_iso_language_name
        if three_letter_iso_language_name is not UNSET:
            field_dict["ThreeLetterISOLanguageName"] = three_letter_iso_language_name
        if three_letter_iso_language_names is not UNSET:
            field_dict["ThreeLetterISOLanguageNames"] = three_letter_iso_language_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        two_letter_iso_language_name = d.pop("TwoLetterISOLanguageName", UNSET)

        def _parse_three_letter_iso_language_name(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        three_letter_iso_language_name = _parse_three_letter_iso_language_name(
            d.pop("ThreeLetterISOLanguageName", UNSET)
        )

        three_letter_iso_language_names = cast(
            List[str], d.pop("ThreeLetterISOLanguageNames", UNSET)
        )

        culture_dto = cls(
            name=name,
            display_name=display_name,
            two_letter_iso_language_name=two_letter_iso_language_name,
            three_letter_iso_language_name=three_letter_iso_language_name,
            three_letter_iso_language_names=three_letter_iso_language_names,
        )

        return culture_dto
