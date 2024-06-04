from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from ..models.sync_play_user_access_type import SyncPlayUserAccessType
from typing import cast, Union
from typing import List
from ..models.unrated_item import UnratedItem

if TYPE_CHECKING:
    from ..models.access_schedule import AccessSchedule


T = TypeVar("T", bound="UserPolicy")


@_attrs_define
class UserPolicy:
    """
    Attributes:
        authentication_provider_id (str):
        password_reset_provider_id (str):
        is_administrator (Union[Unset, bool]): Gets or sets a value indicating whether this instance is administrator.
        is_hidden (Union[Unset, bool]): Gets or sets a value indicating whether this instance is hidden.
        enable_collection_management (Union[Unset, bool]): Gets or sets a value indicating whether this instance can
            manage collections. Default: False.
        enable_subtitle_management (Union[Unset, bool]): Gets or sets a value indicating whether this instance can
            manage subtitles. Default: False.
        enable_lyric_management (Union[Unset, bool]): Gets or sets a value indicating whether this user can manage
            lyrics. Default: False.
        is_disabled (Union[Unset, bool]): Gets or sets a value indicating whether this instance is disabled.
        max_parental_rating (Union[None, Unset, int]): Gets or sets the max parental rating.
        blocked_tags (Union[List[str], None, Unset]):
        allowed_tags (Union[List[str], None, Unset]):
        enable_user_preference_access (Union[Unset, bool]):
        access_schedules (Union[List['AccessSchedule'], None, Unset]):
        block_unrated_items (Union[List[UnratedItem], None, Unset]):
        enable_remote_control_of_other_users (Union[Unset, bool]):
        enable_shared_device_control (Union[Unset, bool]):
        enable_remote_access (Union[Unset, bool]):
        enable_live_tv_management (Union[Unset, bool]):
        enable_live_tv_access (Union[Unset, bool]):
        enable_media_playback (Union[Unset, bool]):
        enable_audio_playback_transcoding (Union[Unset, bool]):
        enable_video_playback_transcoding (Union[Unset, bool]):
        enable_playback_remuxing (Union[Unset, bool]):
        force_remote_source_transcoding (Union[Unset, bool]):
        enable_content_deletion (Union[Unset, bool]):
        enable_content_deletion_from_folders (Union[List[str], None, Unset]):
        enable_content_downloading (Union[Unset, bool]):
        enable_sync_transcoding (Union[Unset, bool]): Gets or sets a value indicating whether [enable synchronize].
        enable_media_conversion (Union[Unset, bool]):
        enabled_devices (Union[List[str], None, Unset]):
        enable_all_devices (Union[Unset, bool]):
        enabled_channels (Union[List[str], None, Unset]):
        enable_all_channels (Union[Unset, bool]):
        enabled_folders (Union[List[str], None, Unset]):
        enable_all_folders (Union[Unset, bool]):
        invalid_login_attempt_count (Union[Unset, int]):
        login_attempts_before_lockout (Union[Unset, int]):
        max_active_sessions (Union[Unset, int]):
        enable_public_sharing (Union[Unset, bool]):
        blocked_media_folders (Union[List[str], None, Unset]):
        blocked_channels (Union[List[str], None, Unset]):
        remote_client_bitrate_limit (Union[Unset, int]):
        sync_play_access (Union[Unset, SyncPlayUserAccessType]): Enum SyncPlayUserAccessType.
    """

    authentication_provider_id: str
    password_reset_provider_id: str
    is_administrator: Union[Unset, bool] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    enable_collection_management: Union[Unset, bool] = False
    enable_subtitle_management: Union[Unset, bool] = False
    enable_lyric_management: Union[Unset, bool] = False
    is_disabled: Union[Unset, bool] = UNSET
    max_parental_rating: Union[None, Unset, int] = UNSET
    blocked_tags: Union[List[str], None, Unset] = UNSET
    allowed_tags: Union[List[str], None, Unset] = UNSET
    enable_user_preference_access: Union[Unset, bool] = UNSET
    access_schedules: Union[List["AccessSchedule"], None, Unset] = UNSET
    block_unrated_items: Union[List[UnratedItem], None, Unset] = UNSET
    enable_remote_control_of_other_users: Union[Unset, bool] = UNSET
    enable_shared_device_control: Union[Unset, bool] = UNSET
    enable_remote_access: Union[Unset, bool] = UNSET
    enable_live_tv_management: Union[Unset, bool] = UNSET
    enable_live_tv_access: Union[Unset, bool] = UNSET
    enable_media_playback: Union[Unset, bool] = UNSET
    enable_audio_playback_transcoding: Union[Unset, bool] = UNSET
    enable_video_playback_transcoding: Union[Unset, bool] = UNSET
    enable_playback_remuxing: Union[Unset, bool] = UNSET
    force_remote_source_transcoding: Union[Unset, bool] = UNSET
    enable_content_deletion: Union[Unset, bool] = UNSET
    enable_content_deletion_from_folders: Union[List[str], None, Unset] = UNSET
    enable_content_downloading: Union[Unset, bool] = UNSET
    enable_sync_transcoding: Union[Unset, bool] = UNSET
    enable_media_conversion: Union[Unset, bool] = UNSET
    enabled_devices: Union[List[str], None, Unset] = UNSET
    enable_all_devices: Union[Unset, bool] = UNSET
    enabled_channels: Union[List[str], None, Unset] = UNSET
    enable_all_channels: Union[Unset, bool] = UNSET
    enabled_folders: Union[List[str], None, Unset] = UNSET
    enable_all_folders: Union[Unset, bool] = UNSET
    invalid_login_attempt_count: Union[Unset, int] = UNSET
    login_attempts_before_lockout: Union[Unset, int] = UNSET
    max_active_sessions: Union[Unset, int] = UNSET
    enable_public_sharing: Union[Unset, bool] = UNSET
    blocked_media_folders: Union[List[str], None, Unset] = UNSET
    blocked_channels: Union[List[str], None, Unset] = UNSET
    remote_client_bitrate_limit: Union[Unset, int] = UNSET
    sync_play_access: Union[Unset, SyncPlayUserAccessType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        authentication_provider_id = self.authentication_provider_id

        password_reset_provider_id = self.password_reset_provider_id

        is_administrator = self.is_administrator

        is_hidden = self.is_hidden

        enable_collection_management = self.enable_collection_management

        enable_subtitle_management = self.enable_subtitle_management

        enable_lyric_management = self.enable_lyric_management

        is_disabled = self.is_disabled

        max_parental_rating: Union[None, Unset, int]
        if isinstance(self.max_parental_rating, Unset):
            max_parental_rating = UNSET
        else:
            max_parental_rating = self.max_parental_rating

        blocked_tags: Union[List[str], None, Unset]
        if isinstance(self.blocked_tags, Unset):
            blocked_tags = UNSET
        elif isinstance(self.blocked_tags, list):
            blocked_tags = self.blocked_tags

        else:
            blocked_tags = self.blocked_tags

        allowed_tags: Union[List[str], None, Unset]
        if isinstance(self.allowed_tags, Unset):
            allowed_tags = UNSET
        elif isinstance(self.allowed_tags, list):
            allowed_tags = self.allowed_tags

        else:
            allowed_tags = self.allowed_tags

        enable_user_preference_access = self.enable_user_preference_access

        access_schedules: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.access_schedules, Unset):
            access_schedules = UNSET
        elif isinstance(self.access_schedules, list):
            access_schedules = []
            for access_schedules_type_0_item_data in self.access_schedules:
                access_schedules_type_0_item = (
                    access_schedules_type_0_item_data.to_dict()
                )
                access_schedules.append(access_schedules_type_0_item)

        else:
            access_schedules = self.access_schedules

        block_unrated_items: Union[List[str], None, Unset]
        if isinstance(self.block_unrated_items, Unset):
            block_unrated_items = UNSET
        elif isinstance(self.block_unrated_items, list):
            block_unrated_items = []
            for block_unrated_items_type_0_item_data in self.block_unrated_items:
                block_unrated_items_type_0_item = (
                    block_unrated_items_type_0_item_data.value
                )
                block_unrated_items.append(block_unrated_items_type_0_item)

        else:
            block_unrated_items = self.block_unrated_items

        enable_remote_control_of_other_users = self.enable_remote_control_of_other_users

        enable_shared_device_control = self.enable_shared_device_control

        enable_remote_access = self.enable_remote_access

        enable_live_tv_management = self.enable_live_tv_management

        enable_live_tv_access = self.enable_live_tv_access

        enable_media_playback = self.enable_media_playback

        enable_audio_playback_transcoding = self.enable_audio_playback_transcoding

        enable_video_playback_transcoding = self.enable_video_playback_transcoding

        enable_playback_remuxing = self.enable_playback_remuxing

        force_remote_source_transcoding = self.force_remote_source_transcoding

        enable_content_deletion = self.enable_content_deletion

        enable_content_deletion_from_folders: Union[List[str], None, Unset]
        if isinstance(self.enable_content_deletion_from_folders, Unset):
            enable_content_deletion_from_folders = UNSET
        elif isinstance(self.enable_content_deletion_from_folders, list):
            enable_content_deletion_from_folders = (
                self.enable_content_deletion_from_folders
            )

        else:
            enable_content_deletion_from_folders = (
                self.enable_content_deletion_from_folders
            )

        enable_content_downloading = self.enable_content_downloading

        enable_sync_transcoding = self.enable_sync_transcoding

        enable_media_conversion = self.enable_media_conversion

        enabled_devices: Union[List[str], None, Unset]
        if isinstance(self.enabled_devices, Unset):
            enabled_devices = UNSET
        elif isinstance(self.enabled_devices, list):
            enabled_devices = self.enabled_devices

        else:
            enabled_devices = self.enabled_devices

        enable_all_devices = self.enable_all_devices

        enabled_channels: Union[List[str], None, Unset]
        if isinstance(self.enabled_channels, Unset):
            enabled_channels = UNSET
        elif isinstance(self.enabled_channels, list):
            enabled_channels = self.enabled_channels

        else:
            enabled_channels = self.enabled_channels

        enable_all_channels = self.enable_all_channels

        enabled_folders: Union[List[str], None, Unset]
        if isinstance(self.enabled_folders, Unset):
            enabled_folders = UNSET
        elif isinstance(self.enabled_folders, list):
            enabled_folders = self.enabled_folders

        else:
            enabled_folders = self.enabled_folders

        enable_all_folders = self.enable_all_folders

        invalid_login_attempt_count = self.invalid_login_attempt_count

        login_attempts_before_lockout = self.login_attempts_before_lockout

        max_active_sessions = self.max_active_sessions

        enable_public_sharing = self.enable_public_sharing

        blocked_media_folders: Union[List[str], None, Unset]
        if isinstance(self.blocked_media_folders, Unset):
            blocked_media_folders = UNSET
        elif isinstance(self.blocked_media_folders, list):
            blocked_media_folders = self.blocked_media_folders

        else:
            blocked_media_folders = self.blocked_media_folders

        blocked_channels: Union[List[str], None, Unset]
        if isinstance(self.blocked_channels, Unset):
            blocked_channels = UNSET
        elif isinstance(self.blocked_channels, list):
            blocked_channels = self.blocked_channels

        else:
            blocked_channels = self.blocked_channels

        remote_client_bitrate_limit = self.remote_client_bitrate_limit

        sync_play_access: Union[Unset, str] = UNSET
        if not isinstance(self.sync_play_access, Unset):
            sync_play_access = self.sync_play_access.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "AuthenticationProviderId": authentication_provider_id,
                "PasswordResetProviderId": password_reset_provider_id,
            }
        )
        if is_administrator is not UNSET:
            field_dict["IsAdministrator"] = is_administrator
        if is_hidden is not UNSET:
            field_dict["IsHidden"] = is_hidden
        if enable_collection_management is not UNSET:
            field_dict["EnableCollectionManagement"] = enable_collection_management
        if enable_subtitle_management is not UNSET:
            field_dict["EnableSubtitleManagement"] = enable_subtitle_management
        if enable_lyric_management is not UNSET:
            field_dict["EnableLyricManagement"] = enable_lyric_management
        if is_disabled is not UNSET:
            field_dict["IsDisabled"] = is_disabled
        if max_parental_rating is not UNSET:
            field_dict["MaxParentalRating"] = max_parental_rating
        if blocked_tags is not UNSET:
            field_dict["BlockedTags"] = blocked_tags
        if allowed_tags is not UNSET:
            field_dict["AllowedTags"] = allowed_tags
        if enable_user_preference_access is not UNSET:
            field_dict["EnableUserPreferenceAccess"] = enable_user_preference_access
        if access_schedules is not UNSET:
            field_dict["AccessSchedules"] = access_schedules
        if block_unrated_items is not UNSET:
            field_dict["BlockUnratedItems"] = block_unrated_items
        if enable_remote_control_of_other_users is not UNSET:
            field_dict["EnableRemoteControlOfOtherUsers"] = (
                enable_remote_control_of_other_users
            )
        if enable_shared_device_control is not UNSET:
            field_dict["EnableSharedDeviceControl"] = enable_shared_device_control
        if enable_remote_access is not UNSET:
            field_dict["EnableRemoteAccess"] = enable_remote_access
        if enable_live_tv_management is not UNSET:
            field_dict["EnableLiveTvManagement"] = enable_live_tv_management
        if enable_live_tv_access is not UNSET:
            field_dict["EnableLiveTvAccess"] = enable_live_tv_access
        if enable_media_playback is not UNSET:
            field_dict["EnableMediaPlayback"] = enable_media_playback
        if enable_audio_playback_transcoding is not UNSET:
            field_dict["EnableAudioPlaybackTranscoding"] = (
                enable_audio_playback_transcoding
            )
        if enable_video_playback_transcoding is not UNSET:
            field_dict["EnableVideoPlaybackTranscoding"] = (
                enable_video_playback_transcoding
            )
        if enable_playback_remuxing is not UNSET:
            field_dict["EnablePlaybackRemuxing"] = enable_playback_remuxing
        if force_remote_source_transcoding is not UNSET:
            field_dict["ForceRemoteSourceTranscoding"] = force_remote_source_transcoding
        if enable_content_deletion is not UNSET:
            field_dict["EnableContentDeletion"] = enable_content_deletion
        if enable_content_deletion_from_folders is not UNSET:
            field_dict["EnableContentDeletionFromFolders"] = (
                enable_content_deletion_from_folders
            )
        if enable_content_downloading is not UNSET:
            field_dict["EnableContentDownloading"] = enable_content_downloading
        if enable_sync_transcoding is not UNSET:
            field_dict["EnableSyncTranscoding"] = enable_sync_transcoding
        if enable_media_conversion is not UNSET:
            field_dict["EnableMediaConversion"] = enable_media_conversion
        if enabled_devices is not UNSET:
            field_dict["EnabledDevices"] = enabled_devices
        if enable_all_devices is not UNSET:
            field_dict["EnableAllDevices"] = enable_all_devices
        if enabled_channels is not UNSET:
            field_dict["EnabledChannels"] = enabled_channels
        if enable_all_channels is not UNSET:
            field_dict["EnableAllChannels"] = enable_all_channels
        if enabled_folders is not UNSET:
            field_dict["EnabledFolders"] = enabled_folders
        if enable_all_folders is not UNSET:
            field_dict["EnableAllFolders"] = enable_all_folders
        if invalid_login_attempt_count is not UNSET:
            field_dict["InvalidLoginAttemptCount"] = invalid_login_attempt_count
        if login_attempts_before_lockout is not UNSET:
            field_dict["LoginAttemptsBeforeLockout"] = login_attempts_before_lockout
        if max_active_sessions is not UNSET:
            field_dict["MaxActiveSessions"] = max_active_sessions
        if enable_public_sharing is not UNSET:
            field_dict["EnablePublicSharing"] = enable_public_sharing
        if blocked_media_folders is not UNSET:
            field_dict["BlockedMediaFolders"] = blocked_media_folders
        if blocked_channels is not UNSET:
            field_dict["BlockedChannels"] = blocked_channels
        if remote_client_bitrate_limit is not UNSET:
            field_dict["RemoteClientBitrateLimit"] = remote_client_bitrate_limit
        if sync_play_access is not UNSET:
            field_dict["SyncPlayAccess"] = sync_play_access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_schedule import AccessSchedule

        d = src_dict.copy()
        authentication_provider_id = d.pop("AuthenticationProviderId")

        password_reset_provider_id = d.pop("PasswordResetProviderId")

        is_administrator = d.pop("IsAdministrator", UNSET)

        is_hidden = d.pop("IsHidden", UNSET)

        enable_collection_management = d.pop("EnableCollectionManagement", UNSET)

        enable_subtitle_management = d.pop("EnableSubtitleManagement", UNSET)

        enable_lyric_management = d.pop("EnableLyricManagement", UNSET)

        is_disabled = d.pop("IsDisabled", UNSET)

        def _parse_max_parental_rating(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_parental_rating = _parse_max_parental_rating(
            d.pop("MaxParentalRating", UNSET)
        )

        def _parse_blocked_tags(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_tags_type_0 = cast(List[str], data)

                return blocked_tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        blocked_tags = _parse_blocked_tags(d.pop("BlockedTags", UNSET))

        def _parse_allowed_tags(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_tags_type_0 = cast(List[str], data)

                return allowed_tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        allowed_tags = _parse_allowed_tags(d.pop("AllowedTags", UNSET))

        enable_user_preference_access = d.pop("EnableUserPreferenceAccess", UNSET)

        def _parse_access_schedules(
            data: object,
        ) -> Union[List["AccessSchedule"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_schedules_type_0 = []
                _access_schedules_type_0 = data
                for access_schedules_type_0_item_data in _access_schedules_type_0:
                    access_schedules_type_0_item = AccessSchedule.from_dict(
                        access_schedules_type_0_item_data
                    )

                    access_schedules_type_0.append(access_schedules_type_0_item)

                return access_schedules_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AccessSchedule"], None, Unset], data)

        access_schedules = _parse_access_schedules(d.pop("AccessSchedules", UNSET))

        def _parse_block_unrated_items(
            data: object,
        ) -> Union[List[UnratedItem], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                block_unrated_items_type_0 = []
                _block_unrated_items_type_0 = data
                for block_unrated_items_type_0_item_data in _block_unrated_items_type_0:
                    block_unrated_items_type_0_item = UnratedItem(
                        block_unrated_items_type_0_item_data
                    )

                    block_unrated_items_type_0.append(block_unrated_items_type_0_item)

                return block_unrated_items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[UnratedItem], None, Unset], data)

        block_unrated_items = _parse_block_unrated_items(
            d.pop("BlockUnratedItems", UNSET)
        )

        enable_remote_control_of_other_users = d.pop(
            "EnableRemoteControlOfOtherUsers", UNSET
        )

        enable_shared_device_control = d.pop("EnableSharedDeviceControl", UNSET)

        enable_remote_access = d.pop("EnableRemoteAccess", UNSET)

        enable_live_tv_management = d.pop("EnableLiveTvManagement", UNSET)

        enable_live_tv_access = d.pop("EnableLiveTvAccess", UNSET)

        enable_media_playback = d.pop("EnableMediaPlayback", UNSET)

        enable_audio_playback_transcoding = d.pop(
            "EnableAudioPlaybackTranscoding", UNSET
        )

        enable_video_playback_transcoding = d.pop(
            "EnableVideoPlaybackTranscoding", UNSET
        )

        enable_playback_remuxing = d.pop("EnablePlaybackRemuxing", UNSET)

        force_remote_source_transcoding = d.pop("ForceRemoteSourceTranscoding", UNSET)

        enable_content_deletion = d.pop("EnableContentDeletion", UNSET)

        def _parse_enable_content_deletion_from_folders(
            data: object,
        ) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enable_content_deletion_from_folders_type_0 = cast(List[str], data)

                return enable_content_deletion_from_folders_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        enable_content_deletion_from_folders = (
            _parse_enable_content_deletion_from_folders(
                d.pop("EnableContentDeletionFromFolders", UNSET)
            )
        )

        enable_content_downloading = d.pop("EnableContentDownloading", UNSET)

        enable_sync_transcoding = d.pop("EnableSyncTranscoding", UNSET)

        enable_media_conversion = d.pop("EnableMediaConversion", UNSET)

        def _parse_enabled_devices(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enabled_devices_type_0 = cast(List[str], data)

                return enabled_devices_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        enabled_devices = _parse_enabled_devices(d.pop("EnabledDevices", UNSET))

        enable_all_devices = d.pop("EnableAllDevices", UNSET)

        def _parse_enabled_channels(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enabled_channels_type_0 = cast(List[str], data)

                return enabled_channels_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        enabled_channels = _parse_enabled_channels(d.pop("EnabledChannels", UNSET))

        enable_all_channels = d.pop("EnableAllChannels", UNSET)

        def _parse_enabled_folders(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enabled_folders_type_0 = cast(List[str], data)

                return enabled_folders_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        enabled_folders = _parse_enabled_folders(d.pop("EnabledFolders", UNSET))

        enable_all_folders = d.pop("EnableAllFolders", UNSET)

        invalid_login_attempt_count = d.pop("InvalidLoginAttemptCount", UNSET)

        login_attempts_before_lockout = d.pop("LoginAttemptsBeforeLockout", UNSET)

        max_active_sessions = d.pop("MaxActiveSessions", UNSET)

        enable_public_sharing = d.pop("EnablePublicSharing", UNSET)

        def _parse_blocked_media_folders(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_media_folders_type_0 = cast(List[str], data)

                return blocked_media_folders_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        blocked_media_folders = _parse_blocked_media_folders(
            d.pop("BlockedMediaFolders", UNSET)
        )

        def _parse_blocked_channels(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_channels_type_0 = cast(List[str], data)

                return blocked_channels_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        blocked_channels = _parse_blocked_channels(d.pop("BlockedChannels", UNSET))

        remote_client_bitrate_limit = d.pop("RemoteClientBitrateLimit", UNSET)

        _sync_play_access = d.pop("SyncPlayAccess", UNSET)
        sync_play_access: Union[Unset, SyncPlayUserAccessType]
        if isinstance(_sync_play_access, Unset):
            sync_play_access = UNSET
        else:
            sync_play_access = SyncPlayUserAccessType(_sync_play_access)

        user_policy = cls(
            authentication_provider_id=authentication_provider_id,
            password_reset_provider_id=password_reset_provider_id,
            is_administrator=is_administrator,
            is_hidden=is_hidden,
            enable_collection_management=enable_collection_management,
            enable_subtitle_management=enable_subtitle_management,
            enable_lyric_management=enable_lyric_management,
            is_disabled=is_disabled,
            max_parental_rating=max_parental_rating,
            blocked_tags=blocked_tags,
            allowed_tags=allowed_tags,
            enable_user_preference_access=enable_user_preference_access,
            access_schedules=access_schedules,
            block_unrated_items=block_unrated_items,
            enable_remote_control_of_other_users=enable_remote_control_of_other_users,
            enable_shared_device_control=enable_shared_device_control,
            enable_remote_access=enable_remote_access,
            enable_live_tv_management=enable_live_tv_management,
            enable_live_tv_access=enable_live_tv_access,
            enable_media_playback=enable_media_playback,
            enable_audio_playback_transcoding=enable_audio_playback_transcoding,
            enable_video_playback_transcoding=enable_video_playback_transcoding,
            enable_playback_remuxing=enable_playback_remuxing,
            force_remote_source_transcoding=force_remote_source_transcoding,
            enable_content_deletion=enable_content_deletion,
            enable_content_deletion_from_folders=enable_content_deletion_from_folders,
            enable_content_downloading=enable_content_downloading,
            enable_sync_transcoding=enable_sync_transcoding,
            enable_media_conversion=enable_media_conversion,
            enabled_devices=enabled_devices,
            enable_all_devices=enable_all_devices,
            enabled_channels=enabled_channels,
            enable_all_channels=enable_all_channels,
            enabled_folders=enabled_folders,
            enable_all_folders=enable_all_folders,
            invalid_login_attempt_count=invalid_login_attempt_count,
            login_attempts_before_lockout=login_attempts_before_lockout,
            max_active_sessions=max_active_sessions,
            enable_public_sharing=enable_public_sharing,
            blocked_media_folders=blocked_media_folders,
            blocked_channels=blocked_channels,
            remote_client_bitrate_limit=remote_client_bitrate_limit,
            sync_play_access=sync_play_access,
        )

        return user_policy
