from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

import datetime
from typing import cast
from typing import Union
from dateutil.parser import isoparse


T = TypeVar("T", bound="RemoteSubtitleInfo")


@_attrs_define
class RemoteSubtitleInfo:
    """
    Attributes:
        three_letter_iso_language_name (Union[None, Unset, str]):
        id (Union[None, Unset, str]):
        provider_name (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        format_ (Union[None, Unset, str]):
        author (Union[None, Unset, str]):
        comment (Union[None, Unset, str]):
        date_created (Union[None, Unset, datetime.datetime]):
        community_rating (Union[None, Unset, float]):
        frame_rate (Union[None, Unset, float]):
        download_count (Union[None, Unset, int]):
        is_hash_match (Union[None, Unset, bool]):
        ai_translated (Union[None, Unset, bool]):
        machine_translated (Union[None, Unset, bool]):
        forced (Union[None, Unset, bool]):
        hearing_impaired (Union[None, Unset, bool]):
    """

    three_letter_iso_language_name: Union[None, Unset, str] = UNSET
    id: Union[None, Unset, str] = UNSET
    provider_name: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    format_: Union[None, Unset, str] = UNSET
    author: Union[None, Unset, str] = UNSET
    comment: Union[None, Unset, str] = UNSET
    date_created: Union[None, Unset, datetime.datetime] = UNSET
    community_rating: Union[None, Unset, float] = UNSET
    frame_rate: Union[None, Unset, float] = UNSET
    download_count: Union[None, Unset, int] = UNSET
    is_hash_match: Union[None, Unset, bool] = UNSET
    ai_translated: Union[None, Unset, bool] = UNSET
    machine_translated: Union[None, Unset, bool] = UNSET
    forced: Union[None, Unset, bool] = UNSET
    hearing_impaired: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        three_letter_iso_language_name: Union[None, Unset, str]
        if isinstance(self.three_letter_iso_language_name, Unset):
            three_letter_iso_language_name = UNSET
        else:
            three_letter_iso_language_name = self.three_letter_iso_language_name

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        provider_name: Union[None, Unset, str]
        if isinstance(self.provider_name, Unset):
            provider_name = UNSET
        else:
            provider_name = self.provider_name

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        format_: Union[None, Unset, str]
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        author: Union[None, Unset, str]
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        date_created: Union[None, Unset, str]
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        community_rating: Union[None, Unset, float]
        if isinstance(self.community_rating, Unset):
            community_rating = UNSET
        else:
            community_rating = self.community_rating

        frame_rate: Union[None, Unset, float]
        if isinstance(self.frame_rate, Unset):
            frame_rate = UNSET
        else:
            frame_rate = self.frame_rate

        download_count: Union[None, Unset, int]
        if isinstance(self.download_count, Unset):
            download_count = UNSET
        else:
            download_count = self.download_count

        is_hash_match: Union[None, Unset, bool]
        if isinstance(self.is_hash_match, Unset):
            is_hash_match = UNSET
        else:
            is_hash_match = self.is_hash_match

        ai_translated: Union[None, Unset, bool]
        if isinstance(self.ai_translated, Unset):
            ai_translated = UNSET
        else:
            ai_translated = self.ai_translated

        machine_translated: Union[None, Unset, bool]
        if isinstance(self.machine_translated, Unset):
            machine_translated = UNSET
        else:
            machine_translated = self.machine_translated

        forced: Union[None, Unset, bool]
        if isinstance(self.forced, Unset):
            forced = UNSET
        else:
            forced = self.forced

        hearing_impaired: Union[None, Unset, bool]
        if isinstance(self.hearing_impaired, Unset):
            hearing_impaired = UNSET
        else:
            hearing_impaired = self.hearing_impaired

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if three_letter_iso_language_name is not UNSET:
            field_dict["ThreeLetterISOLanguageName"] = three_letter_iso_language_name
        if id is not UNSET:
            field_dict["Id"] = id
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name
        if name is not UNSET:
            field_dict["Name"] = name
        if format_ is not UNSET:
            field_dict["Format"] = format_
        if author is not UNSET:
            field_dict["Author"] = author
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if community_rating is not UNSET:
            field_dict["CommunityRating"] = community_rating
        if frame_rate is not UNSET:
            field_dict["FrameRate"] = frame_rate
        if download_count is not UNSET:
            field_dict["DownloadCount"] = download_count
        if is_hash_match is not UNSET:
            field_dict["IsHashMatch"] = is_hash_match
        if ai_translated is not UNSET:
            field_dict["AiTranslated"] = ai_translated
        if machine_translated is not UNSET:
            field_dict["MachineTranslated"] = machine_translated
        if forced is not UNSET:
            field_dict["Forced"] = forced
        if hearing_impaired is not UNSET:
            field_dict["HearingImpaired"] = hearing_impaired

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_three_letter_iso_language_name(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        three_letter_iso_language_name = _parse_three_letter_iso_language_name(
            d.pop("ThreeLetterISOLanguageName", UNSET)
        )

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_provider_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_name = _parse_provider_name(d.pop("ProviderName", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_format_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        format_ = _parse_format_(d.pop("Format", UNSET))

        def _parse_author(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        author = _parse_author(d.pop("Author", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("Comment", UNSET))

        def _parse_date_created(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = isoparse(data)

                return date_created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_created = _parse_date_created(d.pop("DateCreated", UNSET))

        def _parse_community_rating(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        community_rating = _parse_community_rating(d.pop("CommunityRating", UNSET))

        def _parse_frame_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        frame_rate = _parse_frame_rate(d.pop("FrameRate", UNSET))

        def _parse_download_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        download_count = _parse_download_count(d.pop("DownloadCount", UNSET))

        def _parse_is_hash_match(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_hash_match = _parse_is_hash_match(d.pop("IsHashMatch", UNSET))

        def _parse_ai_translated(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        ai_translated = _parse_ai_translated(d.pop("AiTranslated", UNSET))

        def _parse_machine_translated(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        machine_translated = _parse_machine_translated(
            d.pop("MachineTranslated", UNSET)
        )

        def _parse_forced(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        forced = _parse_forced(d.pop("Forced", UNSET))

        def _parse_hearing_impaired(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        hearing_impaired = _parse_hearing_impaired(d.pop("HearingImpaired", UNSET))

        remote_subtitle_info = cls(
            three_letter_iso_language_name=three_letter_iso_language_name,
            id=id,
            provider_name=provider_name,
            name=name,
            format_=format_,
            author=author,
            comment=comment,
            date_created=date_created,
            community_rating=community_rating,
            frame_rate=frame_rate,
            download_count=download_count,
            is_hash_match=is_hash_match,
            ai_translated=ai_translated,
            machine_translated=machine_translated,
            forced=forced,
            hearing_impaired=hearing_impaired,
        )

        return remote_subtitle_info
