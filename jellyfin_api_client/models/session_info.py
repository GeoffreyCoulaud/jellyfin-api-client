from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

import datetime
from ..models.media_type import MediaType
from typing import cast
from typing import List
from typing import Union
from dateutil.parser import isoparse
from ..models.general_command_type import GeneralCommandType

if TYPE_CHECKING:
    from ..models.queue_item import QueueItem
    from ..models.base_item_dto import BaseItemDto
    from ..models.client_capabilities import ClientCapabilities
    from ..models.transcoding_info import TranscodingInfo
    from ..models.player_state_info import PlayerStateInfo
    from ..models.session_user_info import SessionUserInfo


T = TypeVar("T", bound="SessionInfo")


@_attrs_define
class SessionInfo:
    """Class SessionInfo.

    Attributes:
        play_state (Union['PlayerStateInfo', None, Unset]):
        additional_users (Union[List['SessionUserInfo'], None, Unset]):
        capabilities (Union['ClientCapabilities', None, Unset]):
        remote_end_point (Union[None, Unset, str]): Gets or sets the remote end point.
        playable_media_types (Union[List[MediaType], None, Unset]): Gets the playable media types.
        id (Union[None, Unset, str]): Gets or sets the id.
        user_id (Union[Unset, str]): Gets or sets the user id.
        user_name (Union[None, Unset, str]): Gets or sets the username.
        client (Union[None, Unset, str]): Gets or sets the type of the client.
        last_activity_date (Union[Unset, datetime.datetime]): Gets or sets the last activity date.
        last_playback_check_in (Union[Unset, datetime.datetime]): Gets or sets the last playback check in.
        last_paused_date (Union[None, Unset, datetime.datetime]): Gets or sets the last paused date.
        device_name (Union[None, Unset, str]): Gets or sets the name of the device.
        device_type (Union[None, Unset, str]): Gets or sets the type of the device.
        now_playing_item (Union['BaseItemDto', None, Unset]): Gets or sets the now playing item.
        now_viewing_item (Union['BaseItemDto', None, Unset]): This is strictly used as a data transfer object from the
            api layer.
            This holds information about a BaseItem in a format that is convenient for the client.
        device_id (Union[None, Unset, str]): Gets or sets the device id.
        application_version (Union[None, Unset, str]): Gets or sets the application version.
        transcoding_info (Union['TranscodingInfo', None, Unset]):
        is_active (Union[Unset, bool]): Gets a value indicating whether this instance is active.
        supports_media_control (Union[Unset, bool]):
        supports_remote_control (Union[Unset, bool]):
        now_playing_queue (Union[List['QueueItem'], None, Unset]):
        now_playing_queue_full_items (Union[List['BaseItemDto'], None, Unset]):
        has_custom_device_name (Union[Unset, bool]):
        playlist_item_id (Union[None, Unset, str]):
        server_id (Union[None, Unset, str]):
        user_primary_image_tag (Union[None, Unset, str]):
        supported_commands (Union[List[GeneralCommandType], None, Unset]): Gets the supported commands.
    """

    play_state: Union["PlayerStateInfo", None, Unset] = UNSET
    additional_users: Union[List["SessionUserInfo"], None, Unset] = UNSET
    capabilities: Union["ClientCapabilities", None, Unset] = UNSET
    remote_end_point: Union[None, Unset, str] = UNSET
    playable_media_types: Union[List[MediaType], None, Unset] = UNSET
    id: Union[None, Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    user_name: Union[None, Unset, str] = UNSET
    client: Union[None, Unset, str] = UNSET
    last_activity_date: Union[Unset, datetime.datetime] = UNSET
    last_playback_check_in: Union[Unset, datetime.datetime] = UNSET
    last_paused_date: Union[None, Unset, datetime.datetime] = UNSET
    device_name: Union[None, Unset, str] = UNSET
    device_type: Union[None, Unset, str] = UNSET
    now_playing_item: Union["BaseItemDto", None, Unset] = UNSET
    now_viewing_item: Union["BaseItemDto", None, Unset] = UNSET
    device_id: Union[None, Unset, str] = UNSET
    application_version: Union[None, Unset, str] = UNSET
    transcoding_info: Union["TranscodingInfo", None, Unset] = UNSET
    is_active: Union[Unset, bool] = UNSET
    supports_media_control: Union[Unset, bool] = UNSET
    supports_remote_control: Union[Unset, bool] = UNSET
    now_playing_queue: Union[List["QueueItem"], None, Unset] = UNSET
    now_playing_queue_full_items: Union[List["BaseItemDto"], None, Unset] = UNSET
    has_custom_device_name: Union[Unset, bool] = UNSET
    playlist_item_id: Union[None, Unset, str] = UNSET
    server_id: Union[None, Unset, str] = UNSET
    user_primary_image_tag: Union[None, Unset, str] = UNSET
    supported_commands: Union[List[GeneralCommandType], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.base_item_dto import BaseItemDto
        from ..models.client_capabilities import ClientCapabilities
        from ..models.transcoding_info import TranscodingInfo
        from ..models.player_state_info import PlayerStateInfo

        play_state: Union[Dict[str, Any], None, Unset]
        if isinstance(self.play_state, Unset):
            play_state = UNSET
        elif isinstance(self.play_state, PlayerStateInfo):
            play_state = self.play_state.to_dict()
        else:
            play_state = self.play_state

        additional_users: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.additional_users, Unset):
            additional_users = UNSET
        elif isinstance(self.additional_users, list):
            additional_users = []
            for additional_users_type_0_item_data in self.additional_users:
                additional_users_type_0_item = (
                    additional_users_type_0_item_data.to_dict()
                )
                additional_users.append(additional_users_type_0_item)

        else:
            additional_users = self.additional_users

        capabilities: Union[Dict[str, Any], None, Unset]
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, ClientCapabilities):
            capabilities = self.capabilities.to_dict()
        else:
            capabilities = self.capabilities

        remote_end_point: Union[None, Unset, str]
        if isinstance(self.remote_end_point, Unset):
            remote_end_point = UNSET
        else:
            remote_end_point = self.remote_end_point

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

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        user_id = self.user_id

        user_name: Union[None, Unset, str]
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        client: Union[None, Unset, str]
        if isinstance(self.client, Unset):
            client = UNSET
        else:
            client = self.client

        last_activity_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_activity_date, Unset):
            last_activity_date = self.last_activity_date.isoformat()

        last_playback_check_in: Union[Unset, str] = UNSET
        if not isinstance(self.last_playback_check_in, Unset):
            last_playback_check_in = self.last_playback_check_in.isoformat()

        last_paused_date: Union[None, Unset, str]
        if isinstance(self.last_paused_date, Unset):
            last_paused_date = UNSET
        elif isinstance(self.last_paused_date, datetime.datetime):
            last_paused_date = self.last_paused_date.isoformat()
        else:
            last_paused_date = self.last_paused_date

        device_name: Union[None, Unset, str]
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        device_type: Union[None, Unset, str]
        if isinstance(self.device_type, Unset):
            device_type = UNSET
        else:
            device_type = self.device_type

        now_playing_item: Union[Dict[str, Any], None, Unset]
        if isinstance(self.now_playing_item, Unset):
            now_playing_item = UNSET
        elif isinstance(self.now_playing_item, BaseItemDto):
            now_playing_item = self.now_playing_item.to_dict()
        else:
            now_playing_item = self.now_playing_item

        now_viewing_item: Union[Dict[str, Any], None, Unset]
        if isinstance(self.now_viewing_item, Unset):
            now_viewing_item = UNSET
        elif isinstance(self.now_viewing_item, BaseItemDto):
            now_viewing_item = self.now_viewing_item.to_dict()
        else:
            now_viewing_item = self.now_viewing_item

        device_id: Union[None, Unset, str]
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

        application_version: Union[None, Unset, str]
        if isinstance(self.application_version, Unset):
            application_version = UNSET
        else:
            application_version = self.application_version

        transcoding_info: Union[Dict[str, Any], None, Unset]
        if isinstance(self.transcoding_info, Unset):
            transcoding_info = UNSET
        elif isinstance(self.transcoding_info, TranscodingInfo):
            transcoding_info = self.transcoding_info.to_dict()
        else:
            transcoding_info = self.transcoding_info

        is_active = self.is_active

        supports_media_control = self.supports_media_control

        supports_remote_control = self.supports_remote_control

        now_playing_queue: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.now_playing_queue, Unset):
            now_playing_queue = UNSET
        elif isinstance(self.now_playing_queue, list):
            now_playing_queue = []
            for now_playing_queue_type_0_item_data in self.now_playing_queue:
                now_playing_queue_type_0_item = (
                    now_playing_queue_type_0_item_data.to_dict()
                )
                now_playing_queue.append(now_playing_queue_type_0_item)

        else:
            now_playing_queue = self.now_playing_queue

        now_playing_queue_full_items: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.now_playing_queue_full_items, Unset):
            now_playing_queue_full_items = UNSET
        elif isinstance(self.now_playing_queue_full_items, list):
            now_playing_queue_full_items = []
            for (
                now_playing_queue_full_items_type_0_item_data
            ) in self.now_playing_queue_full_items:
                now_playing_queue_full_items_type_0_item = (
                    now_playing_queue_full_items_type_0_item_data.to_dict()
                )
                now_playing_queue_full_items.append(
                    now_playing_queue_full_items_type_0_item
                )

        else:
            now_playing_queue_full_items = self.now_playing_queue_full_items

        has_custom_device_name = self.has_custom_device_name

        playlist_item_id: Union[None, Unset, str]
        if isinstance(self.playlist_item_id, Unset):
            playlist_item_id = UNSET
        else:
            playlist_item_id = self.playlist_item_id

        server_id: Union[None, Unset, str]
        if isinstance(self.server_id, Unset):
            server_id = UNSET
        else:
            server_id = self.server_id

        user_primary_image_tag: Union[None, Unset, str]
        if isinstance(self.user_primary_image_tag, Unset):
            user_primary_image_tag = UNSET
        else:
            user_primary_image_tag = self.user_primary_image_tag

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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if play_state is not UNSET:
            field_dict["PlayState"] = play_state
        if additional_users is not UNSET:
            field_dict["AdditionalUsers"] = additional_users
        if capabilities is not UNSET:
            field_dict["Capabilities"] = capabilities
        if remote_end_point is not UNSET:
            field_dict["RemoteEndPoint"] = remote_end_point
        if playable_media_types is not UNSET:
            field_dict["PlayableMediaTypes"] = playable_media_types
        if id is not UNSET:
            field_dict["Id"] = id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if client is not UNSET:
            field_dict["Client"] = client
        if last_activity_date is not UNSET:
            field_dict["LastActivityDate"] = last_activity_date
        if last_playback_check_in is not UNSET:
            field_dict["LastPlaybackCheckIn"] = last_playback_check_in
        if last_paused_date is not UNSET:
            field_dict["LastPausedDate"] = last_paused_date
        if device_name is not UNSET:
            field_dict["DeviceName"] = device_name
        if device_type is not UNSET:
            field_dict["DeviceType"] = device_type
        if now_playing_item is not UNSET:
            field_dict["NowPlayingItem"] = now_playing_item
        if now_viewing_item is not UNSET:
            field_dict["NowViewingItem"] = now_viewing_item
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if application_version is not UNSET:
            field_dict["ApplicationVersion"] = application_version
        if transcoding_info is not UNSET:
            field_dict["TranscodingInfo"] = transcoding_info
        if is_active is not UNSET:
            field_dict["IsActive"] = is_active
        if supports_media_control is not UNSET:
            field_dict["SupportsMediaControl"] = supports_media_control
        if supports_remote_control is not UNSET:
            field_dict["SupportsRemoteControl"] = supports_remote_control
        if now_playing_queue is not UNSET:
            field_dict["NowPlayingQueue"] = now_playing_queue
        if now_playing_queue_full_items is not UNSET:
            field_dict["NowPlayingQueueFullItems"] = now_playing_queue_full_items
        if has_custom_device_name is not UNSET:
            field_dict["HasCustomDeviceName"] = has_custom_device_name
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id
        if user_primary_image_tag is not UNSET:
            field_dict["UserPrimaryImageTag"] = user_primary_image_tag
        if supported_commands is not UNSET:
            field_dict["SupportedCommands"] = supported_commands

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.queue_item import QueueItem
        from ..models.base_item_dto import BaseItemDto
        from ..models.client_capabilities import ClientCapabilities
        from ..models.transcoding_info import TranscodingInfo
        from ..models.player_state_info import PlayerStateInfo
        from ..models.session_user_info import SessionUserInfo

        d = src_dict.copy()

        def _parse_play_state(data: object) -> Union["PlayerStateInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                play_state_type_1 = PlayerStateInfo.from_dict(data)

                return play_state_type_1
            except:  # noqa: E722
                pass
            return cast(Union["PlayerStateInfo", None, Unset], data)

        play_state = _parse_play_state(d.pop("PlayState", UNSET))

        def _parse_additional_users(
            data: object,
        ) -> Union[List["SessionUserInfo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_users_type_0 = []
                _additional_users_type_0 = data
                for additional_users_type_0_item_data in _additional_users_type_0:
                    additional_users_type_0_item = SessionUserInfo.from_dict(
                        additional_users_type_0_item_data
                    )

                    additional_users_type_0.append(additional_users_type_0_item)

                return additional_users_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SessionUserInfo"], None, Unset], data)

        additional_users = _parse_additional_users(d.pop("AdditionalUsers", UNSET))

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

        def _parse_remote_end_point(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remote_end_point = _parse_remote_end_point(d.pop("RemoteEndPoint", UNSET))

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

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        user_id = d.pop("UserId", UNSET)

        def _parse_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_name = _parse_user_name(d.pop("UserName", UNSET))

        def _parse_client(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client = _parse_client(d.pop("Client", UNSET))

        _last_activity_date = d.pop("LastActivityDate", UNSET)
        last_activity_date: Union[Unset, datetime.datetime]
        if isinstance(_last_activity_date, Unset):
            last_activity_date = UNSET
        else:
            last_activity_date = isoparse(_last_activity_date)

        _last_playback_check_in = d.pop("LastPlaybackCheckIn", UNSET)
        last_playback_check_in: Union[Unset, datetime.datetime]
        if isinstance(_last_playback_check_in, Unset):
            last_playback_check_in = UNSET
        else:
            last_playback_check_in = isoparse(_last_playback_check_in)

        def _parse_last_paused_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_paused_date_type_0 = isoparse(data)

                return last_paused_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_paused_date = _parse_last_paused_date(d.pop("LastPausedDate", UNSET))

        def _parse_device_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_name = _parse_device_name(d.pop("DeviceName", UNSET))

        def _parse_device_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_type = _parse_device_type(d.pop("DeviceType", UNSET))

        def _parse_now_playing_item(data: object) -> Union["BaseItemDto", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                now_playing_item_type_1 = BaseItemDto.from_dict(data)

                return now_playing_item_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemDto", None, Unset], data)

        now_playing_item = _parse_now_playing_item(d.pop("NowPlayingItem", UNSET))

        def _parse_now_viewing_item(data: object) -> Union["BaseItemDto", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                now_viewing_item_type_1 = BaseItemDto.from_dict(data)

                return now_viewing_item_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemDto", None, Unset], data)

        now_viewing_item = _parse_now_viewing_item(d.pop("NowViewingItem", UNSET))

        def _parse_device_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_id = _parse_device_id(d.pop("DeviceId", UNSET))

        def _parse_application_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        application_version = _parse_application_version(
            d.pop("ApplicationVersion", UNSET)
        )

        def _parse_transcoding_info(
            data: object,
        ) -> Union["TranscodingInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcoding_info_type_1 = TranscodingInfo.from_dict(data)

                return transcoding_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["TranscodingInfo", None, Unset], data)

        transcoding_info = _parse_transcoding_info(d.pop("TranscodingInfo", UNSET))

        is_active = d.pop("IsActive", UNSET)

        supports_media_control = d.pop("SupportsMediaControl", UNSET)

        supports_remote_control = d.pop("SupportsRemoteControl", UNSET)

        def _parse_now_playing_queue(
            data: object,
        ) -> Union[List["QueueItem"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                now_playing_queue_type_0 = []
                _now_playing_queue_type_0 = data
                for now_playing_queue_type_0_item_data in _now_playing_queue_type_0:
                    now_playing_queue_type_0_item = QueueItem.from_dict(
                        now_playing_queue_type_0_item_data
                    )

                    now_playing_queue_type_0.append(now_playing_queue_type_0_item)

                return now_playing_queue_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["QueueItem"], None, Unset], data)

        now_playing_queue = _parse_now_playing_queue(d.pop("NowPlayingQueue", UNSET))

        def _parse_now_playing_queue_full_items(
            data: object,
        ) -> Union[List["BaseItemDto"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                now_playing_queue_full_items_type_0 = []
                _now_playing_queue_full_items_type_0 = data
                for (
                    now_playing_queue_full_items_type_0_item_data
                ) in _now_playing_queue_full_items_type_0:
                    now_playing_queue_full_items_type_0_item = BaseItemDto.from_dict(
                        now_playing_queue_full_items_type_0_item_data
                    )

                    now_playing_queue_full_items_type_0.append(
                        now_playing_queue_full_items_type_0_item
                    )

                return now_playing_queue_full_items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["BaseItemDto"], None, Unset], data)

        now_playing_queue_full_items = _parse_now_playing_queue_full_items(
            d.pop("NowPlayingQueueFullItems", UNSET)
        )

        has_custom_device_name = d.pop("HasCustomDeviceName", UNSET)

        def _parse_playlist_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        playlist_item_id = _parse_playlist_item_id(d.pop("PlaylistItemId", UNSET))

        def _parse_server_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        server_id = _parse_server_id(d.pop("ServerId", UNSET))

        def _parse_user_primary_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_primary_image_tag = _parse_user_primary_image_tag(
            d.pop("UserPrimaryImageTag", UNSET)
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

        session_info = cls(
            play_state=play_state,
            additional_users=additional_users,
            capabilities=capabilities,
            remote_end_point=remote_end_point,
            playable_media_types=playable_media_types,
            id=id,
            user_id=user_id,
            user_name=user_name,
            client=client,
            last_activity_date=last_activity_date,
            last_playback_check_in=last_playback_check_in,
            last_paused_date=last_paused_date,
            device_name=device_name,
            device_type=device_type,
            now_playing_item=now_playing_item,
            now_viewing_item=now_viewing_item,
            device_id=device_id,
            application_version=application_version,
            transcoding_info=transcoding_info,
            is_active=is_active,
            supports_media_control=supports_media_control,
            supports_remote_control=supports_remote_control,
            now_playing_queue=now_playing_queue,
            now_playing_queue_full_items=now_playing_queue_full_items,
            has_custom_device_name=has_custom_device_name,
            playlist_item_id=playlist_item_id,
            server_id=server_id,
            user_primary_image_tag=user_primary_image_tag,
            supported_commands=supported_commands,
        )

        return session_info
