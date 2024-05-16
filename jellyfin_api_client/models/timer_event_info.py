from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="TimerEventInfo")


@_attrs_define
class TimerEventInfo:
    """
    Attributes:
        id (Union[Unset, str]):
        program_id (Union[None, Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    program_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        program_id: Union[None, Unset, str]
        if isinstance(self.program_id, Unset):
            program_id = UNSET
        else:
            program_id = self.program_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if program_id is not UNSET:
            field_dict["ProgramId"] = program_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        def _parse_program_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        program_id = _parse_program_id(d.pop("ProgramId", UNSET))

        timer_event_info = cls(
            id=id,
            program_id=program_id,
        )

        return timer_event_info
