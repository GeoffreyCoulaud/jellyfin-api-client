from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from typing import cast, Union
from typing import Dict
from ..types import UNSET, Unset
from typing import Union
from typing import cast
from ..models.recommendation_type import RecommendationType

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto


T = TypeVar("T", bound="RecommendationDto")


@_attrs_define
class RecommendationDto:
    """
    Attributes:
        items (Union[List['BaseItemDto'], None, Unset]):
        recommendation_type (Union[Unset, RecommendationType]):
        baseline_item_name (Union[None, Unset, str]):
        category_id (Union[Unset, str]):
    """

    items: Union[List["BaseItemDto"], None, Unset] = UNSET
    recommendation_type: Union[Unset, RecommendationType] = UNSET
    baseline_item_name: Union[None, Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.base_item_dto import BaseItemDto

        items: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        recommendation_type: Union[Unset, str] = UNSET
        if not isinstance(self.recommendation_type, Unset):
            recommendation_type = self.recommendation_type.value

        baseline_item_name: Union[None, Unset, str]
        if isinstance(self.baseline_item_name, Unset):
            baseline_item_name = UNSET
        else:
            baseline_item_name = self.baseline_item_name

        category_id = self.category_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if items is not UNSET:
            field_dict["Items"] = items
        if recommendation_type is not UNSET:
            field_dict["RecommendationType"] = recommendation_type
        if baseline_item_name is not UNSET:
            field_dict["BaselineItemName"] = baseline_item_name
        if category_id is not UNSET:
            field_dict["CategoryId"] = category_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto

        d = src_dict.copy()

        def _parse_items(data: object) -> Union[List["BaseItemDto"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = BaseItemDto.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["BaseItemDto"], None, Unset], data)

        items = _parse_items(d.pop("Items", UNSET))

        _recommendation_type = d.pop("RecommendationType", UNSET)
        recommendation_type: Union[Unset, RecommendationType]
        if isinstance(_recommendation_type, Unset):
            recommendation_type = UNSET
        else:
            recommendation_type = RecommendationType(_recommendation_type)

        def _parse_baseline_item_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        baseline_item_name = _parse_baseline_item_name(d.pop("BaselineItemName", UNSET))

        category_id = d.pop("CategoryId", UNSET)

        recommendation_dto = cls(
            items=items,
            recommendation_type=recommendation_type,
            baseline_item_name=baseline_item_name,
            category_id=category_id,
        )

        return recommendation_dto
