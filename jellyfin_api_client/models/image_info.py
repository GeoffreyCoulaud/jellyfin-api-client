from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from ..models.image_type import ImageType
from typing import cast, Union


T = TypeVar("T", bound="ImageInfo")


@_attrs_define
class ImageInfo:
    """Class ImageInfo.

    Attributes:
        image_type (Union[Unset, ImageType]): Enum ImageType.
        image_index (Union[None, Unset, int]): Gets or sets the index of the image.
        image_tag (Union[None, Unset, str]): Gets or sets the image tag.
        path (Union[None, Unset, str]): Gets or sets the path.
        blur_hash (Union[None, Unset, str]): Gets or sets the blurhash.
        height (Union[None, Unset, int]): Gets or sets the height.
        width (Union[None, Unset, int]): Gets or sets the width.
        size (Union[Unset, int]): Gets or sets the size.
    """

    image_type: Union[Unset, ImageType] = UNSET
    image_index: Union[None, Unset, int] = UNSET
    image_tag: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    blur_hash: Union[None, Unset, str] = UNSET
    height: Union[None, Unset, int] = UNSET
    width: Union[None, Unset, int] = UNSET
    size: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        image_type: Union[Unset, str] = UNSET
        if not isinstance(self.image_type, Unset):
            image_type = self.image_type.value

        image_index: Union[None, Unset, int]
        if isinstance(self.image_index, Unset):
            image_index = UNSET
        else:
            image_index = self.image_index

        image_tag: Union[None, Unset, str]
        if isinstance(self.image_tag, Unset):
            image_tag = UNSET
        else:
            image_tag = self.image_tag

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        blur_hash: Union[None, Unset, str]
        if isinstance(self.blur_hash, Unset):
            blur_hash = UNSET
        else:
            blur_hash = self.blur_hash

        height: Union[None, Unset, int]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        width: Union[None, Unset, int]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if image_type is not UNSET:
            field_dict["ImageType"] = image_type
        if image_index is not UNSET:
            field_dict["ImageIndex"] = image_index
        if image_tag is not UNSET:
            field_dict["ImageTag"] = image_tag
        if path is not UNSET:
            field_dict["Path"] = path
        if blur_hash is not UNSET:
            field_dict["BlurHash"] = blur_hash
        if height is not UNSET:
            field_dict["Height"] = height
        if width is not UNSET:
            field_dict["Width"] = width
        if size is not UNSET:
            field_dict["Size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _image_type = d.pop("ImageType", UNSET)
        image_type: Union[Unset, ImageType]
        if isinstance(_image_type, Unset):
            image_type = UNSET
        else:
            image_type = ImageType(_image_type)

        def _parse_image_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        image_index = _parse_image_index(d.pop("ImageIndex", UNSET))

        def _parse_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_tag = _parse_image_tag(d.pop("ImageTag", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_blur_hash(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        blur_hash = _parse_blur_hash(d.pop("BlurHash", UNSET))

        def _parse_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        height = _parse_height(d.pop("Height", UNSET))

        def _parse_width(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        width = _parse_width(d.pop("Width", UNSET))

        size = d.pop("Size", UNSET)

        image_info = cls(
            image_type=image_type,
            image_index=image_index,
            image_tag=image_tag,
            path=path,
            blur_hash=blur_hash,
            height=height,
            width=width,
            size=size,
        )

        return image_info
