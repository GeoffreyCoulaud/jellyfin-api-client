from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union
from typing import Dict

if TYPE_CHECKING:
    from ..models.base_item_person_image_blur_hashes_type_0_logo import BaseItemPersonImageBlurHashesType0Logo
    from ..models.base_item_person_image_blur_hashes_type_0_primary import BaseItemPersonImageBlurHashesType0Primary
    from ..models.base_item_person_image_blur_hashes_type_0_banner import BaseItemPersonImageBlurHashesType0Banner
    from ..models.base_item_person_image_blur_hashes_type_0_menu import BaseItemPersonImageBlurHashesType0Menu
    from ..models.base_item_person_image_blur_hashes_type_0_box_rear import BaseItemPersonImageBlurHashesType0BoxRear
    from ..models.base_item_person_image_blur_hashes_type_0_disc import BaseItemPersonImageBlurHashesType0Disc
    from ..models.base_item_person_image_blur_hashes_type_0_art import BaseItemPersonImageBlurHashesType0Art
    from ..models.base_item_person_image_blur_hashes_type_0_thumb import BaseItemPersonImageBlurHashesType0Thumb
    from ..models.base_item_person_image_blur_hashes_type_0_box import BaseItemPersonImageBlurHashesType0Box
    from ..models.base_item_person_image_blur_hashes_type_0_backdrop import BaseItemPersonImageBlurHashesType0Backdrop
    from ..models.base_item_person_image_blur_hashes_type_0_profile import BaseItemPersonImageBlurHashesType0Profile
    from ..models.base_item_person_image_blur_hashes_type_0_chapter import BaseItemPersonImageBlurHashesType0Chapter
    from ..models.base_item_person_image_blur_hashes_type_0_screenshot import (
        BaseItemPersonImageBlurHashesType0Screenshot,
    )


T = TypeVar("T", bound="BaseItemPersonImageBlurHashesType0")


