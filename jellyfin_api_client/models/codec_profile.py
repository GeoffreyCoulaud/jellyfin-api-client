from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from typing import cast, Union
from typing import Dict
from ..types import UNSET, Unset
from ..models.codec_type import CodecType
from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="CodecProfile")


@_attrs_define
class CodecProfile:
    """
    Attributes:
        type (Union[Unset, CodecType]):
        conditions (Union[List['ProfileCondition'], None, Unset]):
        apply_conditions (Union[List['ProfileCondition'], None, Unset]):
        codec (Union[None, Unset, str]):
        container (Union[None, Unset, str]):
    """

    type: Union[Unset, CodecType] = UNSET
    conditions: Union[List["ProfileCondition"], None, Unset] = UNSET
    apply_conditions: Union[List["ProfileCondition"], None, Unset] = UNSET
    codec: Union[None, Unset, str] = UNSET
    container: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.profile_condition import ProfileCondition

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        conditions: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item = conditions_type_0_item_data.to_dict()
                conditions.append(conditions_type_0_item)

        else:
            conditions = self.conditions

        apply_conditions: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.apply_conditions, Unset):
            apply_conditions = UNSET
        elif isinstance(self.apply_conditions, list):
            apply_conditions = []
            for apply_conditions_type_0_item_data in self.apply_conditions:
                apply_conditions_type_0_item = apply_conditions_type_0_item_data.to_dict()
                apply_conditions.append(apply_conditions_type_0_item)

        else:
            apply_conditions = self.apply_conditions

        codec: Union[None, Unset, str]
        if isinstance(self.codec, Unset):
            codec = UNSET
        else:
            codec = self.codec

        container: Union[None, Unset, str]
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions
        if apply_conditions is not UNSET:
            field_dict["ApplyConditions"] = apply_conditions
        if codec is not UNSET:
            field_dict["Codec"] = codec
        if container is not UNSET:
            field_dict["Container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.profile_condition import ProfileCondition

        d = src_dict.copy()
        _type = d.pop("Type", UNSET)
        type: Union[Unset, CodecType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodecType(_type)

        def _parse_conditions(data: object) -> Union[List["ProfileCondition"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in _conditions_type_0:
                    conditions_type_0_item = ProfileCondition.from_dict(conditions_type_0_item_data)

                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ProfileCondition"], None, Unset], data)

        conditions = _parse_conditions(d.pop("Conditions", UNSET))

        def _parse_apply_conditions(data: object) -> Union[List["ProfileCondition"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                apply_conditions_type_0 = []
                _apply_conditions_type_0 = data
                for apply_conditions_type_0_item_data in _apply_conditions_type_0:
                    apply_conditions_type_0_item = ProfileCondition.from_dict(apply_conditions_type_0_item_data)

                    apply_conditions_type_0.append(apply_conditions_type_0_item)

                return apply_conditions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ProfileCondition"], None, Unset], data)

        apply_conditions = _parse_apply_conditions(d.pop("ApplyConditions", UNSET))

        def _parse_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        codec = _parse_codec(d.pop("Codec", UNSET))

        def _parse_container(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        container = _parse_container(d.pop("Container", UNSET))

        codec_profile = cls(
            type=type,
            conditions=conditions,
            apply_conditions=apply_conditions,
            codec=codec,
            container=container,
        )

        return codec_profile
