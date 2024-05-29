from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from typing import List

if TYPE_CHECKING:
    from ..models.playlist_user_permissions import PlaylistUserPermissions


T = TypeVar("T", bound="UpdatePlaylistDto")


@_attrs_define
class UpdatePlaylistDto:
    """Update existing playlist dto. Fields set to `null` will not be updated and keep their current values.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name of the new playlist.
        ids (Union[List[str], None, Unset]): Gets or sets item ids of the playlist.
        users (Union[List['PlaylistUserPermissions'], None, Unset]): Gets or sets the playlist users.
        is_public (Union[None, Unset, bool]): Gets or sets a value indicating whether the playlist is public.
    """

    name: Union[None, Unset, str] = UNSET
    ids: Union[List[str], None, Unset] = UNSET
    users: Union[List["PlaylistUserPermissions"], None, Unset] = UNSET
    is_public: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        ids: Union[List[str], None, Unset]
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = self.ids

        else:
            ids = self.ids

        users: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)

        else:
            users = self.users

        is_public: Union[None, Unset, bool]
        if isinstance(self.is_public, Unset):
            is_public = UNSET
        else:
            is_public = self.is_public

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if ids is not UNSET:
            field_dict["Ids"] = ids
        if users is not UNSET:
            field_dict["Users"] = users
        if is_public is not UNSET:
            field_dict["IsPublic"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.playlist_user_permissions import PlaylistUserPermissions

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_ids(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = cast(List[str], data)

                return ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        ids = _parse_ids(d.pop("Ids", UNSET))

        def _parse_users(
            data: object,
        ) -> Union[List["PlaylistUserPermissions"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in _users_type_0:
                    users_type_0_item = PlaylistUserPermissions.from_dict(
                        users_type_0_item_data
                    )

                    users_type_0.append(users_type_0_item)

                return users_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PlaylistUserPermissions"], None, Unset], data)

        users = _parse_users(d.pop("Users", UNSET))

        def _parse_is_public(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_public = _parse_is_public(d.pop("IsPublic", UNSET))

        update_playlist_dto = cls(
            name=name,
            ids=ids,
            users=users,
            is_public=is_public,
        )

        return update_playlist_dto
