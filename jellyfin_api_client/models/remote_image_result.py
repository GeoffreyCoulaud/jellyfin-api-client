from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from typing import cast, Union
from typing import Dict
from ..types import UNSET, Unset
from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.remote_image_info import RemoteImageInfo


T = TypeVar("T", bound="RemoteImageResult")


@_attrs_define
class RemoteImageResult:
    """Class RemoteImageResult.

    Attributes:
        images (Union[List['RemoteImageInfo'], None, Unset]): Gets or sets the images.
        total_record_count (Union[Unset, int]): Gets or sets the total record count.
        providers (Union[List[str], None, Unset]): Gets or sets the providers.
    """

    images: Union[List["RemoteImageInfo"], None, Unset] = UNSET
    total_record_count: Union[Unset, int] = UNSET
    providers: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.remote_image_info import RemoteImageInfo

        images: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

        total_record_count = self.total_record_count

        providers: Union[List[str], None, Unset]
        if isinstance(self.providers, Unset):
            providers = UNSET
        elif isinstance(self.providers, list):
            providers = self.providers

        else:
            providers = self.providers

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if images is not UNSET:
            field_dict["Images"] = images
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count
        if providers is not UNSET:
            field_dict["Providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.remote_image_info import RemoteImageInfo

        d = src_dict.copy()

        def _parse_images(data: object) -> Union[List["RemoteImageInfo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = RemoteImageInfo.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["RemoteImageInfo"], None, Unset], data)

        images = _parse_images(d.pop("Images", UNSET))

        total_record_count = d.pop("TotalRecordCount", UNSET)

        def _parse_providers(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                providers_type_0 = cast(List[str], data)

                return providers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        providers = _parse_providers(d.pop("Providers", UNSET))

        remote_image_result = cls(
            images=images,
            total_record_count=total_record_count,
            providers=providers,
        )

        return remote_image_result
