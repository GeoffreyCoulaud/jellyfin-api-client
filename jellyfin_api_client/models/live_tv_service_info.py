from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, List
from ..models.live_tv_service_status import LiveTvServiceStatus
from typing import Union


T = TypeVar("T", bound="LiveTvServiceInfo")


@_attrs_define
class LiveTvServiceInfo:
    """Class ServiceInfo.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        home_page_url (Union[None, Unset, str]): Gets or sets the home page URL.
        status (Union[Unset, LiveTvServiceStatus]):
        status_message (Union[None, Unset, str]): Gets or sets the status message.
        version (Union[None, Unset, str]): Gets or sets the version.
        has_update_available (Union[Unset, bool]): Gets or sets a value indicating whether this instance has update
            available.
        is_visible (Union[Unset, bool]): Gets or sets a value indicating whether this instance is visible.
        tuners (Union[List[str], None, Unset]):
    """

    name: Union[None, Unset, str] = UNSET
    home_page_url: Union[None, Unset, str] = UNSET
    status: Union[Unset, LiveTvServiceStatus] = UNSET
    status_message: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    has_update_available: Union[Unset, bool] = UNSET
    is_visible: Union[Unset, bool] = UNSET
    tuners: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        home_page_url: Union[None, Unset, str]
        if isinstance(self.home_page_url, Unset):
            home_page_url = UNSET
        else:
            home_page_url = self.home_page_url

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_message: Union[None, Unset, str]
        if isinstance(self.status_message, Unset):
            status_message = UNSET
        else:
            status_message = self.status_message

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        has_update_available = self.has_update_available

        is_visible = self.is_visible

        tuners: Union[List[str], None, Unset]
        if isinstance(self.tuners, Unset):
            tuners = UNSET
        elif isinstance(self.tuners, list):
            tuners = self.tuners

        else:
            tuners = self.tuners

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if home_page_url is not UNSET:
            field_dict["HomePageUrl"] = home_page_url
        if status is not UNSET:
            field_dict["Status"] = status
        if status_message is not UNSET:
            field_dict["StatusMessage"] = status_message
        if version is not UNSET:
            field_dict["Version"] = version
        if has_update_available is not UNSET:
            field_dict["HasUpdateAvailable"] = has_update_available
        if is_visible is not UNSET:
            field_dict["IsVisible"] = is_visible
        if tuners is not UNSET:
            field_dict["Tuners"] = tuners

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_home_page_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        home_page_url = _parse_home_page_url(d.pop("HomePageUrl", UNSET))

        _status = d.pop("Status", UNSET)
        status: Union[Unset, LiveTvServiceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LiveTvServiceStatus(_status)

        def _parse_status_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status_message = _parse_status_message(d.pop("StatusMessage", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("Version", UNSET))

        has_update_available = d.pop("HasUpdateAvailable", UNSET)

        is_visible = d.pop("IsVisible", UNSET)

        def _parse_tuners(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tuners_type_0 = cast(List[str], data)

                return tuners_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        tuners = _parse_tuners(d.pop("Tuners", UNSET))

        live_tv_service_info = cls(
            name=name,
            home_page_url=home_page_url,
            status=status,
            status_message=status_message,
            version=version,
            has_update_available=has_update_available,
            is_visible=is_visible,
            tuners=tuners,
        )

        return live_tv_service_info
