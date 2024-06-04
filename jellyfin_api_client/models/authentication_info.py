from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union
import datetime
from dateutil.parser import isoparse


T = TypeVar("T", bound="AuthenticationInfo")


@_attrs_define
class AuthenticationInfo:
    """
    Attributes:
        id (Union[Unset, int]): Gets or sets the identifier.
        access_token (Union[None, Unset, str]): Gets or sets the access token.
        device_id (Union[None, Unset, str]): Gets or sets the device identifier.
        app_name (Union[None, Unset, str]): Gets or sets the name of the application.
        app_version (Union[None, Unset, str]): Gets or sets the application version.
        device_name (Union[None, Unset, str]): Gets or sets the name of the device.
        user_id (Union[Unset, str]): Gets or sets the user identifier.
        is_active (Union[Unset, bool]): Gets or sets a value indicating whether this instance is active.
        date_created (Union[Unset, datetime.datetime]): Gets or sets the date created.
        date_revoked (Union[None, Unset, datetime.datetime]): Gets or sets the date revoked.
        date_last_activity (Union[Unset, datetime.datetime]):
        user_name (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    access_token: Union[None, Unset, str] = UNSET
    device_id: Union[None, Unset, str] = UNSET
    app_name: Union[None, Unset, str] = UNSET
    app_version: Union[None, Unset, str] = UNSET
    device_name: Union[None, Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    date_revoked: Union[None, Unset, datetime.datetime] = UNSET
    date_last_activity: Union[Unset, datetime.datetime] = UNSET
    user_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        access_token: Union[None, Unset, str]
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        device_id: Union[None, Unset, str]
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

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

        device_name: Union[None, Unset, str]
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        user_id = self.user_id

        is_active = self.is_active

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_revoked: Union[None, Unset, str]
        if isinstance(self.date_revoked, Unset):
            date_revoked = UNSET
        elif isinstance(self.date_revoked, datetime.datetime):
            date_revoked = self.date_revoked.isoformat()
        else:
            date_revoked = self.date_revoked

        date_last_activity: Union[Unset, str] = UNSET
        if not isinstance(self.date_last_activity, Unset):
            date_last_activity = self.date_last_activity.isoformat()

        user_name: Union[None, Unset, str]
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if app_name is not UNSET:
            field_dict["AppName"] = app_name
        if app_version is not UNSET:
            field_dict["AppVersion"] = app_version
        if device_name is not UNSET:
            field_dict["DeviceName"] = device_name
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if is_active is not UNSET:
            field_dict["IsActive"] = is_active
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if date_revoked is not UNSET:
            field_dict["DateRevoked"] = date_revoked
        if date_last_activity is not UNSET:
            field_dict["DateLastActivity"] = date_last_activity
        if user_name is not UNSET:
            field_dict["UserName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        def _parse_access_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        access_token = _parse_access_token(d.pop("AccessToken", UNSET))

        def _parse_device_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_id = _parse_device_id(d.pop("DeviceId", UNSET))

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

        def _parse_device_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_name = _parse_device_name(d.pop("DeviceName", UNSET))

        user_id = d.pop("UserId", UNSET)

        is_active = d.pop("IsActive", UNSET)

        _date_created = d.pop("DateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        def _parse_date_revoked(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_revoked_type_0 = isoparse(data)

                return date_revoked_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_revoked = _parse_date_revoked(d.pop("DateRevoked", UNSET))

        _date_last_activity = d.pop("DateLastActivity", UNSET)
        date_last_activity: Union[Unset, datetime.datetime]
        if isinstance(_date_last_activity, Unset):
            date_last_activity = UNSET
        else:
            date_last_activity = isoparse(_date_last_activity)

        def _parse_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_name = _parse_user_name(d.pop("UserName", UNSET))

        authentication_info = cls(
            id=id,
            access_token=access_token,
            device_id=device_id,
            app_name=app_name,
            app_version=app_version,
            device_name=device_name,
            user_id=user_id,
            is_active=is_active,
            date_created=date_created,
            date_revoked=date_revoked,
            date_last_activity=date_last_activity,
            user_name=user_name,
        )

        return authentication_info
