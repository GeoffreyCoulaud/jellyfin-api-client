from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..models.subtitle_delivery_method import SubtitleDeliveryMethod
from ..types import UNSET, Unset


T = TypeVar("T", bound="SubtitleProfile")


@_attrs_define
class SubtitleProfile:
    """
    Attributes:
        format_ (Union[None, Unset, str]):
        method (Union[Unset, SubtitleDeliveryMethod]): Delivery method to use during playback of a specific subtitle
            format.
        didl_mode (Union[None, Unset, str]):
        language (Union[None, Unset, str]):
        container (Union[None, Unset, str]):
    """

    format_: Union[None, Unset, str] = UNSET
    method: Union[Unset, SubtitleDeliveryMethod] = UNSET
    didl_mode: Union[None, Unset, str] = UNSET
    language: Union[None, Unset, str] = UNSET
    container: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        format_: Union[None, Unset, str]
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        didl_mode: Union[None, Unset, str]
        if isinstance(self.didl_mode, Unset):
            didl_mode = UNSET
        else:
            didl_mode = self.didl_mode

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        container: Union[None, Unset, str]
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["Format"] = format_
        if method is not UNSET:
            field_dict["Method"] = method
        if didl_mode is not UNSET:
            field_dict["DidlMode"] = didl_mode
        if language is not UNSET:
            field_dict["Language"] = language
        if container is not UNSET:
            field_dict["Container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_format_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        format_ = _parse_format_(d.pop("Format", UNSET))

        _method = d.pop("Method", UNSET)
        method: Union[Unset, SubtitleDeliveryMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = SubtitleDeliveryMethod(_method)

        def _parse_didl_mode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        didl_mode = _parse_didl_mode(d.pop("DidlMode", UNSET))

        def _parse_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language = _parse_language(d.pop("Language", UNSET))

        def _parse_container(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        container = _parse_container(d.pop("Container", UNSET))

        subtitle_profile = cls(
            format_=format_,
            method=method,
            didl_mode=didl_mode,
            language=language,
            container=container,
        )

        return subtitle_profile
