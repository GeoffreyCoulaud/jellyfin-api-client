from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

import datetime
from typing import cast
from typing import Union
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.client_capabilities import ClientCapabilities


T = TypeVar("T", bound="DeviceInfo")


@_attrs_define
class DeviceInfo:
    """
    Attributes:
        name (Union[None, Unset, str]):
        custom_name (Union[None, Unset, str]):
        access_token (Union[None, Unset, str]): Gets or sets the access token.
        id (Union[None, Unset, str]): Gets or sets the identifier.
        last_user_name (Union[None, Unset, str]): Gets or sets the last name of the user.
        app_name (Union[None, Unset, str]): Gets or sets the name of the application.
        app_version (Union[None, Unset, str]): Gets or sets the application version.
        last_user_id (Union[Unset, str]): Gets or sets the last user identifier.
        date_last_activity (Union[Unset, datetime.datetime]): Gets or sets the date last modified.
        capabilities (Union['ClientCapabilities', None, Unset]): Gets or sets the capabilities.
        icon_url (Union[None, Unset, str]):
    """

    name: Union[None, Unset, str] = UNSET
    custom_name: Union[None, Unset, str] = UNSET
    access_token: Union[None, Unset, str] = UNSET
    id: Union[None, Unset, str] = UNSET
    last_user_name: Union[None, Unset, str] = UNSET
    app_name: Union[None, Unset, str] = UNSET
    app_version: Union[None, Unset, str] = UNSET
    last_user_id: Union[Unset, str] = UNSET
    date_last_activity: Union[Unset, datetime.datetime] = UNSET
    capabilities: Union["ClientCapabilities", None, Unset] = UNSET
    icon_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.client_capabilities import ClientCapabilities

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        custom_name: Union[None, Unset, str]
        if isinstance(self.custom_name, Unset):
            custom_name = UNSET
        else:
            custom_name = self.custom_name

        access_token: Union[None, Unset, str]
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        last_user_name: Union[None, Unset, str]
        if isinstance(self.last_user_name, Unset):
            last_user_name = UNSET
        else:
            last_user_name = self.last_user_name

        app_name: Union[None, Unset, str]
        if isinstance(self.app_name, Unset):
            app_name = UNSET
        else:
            app_name = self.app_name

        app_version: Union[None, Unset, str]
        if isinstance(self.app_version, Unset):
            app_version = UNSET
        else:
            app_version = self.app_version

        last_user_id = self.last_user_id

        date_last_activity: Union[Unset, str] = UNSET
        if not isinstance(self.date_last_activity, Unset):
            date_last_activity = self.date_last_activity.isoformat()

        capabilities: Union[Dict[str, Any], None, Unset]
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, ClientCapabilities):
            capabilities = self.capabilities.to_dict()
        else:
            capabilities = self.capabilities

        icon_url: Union[None, Unset, str]
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if custom_name is not UNSET:
            field_dict["CustomName"] = custom_name
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if id is not UNSET:
            field_dict["Id"] = id
        if last_user_name is not UNSET:
            field_dict["LastUserName"] = last_user_name
        if app_name is not UNSET:
            field_dict["AppName"] = app_name
        if app_version is not UNSET:
            field_dict["AppVersion"] = app_version
        if last_user_id is not UNSET:
            field_dict["LastUserId"] = last_user_id
        if date_last_activity is not UNSET:
            field_dict["DateLastActivity"] = date_last_activity
        if capabilities is not UNSET:
            field_dict["Capabilities"] = capabilities
        if icon_url is not UNSET:
            field_dict["IconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_capabilities import ClientCapabilities

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_custom_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_name = _parse_custom_name(d.pop("CustomName", UNSET))

        def _parse_access_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        access_token = _parse_access_token(d.pop("AccessToken", UNSET))

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_last_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_user_name = _parse_last_user_name(d.pop("LastUserName", UNSET))

        def _parse_app_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_name = _parse_app_name(d.pop("AppName", UNSET))

        def _parse_app_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_version = _parse_app_version(d.pop("AppVersion", UNSET))

        last_user_id = d.pop("LastUserId", UNSET)

        _date_last_activity = d.pop("DateLastActivity", UNSET)
        date_last_activity: Union[Unset, datetime.datetime]
        if isinstance(_date_last_activity, Unset):
            date_last_activity = UNSET
        else:
            date_last_activity = isoparse(_date_last_activity)

        def _parse_capabilities(
            data: object,
        ) -> Union["ClientCapabilities", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                capabilities_type_1 = ClientCapabilities.from_dict(data)

                return capabilities_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ClientCapabilities", None, Unset], data)

        capabilities = _parse_capabilities(d.pop("Capabilities", UNSET))

        def _parse_icon_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_url = _parse_icon_url(d.pop("IconUrl", UNSET))

        device_info = cls(
            name=name,
            custom_name=custom_name,
            access_token=access_token,
            id=id,
            last_user_name=last_user_name,
            app_name=app_name,
            app_version=app_version,
            last_user_id=last_user_id,
            date_last_activity=date_last_activity,
            capabilities=capabilities,
            icon_url=icon_url,
        )

        return device_info