@_attrs_define
class BaseItemPersonImageBlurHashesType0:
    """Gets or sets the primary image blurhash.

    Attributes:
        primary (Union[Unset, BaseItemPersonImageBlurHashesType0Primary]):
        art (Union[Unset, BaseItemPersonImageBlurHashesType0Art]):
        backdrop (Union[Unset, BaseItemPersonImageBlurHashesType0Backdrop]):
        banner (Union[Unset, BaseItemPersonImageBlurHashesType0Banner]):
        logo (Union[Unset, BaseItemPersonImageBlurHashesType0Logo]):
        thumb (Union[Unset, BaseItemPersonImageBlurHashesType0Thumb]):
        disc (Union[Unset, BaseItemPersonImageBlurHashesType0Disc]):
        box (Union[Unset, BaseItemPersonImageBlurHashesType0Box]):
        screenshot (Union[Unset, BaseItemPersonImageBlurHashesType0Screenshot]):
        menu (Union[Unset, BaseItemPersonImageBlurHashesType0Menu]):
        chapter (Union[Unset, BaseItemPersonImageBlurHashesType0Chapter]):
        box_rear (Union[Unset, BaseItemPersonImageBlurHashesType0BoxRear]):
        profile (Union[Unset, BaseItemPersonImageBlurHashesType0Profile]):
    """

    primary: Union[Unset, "BaseItemPersonImageBlurHashesType0Primary"] = UNSET
    art: Union[Unset, "BaseItemPersonImageBlurHashesType0Art"] = UNSET
    backdrop: Union[Unset, "BaseItemPersonImageBlurHashesType0Backdrop"] = UNSET
    banner: Union[Unset, "BaseItemPersonImageBlurHashesType0Banner"] = UNSET
    logo: Union[Unset, "BaseItemPersonImageBlurHashesType0Logo"] = UNSET
    thumb: Union[Unset, "BaseItemPersonImageBlurHashesType0Thumb"] = UNSET
    disc: Union[Unset, "BaseItemPersonImageBlurHashesType0Disc"] = UNSET
    box: Union[Unset, "BaseItemPersonImageBlurHashesType0Box"] = UNSET
    screenshot: Union[Unset, "BaseItemPersonImageBlurHashesType0Screenshot"] = UNSET
    menu: Union[Unset, "BaseItemPersonImageBlurHashesType0Menu"] = UNSET
    chapter: Union[Unset, "BaseItemPersonImageBlurHashesType0Chapter"] = UNSET
    box_rear: Union[Unset, "BaseItemPersonImageBlurHashesType0BoxRear"] = UNSET
    profile: Union[Unset, "BaseItemPersonImageBlurHashesType0Profile"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.base_item_person_image_blur_hashes_type_0_logo import BaseItemPersonImageBlurHashesType0Logo
        from ..models.base_item_person_image_blur_hashes_type_0_primary import BaseItemPersonImageBlurHashesType0Primary
        from ..models.base_item_person_image_blur_hashes_type_0_banner import BaseItemPersonImageBlurHashesType0Banner
        from ..models.base_item_person_image_blur_hashes_type_0_menu import BaseItemPersonImageBlurHashesType0Menu
        from ..models.base_item_person_image_blur_hashes_type_0_box_rear import (
            BaseItemPersonImageBlurHashesType0BoxRear,
        )
        from ..models.base_item_person_image_blur_hashes_type_0_disc import BaseItemPersonImageBlurHashesType0Disc
        from ..models.base_item_person_image_blur_hashes_type_0_art import BaseItemPersonImageBlurHashesType0Art
        from ..models.base_item_person_image_blur_hashes_type_0_thumb import BaseItemPersonImageBlurHashesType0Thumb
        from ..models.base_item_person_image_blur_hashes_type_0_box import BaseItemPersonImageBlurHashesType0Box
        from ..models.base_item_person_image_blur_hashes_type_0_backdrop import (
            BaseItemPersonImageBlurHashesType0Backdrop,
        )
        from ..models.base_item_person_image_blur_hashes_type_0_profile import BaseItemPersonImageBlurHashesType0Profile
        from ..models.base_item_person_image_blur_hashes_type_0_chapter import BaseItemPersonImageBlurHashesType0Chapter
        from ..models.base_item_person_image_blur_hashes_type_0_screenshot import (
            BaseItemPersonImageBlurHashesType0Screenshot,
        )

        primary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.primary, Unset):
            primary = self.primary.to_dict()

        art: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.art, Unset):
            art = self.art.to_dict()

        backdrop: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.backdrop, Unset):
            backdrop = self.backdrop.to_dict()

        banner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.banner, Unset):
            banner = self.banner.to_dict()

        logo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.logo, Unset):
            logo = self.logo.to_dict()

        thumb: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.thumb, Unset):
            thumb = self.thumb.to_dict()

        disc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disc, Unset):
            disc = self.disc.to_dict()

        box: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.box, Unset):
            box = self.box.to_dict()

        screenshot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.screenshot, Unset):
            screenshot = self.screenshot.to_dict()

        menu: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.menu, Unset):
            menu = self.menu.to_dict()

        chapter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chapter, Unset):
            chapter = self.chapter.to_dict()

        box_rear: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.box_rear, Unset):
            box_rear = self.box_rear.to_dict()

        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary is not UNSET:
            field_dict["Primary"] = primary
        if art is not UNSET:
            field_dict["Art"] = art
        if backdrop is not UNSET:
            field_dict["Backdrop"] = backdrop
        if banner is not UNSET:
            field_dict["Banner"] = banner
        if logo is not UNSET:
            field_dict["Logo"] = logo
        if thumb is not UNSET:
            field_dict["Thumb"] = thumb
        if disc is not UNSET:
            field_dict["Disc"] = disc
        if box is not UNSET:
            field_dict["Box"] = box
        if screenshot is not UNSET:
            field_dict["Screenshot"] = screenshot
        if menu is not UNSET:
            field_dict["Menu"] = menu
        if chapter is not UNSET:
            field_dict["Chapter"] = chapter
        if box_rear is not UNSET:
            field_dict["BoxRear"] = box_rear
        if profile is not UNSET:
            field_dict["Profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_person_image_blur_hashes_type_0_logo import BaseItemPersonImageBlurHashesType0Logo
        from ..models.base_item_person_image_blur_hashes_type_0_primary import BaseItemPersonImageBlurHashesType0Primary
        from ..models.base_item_person_image_blur_hashes_type_0_banner import BaseItemPersonImageBlurHashesType0Banner
        from ..models.base_item_person_image_blur_hashes_type_0_menu import BaseItemPersonImageBlurHashesType0Menu
        from ..models.base_item_person_image_blur_hashes_type_0_box_rear import (
            BaseItemPersonImageBlurHashesType0BoxRear,
        )
        from ..models.base_item_person_image_blur_hashes_type_0_disc import BaseItemPersonImageBlurHashesType0Disc
        from ..models.base_item_person_image_blur_hashes_type_0_art import BaseItemPersonImageBlurHashesType0Art
        from ..models.base_item_person_image_blur_hashes_type_0_thumb import BaseItemPersonImageBlurHashesType0Thumb
        from ..models.base_item_person_image_blur_hashes_type_0_box import BaseItemPersonImageBlurHashesType0Box
        from ..models.base_item_person_image_blur_hashes_type_0_backdrop import (
            BaseItemPersonImageBlurHashesType0Backdrop,
        )
        from ..models.base_item_person_image_blur_hashes_type_0_profile import BaseItemPersonImageBlurHashesType0Profile
        from ..models.base_item_person_image_blur_hashes_type_0_chapter import BaseItemPersonImageBlurHashesType0Chapter
        from ..models.base_item_person_image_blur_hashes_type_0_screenshot import (
            BaseItemPersonImageBlurHashesType0Screenshot,
        )

        d = src_dict.copy()
        _primary = d.pop("Primary", UNSET)
        primary: Union[Unset, BaseItemPersonImageBlurHashesType0Primary]
        if isinstance(_primary, Unset):
            primary = UNSET
        else:
            primary = BaseItemPersonImageBlurHashesType0Primary.from_dict(_primary)

        _art = d.pop("Art", UNSET)
        art: Union[Unset, BaseItemPersonImageBlurHashesType0Art]
        if isinstance(_art, Unset):
            art = UNSET
        else:
            art = BaseItemPersonImageBlurHashesType0Art.from_dict(_art)

        _backdrop = d.pop("Backdrop", UNSET)
        backdrop: Union[Unset, BaseItemPersonImageBlurHashesType0Backdrop]
        if isinstance(_backdrop, Unset):
            backdrop = UNSET
        else:
            backdrop = BaseItemPersonImageBlurHashesType0Backdrop.from_dict(_backdrop)

        _banner = d.pop("Banner", UNSET)
        banner: Union[Unset, BaseItemPersonImageBlurHashesType0Banner]
        if isinstance(_banner, Unset):
            banner = UNSET
        else:
            banner = BaseItemPersonImageBlurHashesType0Banner.from_dict(_banner)

        _logo = d.pop("Logo", UNSET)
        logo: Union[Unset, BaseItemPersonImageBlurHashesType0Logo]
        if isinstance(_logo, Unset):
            logo = UNSET
        else:
            logo = BaseItemPersonImageBlurHashesType0Logo.from_dict(_logo)

        _thumb = d.pop("Thumb", UNSET)
        thumb: Union[Unset, BaseItemPersonImageBlurHashesType0Thumb]
        if isinstance(_thumb, Unset):
            thumb = UNSET
        else:
            thumb = BaseItemPersonImageBlurHashesType0Thumb.from_dict(_thumb)

        _disc = d.pop("Disc", UNSET)
        disc: Union[Unset, BaseItemPersonImageBlurHashesType0Disc]
        if isinstance(_disc, Unset):
            disc = UNSET
        else:
            disc = BaseItemPersonImageBlurHashesType0Disc.from_dict(_disc)

        _box = d.pop("Box", UNSET)
        box: Union[Unset, BaseItemPersonImageBlurHashesType0Box]
        if isinstance(_box, Unset):
            box = UNSET
        else:
            box = BaseItemPersonImageBlurHashesType0Box.from_dict(_box)

        _screenshot = d.pop("Screenshot", UNSET)
        screenshot: Union[Unset, BaseItemPersonImageBlurHashesType0Screenshot]
        if isinstance(_screenshot, Unset):
            screenshot = UNSET
        else:
            screenshot = BaseItemPersonImageBlurHashesType0Screenshot.from_dict(_screenshot)

        _menu = d.pop("Menu", UNSET)
        menu: Union[Unset, BaseItemPersonImageBlurHashesType0Menu]
        if isinstance(_menu, Unset):
            menu = UNSET
        else:
            menu = BaseItemPersonImageBlurHashesType0Menu.from_dict(_menu)

        _chapter = d.pop("Chapter", UNSET)
        chapter: Union[Unset, BaseItemPersonImageBlurHashesType0Chapter]
        if isinstance(_chapter, Unset):
            chapter = UNSET
        else:
            chapter = BaseItemPersonImageBlurHashesType0Chapter.from_dict(_chapter)

        _box_rear = d.pop("BoxRear", UNSET)
        box_rear: Union[Unset, BaseItemPersonImageBlurHashesType0BoxRear]
        if isinstance(_box_rear, Unset):
            box_rear = UNSET
        else:
            box_rear = BaseItemPersonImageBlurHashesType0BoxRear.from_dict(_box_rear)

        _profile = d.pop("Profile", UNSET)
        profile: Union[Unset, BaseItemPersonImageBlurHashesType0Profile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = BaseItemPersonImageBlurHashesType0Profile.from_dict(_profile)

        base_item_person_image_blur_hashes_type_0 = cls(
            primary=primary,
            art=art,
            backdrop=backdrop,
            banner=banner,
            logo=logo,
            thumb=thumb,
            disc=disc,
            box=box,
            screenshot=screenshot,
            menu=menu,
            chapter=chapter,
            box_rear=box_rear,
            profile=profile,
        )

        base_item_person_image_blur_hashes_type_0.additional_properties = d
        return base_item_person_image_blur_hashes_type_0

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
