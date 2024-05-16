from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from typing import cast, Union
from typing import Dict
from ..types import UNSET, Unset
from ..models.create_playlist_dto_media_type import CreatePlaylistDtoMediaType
from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.playlist_user_permissions import PlaylistUserPermissions


T = TypeVar("T", bound="CreatePlaylistDto")


@_attrs_define
class CreatePlaylistDto:
    """Create new playlist dto.

    Attributes:
        name (Union[Unset, str]): Gets or sets the name of the new playlist.
        ids (Union[Unset, List[str]]): Gets or sets item ids to add to the playlist.
        user_id (Union[None, Unset, str]): Gets or sets the user id.
        media_type (Union[Unset, CreatePlaylistDtoMediaType]): Gets or sets the media type.
        users (Union[Unset, List['PlaylistUserPermissions']]): Gets or sets the playlist users.
        is_public (Union[Unset, bool]): Gets or sets a value indicating whether the playlist is public.
    """

    name: Union[Unset, str] = UNSET
    ids: Union[Unset, List[str]] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    media_type: Union[Unset, CreatePlaylistDtoMediaType] = UNSET
    users: Union[Unset, List["PlaylistUserPermissions"]] = UNSET
    is_public: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.playlist_user_permissions import PlaylistUserPermissions

        name = self.name

        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        media_type: Union[Unset, str] = UNSET
        if not isinstance(self.media_type, Unset):
            media_type = self.media_type.value

        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        is_public = self.is_public

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if ids is not UNSET:
            field_dict["Ids"] = ids
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if media_type is not UNSET:
            field_dict["MediaType"] = media_type
        if users is not UNSET:
            field_dict["Users"] = users
        if is_public is not UNSET:
            field_dict["IsPublic"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.playlist_user_permissions import PlaylistUserPermissions

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        ids = cast(List[str], d.pop("Ids", UNSET))

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("UserId", UNSET))

        _media_type = d.pop("MediaType", UNSET)
        media_type: Union[Unset, CreatePlaylistDtoMediaType]
        if isinstance(_media_type, Unset):
            media_type = UNSET
        else:
            media_type = CreatePlaylistDtoMediaType(_media_type)

        users = []
        _users = d.pop("Users", UNSET)
        for users_item_data in _users or []:
            users_item = PlaylistUserPermissions.from_dict(users_item_data)

            users.append(users_item)

        is_public = d.pop("IsPublic", UNSET)

        create_playlist_dto = cls(
            name=name,
            ids=ids,
            user_id=user_id,
            media_type=media_type,
            users=users,
            is_public=is_public,
        )

        return create_playlist_dto
