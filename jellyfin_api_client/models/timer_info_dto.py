from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

import datetime
from ..models.recording_status import RecordingStatus
from typing import cast
from typing import List
from ..models.keep_until import KeepUntil
from typing import Union
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto


T = TypeVar("T", bound="TimerInfoDto")


@_attrs_define
class TimerInfoDto:
    """
    Attributes:
        id (Union[None, Unset, str]): Gets or sets the Id of the recording.
        type (Union[None, Unset, str]):
        server_id (Union[None, Unset, str]): Gets or sets the server identifier.
        external_id (Union[None, Unset, str]): Gets or sets the external identifier.
        channel_id (Union[Unset, str]): Gets or sets the channel id of the recording.
        external_channel_id (Union[None, Unset, str]): Gets or sets the external channel identifier.
        channel_name (Union[None, Unset, str]): Gets or sets the channel name of the recording.
        channel_primary_image_tag (Union[None, Unset, str]):
        program_id (Union[None, Unset, str]): Gets or sets the program identifier.
        external_program_id (Union[None, Unset, str]): Gets or sets the external program identifier.
        name (Union[None, Unset, str]): Gets or sets the name of the recording.
        overview (Union[None, Unset, str]): Gets or sets the description of the recording.
        start_date (Union[Unset, datetime.datetime]): Gets or sets the start date of the recording, in UTC.
        end_date (Union[Unset, datetime.datetime]): Gets or sets the end date of the recording, in UTC.
        service_name (Union[None, Unset, str]): Gets or sets the name of the service.
        priority (Union[Unset, int]): Gets or sets the priority.
        pre_padding_seconds (Union[Unset, int]): Gets or sets the pre padding seconds.
        post_padding_seconds (Union[Unset, int]): Gets or sets the post padding seconds.
        is_pre_padding_required (Union[Unset, bool]): Gets or sets a value indicating whether this instance is pre
            padding required.
        parent_backdrop_item_id (Union[None, Unset, str]): Gets or sets the Id of the Parent that has a backdrop if the
            item does not have one.
        parent_backdrop_image_tags (Union[List[str], None, Unset]): Gets or sets the parent backdrop image tags.
        is_post_padding_required (Union[Unset, bool]): Gets or sets a value indicating whether this instance is post
            padding required.
        keep_until (Union[Unset, KeepUntil]):
        status (Union[Unset, RecordingStatus]):
        series_timer_id (Union[None, Unset, str]): Gets or sets the series timer identifier.
        external_series_timer_id (Union[None, Unset, str]): Gets or sets the external series timer identifier.
        run_time_ticks (Union[None, Unset, int]): Gets or sets the run time ticks.
        program_info (Union['BaseItemDto', None, Unset]): Gets or sets the program information.
    """

    id: Union[None, Unset, str] = UNSET
    type: Union[None, Unset, str] = UNSET
    server_id: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    channel_id: Union[Unset, str] = UNSET
    external_channel_id: Union[None, Unset, str] = UNSET
    channel_name: Union[None, Unset, str] = UNSET
    channel_primary_image_tag: Union[None, Unset, str] = UNSET
    program_id: Union[None, Unset, str] = UNSET
    external_program_id: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    overview: Union[None, Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    service_name: Union[None, Unset, str] = UNSET
    priority: Union[Unset, int] = UNSET
    pre_padding_seconds: Union[Unset, int] = UNSET
    post_padding_seconds: Union[Unset, int] = UNSET
    is_pre_padding_required: Union[Unset, bool] = UNSET
    parent_backdrop_item_id: Union[None, Unset, str] = UNSET
    parent_backdrop_image_tags: Union[List[str], None, Unset] = UNSET
    is_post_padding_required: Union[Unset, bool] = UNSET
    keep_until: Union[Unset, KeepUntil] = UNSET
    status: Union[Unset, RecordingStatus] = UNSET
    series_timer_id: Union[None, Unset, str] = UNSET
    external_series_timer_id: Union[None, Unset, str] = UNSET
    run_time_ticks: Union[None, Unset, int] = UNSET
    program_info: Union["BaseItemDto", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.base_item_dto import BaseItemDto

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        server_id: Union[None, Unset, str]
        if isinstance(self.server_id, Unset):
            server_id = UNSET
        else:
            server_id = self.server_id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        channel_id = self.channel_id

        external_channel_id: Union[None, Unset, str]
        if isinstance(self.external_channel_id, Unset):
            external_channel_id = UNSET
        else:
            external_channel_id = self.external_channel_id

        channel_name: Union[None, Unset, str]
        if isinstance(self.channel_name, Unset):
            channel_name = UNSET
        else:
            channel_name = self.channel_name

        channel_primary_image_tag: Union[None, Unset, str]
        if isinstance(self.channel_primary_image_tag, Unset):
            channel_primary_image_tag = UNSET
        else:
            channel_primary_image_tag = self.channel_primary_image_tag

        program_id: Union[None, Unset, str]
        if isinstance(self.program_id, Unset):
            program_id = UNSET
        else:
            program_id = self.program_id

        external_program_id: Union[None, Unset, str]
        if isinstance(self.external_program_id, Unset):
            external_program_id = UNSET
        else:
            external_program_id = self.external_program_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        overview: Union[None, Unset, str]
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        service_name: Union[None, Unset, str]
        if isinstance(self.service_name, Unset):
            service_name = UNSET
        else:
            service_name = self.service_name

        priority = self.priority

        pre_padding_seconds = self.pre_padding_seconds

        post_padding_seconds = self.post_padding_seconds

        is_pre_padding_required = self.is_pre_padding_required

        parent_backdrop_item_id: Union[None, Unset, str]
        if isinstance(self.parent_backdrop_item_id, Unset):
            parent_backdrop_item_id = UNSET
        else:
            parent_backdrop_item_id = self.parent_backdrop_item_id

        parent_backdrop_image_tags: Union[List[str], None, Unset]
        if isinstance(self.parent_backdrop_image_tags, Unset):
            parent_backdrop_image_tags = UNSET
        elif isinstance(self.parent_backdrop_image_tags, list):
            parent_backdrop_image_tags = self.parent_backdrop_image_tags

        else:
            parent_backdrop_image_tags = self.parent_backdrop_image_tags

        is_post_padding_required = self.is_post_padding_required

        keep_until: Union[Unset, str] = UNSET
        if not isinstance(self.keep_until, Unset):
            keep_until = self.keep_until.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        series_timer_id: Union[None, Unset, str]
        if isinstance(self.series_timer_id, Unset):
            series_timer_id = UNSET
        else:
            series_timer_id = self.series_timer_id

        external_series_timer_id: Union[None, Unset, str]
        if isinstance(self.external_series_timer_id, Unset):
            external_series_timer_id = UNSET
        else:
            external_series_timer_id = self.external_series_timer_id

        run_time_ticks: Union[None, Unset, int]
        if isinstance(self.run_time_ticks, Unset):
            run_time_ticks = UNSET
        else:
            run_time_ticks = self.run_time_ticks

        program_info: Union[Dict[str, Any], None, Unset]
        if isinstance(self.program_info, Unset):
            program_info = UNSET
        elif isinstance(self.program_info, BaseItemDto):
            program_info = self.program_info.to_dict()
        else:
            program_info = self.program_info

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if type is not UNSET:
            field_dict["Type"] = type
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id
        if external_id is not UNSET:
            field_dict["ExternalId"] = external_id
        if channel_id is not UNSET:
            field_dict["ChannelId"] = channel_id
        if external_channel_id is not UNSET:
            field_dict["ExternalChannelId"] = external_channel_id
        if channel_name is not UNSET:
            field_dict["ChannelName"] = channel_name
        if channel_primary_image_tag is not UNSET:
            field_dict["ChannelPrimaryImageTag"] = channel_primary_image_tag
        if program_id is not UNSET:
            field_dict["ProgramId"] = program_id
        if external_program_id is not UNSET:
            field_dict["ExternalProgramId"] = external_program_id
        if name is not UNSET:
            field_dict["Name"] = name
        if overview is not UNSET:
            field_dict["Overview"] = overview
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if service_name is not UNSET:
            field_dict["ServiceName"] = service_name
        if priority is not UNSET:
            field_dict["Priority"] = priority
        if pre_padding_seconds is not UNSET:
            field_dict["PrePaddingSeconds"] = pre_padding_seconds
        if post_padding_seconds is not UNSET:
            field_dict["PostPaddingSeconds"] = post_padding_seconds
        if is_pre_padding_required is not UNSET:
            field_dict["IsPrePaddingRequired"] = is_pre_padding_required
        if parent_backdrop_item_id is not UNSET:
            field_dict["ParentBackdropItemId"] = parent_backdrop_item_id
        if parent_backdrop_image_tags is not UNSET:
            field_dict["ParentBackdropImageTags"] = parent_backdrop_image_tags
        if is_post_padding_required is not UNSET:
            field_dict["IsPostPaddingRequired"] = is_post_padding_required
        if keep_until is not UNSET:
            field_dict["KeepUntil"] = keep_until
        if status is not UNSET:
            field_dict["Status"] = status
        if series_timer_id is not UNSET:
            field_dict["SeriesTimerId"] = series_timer_id
        if external_series_timer_id is not UNSET:
            field_dict["ExternalSeriesTimerId"] = external_series_timer_id
        if run_time_ticks is not UNSET:
            field_dict["RunTimeTicks"] = run_time_ticks
        if program_info is not UNSET:
            field_dict["ProgramInfo"] = program_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto

        d = src_dict.copy()

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type = _parse_type(d.pop("Type", UNSET))

        def _parse_server_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        server_id = _parse_server_id(d.pop("ServerId", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("ExternalId", UNSET))

        channel_id = d.pop("ChannelId", UNSET)

        def _parse_external_channel_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_channel_id = _parse_external_channel_id(
            d.pop("ExternalChannelId", UNSET)
        )

        def _parse_channel_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_name = _parse_channel_name(d.pop("ChannelName", UNSET))

        def _parse_channel_primary_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_primary_image_tag = _parse_channel_primary_image_tag(
            d.pop("ChannelPrimaryImageTag", UNSET)
        )

        def _parse_program_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        program_id = _parse_program_id(d.pop("ProgramId", UNSET))

        def _parse_external_program_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_program_id = _parse_external_program_id(
            d.pop("ExternalProgramId", UNSET)
        )

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_overview(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        overview = _parse_overview(d.pop("Overview", UNSET))

        _start_date = d.pop("StartDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("EndDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        def _parse_service_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_name = _parse_service_name(d.pop("ServiceName", UNSET))

        priority = d.pop("Priority", UNSET)

        pre_padding_seconds = d.pop("PrePaddingSeconds", UNSET)

        post_padding_seconds = d.pop("PostPaddingSeconds", UNSET)

        is_pre_padding_required = d.pop("IsPrePaddingRequired", UNSET)

        def _parse_parent_backdrop_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_backdrop_item_id = _parse_parent_backdrop_item_id(
            d.pop("ParentBackdropItemId", UNSET)
        )

        def _parse_parent_backdrop_image_tags(
            data: object,
        ) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parent_backdrop_image_tags_type_0 = cast(List[str], data)

                return parent_backdrop_image_tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        parent_backdrop_image_tags = _parse_parent_backdrop_image_tags(
            d.pop("ParentBackdropImageTags", UNSET)
        )

        is_post_padding_required = d.pop("IsPostPaddingRequired", UNSET)

        _keep_until = d.pop("KeepUntil", UNSET)
        keep_until: Union[Unset, KeepUntil]
        if isinstance(_keep_until, Unset):
            keep_until = UNSET
        else:
            keep_until = KeepUntil(_keep_until)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, RecordingStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RecordingStatus(_status)

        def _parse_series_timer_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_timer_id = _parse_series_timer_id(d.pop("SeriesTimerId", UNSET))

        def _parse_external_series_timer_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_series_timer_id = _parse_external_series_timer_id(
            d.pop("ExternalSeriesTimerId", UNSET)
        )

        def _parse_run_time_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        run_time_ticks = _parse_run_time_ticks(d.pop("RunTimeTicks", UNSET))

        def _parse_program_info(data: object) -> Union["BaseItemDto", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                program_info_type_1 = BaseItemDto.from_dict(data)

                return program_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemDto", None, Unset], data)

        program_info = _parse_program_info(d.pop("ProgramInfo", UNSET))

        timer_info_dto = cls(
            id=id,
            type=type,
            server_id=server_id,
            external_id=external_id,
            channel_id=channel_id,
            external_channel_id=external_channel_id,
            channel_name=channel_name,
            channel_primary_image_tag=channel_primary_image_tag,
            program_id=program_id,
            external_program_id=external_program_id,
            name=name,
            overview=overview,
            start_date=start_date,
            end_date=end_date,
            service_name=service_name,
            priority=priority,
            pre_padding_seconds=pre_padding_seconds,
            post_padding_seconds=post_padding_seconds,
            is_pre_padding_required=is_pre_padding_required,
            parent_backdrop_item_id=parent_backdrop_item_id,
            parent_backdrop_image_tags=parent_backdrop_image_tags,
            is_post_padding_required=is_post_padding_required,
            keep_until=keep_until,
            status=status,
            series_timer_id=series_timer_id,
            external_series_timer_id=external_series_timer_id,
            run_time_ticks=run_time_ticks,
            program_info=program_info,
        )

        return timer_info_dto
