from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from ..models.media_type import MediaType
from typing import cast
from typing import List
from typing import Union
from ..models.general_command_type import GeneralCommandType

if TYPE_CHECKING:
    from ..models.device_profile import DeviceProfile


T = TypeVar("T", bound="ClientCapabilities")


@_attrs_define
class ClientCapabilities:
    """
    Attributes:
        playable_media_types (Union[List[MediaType], None, Unset]):
        supported_commands (Union[List[GeneralCommandType], None, Unset]):
        supports_media_control (Union[Unset, bool]):
        supports_persistent_identifier (Union[Unset, bool]):
        device_profile (Union['DeviceProfile', None, Unset]): A MediaBrowser.Model.Dlna.DeviceProfile represents a set
            of metadata which determines which content a certain device is able to play.
            <br />
            Specifically, it defines the supported <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
            <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including
            codec profiles and levels)
            the device is able to direct play (without transcoding or remuxing),
            as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
            transcode to</see> in case it isn't.
        app_store_url (Union[None, Unset, str]):
        icon_url (Union[None, Unset, str]):
        supports_content_uploading (Union[None, Unset, bool]):  Default: False.
        supports_sync (Union[None, Unset, bool]):  Default: False.
    """

    playable_media_types: Union[List[MediaType], None, Unset] = UNSET
    supported_commands: Union[List[GeneralCommandType], None, Unset] = UNSET
    supports_media_control: Union[Unset, bool] = UNSET
    supports_persistent_identifier: Union[Unset, bool] = UNSET
    device_profile: Union["DeviceProfile", None, Unset] = UNSET
    app_store_url: Union[None, Unset, str] = UNSET
    icon_url: Union[None, Unset, str] = UNSET
    supports_content_uploading: Union[None, Unset, bool] = False
    supports_sync: Union[None, Unset, bool] = False

    def to_dict(self) -> Dict[str, Any]:
        from ..models.device_profile import DeviceProfile

        playable_media_types: Union[List[str], None, Unset]
        if isinstance(self.playable_media_types, Unset):
            playable_media_types = UNSET
        elif isinstance(self.playable_media_types, list):
            playable_media_types = []
            for playable_media_types_type_0_item_data in self.playable_media_types:
                playable_media_types_type_0_item = (
                    playable_media_types_type_0_item_data.value
                )
                playable_media_types.append(playable_media_types_type_0_item)

        else:
            playable_media_types = self.playable_media_types

        supported_commands: Union[List[str], None, Unset]
        if isinstance(self.supported_commands, Unset):
            supported_commands = UNSET
        elif isinstance(self.supported_commands, list):
            supported_commands = []
            for supported_commands_type_0_item_data in self.supported_commands:
                supported_commands_type_0_item = (
                    supported_commands_type_0_item_data.value
                )
                supported_commands.append(supported_commands_type_0_item)

        else:
            supported_commands = self.supported_commands

        supports_media_control = self.supports_media_control

        supports_persistent_identifier = self.supports_persistent_identifier

        device_profile: Union[Dict[str, Any], None, Unset]
        if isinstance(self.device_profile, Unset):
            device_profile = UNSET
        elif isinstance(self.device_profile, DeviceProfile):
            device_profile = self.device_profile.to_dict()
        else:
            device_profile = self.device_profile

        app_store_url: Union[None, Unset, str]
        if isinstance(self.app_store_url, Unset):
            app_store_url = UNSET
        else:
            app_store_url = self.app_store_url

        icon_url: Union[None, Unset, str]
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        supports_content_uploading: Union[None, Unset, bool]
        if isinstance(self.supports_content_uploading, Unset):
            supports_content_uploading = UNSET
        else:
            supports_content_uploading = self.supports_content_uploading

        supports_sync: Union[None, Unset, bool]
        if isinstance(self.supports_sync, Unset):
            supports_sync = UNSET
        else:
            supports_sync = self.supports_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if playable_media_types is not UNSET:
            field_dict["PlayableMediaTypes"] = playable_media_types
        if supported_commands is not UNSET:
            field_dict["SupportedCommands"] = supported_commands
        if supports_media_control is not UNSET:
            field_dict["SupportsMediaControl"] = supports_media_control
        if supports_persistent_identifier is not UNSET:
            field_dict["SupportsPersistentIdentifier"] = supports_persistent_identifier
        if device_profile is not UNSET:
            field_dict["DeviceProfile"] = device_profile
        if app_store_url is not UNSET:
            field_dict["AppStoreUrl"] = app_store_url
        if icon_url is not UNSET:
            field_dict["IconUrl"] = icon_url
        if supports_content_uploading is not UNSET:
            field_dict["SupportsContentUploading"] = supports_content_uploading
        if supports_sync is not UNSET:
            field_dict["SupportsSync"] = supports_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_profile import DeviceProfile

        d = src_dict.copy()

        def _parse_playable_media_types(
            data: object,
        ) -> Union[List[MediaType], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                playable_media_types_type_0 = []
                _playable_media_types_type_0 = data
                for (
                    playable_media_types_type_0_item_data
                ) in _playable_media_types_type_0:
                    playable_media_types_type_0_item = MediaType(
                        playable_media_types_type_0_item_data
                    )

                    playable_media_types_type_0.append(playable_media_types_type_0_item)

                return playable_media_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[MediaType], None, Unset], data)

        playable_media_types = _parse_playable_media_types(
            d.pop("PlayableMediaTypes", UNSET)
        )

        def _parse_supported_commands(
            data: object,
        ) -> Union[List[GeneralCommandType], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_commands_type_0 = []
                _supported_commands_type_0 = data
                for supported_commands_type_0_item_data in _supported_commands_type_0:
                    supported_commands_type_0_item = GeneralCommandType(
                        supported_commands_type_0_item_data
                    )

                    supported_commands_type_0.append(supported_commands_type_0_item)

                return supported_commands_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[GeneralCommandType], None, Unset], data)

        supported_commands = _parse_supported_commands(
            d.pop("SupportedCommands", UNSET)
        )

        supports_media_control = d.pop("SupportsMediaControl", UNSET)

        supports_persistent_identifier = d.pop("SupportsPersistentIdentifier", UNSET)

        def _parse_device_profile(data: object) -> Union["DeviceProfile", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_profile_type_1 = DeviceProfile.from_dict(data)

                return device_profile_type_1
            except:  # noqa: E722
                pass
            return cast(Union["DeviceProfile", None, Unset], data)

        device_profile = _parse_device_profile(d.pop("DeviceProfile", UNSET))

        def _parse_app_store_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_store_url = _parse_app_store_url(d.pop("AppStoreUrl", UNSET))

        def _parse_icon_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_url = _parse_icon_url(d.pop("IconUrl", UNSET))

        def _parse_supports_content_uploading(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        supports_content_uploading = _parse_supports_content_uploading(
            d.pop("SupportsContentUploading", UNSET)
        )

        def _parse_supports_sync(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        supports_sync = _parse_supports_sync(d.pop("SupportsSync", UNSET))

        client_capabilities = cls(
            playable_media_types=playable_media_types,
            supported_commands=supported_commands,
            supports_media_control=supports_media_control,
            supports_persistent_identifier=supports_persistent_identifier,
            device_profile=device_profile,
            app_store_url=app_store_url,
            icon_url=icon_url,
            supports_content_uploading=supports_content_uploading,
            supports_sync=supports_sync,
        )

        return client_capabilities
