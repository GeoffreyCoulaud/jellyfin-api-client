from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="BrandingOptions")


@_attrs_define
class BrandingOptions:
    """The branding options.

    Attributes:
        login_disclaimer (Union[None, Unset, str]): Gets or sets the login disclaimer.
        custom_css (Union[None, Unset, str]): Gets or sets the custom CSS.
        splashscreen_enabled (Union[Unset, bool]): Gets or sets a value indicating whether to enable the splashscreen.
    """

    login_disclaimer: Union[None, Unset, str] = UNSET
    custom_css: Union[None, Unset, str] = UNSET
    splashscreen_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        login_disclaimer: Union[None, Unset, str]
        if isinstance(self.login_disclaimer, Unset):
            login_disclaimer = UNSET
        else:
            login_disclaimer = self.login_disclaimer

        custom_css: Union[None, Unset, str]
        if isinstance(self.custom_css, Unset):
            custom_css = UNSET
        else:
            custom_css = self.custom_css

        splashscreen_enabled = self.splashscreen_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if login_disclaimer is not UNSET:
            field_dict["LoginDisclaimer"] = login_disclaimer
        if custom_css is not UNSET:
            field_dict["CustomCss"] = custom_css
        if splashscreen_enabled is not UNSET:
            field_dict["SplashscreenEnabled"] = splashscreen_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_login_disclaimer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        login_disclaimer = _parse_login_disclaimer(d.pop("LoginDisclaimer", UNSET))

        def _parse_custom_css(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_css = _parse_custom_css(d.pop("CustomCss", UNSET))

        splashscreen_enabled = d.pop("SplashscreenEnabled", UNSET)

        branding_options = cls(
            login_disclaimer=login_disclaimer,
            custom_css=custom_css,
            splashscreen_enabled=splashscreen_enabled,
        )

        return branding_options
