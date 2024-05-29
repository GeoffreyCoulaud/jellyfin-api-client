from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast
import datetime
from ..models.task_completion_status import TaskCompletionStatus
from dateutil.parser import isoparse


T = TypeVar("T", bound="TaskResult")


@_attrs_define
class TaskResult:
    """Class TaskExecutionInfo.

    Attributes:
        start_time_utc (Union[Unset, datetime.datetime]): Gets or sets the start time UTC.
        end_time_utc (Union[Unset, datetime.datetime]): Gets or sets the end time UTC.
        status (Union[Unset, TaskCompletionStatus]): Enum TaskCompletionStatus.
        name (Union[None, Unset, str]): Gets or sets the name.
        key (Union[None, Unset, str]): Gets or sets the key.
        id (Union[None, Unset, str]): Gets or sets the id.
        error_message (Union[None, Unset, str]): Gets or sets the error message.
        long_error_message (Union[None, Unset, str]): Gets or sets the long error message.
    """

    start_time_utc: Union[Unset, datetime.datetime] = UNSET
    end_time_utc: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, TaskCompletionStatus] = UNSET
    name: Union[None, Unset, str] = UNSET
    key: Union[None, Unset, str] = UNSET
    id: Union[None, Unset, str] = UNSET
    error_message: Union[None, Unset, str] = UNSET
    long_error_message: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start_time_utc: Union[Unset, str] = UNSET
        if not isinstance(self.start_time_utc, Unset):
            start_time_utc = self.start_time_utc.isoformat()

        end_time_utc: Union[Unset, str] = UNSET
        if not isinstance(self.end_time_utc, Unset):
            end_time_utc = self.end_time_utc.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        key: Union[None, Unset, str]
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        error_message: Union[None, Unset, str]
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        long_error_message: Union[None, Unset, str]
        if isinstance(self.long_error_message, Unset):
            long_error_message = UNSET
        else:
            long_error_message = self.long_error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if start_time_utc is not UNSET:
            field_dict["StartTimeUtc"] = start_time_utc
        if end_time_utc is not UNSET:
            field_dict["EndTimeUtc"] = end_time_utc
        if status is not UNSET:
            field_dict["Status"] = status
        if name is not UNSET:
            field_dict["Name"] = name
        if key is not UNSET:
            field_dict["Key"] = key
        if id is not UNSET:
            field_dict["Id"] = id
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message
        if long_error_message is not UNSET:
            field_dict["LongErrorMessage"] = long_error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _start_time_utc = d.pop("StartTimeUtc", UNSET)
        start_time_utc: Union[Unset, datetime.datetime]
        if isinstance(_start_time_utc, Unset):
            start_time_utc = UNSET
        else:
            start_time_utc = isoparse(_start_time_utc)

        _end_time_utc = d.pop("EndTimeUtc", UNSET)
        end_time_utc: Union[Unset, datetime.datetime]
        if isinstance(_end_time_utc, Unset):
            end_time_utc = UNSET
        else:
            end_time_utc = isoparse(_end_time_utc)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, TaskCompletionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskCompletionStatus(_status)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        key = _parse_key(d.pop("Key", UNSET))

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_error_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error_message = _parse_error_message(d.pop("ErrorMessage", UNSET))

        def _parse_long_error_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        long_error_message = _parse_long_error_message(d.pop("LongErrorMessage", UNSET))

        task_result = cls(
            start_time_utc=start_time_utc,
            end_time_utc=end_time_utc,
            status=status,
            name=name,
            key=key,
            id=id,
            error_message=error_message,
            long_error_message=long_error_message,
        )

        return task_result
