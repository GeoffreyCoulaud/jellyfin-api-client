from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union
from typing import List

if TYPE_CHECKING:
    from ..models.user_item_data_dto import UserItemDataDto


T = TypeVar("T", bound="UserDataChangeInfo")


@_attrs_define
class UserDataChangeInfo:
    """Class UserDataChangeInfo.

    Attributes:
        user_id (Union[None, Unset, str]): Gets or sets the user id.
        user_data_list (Union[List['UserItemDataDto'], None, Unset]): Gets or sets the user data list.
    """

    user_id: Union[None, Unset, str] = UNSET
    user_data_list: Union[List["UserItemDataDto"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        user_data_list: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.user_data_list, Unset):
            user_data_list = UNSET
        elif isinstance(self.user_data_list, list):
            user_data_list = []
            for user_data_list_type_0_item_data in self.user_data_list:
                user_data_list_type_0_item = user_data_list_type_0_item_data.to_dict()
                user_data_list.append(user_data_list_type_0_item)

        else:
            user_data_list = self.user_data_list

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if user_data_list is not UNSET:
            field_dict["UserDataList"] = user_data_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_item_data_dto import UserItemDataDto

        d = src_dict.copy()

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("UserId", UNSET))

        def _parse_user_data_list(
            data: object,
        ) -> Union[List["UserItemDataDto"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_data_list_type_0 = []
                _user_data_list_type_0 = data
                for user_data_list_type_0_item_data in _user_data_list_type_0:
                    user_data_list_type_0_item = UserItemDataDto.from_dict(
                        user_data_list_type_0_item_data
                    )

                    user_data_list_type_0.append(user_data_list_type_0_item)

                return user_data_list_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["UserItemDataDto"], None, Unset], data)

        user_data_list = _parse_user_data_list(d.pop("UserDataList", UNSET))

        user_data_change_info = cls(
            user_id=user_id,
            user_data_list=user_data_list,
        )

        return user_data_change_info
