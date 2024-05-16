from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union
from typing import Dict
from ..models.person_kind import PersonKind
from ..types import UNSET, Unset
from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.base_item_person_image_blur_hashes_type_0 import BaseItemPersonImageBlurHashesType0


T = TypeVar("T", bound="BaseItemPerson")


@_attrs_define
class BaseItemPerson:
    """This is used by the api to get information about a Person within a BaseItem.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        id (Union[Unset, str]): Gets or sets the identifier.
        role (Union[None, Unset, str]): Gets or sets the role.
        type (Union[Unset, PersonKind]): The person kind.
        primary_image_tag (Union[None, Unset, str]): Gets or sets the primary image tag.
        image_blur_hashes (Union['BaseItemPersonImageBlurHashesType0', None, Unset]): Gets or sets the primary image
            blurhash.
    """

    name: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    role: Union[None, Unset, str] = UNSET
    type: Union[Unset, PersonKind] = UNSET
    primary_image_tag: Union[None, Unset, str] = UNSET
    image_blur_hashes: Union["BaseItemPersonImageBlurHashesType0", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.base_item_person_image_blur_hashes_type_0 import BaseItemPersonImageBlurHashesType0

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        id = self.id

        role: Union[None, Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        primary_image_tag: Union[None, Unset, str]
        if isinstance(self.primary_image_tag, Unset):
            primary_image_tag = UNSET
        else:
            primary_image_tag = self.primary_image_tag

        image_blur_hashes: Union[Dict[str, Any], None, Unset]
        if isinstance(self.image_blur_hashes, Unset):
            image_blur_hashes = UNSET
        elif isinstance(self.image_blur_hashes, BaseItemPersonImageBlurHashesType0):
            image_blur_hashes = self.image_blur_hashes.to_dict()
        else:
            image_blur_hashes = self.image_blur_hashes

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id
        if role is not UNSET:
            field_dict["Role"] = role
        if type is not UNSET:
            field_dict["Type"] = type
        if primary_image_tag is not UNSET:
            field_dict["PrimaryImageTag"] = primary_image_tag
        if image_blur_hashes is not UNSET:
            field_dict["ImageBlurHashes"] = image_blur_hashes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_person_image_blur_hashes_type_0 import BaseItemPersonImageBlurHashesType0

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        id = d.pop("Id", UNSET)

        def _parse_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role = _parse_role(d.pop("Role", UNSET))

        _type = d.pop("Type", UNSET)
        type: Union[Unset, PersonKind]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PersonKind(_type)

        def _parse_primary_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_image_tag = _parse_primary_image_tag(d.pop("PrimaryImageTag", UNSET))

        def _parse_image_blur_hashes(data: object) -> Union["BaseItemPersonImageBlurHashesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_blur_hashes_type_0 = BaseItemPersonImageBlurHashesType0.from_dict(data)

                return image_blur_hashes_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemPersonImageBlurHashesType0", None, Unset], data)

        image_blur_hashes = _parse_image_blur_hashes(d.pop("ImageBlurHashes", UNSET))

        base_item_person = cls(
            name=name,
            id=id,
            role=role,
            type=type,
            primary_image_tag=primary_image_tag,
            image_blur_hashes=image_blur_hashes,
        )

        return base_item_person
