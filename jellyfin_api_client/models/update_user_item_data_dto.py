from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

import datetime
from typing import cast
from typing import Union
from dateutil.parser import isoparse


T = TypeVar("T", bound="UpdateUserItemDataDto")


@_attrs_define
class UpdateUserItemDataDto:
    """This is used by the api to get information about a item user data.

    Attributes:
        rating (Union[None, Unset, float]): Gets or sets the rating.
        played_percentage (Union[None, Unset, float]): Gets or sets the played percentage.
        unplayed_item_count (Union[None, Unset, int]): Gets or sets the unplayed item count.
        playback_position_ticks (Union[None, Unset, int]): Gets or sets the playback position ticks.
        play_count (Union[None, Unset, int]): Gets or sets the play count.
        is_favorite (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is favorite.
        likes (Union[None, Unset, bool]): Gets or sets a value indicating whether this
            MediaBrowser.Model.Dto.UpdateUserItemDataDto is likes.
        last_played_date (Union[None, Unset, datetime.datetime]): Gets or sets the last played date.
        played (Union[None, Unset, bool]): Gets or sets a value indicating whether this
            MediaBrowser.Model.Dto.UserItemDataDto is played.
        key (Union[None, Unset, str]): Gets or sets the key.
        item_id (Union[None, Unset, str]): Gets or sets the item identifier.
    """

    rating: Union[None, Unset, float] = UNSET
    played_percentage: Union[None, Unset, float] = UNSET
    unplayed_item_count: Union[None, Unset, int] = UNSET
    playback_position_ticks: Union[None, Unset, int] = UNSET
    play_count: Union[None, Unset, int] = UNSET
    is_favorite: Union[None, Unset, bool] = UNSET
    likes: Union[None, Unset, bool] = UNSET
    last_played_date: Union[None, Unset, datetime.datetime] = UNSET
    played: Union[None, Unset, bool] = UNSET
    key: Union[None, Unset, str] = UNSET
    item_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        rating: Union[None, Unset, float]
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        played_percentage: Union[None, Unset, float]
        if isinstance(self.played_percentage, Unset):
            played_percentage = UNSET
        else:
            played_percentage = self.played_percentage

        unplayed_item_count: Union[None, Unset, int]
        if isinstance(self.unplayed_item_count, Unset):
            unplayed_item_count = UNSET
        else:
            unplayed_item_count = self.unplayed_item_count

        playback_position_ticks: Union[None, Unset, int]
        if isinstance(self.playback_position_ticks, Unset):
            playback_position_ticks = UNSET
        else:
            playback_position_ticks = self.playback_position_ticks

        play_count: Union[None, Unset, int]
        if isinstance(self.play_count, Unset):
            play_count = UNSET
        else:
            play_count = self.play_count

        is_favorite: Union[None, Unset, bool]
        if isinstance(self.is_favorite, Unset):
            is_favorite = UNSET
        else:
            is_favorite = self.is_favorite

        likes: Union[None, Unset, bool]
        if isinstance(self.likes, Unset):
            likes = UNSET
        else:
            likes = self.likes

        last_played_date: Union[None, Unset, str]
        if isinstance(self.last_played_date, Unset):
            last_played_date = UNSET
        elif isinstance(self.last_played_date, datetime.datetime):
            last_played_date = self.last_played_date.isoformat()
        else:
            last_played_date = self.last_played_date

        played: Union[None, Unset, bool]
        if isinstance(self.played, Unset):
            played = UNSET
        else:
            played = self.played

        key: Union[None, Unset, str]
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        item_id: Union[None, Unset, str]
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        else:
            item_id = self.item_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if rating is not UNSET:
            field_dict["Rating"] = rating
        if played_percentage is not UNSET:
            field_dict["PlayedPercentage"] = played_percentage
        if unplayed_item_count is not UNSET:
            field_dict["UnplayedItemCount"] = unplayed_item_count
        if playback_position_ticks is not UNSET:
            field_dict["PlaybackPositionTicks"] = playback_position_ticks
        if play_count is not UNSET:
            field_dict["PlayCount"] = play_count
        if is_favorite is not UNSET:
            field_dict["IsFavorite"] = is_favorite
        if likes is not UNSET:
            field_dict["Likes"] = likes
        if last_played_date is not UNSET:
            field_dict["LastPlayedDate"] = last_played_date
        if played is not UNSET:
            field_dict["Played"] = played
        if key is not UNSET:
            field_dict["Key"] = key
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_rating(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rating = _parse_rating(d.pop("Rating", UNSET))

        def _parse_played_percentage(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        played_percentage = _parse_played_percentage(d.pop("PlayedPercentage", UNSET))

        def _parse_unplayed_item_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        unplayed_item_count = _parse_unplayed_item_count(
            d.pop("UnplayedItemCount", UNSET)
        )

        def _parse_playback_position_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        playback_position_ticks = _parse_playback_position_ticks(
            d.pop("PlaybackPositionTicks", UNSET)
        )

        def _parse_play_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        play_count = _parse_play_count(d.pop("PlayCount", UNSET))

        def _parse_is_favorite(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_favorite = _parse_is_favorite(d.pop("IsFavorite", UNSET))

        def _parse_likes(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        likes = _parse_likes(d.pop("Likes", UNSET))

        def _parse_last_played_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_played_date_type_0 = isoparse(data)

                return last_played_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_played_date = _parse_last_played_date(d.pop("LastPlayedDate", UNSET))

        def _parse_played(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        played = _parse_played(d.pop("Played", UNSET))

        def _parse_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        key = _parse_key(d.pop("Key", UNSET))

        def _parse_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_id = _parse_item_id(d.pop("ItemId", UNSET))

        update_user_item_data_dto = cls(
            rating=rating,
            played_percentage=played_percentage,
            unplayed_item_count=unplayed_item_count,
            playback_position_ticks=playback_position_ticks,
            play_count=play_count,
            is_favorite=is_favorite,
            likes=likes,
            last_played_date=last_played_date,
            played=played,
            key=key,
            item_id=item_id,
        )

        return update_user_item_data_dto
