from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Dict

if TYPE_CHECKING:
    from ..models.trickplay_info import TrickplayInfo


T = TypeVar("T", bound="BaseItemDtoTrickplayType0AdditionalProperty")


@_attrs_define
class BaseItemDtoTrickplayType0AdditionalProperty:
    """ """

    additional_properties: Dict[str, "TrickplayInfo"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.trickplay_info import TrickplayInfo

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trickplay_info import TrickplayInfo

        d = src_dict.copy()
        base_item_dto_trickplay_type_0_additional_property = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TrickplayInfo.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        base_item_dto_trickplay_type_0_additional_property.additional_properties = additional_properties
        return base_item_dto_trickplay_type_0_additional_property

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "TrickplayInfo":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "TrickplayInfo") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
