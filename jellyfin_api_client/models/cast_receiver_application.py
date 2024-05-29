from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union


T = TypeVar("T", bound="CastReceiverApplication")


@_attrs_define
class CastReceiverApplication:
    """The cast receiver application model.

    Attributes:
        id (Union[Unset, str]): Gets or sets the cast receiver application id.
        name (Union[Unset, str]): Gets or sets the cast receiver application name.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        cast_receiver_application = cls(
            id=id,
            name=name,
        )

        return cast_receiver_application
