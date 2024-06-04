from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union
from typing import List
from ..models.task_state import TaskState

if TYPE_CHECKING:
    from ..models.task_result import TaskResult
    from ..models.task_trigger_info import TaskTriggerInfo


T = TypeVar("T", bound="TaskInfo")


@_attrs_define
class TaskInfo:
    """Class TaskInfo.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        state (Union[Unset, TaskState]): Enum TaskState.
        current_progress_percentage (Union[None, Unset, float]): Gets or sets the progress.
        id (Union[None, Unset, str]): Gets or sets the id.
        last_execution_result (Union['TaskResult', None, Unset]): Gets or sets the last execution result.
        triggers (Union[List['TaskTriggerInfo'], None, Unset]): Gets or sets the triggers.
        description (Union[None, Unset, str]): Gets or sets the description.
        category (Union[None, Unset, str]): Gets or sets the category.
        is_hidden (Union[Unset, bool]): Gets or sets a value indicating whether this instance is hidden.
        key (Union[None, Unset, str]): Gets or sets the key.
    """

    name: Union[None, Unset, str] = UNSET
    state: Union[Unset, TaskState] = UNSET
    current_progress_percentage: Union[None, Unset, float] = UNSET
    id: Union[None, Unset, str] = UNSET
    last_execution_result: Union["TaskResult", None, Unset] = UNSET
    triggers: Union[List["TaskTriggerInfo"], None, Unset] = UNSET
    description: Union[None, Unset, str] = UNSET
    category: Union[None, Unset, str] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    key: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.task_result import TaskResult

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        current_progress_percentage: Union[None, Unset, float]
        if isinstance(self.current_progress_percentage, Unset):
            current_progress_percentage = UNSET
        else:
            current_progress_percentage = self.current_progress_percentage

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        last_execution_result: Union[Dict[str, Any], None, Unset]
        if isinstance(self.last_execution_result, Unset):
            last_execution_result = UNSET
        elif isinstance(self.last_execution_result, TaskResult):
            last_execution_result = self.last_execution_result.to_dict()
        else:
            last_execution_result = self.last_execution_result

        triggers: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.triggers, Unset):
            triggers = UNSET
        elif isinstance(self.triggers, list):
            triggers = []
            for triggers_type_0_item_data in self.triggers:
                triggers_type_0_item = triggers_type_0_item_data.to_dict()
                triggers.append(triggers_type_0_item)

        else:
            triggers = self.triggers

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        category: Union[None, Unset, str]
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        is_hidden = self.is_hidden

        key: Union[None, Unset, str]
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if state is not UNSET:
            field_dict["State"] = state
        if current_progress_percentage is not UNSET:
            field_dict["CurrentProgressPercentage"] = current_progress_percentage
        if id is not UNSET:
            field_dict["Id"] = id
        if last_execution_result is not UNSET:
            field_dict["LastExecutionResult"] = last_execution_result
        if triggers is not UNSET:
            field_dict["Triggers"] = triggers
        if description is not UNSET:
            field_dict["Description"] = description
        if category is not UNSET:
            field_dict["Category"] = category
        if is_hidden is not UNSET:
            field_dict["IsHidden"] = is_hidden
        if key is not UNSET:
            field_dict["Key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_result import TaskResult
        from ..models.task_trigger_info import TaskTriggerInfo

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        _state = d.pop("State", UNSET)
        state: Union[Unset, TaskState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = TaskState(_state)

        def _parse_current_progress_percentage(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        current_progress_percentage = _parse_current_progress_percentage(
            d.pop("CurrentProgressPercentage", UNSET)
        )

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_last_execution_result(
            data: object,
        ) -> Union["TaskResult", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_execution_result_type_1 = TaskResult.from_dict(data)

                return last_execution_result_type_1
            except:  # noqa: E722
                pass
            return cast(Union["TaskResult", None, Unset], data)

        last_execution_result = _parse_last_execution_result(
            d.pop("LastExecutionResult", UNSET)
        )

        def _parse_triggers(
            data: object,
        ) -> Union[List["TaskTriggerInfo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                triggers_type_0 = []
                _triggers_type_0 = data
                for triggers_type_0_item_data in _triggers_type_0:
                    triggers_type_0_item = TaskTriggerInfo.from_dict(
                        triggers_type_0_item_data
                    )

                    triggers_type_0.append(triggers_type_0_item)

                return triggers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["TaskTriggerInfo"], None, Unset], data)

        triggers = _parse_triggers(d.pop("Triggers", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("Description", UNSET))

        def _parse_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category = _parse_category(d.pop("Category", UNSET))

        is_hidden = d.pop("IsHidden", UNSET)

        def _parse_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        key = _parse_key(d.pop("Key", UNSET))

        task_info = cls(
            name=name,
            state=state,
            current_progress_percentage=current_progress_percentage,
            id=id,
            last_execution_result=last_execution_result,
            triggers=triggers,
            description=description,
            category=category,
            is_hidden=is_hidden,
            key=key,
        )

        return task_info
