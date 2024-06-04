from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union
from ..models.base_item_dto_play_access import BaseItemDtoPlayAccess
import datetime
from ..models.base_item_dto_video_type import BaseItemDtoVideoType
from ..models.base_item_kind import BaseItemKind
from ..models.media_type import MediaType
from ..models.base_item_dto_collection_type import BaseItemDtoCollectionType
from ..models.base_item_dto_audio import BaseItemDtoAudio
from ..models.base_item_dto_extra_type import BaseItemDtoExtraType
from ..models.base_item_dto_video_3d_format import BaseItemDtoVideo3DFormat
from ..models.base_item_dto_iso_type import BaseItemDtoIsoType
from typing import List
from ..models.base_item_dto_image_orientation import BaseItemDtoImageOrientation
from ..models.day_of_week import DayOfWeek
from ..models.base_item_dto_location_type import BaseItemDtoLocationType
from dateutil.parser import isoparse
from ..models.base_item_dto_channel_type import BaseItemDtoChannelType
from ..models.metadata_field import MetadataField

if TYPE_CHECKING:
    from ..models.chapter_info import ChapterInfo
    from ..models.media_source_info import MediaSourceInfo
    from ..models.base_item_dto_image_blur_hashes_type_0 import (
        BaseItemDtoImageBlurHashesType0,
    )
    from ..models.media_url import MediaUrl
    from ..models.base_item_person import BaseItemPerson
    from ..models.base_item_dto_trickplay_type_0 import BaseItemDtoTrickplayType0
    from ..models.name_guid_pair import NameGuidPair
    from ..models.base_item_dto_provider_ids_type_0 import BaseItemDtoProviderIdsType0
    from ..models.media_stream import MediaStream
    from ..models.external_url import ExternalUrl
    from ..models.base_item_dto_image_tags_type_0 import BaseItemDtoImageTagsType0
    from ..models.user_item_data_dto import UserItemDataDto


T = TypeVar("T", bound="BaseItemDto")


@_attrs_define
class BaseItemDto:
    """This is strictly used as a data transfer object from the api layer.
    This holds information about a BaseItem in a format that is convenient for the client.

        Attributes:
            name (Union[None, Unset, str]): Gets or sets the name.
            original_title (Union[None, Unset, str]):
            server_id (Union[None, Unset, str]): Gets or sets the server identifier.
            id (Union[Unset, str]): Gets or sets the id.
            etag (Union[None, Unset, str]): Gets or sets the etag.
            source_type (Union[None, Unset, str]): Gets or sets the type of the source.
            playlist_item_id (Union[None, Unset, str]): Gets or sets the playlist item identifier.
            date_created (Union[None, Unset, datetime.datetime]): Gets or sets the date created.
            date_last_media_added (Union[None, Unset, datetime.datetime]):
            extra_type (Union[Unset, BaseItemDtoExtraType]):
            airs_before_season_number (Union[None, Unset, int]):
            airs_after_season_number (Union[None, Unset, int]):
            airs_before_episode_number (Union[None, Unset, int]):
            can_delete (Union[None, Unset, bool]):
            can_download (Union[None, Unset, bool]):
            has_lyrics (Union[None, Unset, bool]):
            has_subtitles (Union[None, Unset, bool]):
            preferred_metadata_language (Union[None, Unset, str]):
            preferred_metadata_country_code (Union[None, Unset, str]):
            container (Union[None, Unset, str]):
            sort_name (Union[None, Unset, str]): Gets or sets the name of the sort.
            forced_sort_name (Union[None, Unset, str]):
            video_3d_format (Union[Unset, BaseItemDtoVideo3DFormat]): Gets or sets the video3 D format.
            premiere_date (Union[None, Unset, datetime.datetime]): Gets or sets the premiere date.
            external_urls (Union[List['ExternalUrl'], None, Unset]): Gets or sets the external urls.
            media_sources (Union[List['MediaSourceInfo'], None, Unset]): Gets or sets the media versions.
            critic_rating (Union[None, Unset, float]): Gets or sets the critic rating.
            production_locations (Union[List[str], None, Unset]):
            path (Union[None, Unset, str]): Gets or sets the path.
            enable_media_source_display (Union[None, Unset, bool]):
            official_rating (Union[None, Unset, str]): Gets or sets the official rating.
            custom_rating (Union[None, Unset, str]): Gets or sets the custom rating.
            channel_id (Union[None, Unset, str]): Gets or sets the channel identifier.
            channel_name (Union[None, Unset, str]):
            overview (Union[None, Unset, str]): Gets or sets the overview.
            taglines (Union[List[str], None, Unset]): Gets or sets the taglines.
            genres (Union[List[str], None, Unset]): Gets or sets the genres.
            community_rating (Union[None, Unset, float]): Gets or sets the community rating.
            cumulative_run_time_ticks (Union[None, Unset, int]): Gets or sets the cumulative run time ticks.
            run_time_ticks (Union[None, Unset, int]): Gets or sets the run time ticks.
            play_access (Union[Unset, BaseItemDtoPlayAccess]): Gets or sets the play access.
            aspect_ratio (Union[None, Unset, str]): Gets or sets the aspect ratio.
            production_year (Union[None, Unset, int]): Gets or sets the production year.
            is_place_holder (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is place
                holder.
            number (Union[None, Unset, str]): Gets or sets the number.
            channel_number (Union[None, Unset, str]):
            index_number (Union[None, Unset, int]): Gets or sets the index number.
            index_number_end (Union[None, Unset, int]): Gets or sets the index number end.
            parent_index_number (Union[None, Unset, int]): Gets or sets the parent index number.
            remote_trailers (Union[List['MediaUrl'], None, Unset]): Gets or sets the trailer urls.
            provider_ids (Union['BaseItemDtoProviderIdsType0', None, Unset]): Gets or sets the provider ids.
            is_hd (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is HD.
            is_folder (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is folder.
            parent_id (Union[None, Unset, str]): Gets or sets the parent id.
            type (Union[Unset, BaseItemKind]): The base item kind.
            people (Union[List['BaseItemPerson'], None, Unset]): Gets or sets the people.
            studios (Union[List['NameGuidPair'], None, Unset]): Gets or sets the studios.
            genre_items (Union[List['NameGuidPair'], None, Unset]):
            parent_logo_item_id (Union[None, Unset, str]): Gets or sets whether the item has a logo, this will hold the Id
                of the Parent that has one.
            parent_backdrop_item_id (Union[None, Unset, str]): Gets or sets whether the item has any backdrops, this will
                hold the Id of the Parent that has one.
            parent_backdrop_image_tags (Union[List[str], None, Unset]): Gets or sets the parent backdrop image tags.
            local_trailer_count (Union[None, Unset, int]): Gets or sets the local trailer count.
            user_data (Union['UserItemDataDto', None, Unset]): Gets or sets the user data for this item based on the user
                it's being requested for.
            recursive_item_count (Union[None, Unset, int]): Gets or sets the recursive item count.
            child_count (Union[None, Unset, int]): Gets or sets the child count.
            series_name (Union[None, Unset, str]): Gets or sets the name of the series.
            series_id (Union[None, Unset, str]): Gets or sets the series id.
            season_id (Union[None, Unset, str]): Gets or sets the season identifier.
            special_feature_count (Union[None, Unset, int]): Gets or sets the special feature count.
            display_preferences_id (Union[None, Unset, str]): Gets or sets the display preferences id.
            status (Union[None, Unset, str]): Gets or sets the status.
            air_time (Union[None, Unset, str]): Gets or sets the air time.
            air_days (Union[List[DayOfWeek], None, Unset]): Gets or sets the air days.
            tags (Union[List[str], None, Unset]): Gets or sets the tags.
            primary_image_aspect_ratio (Union[None, Unset, float]): Gets or sets the primary image aspect ratio, after image
                enhancements.
            artists (Union[List[str], None, Unset]): Gets or sets the artists.
            artist_items (Union[List['NameGuidPair'], None, Unset]): Gets or sets the artist items.
            album (Union[None, Unset, str]): Gets or sets the album.
            collection_type (Union[Unset, BaseItemDtoCollectionType]): Gets or sets the type of the collection.
            display_order (Union[None, Unset, str]): Gets or sets the display order.
            album_id (Union[None, Unset, str]): Gets or sets the album id.
            album_primary_image_tag (Union[None, Unset, str]): Gets or sets the album image tag.
            series_primary_image_tag (Union[None, Unset, str]): Gets or sets the series primary image tag.
            album_artist (Union[None, Unset, str]): Gets or sets the album artist.
            album_artists (Union[List['NameGuidPair'], None, Unset]): Gets or sets the album artists.
            season_name (Union[None, Unset, str]): Gets or sets the name of the season.
            media_streams (Union[List['MediaStream'], None, Unset]): Gets or sets the media streams.
            video_type (Union[Unset, BaseItemDtoVideoType]): Gets or sets the type of the video.
            part_count (Union[None, Unset, int]): Gets or sets the part count.
            media_source_count (Union[None, Unset, int]):
            image_tags (Union['BaseItemDtoImageTagsType0', None, Unset]): Gets or sets the image tags.
            backdrop_image_tags (Union[List[str], None, Unset]): Gets or sets the backdrop image tags.
            screenshot_image_tags (Union[List[str], None, Unset]): Gets or sets the screenshot image tags.
            parent_logo_image_tag (Union[None, Unset, str]): Gets or sets the parent logo image tag.
            parent_art_item_id (Union[None, Unset, str]): Gets or sets whether the item has fan art, this will hold the Id
                of the Parent that has one.
            parent_art_image_tag (Union[None, Unset, str]): Gets or sets the parent art image tag.
            series_thumb_image_tag (Union[None, Unset, str]): Gets or sets the series thumb image tag.
            image_blur_hashes (Union['BaseItemDtoImageBlurHashesType0', None, Unset]): Gets or sets the blurhashes for the
                image tags.
                Maps image type to dictionary mapping image tag to blurhash value.
            series_studio (Union[None, Unset, str]): Gets or sets the series studio.
            parent_thumb_item_id (Union[None, Unset, str]): Gets or sets the parent thumb item id.
            parent_thumb_image_tag (Union[None, Unset, str]): Gets or sets the parent thumb image tag.
            parent_primary_image_item_id (Union[None, Unset, str]): Gets or sets the parent primary image item identifier.
            parent_primary_image_tag (Union[None, Unset, str]): Gets or sets the parent primary image tag.
            chapters (Union[List['ChapterInfo'], None, Unset]): Gets or sets the chapters.
            trickplay (Union['BaseItemDtoTrickplayType0', None, Unset]): Gets or sets the trickplay manifest.
            location_type (Union[Unset, BaseItemDtoLocationType]): Gets or sets the type of the location.
            iso_type (Union[Unset, BaseItemDtoIsoType]): Gets or sets the type of the iso.
            media_type (Union[Unset, MediaType]): Media types.
            end_date (Union[None, Unset, datetime.datetime]): Gets or sets the end date.
            locked_fields (Union[List[MetadataField], None, Unset]): Gets or sets the locked fields.
            trailer_count (Union[None, Unset, int]): Gets or sets the trailer count.
            movie_count (Union[None, Unset, int]): Gets or sets the movie count.
            series_count (Union[None, Unset, int]): Gets or sets the series count.
            program_count (Union[None, Unset, int]):
            episode_count (Union[None, Unset, int]): Gets or sets the episode count.
            song_count (Union[None, Unset, int]): Gets or sets the song count.
            album_count (Union[None, Unset, int]): Gets or sets the album count.
            artist_count (Union[None, Unset, int]):
            music_video_count (Union[None, Unset, int]): Gets or sets the music video count.
            lock_data (Union[None, Unset, bool]): Gets or sets a value indicating whether [enable internet providers].
            width (Union[None, Unset, int]):
            height (Union[None, Unset, int]):
            camera_make (Union[None, Unset, str]):
            camera_model (Union[None, Unset, str]):
            software (Union[None, Unset, str]):
            exposure_time (Union[None, Unset, float]):
            focal_length (Union[None, Unset, float]):
            image_orientation (Union[Unset, BaseItemDtoImageOrientation]):
            aperture (Union[None, Unset, float]):
            shutter_speed (Union[None, Unset, float]):
            latitude (Union[None, Unset, float]):
            longitude (Union[None, Unset, float]):
            altitude (Union[None, Unset, float]):
            iso_speed_rating (Union[None, Unset, int]):
            series_timer_id (Union[None, Unset, str]): Gets or sets the series timer identifier.
            program_id (Union[None, Unset, str]): Gets or sets the program identifier.
            channel_primary_image_tag (Union[None, Unset, str]): Gets or sets the channel primary image tag.
            start_date (Union[None, Unset, datetime.datetime]): Gets or sets the start date of the recording, in UTC.
            completion_percentage (Union[None, Unset, float]): Gets or sets the completion percentage.
            is_repeat (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is repeat.
            episode_title (Union[None, Unset, str]): Gets or sets the episode title.
            channel_type (Union[Unset, BaseItemDtoChannelType]): Gets or sets the type of the channel.
            audio (Union[Unset, BaseItemDtoAudio]): Gets or sets the audio.
            is_movie (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is movie.
            is_sports (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is sports.
            is_series (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is series.
            is_live (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is live.
            is_news (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is news.
            is_kids (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is kids.
            is_premiere (Union[None, Unset, bool]): Gets or sets a value indicating whether this instance is premiere.
            timer_id (Union[None, Unset, str]): Gets or sets the timer identifier.
            normalization_gain (Union[None, Unset, float]): Gets or sets the gain required for audio normalization.
            current_program (Union['BaseItemDto', None, Unset]): Gets or sets the current program.
    """

    name: Union[None, Unset, str] = UNSET
    original_title: Union[None, Unset, str] = UNSET
    server_id: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    etag: Union[None, Unset, str] = UNSET
    source_type: Union[None, Unset, str] = UNSET
    playlist_item_id: Union[None, Unset, str] = UNSET
    date_created: Union[None, Unset, datetime.datetime] = UNSET
    date_last_media_added: Union[None, Unset, datetime.datetime] = UNSET
    extra_type: Union[Unset, BaseItemDtoExtraType] = UNSET
    airs_before_season_number: Union[None, Unset, int] = UNSET
    airs_after_season_number: Union[None, Unset, int] = UNSET
    airs_before_episode_number: Union[None, Unset, int] = UNSET
    can_delete: Union[None, Unset, bool] = UNSET
    can_download: Union[None, Unset, bool] = UNSET
    has_lyrics: Union[None, Unset, bool] = UNSET
    has_subtitles: Union[None, Unset, bool] = UNSET
    preferred_metadata_language: Union[None, Unset, str] = UNSET
    preferred_metadata_country_code: Union[None, Unset, str] = UNSET
    container: Union[None, Unset, str] = UNSET
    sort_name: Union[None, Unset, str] = UNSET
    forced_sort_name: Union[None, Unset, str] = UNSET
    video_3d_format: Union[Unset, BaseItemDtoVideo3DFormat] = UNSET
    premiere_date: Union[None, Unset, datetime.datetime] = UNSET
    external_urls: Union[List["ExternalUrl"], None, Unset] = UNSET
    media_sources: Union[List["MediaSourceInfo"], None, Unset] = UNSET
    critic_rating: Union[None, Unset, float] = UNSET
    production_locations: Union[List[str], None, Unset] = UNSET
    path: Union[None, Unset, str] = UNSET
    enable_media_source_display: Union[None, Unset, bool] = UNSET
    official_rating: Union[None, Unset, str] = UNSET
    custom_rating: Union[None, Unset, str] = UNSET
    channel_id: Union[None, Unset, str] = UNSET
    channel_name: Union[None, Unset, str] = UNSET
    overview: Union[None, Unset, str] = UNSET
    taglines: Union[List[str], None, Unset] = UNSET
    genres: Union[List[str], None, Unset] = UNSET
    community_rating: Union[None, Unset, float] = UNSET
    cumulative_run_time_ticks: Union[None, Unset, int] = UNSET
    run_time_ticks: Union[None, Unset, int] = UNSET
    play_access: Union[Unset, BaseItemDtoPlayAccess] = UNSET
    aspect_ratio: Union[None, Unset, str] = UNSET
    production_year: Union[None, Unset, int] = UNSET
    is_place_holder: Union[None, Unset, bool] = UNSET
    number: Union[None, Unset, str] = UNSET
    channel_number: Union[None, Unset, str] = UNSET
    index_number: Union[None, Unset, int] = UNSET
    index_number_end: Union[None, Unset, int] = UNSET
    parent_index_number: Union[None, Unset, int] = UNSET
    remote_trailers: Union[List["MediaUrl"], None, Unset] = UNSET
    provider_ids: Union["BaseItemDtoProviderIdsType0", None, Unset] = UNSET
    is_hd: Union[None, Unset, bool] = UNSET
    is_folder: Union[None, Unset, bool] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    type: Union[Unset, BaseItemKind] = UNSET
    people: Union[List["BaseItemPerson"], None, Unset] = UNSET
    studios: Union[List["NameGuidPair"], None, Unset] = UNSET
    genre_items: Union[List["NameGuidPair"], None, Unset] = UNSET
    parent_logo_item_id: Union[None, Unset, str] = UNSET
    parent_backdrop_item_id: Union[None, Unset, str] = UNSET
    parent_backdrop_image_tags: Union[List[str], None, Unset] = UNSET
    local_trailer_count: Union[None, Unset, int] = UNSET
    user_data: Union["UserItemDataDto", None, Unset] = UNSET
    recursive_item_count: Union[None, Unset, int] = UNSET
    child_count: Union[None, Unset, int] = UNSET
    series_name: Union[None, Unset, str] = UNSET
    series_id: Union[None, Unset, str] = UNSET
    season_id: Union[None, Unset, str] = UNSET
    special_feature_count: Union[None, Unset, int] = UNSET
    display_preferences_id: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    air_time: Union[None, Unset, str] = UNSET
    air_days: Union[List[DayOfWeek], None, Unset] = UNSET
    tags: Union[List[str], None, Unset] = UNSET
    primary_image_aspect_ratio: Union[None, Unset, float] = UNSET
    artists: Union[List[str], None, Unset] = UNSET
    artist_items: Union[List["NameGuidPair"], None, Unset] = UNSET
    album: Union[None, Unset, str] = UNSET
    collection_type: Union[Unset, BaseItemDtoCollectionType] = UNSET
    display_order: Union[None, Unset, str] = UNSET
    album_id: Union[None, Unset, str] = UNSET
    album_primary_image_tag: Union[None, Unset, str] = UNSET
    series_primary_image_tag: Union[None, Unset, str] = UNSET
    album_artist: Union[None, Unset, str] = UNSET
    album_artists: Union[List["NameGuidPair"], None, Unset] = UNSET
    season_name: Union[None, Unset, str] = UNSET
    media_streams: Union[List["MediaStream"], None, Unset] = UNSET
    video_type: Union[Unset, BaseItemDtoVideoType] = UNSET
    part_count: Union[None, Unset, int] = UNSET
    media_source_count: Union[None, Unset, int] = UNSET
    image_tags: Union["BaseItemDtoImageTagsType0", None, Unset] = UNSET
    backdrop_image_tags: Union[List[str], None, Unset] = UNSET
    screenshot_image_tags: Union[List[str], None, Unset] = UNSET
    parent_logo_image_tag: Union[None, Unset, str] = UNSET
    parent_art_item_id: Union[None, Unset, str] = UNSET
    parent_art_image_tag: Union[None, Unset, str] = UNSET
    series_thumb_image_tag: Union[None, Unset, str] = UNSET
    image_blur_hashes: Union["BaseItemDtoImageBlurHashesType0", None, Unset] = UNSET
    series_studio: Union[None, Unset, str] = UNSET
    parent_thumb_item_id: Union[None, Unset, str] = UNSET
    parent_thumb_image_tag: Union[None, Unset, str] = UNSET
    parent_primary_image_item_id: Union[None, Unset, str] = UNSET
    parent_primary_image_tag: Union[None, Unset, str] = UNSET
    chapters: Union[List["ChapterInfo"], None, Unset] = UNSET
    trickplay: Union["BaseItemDtoTrickplayType0", None, Unset] = UNSET
    location_type: Union[Unset, BaseItemDtoLocationType] = UNSET
    iso_type: Union[Unset, BaseItemDtoIsoType] = UNSET
    media_type: Union[Unset, MediaType] = UNSET
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    locked_fields: Union[List[MetadataField], None, Unset] = UNSET
    trailer_count: Union[None, Unset, int] = UNSET
    movie_count: Union[None, Unset, int] = UNSET
    series_count: Union[None, Unset, int] = UNSET
    program_count: Union[None, Unset, int] = UNSET
    episode_count: Union[None, Unset, int] = UNSET
    song_count: Union[None, Unset, int] = UNSET
    album_count: Union[None, Unset, int] = UNSET
    artist_count: Union[None, Unset, int] = UNSET
    music_video_count: Union[None, Unset, int] = UNSET
    lock_data: Union[None, Unset, bool] = UNSET
    width: Union[None, Unset, int] = UNSET
    height: Union[None, Unset, int] = UNSET
    camera_make: Union[None, Unset, str] = UNSET
    camera_model: Union[None, Unset, str] = UNSET
    software: Union[None, Unset, str] = UNSET
    exposure_time: Union[None, Unset, float] = UNSET
    focal_length: Union[None, Unset, float] = UNSET
    image_orientation: Union[Unset, BaseItemDtoImageOrientation] = UNSET
    aperture: Union[None, Unset, float] = UNSET
    shutter_speed: Union[None, Unset, float] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    altitude: Union[None, Unset, float] = UNSET
    iso_speed_rating: Union[None, Unset, int] = UNSET
    series_timer_id: Union[None, Unset, str] = UNSET
    program_id: Union[None, Unset, str] = UNSET
    channel_primary_image_tag: Union[None, Unset, str] = UNSET
    start_date: Union[None, Unset, datetime.datetime] = UNSET
    completion_percentage: Union[None, Unset, float] = UNSET
    is_repeat: Union[None, Unset, bool] = UNSET
    episode_title: Union[None, Unset, str] = UNSET
    channel_type: Union[Unset, BaseItemDtoChannelType] = UNSET
    audio: Union[Unset, BaseItemDtoAudio] = UNSET
    is_movie: Union[None, Unset, bool] = UNSET
    is_sports: Union[None, Unset, bool] = UNSET
    is_series: Union[None, Unset, bool] = UNSET
    is_live: Union[None, Unset, bool] = UNSET
    is_news: Union[None, Unset, bool] = UNSET
    is_kids: Union[None, Unset, bool] = UNSET
    is_premiere: Union[None, Unset, bool] = UNSET
    timer_id: Union[None, Unset, str] = UNSET
    normalization_gain: Union[None, Unset, float] = UNSET
    current_program: Union["BaseItemDto", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.base_item_dto_image_blur_hashes_type_0 import (
            BaseItemDtoImageBlurHashesType0,
        )
        from ..models.base_item_dto_trickplay_type_0 import BaseItemDtoTrickplayType0
        from ..models.base_item_dto_provider_ids_type_0 import (
            BaseItemDtoProviderIdsType0,
        )
        from ..models.base_item_dto_image_tags_type_0 import BaseItemDtoImageTagsType0
        from ..models.user_item_data_dto import UserItemDataDto

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        original_title: Union[None, Unset, str]
        if isinstance(self.original_title, Unset):
            original_title = UNSET
        else:
            original_title = self.original_title

        server_id: Union[None, Unset, str]
        if isinstance(self.server_id, Unset):
            server_id = UNSET
        else:
            server_id = self.server_id

        id = self.id

        etag: Union[None, Unset, str]
        if isinstance(self.etag, Unset):
            etag = UNSET
        else:
            etag = self.etag

        source_type: Union[None, Unset, str]
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        else:
            source_type = self.source_type

        playlist_item_id: Union[None, Unset, str]
        if isinstance(self.playlist_item_id, Unset):
            playlist_item_id = UNSET
        else:
            playlist_item_id = self.playlist_item_id

        date_created: Union[None, Unset, str]
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_last_media_added: Union[None, Unset, str]
        if isinstance(self.date_last_media_added, Unset):
            date_last_media_added = UNSET
        elif isinstance(self.date_last_media_added, datetime.datetime):
            date_last_media_added = self.date_last_media_added.isoformat()
        else:
            date_last_media_added = self.date_last_media_added

        extra_type: Union[Unset, str] = UNSET
        if not isinstance(self.extra_type, Unset):
            extra_type = self.extra_type.value

        airs_before_season_number: Union[None, Unset, int]
        if isinstance(self.airs_before_season_number, Unset):
            airs_before_season_number = UNSET
        else:
            airs_before_season_number = self.airs_before_season_number

        airs_after_season_number: Union[None, Unset, int]
        if isinstance(self.airs_after_season_number, Unset):
            airs_after_season_number = UNSET
        else:
            airs_after_season_number = self.airs_after_season_number

        airs_before_episode_number: Union[None, Unset, int]
        if isinstance(self.airs_before_episode_number, Unset):
            airs_before_episode_number = UNSET
        else:
            airs_before_episode_number = self.airs_before_episode_number

        can_delete: Union[None, Unset, bool]
        if isinstance(self.can_delete, Unset):
            can_delete = UNSET
        else:
            can_delete = self.can_delete

        can_download: Union[None, Unset, bool]
        if isinstance(self.can_download, Unset):
            can_download = UNSET
        else:
            can_download = self.can_download

        has_lyrics: Union[None, Unset, bool]
        if isinstance(self.has_lyrics, Unset):
            has_lyrics = UNSET
        else:
            has_lyrics = self.has_lyrics

        has_subtitles: Union[None, Unset, bool]
        if isinstance(self.has_subtitles, Unset):
            has_subtitles = UNSET
        else:
            has_subtitles = self.has_subtitles

        preferred_metadata_language: Union[None, Unset, str]
        if isinstance(self.preferred_metadata_language, Unset):
            preferred_metadata_language = UNSET
        else:
            preferred_metadata_language = self.preferred_metadata_language

        preferred_metadata_country_code: Union[None, Unset, str]
        if isinstance(self.preferred_metadata_country_code, Unset):
            preferred_metadata_country_code = UNSET
        else:
            preferred_metadata_country_code = self.preferred_metadata_country_code

        container: Union[None, Unset, str]
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        sort_name: Union[None, Unset, str]
        if isinstance(self.sort_name, Unset):
            sort_name = UNSET
        else:
            sort_name = self.sort_name

        forced_sort_name: Union[None, Unset, str]
        if isinstance(self.forced_sort_name, Unset):
            forced_sort_name = UNSET
        else:
            forced_sort_name = self.forced_sort_name

        video_3d_format: Union[Unset, str] = UNSET
        if not isinstance(self.video_3d_format, Unset):
            video_3d_format = self.video_3d_format.value

        premiere_date: Union[None, Unset, str]
        if isinstance(self.premiere_date, Unset):
            premiere_date = UNSET
        elif isinstance(self.premiere_date, datetime.datetime):
            premiere_date = self.premiere_date.isoformat()
        else:
            premiere_date = self.premiere_date

        external_urls: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.external_urls, Unset):
            external_urls = UNSET
        elif isinstance(self.external_urls, list):
            external_urls = []
            for external_urls_type_0_item_data in self.external_urls:
                external_urls_type_0_item = external_urls_type_0_item_data.to_dict()
                external_urls.append(external_urls_type_0_item)

        else:
            external_urls = self.external_urls

        media_sources: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.media_sources, Unset):
            media_sources = UNSET
        elif isinstance(self.media_sources, list):
            media_sources = []
            for media_sources_type_0_item_data in self.media_sources:
                media_sources_type_0_item = media_sources_type_0_item_data.to_dict()
                media_sources.append(media_sources_type_0_item)

        else:
            media_sources = self.media_sources

        critic_rating: Union[None, Unset, float]
        if isinstance(self.critic_rating, Unset):
            critic_rating = UNSET
        else:
            critic_rating = self.critic_rating

        production_locations: Union[List[str], None, Unset]
        if isinstance(self.production_locations, Unset):
            production_locations = UNSET
        elif isinstance(self.production_locations, list):
            production_locations = self.production_locations

        else:
            production_locations = self.production_locations

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        enable_media_source_display: Union[None, Unset, bool]
        if isinstance(self.enable_media_source_display, Unset):
            enable_media_source_display = UNSET
        else:
            enable_media_source_display = self.enable_media_source_display

        official_rating: Union[None, Unset, str]
        if isinstance(self.official_rating, Unset):
            official_rating = UNSET
        else:
            official_rating = self.official_rating

        custom_rating: Union[None, Unset, str]
        if isinstance(self.custom_rating, Unset):
            custom_rating = UNSET
        else:
            custom_rating = self.custom_rating

        channel_id: Union[None, Unset, str]
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        else:
            channel_id = self.channel_id

        channel_name: Union[None, Unset, str]
        if isinstance(self.channel_name, Unset):
            channel_name = UNSET
        else:
            channel_name = self.channel_name

        overview: Union[None, Unset, str]
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        taglines: Union[List[str], None, Unset]
        if isinstance(self.taglines, Unset):
            taglines = UNSET
        elif isinstance(self.taglines, list):
            taglines = self.taglines

        else:
            taglines = self.taglines

        genres: Union[List[str], None, Unset]
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        community_rating: Union[None, Unset, float]
        if isinstance(self.community_rating, Unset):
            community_rating = UNSET
        else:
            community_rating = self.community_rating

        cumulative_run_time_ticks: Union[None, Unset, int]
        if isinstance(self.cumulative_run_time_ticks, Unset):
            cumulative_run_time_ticks = UNSET
        else:
            cumulative_run_time_ticks = self.cumulative_run_time_ticks

        run_time_ticks: Union[None, Unset, int]
        if isinstance(self.run_time_ticks, Unset):
            run_time_ticks = UNSET
        else:
            run_time_ticks = self.run_time_ticks

        play_access: Union[Unset, str] = UNSET
        if not isinstance(self.play_access, Unset):
            play_access = self.play_access.value

        aspect_ratio: Union[None, Unset, str]
        if isinstance(self.aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = self.aspect_ratio

        production_year: Union[None, Unset, int]
        if isinstance(self.production_year, Unset):
            production_year = UNSET
        else:
            production_year = self.production_year

        is_place_holder: Union[None, Unset, bool]
        if isinstance(self.is_place_holder, Unset):
            is_place_holder = UNSET
        else:
            is_place_holder = self.is_place_holder

        number: Union[None, Unset, str]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        channel_number: Union[None, Unset, str]
        if isinstance(self.channel_number, Unset):
            channel_number = UNSET
        else:
            channel_number = self.channel_number

        index_number: Union[None, Unset, int]
        if isinstance(self.index_number, Unset):
            index_number = UNSET
        else:
            index_number = self.index_number

        index_number_end: Union[None, Unset, int]
        if isinstance(self.index_number_end, Unset):
            index_number_end = UNSET
        else:
            index_number_end = self.index_number_end

        parent_index_number: Union[None, Unset, int]
        if isinstance(self.parent_index_number, Unset):
            parent_index_number = UNSET
        else:
            parent_index_number = self.parent_index_number

        remote_trailers: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.remote_trailers, Unset):
            remote_trailers = UNSET
        elif isinstance(self.remote_trailers, list):
            remote_trailers = []
            for remote_trailers_type_0_item_data in self.remote_trailers:
                remote_trailers_type_0_item = remote_trailers_type_0_item_data.to_dict()
                remote_trailers.append(remote_trailers_type_0_item)

        else:
            remote_trailers = self.remote_trailers

        provider_ids: Union[Dict[str, Any], None, Unset]
        if isinstance(self.provider_ids, Unset):
            provider_ids = UNSET
        elif isinstance(self.provider_ids, BaseItemDtoProviderIdsType0):
            provider_ids = self.provider_ids.to_dict()
        else:
            provider_ids = self.provider_ids

        is_hd: Union[None, Unset, bool]
        if isinstance(self.is_hd, Unset):
            is_hd = UNSET
        else:
            is_hd = self.is_hd

        is_folder: Union[None, Unset, bool]
        if isinstance(self.is_folder, Unset):
            is_folder = UNSET
        else:
            is_folder = self.is_folder

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        people: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.people, Unset):
            people = UNSET
        elif isinstance(self.people, list):
            people = []
            for people_type_0_item_data in self.people:
                people_type_0_item = people_type_0_item_data.to_dict()
                people.append(people_type_0_item)

        else:
            people = self.people

        studios: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.studios, Unset):
            studios = UNSET
        elif isinstance(self.studios, list):
            studios = []
            for studios_type_0_item_data in self.studios:
                studios_type_0_item = studios_type_0_item_data.to_dict()
                studios.append(studios_type_0_item)

        else:
            studios = self.studios

        genre_items: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.genre_items, Unset):
            genre_items = UNSET
        elif isinstance(self.genre_items, list):
            genre_items = []
            for genre_items_type_0_item_data in self.genre_items:
                genre_items_type_0_item = genre_items_type_0_item_data.to_dict()
                genre_items.append(genre_items_type_0_item)

        else:
            genre_items = self.genre_items

        parent_logo_item_id: Union[None, Unset, str]
        if isinstance(self.parent_logo_item_id, Unset):
            parent_logo_item_id = UNSET
        else:
            parent_logo_item_id = self.parent_logo_item_id

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

        local_trailer_count: Union[None, Unset, int]
        if isinstance(self.local_trailer_count, Unset):
            local_trailer_count = UNSET
        else:
            local_trailer_count = self.local_trailer_count

        user_data: Union[Dict[str, Any], None, Unset]
        if isinstance(self.user_data, Unset):
            user_data = UNSET
        elif isinstance(self.user_data, UserItemDataDto):
            user_data = self.user_data.to_dict()
        else:
            user_data = self.user_data

        recursive_item_count: Union[None, Unset, int]
        if isinstance(self.recursive_item_count, Unset):
            recursive_item_count = UNSET
        else:
            recursive_item_count = self.recursive_item_count

        child_count: Union[None, Unset, int]
        if isinstance(self.child_count, Unset):
            child_count = UNSET
        else:
            child_count = self.child_count

        series_name: Union[None, Unset, str]
        if isinstance(self.series_name, Unset):
            series_name = UNSET
        else:
            series_name = self.series_name

        series_id: Union[None, Unset, str]
        if isinstance(self.series_id, Unset):
            series_id = UNSET
        else:
            series_id = self.series_id

        season_id: Union[None, Unset, str]
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        else:
            season_id = self.season_id

        special_feature_count: Union[None, Unset, int]
        if isinstance(self.special_feature_count, Unset):
            special_feature_count = UNSET
        else:
            special_feature_count = self.special_feature_count

        display_preferences_id: Union[None, Unset, str]
        if isinstance(self.display_preferences_id, Unset):
            display_preferences_id = UNSET
        else:
            display_preferences_id = self.display_preferences_id

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        air_time: Union[None, Unset, str]
        if isinstance(self.air_time, Unset):
            air_time = UNSET
        else:
            air_time = self.air_time

        air_days: Union[List[str], None, Unset]
        if isinstance(self.air_days, Unset):
            air_days = UNSET
        elif isinstance(self.air_days, list):
            air_days = []
            for air_days_type_0_item_data in self.air_days:
                air_days_type_0_item = air_days_type_0_item_data.value
                air_days.append(air_days_type_0_item)

        else:
            air_days = self.air_days

        tags: Union[List[str], None, Unset]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        primary_image_aspect_ratio: Union[None, Unset, float]
        if isinstance(self.primary_image_aspect_ratio, Unset):
            primary_image_aspect_ratio = UNSET
        else:
            primary_image_aspect_ratio = self.primary_image_aspect_ratio

        artists: Union[List[str], None, Unset]
        if isinstance(self.artists, Unset):
            artists = UNSET
        elif isinstance(self.artists, list):
            artists = self.artists

        else:
            artists = self.artists

        artist_items: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.artist_items, Unset):
            artist_items = UNSET
        elif isinstance(self.artist_items, list):
            artist_items = []
            for artist_items_type_0_item_data in self.artist_items:
                artist_items_type_0_item = artist_items_type_0_item_data.to_dict()
                artist_items.append(artist_items_type_0_item)

        else:
            artist_items = self.artist_items

        album: Union[None, Unset, str]
        if isinstance(self.album, Unset):
            album = UNSET
        else:
            album = self.album

        collection_type: Union[Unset, str] = UNSET
        if not isinstance(self.collection_type, Unset):
            collection_type = self.collection_type.value

        display_order: Union[None, Unset, str]
        if isinstance(self.display_order, Unset):
            display_order = UNSET
        else:
            display_order = self.display_order

        album_id: Union[None, Unset, str]
        if isinstance(self.album_id, Unset):
            album_id = UNSET
        else:
            album_id = self.album_id

        album_primary_image_tag: Union[None, Unset, str]
        if isinstance(self.album_primary_image_tag, Unset):
            album_primary_image_tag = UNSET
        else:
            album_primary_image_tag = self.album_primary_image_tag

        series_primary_image_tag: Union[None, Unset, str]
        if isinstance(self.series_primary_image_tag, Unset):
            series_primary_image_tag = UNSET
        else:
            series_primary_image_tag = self.series_primary_image_tag

        album_artist: Union[None, Unset, str]
        if isinstance(self.album_artist, Unset):
            album_artist = UNSET
        else:
            album_artist = self.album_artist

        album_artists: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.album_artists, Unset):
            album_artists = UNSET
        elif isinstance(self.album_artists, list):
            album_artists = []
            for album_artists_type_0_item_data in self.album_artists:
                album_artists_type_0_item = album_artists_type_0_item_data.to_dict()
                album_artists.append(album_artists_type_0_item)

        else:
            album_artists = self.album_artists

        season_name: Union[None, Unset, str]
        if isinstance(self.season_name, Unset):
            season_name = UNSET
        else:
            season_name = self.season_name

        media_streams: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.media_streams, Unset):
            media_streams = UNSET
        elif isinstance(self.media_streams, list):
            media_streams = []
            for media_streams_type_0_item_data in self.media_streams:
                media_streams_type_0_item = media_streams_type_0_item_data.to_dict()
                media_streams.append(media_streams_type_0_item)

        else:
            media_streams = self.media_streams

        video_type: Union[Unset, str] = UNSET
        if not isinstance(self.video_type, Unset):
            video_type = self.video_type.value

        part_count: Union[None, Unset, int]
        if isinstance(self.part_count, Unset):
            part_count = UNSET
        else:
            part_count = self.part_count

        media_source_count: Union[None, Unset, int]
        if isinstance(self.media_source_count, Unset):
            media_source_count = UNSET
        else:
            media_source_count = self.media_source_count

        image_tags: Union[Dict[str, Any], None, Unset]
        if isinstance(self.image_tags, Unset):
            image_tags = UNSET
        elif isinstance(self.image_tags, BaseItemDtoImageTagsType0):
            image_tags = self.image_tags.to_dict()
        else:
            image_tags = self.image_tags

        backdrop_image_tags: Union[List[str], None, Unset]
        if isinstance(self.backdrop_image_tags, Unset):
            backdrop_image_tags = UNSET
        elif isinstance(self.backdrop_image_tags, list):
            backdrop_image_tags = self.backdrop_image_tags

        else:
            backdrop_image_tags = self.backdrop_image_tags

        screenshot_image_tags: Union[List[str], None, Unset]
        if isinstance(self.screenshot_image_tags, Unset):
            screenshot_image_tags = UNSET
        elif isinstance(self.screenshot_image_tags, list):
            screenshot_image_tags = self.screenshot_image_tags

        else:
            screenshot_image_tags = self.screenshot_image_tags

        parent_logo_image_tag: Union[None, Unset, str]
        if isinstance(self.parent_logo_image_tag, Unset):
            parent_logo_image_tag = UNSET
        else:
            parent_logo_image_tag = self.parent_logo_image_tag

        parent_art_item_id: Union[None, Unset, str]
        if isinstance(self.parent_art_item_id, Unset):
            parent_art_item_id = UNSET
        else:
            parent_art_item_id = self.parent_art_item_id

        parent_art_image_tag: Union[None, Unset, str]
        if isinstance(self.parent_art_image_tag, Unset):
            parent_art_image_tag = UNSET
        else:
            parent_art_image_tag = self.parent_art_image_tag

        series_thumb_image_tag: Union[None, Unset, str]
        if isinstance(self.series_thumb_image_tag, Unset):
            series_thumb_image_tag = UNSET
        else:
            series_thumb_image_tag = self.series_thumb_image_tag

        image_blur_hashes: Union[Dict[str, Any], None, Unset]
        if isinstance(self.image_blur_hashes, Unset):
            image_blur_hashes = UNSET
        elif isinstance(self.image_blur_hashes, BaseItemDtoImageBlurHashesType0):
            image_blur_hashes = self.image_blur_hashes.to_dict()
        else:
            image_blur_hashes = self.image_blur_hashes

        series_studio: Union[None, Unset, str]
        if isinstance(self.series_studio, Unset):
            series_studio = UNSET
        else:
            series_studio = self.series_studio

        parent_thumb_item_id: Union[None, Unset, str]
        if isinstance(self.parent_thumb_item_id, Unset):
            parent_thumb_item_id = UNSET
        else:
            parent_thumb_item_id = self.parent_thumb_item_id

        parent_thumb_image_tag: Union[None, Unset, str]
        if isinstance(self.parent_thumb_image_tag, Unset):
            parent_thumb_image_tag = UNSET
        else:
            parent_thumb_image_tag = self.parent_thumb_image_tag

        parent_primary_image_item_id: Union[None, Unset, str]
        if isinstance(self.parent_primary_image_item_id, Unset):
            parent_primary_image_item_id = UNSET
        else:
            parent_primary_image_item_id = self.parent_primary_image_item_id

        parent_primary_image_tag: Union[None, Unset, str]
        if isinstance(self.parent_primary_image_tag, Unset):
            parent_primary_image_tag = UNSET
        else:
            parent_primary_image_tag = self.parent_primary_image_tag

        chapters: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.chapters, Unset):
            chapters = UNSET
        elif isinstance(self.chapters, list):
            chapters = []
            for chapters_type_0_item_data in self.chapters:
                chapters_type_0_item = chapters_type_0_item_data.to_dict()
                chapters.append(chapters_type_0_item)

        else:
            chapters = self.chapters

        trickplay: Union[Dict[str, Any], None, Unset]
        if isinstance(self.trickplay, Unset):
            trickplay = UNSET
        elif isinstance(self.trickplay, BaseItemDtoTrickplayType0):
            trickplay = self.trickplay.to_dict()
        else:
            trickplay = self.trickplay

        location_type: Union[Unset, str] = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        iso_type: Union[Unset, str] = UNSET
        if not isinstance(self.iso_type, Unset):
            iso_type = self.iso_type.value

        media_type: Union[Unset, str] = UNSET
        if not isinstance(self.media_type, Unset):
            media_type = self.media_type.value

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        locked_fields: Union[List[str], None, Unset]
        if isinstance(self.locked_fields, Unset):
            locked_fields = UNSET
        elif isinstance(self.locked_fields, list):
            locked_fields = []
            for locked_fields_type_0_item_data in self.locked_fields:
                locked_fields_type_0_item = locked_fields_type_0_item_data.value
                locked_fields.append(locked_fields_type_0_item)

        else:
            locked_fields = self.locked_fields

        trailer_count: Union[None, Unset, int]
        if isinstance(self.trailer_count, Unset):
            trailer_count = UNSET
        else:
            trailer_count = self.trailer_count

        movie_count: Union[None, Unset, int]
        if isinstance(self.movie_count, Unset):
            movie_count = UNSET
        else:
            movie_count = self.movie_count

        series_count: Union[None, Unset, int]
        if isinstance(self.series_count, Unset):
            series_count = UNSET
        else:
            series_count = self.series_count

        program_count: Union[None, Unset, int]
        if isinstance(self.program_count, Unset):
            program_count = UNSET
        else:
            program_count = self.program_count

        episode_count: Union[None, Unset, int]
        if isinstance(self.episode_count, Unset):
            episode_count = UNSET
        else:
            episode_count = self.episode_count

        song_count: Union[None, Unset, int]
        if isinstance(self.song_count, Unset):
            song_count = UNSET
        else:
            song_count = self.song_count

        album_count: Union[None, Unset, int]
        if isinstance(self.album_count, Unset):
            album_count = UNSET
        else:
            album_count = self.album_count

        artist_count: Union[None, Unset, int]
        if isinstance(self.artist_count, Unset):
            artist_count = UNSET
        else:
            artist_count = self.artist_count

        music_video_count: Union[None, Unset, int]
        if isinstance(self.music_video_count, Unset):
            music_video_count = UNSET
        else:
            music_video_count = self.music_video_count

        lock_data: Union[None, Unset, bool]
        if isinstance(self.lock_data, Unset):
            lock_data = UNSET
        else:
            lock_data = self.lock_data

        width: Union[None, Unset, int]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: Union[None, Unset, int]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        camera_make: Union[None, Unset, str]
        if isinstance(self.camera_make, Unset):
            camera_make = UNSET
        else:
            camera_make = self.camera_make

        camera_model: Union[None, Unset, str]
        if isinstance(self.camera_model, Unset):
            camera_model = UNSET
        else:
            camera_model = self.camera_model

        software: Union[None, Unset, str]
        if isinstance(self.software, Unset):
            software = UNSET
        else:
            software = self.software

        exposure_time: Union[None, Unset, float]
        if isinstance(self.exposure_time, Unset):
            exposure_time = UNSET
        else:
            exposure_time = self.exposure_time

        focal_length: Union[None, Unset, float]
        if isinstance(self.focal_length, Unset):
            focal_length = UNSET
        else:
            focal_length = self.focal_length

        image_orientation: Union[Unset, str] = UNSET
        if not isinstance(self.image_orientation, Unset):
            image_orientation = self.image_orientation.value

        aperture: Union[None, Unset, float]
        if isinstance(self.aperture, Unset):
            aperture = UNSET
        else:
            aperture = self.aperture

        shutter_speed: Union[None, Unset, float]
        if isinstance(self.shutter_speed, Unset):
            shutter_speed = UNSET
        else:
            shutter_speed = self.shutter_speed

        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        altitude: Union[None, Unset, float]
        if isinstance(self.altitude, Unset):
            altitude = UNSET
        else:
            altitude = self.altitude

        iso_speed_rating: Union[None, Unset, int]
        if isinstance(self.iso_speed_rating, Unset):
            iso_speed_rating = UNSET
        else:
            iso_speed_rating = self.iso_speed_rating

        series_timer_id: Union[None, Unset, str]
        if isinstance(self.series_timer_id, Unset):
            series_timer_id = UNSET
        else:
            series_timer_id = self.series_timer_id

        program_id: Union[None, Unset, str]
        if isinstance(self.program_id, Unset):
            program_id = UNSET
        else:
            program_id = self.program_id

        channel_primary_image_tag: Union[None, Unset, str]
        if isinstance(self.channel_primary_image_tag, Unset):
            channel_primary_image_tag = UNSET
        else:
            channel_primary_image_tag = self.channel_primary_image_tag

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        completion_percentage: Union[None, Unset, float]
        if isinstance(self.completion_percentage, Unset):
            completion_percentage = UNSET
        else:
            completion_percentage = self.completion_percentage

        is_repeat: Union[None, Unset, bool]
        if isinstance(self.is_repeat, Unset):
            is_repeat = UNSET
        else:
            is_repeat = self.is_repeat

        episode_title: Union[None, Unset, str]
        if isinstance(self.episode_title, Unset):
            episode_title = UNSET
        else:
            episode_title = self.episode_title

        channel_type: Union[Unset, str] = UNSET
        if not isinstance(self.channel_type, Unset):
            channel_type = self.channel_type.value

        audio: Union[Unset, str] = UNSET
        if not isinstance(self.audio, Unset):
            audio = self.audio.value

        is_movie: Union[None, Unset, bool]
        if isinstance(self.is_movie, Unset):
            is_movie = UNSET
        else:
            is_movie = self.is_movie

        is_sports: Union[None, Unset, bool]
        if isinstance(self.is_sports, Unset):
            is_sports = UNSET
        else:
            is_sports = self.is_sports

        is_series: Union[None, Unset, bool]
        if isinstance(self.is_series, Unset):
            is_series = UNSET
        else:
            is_series = self.is_series

        is_live: Union[None, Unset, bool]
        if isinstance(self.is_live, Unset):
            is_live = UNSET
        else:
            is_live = self.is_live

        is_news: Union[None, Unset, bool]
        if isinstance(self.is_news, Unset):
            is_news = UNSET
        else:
            is_news = self.is_news

        is_kids: Union[None, Unset, bool]
        if isinstance(self.is_kids, Unset):
            is_kids = UNSET
        else:
            is_kids = self.is_kids

        is_premiere: Union[None, Unset, bool]
        if isinstance(self.is_premiere, Unset):
            is_premiere = UNSET
        else:
            is_premiere = self.is_premiere

        timer_id: Union[None, Unset, str]
        if isinstance(self.timer_id, Unset):
            timer_id = UNSET
        else:
            timer_id = self.timer_id

        normalization_gain: Union[None, Unset, float]
        if isinstance(self.normalization_gain, Unset):
            normalization_gain = UNSET
        else:
            normalization_gain = self.normalization_gain

        current_program: Union[Dict[str, Any], None, Unset]
        if isinstance(self.current_program, Unset):
            current_program = UNSET
        elif isinstance(self.current_program, BaseItemDto):
            current_program = self.current_program.to_dict()
        else:
            current_program = self.current_program

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if original_title is not UNSET:
            field_dict["OriginalTitle"] = original_title
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id
        if id is not UNSET:
            field_dict["Id"] = id
        if etag is not UNSET:
            field_dict["Etag"] = etag
        if source_type is not UNSET:
            field_dict["SourceType"] = source_type
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if date_last_media_added is not UNSET:
            field_dict["DateLastMediaAdded"] = date_last_media_added
        if extra_type is not UNSET:
            field_dict["ExtraType"] = extra_type
        if airs_before_season_number is not UNSET:
            field_dict["AirsBeforeSeasonNumber"] = airs_before_season_number
        if airs_after_season_number is not UNSET:
            field_dict["AirsAfterSeasonNumber"] = airs_after_season_number
        if airs_before_episode_number is not UNSET:
            field_dict["AirsBeforeEpisodeNumber"] = airs_before_episode_number
        if can_delete is not UNSET:
            field_dict["CanDelete"] = can_delete
        if can_download is not UNSET:
            field_dict["CanDownload"] = can_download
        if has_lyrics is not UNSET:
            field_dict["HasLyrics"] = has_lyrics
        if has_subtitles is not UNSET:
            field_dict["HasSubtitles"] = has_subtitles
        if preferred_metadata_language is not UNSET:
            field_dict["PreferredMetadataLanguage"] = preferred_metadata_language
        if preferred_metadata_country_code is not UNSET:
            field_dict["PreferredMetadataCountryCode"] = preferred_metadata_country_code
        if container is not UNSET:
            field_dict["Container"] = container
        if sort_name is not UNSET:
            field_dict["SortName"] = sort_name
        if forced_sort_name is not UNSET:
            field_dict["ForcedSortName"] = forced_sort_name
        if video_3d_format is not UNSET:
            field_dict["Video3DFormat"] = video_3d_format
        if premiere_date is not UNSET:
            field_dict["PremiereDate"] = premiere_date
        if external_urls is not UNSET:
            field_dict["ExternalUrls"] = external_urls
        if media_sources is not UNSET:
            field_dict["MediaSources"] = media_sources
        if critic_rating is not UNSET:
            field_dict["CriticRating"] = critic_rating
        if production_locations is not UNSET:
            field_dict["ProductionLocations"] = production_locations
        if path is not UNSET:
            field_dict["Path"] = path
        if enable_media_source_display is not UNSET:
            field_dict["EnableMediaSourceDisplay"] = enable_media_source_display
        if official_rating is not UNSET:
            field_dict["OfficialRating"] = official_rating
        if custom_rating is not UNSET:
            field_dict["CustomRating"] = custom_rating
        if channel_id is not UNSET:
            field_dict["ChannelId"] = channel_id
        if channel_name is not UNSET:
            field_dict["ChannelName"] = channel_name
        if overview is not UNSET:
            field_dict["Overview"] = overview
        if taglines is not UNSET:
            field_dict["Taglines"] = taglines
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if community_rating is not UNSET:
            field_dict["CommunityRating"] = community_rating
        if cumulative_run_time_ticks is not UNSET:
            field_dict["CumulativeRunTimeTicks"] = cumulative_run_time_ticks
        if run_time_ticks is not UNSET:
            field_dict["RunTimeTicks"] = run_time_ticks
        if play_access is not UNSET:
            field_dict["PlayAccess"] = play_access
        if aspect_ratio is not UNSET:
            field_dict["AspectRatio"] = aspect_ratio
        if production_year is not UNSET:
            field_dict["ProductionYear"] = production_year
        if is_place_holder is not UNSET:
            field_dict["IsPlaceHolder"] = is_place_holder
        if number is not UNSET:
            field_dict["Number"] = number
        if channel_number is not UNSET:
            field_dict["ChannelNumber"] = channel_number
        if index_number is not UNSET:
            field_dict["IndexNumber"] = index_number
        if index_number_end is not UNSET:
            field_dict["IndexNumberEnd"] = index_number_end
        if parent_index_number is not UNSET:
            field_dict["ParentIndexNumber"] = parent_index_number
        if remote_trailers is not UNSET:
            field_dict["RemoteTrailers"] = remote_trailers
        if provider_ids is not UNSET:
            field_dict["ProviderIds"] = provider_ids
        if is_hd is not UNSET:
            field_dict["IsHD"] = is_hd
        if is_folder is not UNSET:
            field_dict["IsFolder"] = is_folder
        if parent_id is not UNSET:
            field_dict["ParentId"] = parent_id
        if type is not UNSET:
            field_dict["Type"] = type
        if people is not UNSET:
            field_dict["People"] = people
        if studios is not UNSET:
            field_dict["Studios"] = studios
        if genre_items is not UNSET:
            field_dict["GenreItems"] = genre_items
        if parent_logo_item_id is not UNSET:
            field_dict["ParentLogoItemId"] = parent_logo_item_id
        if parent_backdrop_item_id is not UNSET:
            field_dict["ParentBackdropItemId"] = parent_backdrop_item_id
        if parent_backdrop_image_tags is not UNSET:
            field_dict["ParentBackdropImageTags"] = parent_backdrop_image_tags
        if local_trailer_count is not UNSET:
            field_dict["LocalTrailerCount"] = local_trailer_count
        if user_data is not UNSET:
            field_dict["UserData"] = user_data
        if recursive_item_count is not UNSET:
            field_dict["RecursiveItemCount"] = recursive_item_count
        if child_count is not UNSET:
            field_dict["ChildCount"] = child_count
        if series_name is not UNSET:
            field_dict["SeriesName"] = series_name
        if series_id is not UNSET:
            field_dict["SeriesId"] = series_id
        if season_id is not UNSET:
            field_dict["SeasonId"] = season_id
        if special_feature_count is not UNSET:
            field_dict["SpecialFeatureCount"] = special_feature_count
        if display_preferences_id is not UNSET:
            field_dict["DisplayPreferencesId"] = display_preferences_id
        if status is not UNSET:
            field_dict["Status"] = status
        if air_time is not UNSET:
            field_dict["AirTime"] = air_time
        if air_days is not UNSET:
            field_dict["AirDays"] = air_days
        if tags is not UNSET:
            field_dict["Tags"] = tags
        if primary_image_aspect_ratio is not UNSET:
            field_dict["PrimaryImageAspectRatio"] = primary_image_aspect_ratio
        if artists is not UNSET:
            field_dict["Artists"] = artists
        if artist_items is not UNSET:
            field_dict["ArtistItems"] = artist_items
        if album is not UNSET:
            field_dict["Album"] = album
        if collection_type is not UNSET:
            field_dict["CollectionType"] = collection_type
        if display_order is not UNSET:
            field_dict["DisplayOrder"] = display_order
        if album_id is not UNSET:
            field_dict["AlbumId"] = album_id
        if album_primary_image_tag is not UNSET:
            field_dict["AlbumPrimaryImageTag"] = album_primary_image_tag
        if series_primary_image_tag is not UNSET:
            field_dict["SeriesPrimaryImageTag"] = series_primary_image_tag
        if album_artist is not UNSET:
            field_dict["AlbumArtist"] = album_artist
        if album_artists is not UNSET:
            field_dict["AlbumArtists"] = album_artists
        if season_name is not UNSET:
            field_dict["SeasonName"] = season_name
        if media_streams is not UNSET:
            field_dict["MediaStreams"] = media_streams
        if video_type is not UNSET:
            field_dict["VideoType"] = video_type
        if part_count is not UNSET:
            field_dict["PartCount"] = part_count
        if media_source_count is not UNSET:
            field_dict["MediaSourceCount"] = media_source_count
        if image_tags is not UNSET:
            field_dict["ImageTags"] = image_tags
        if backdrop_image_tags is not UNSET:
            field_dict["BackdropImageTags"] = backdrop_image_tags
        if screenshot_image_tags is not UNSET:
            field_dict["ScreenshotImageTags"] = screenshot_image_tags
        if parent_logo_image_tag is not UNSET:
            field_dict["ParentLogoImageTag"] = parent_logo_image_tag
        if parent_art_item_id is not UNSET:
            field_dict["ParentArtItemId"] = parent_art_item_id
        if parent_art_image_tag is not UNSET:
            field_dict["ParentArtImageTag"] = parent_art_image_tag
        if series_thumb_image_tag is not UNSET:
            field_dict["SeriesThumbImageTag"] = series_thumb_image_tag
        if image_blur_hashes is not UNSET:
            field_dict["ImageBlurHashes"] = image_blur_hashes
        if series_studio is not UNSET:
            field_dict["SeriesStudio"] = series_studio
        if parent_thumb_item_id is not UNSET:
            field_dict["ParentThumbItemId"] = parent_thumb_item_id
        if parent_thumb_image_tag is not UNSET:
            field_dict["ParentThumbImageTag"] = parent_thumb_image_tag
        if parent_primary_image_item_id is not UNSET:
            field_dict["ParentPrimaryImageItemId"] = parent_primary_image_item_id
        if parent_primary_image_tag is not UNSET:
            field_dict["ParentPrimaryImageTag"] = parent_primary_image_tag
        if chapters is not UNSET:
            field_dict["Chapters"] = chapters
        if trickplay is not UNSET:
            field_dict["Trickplay"] = trickplay
        if location_type is not UNSET:
            field_dict["LocationType"] = location_type
        if iso_type is not UNSET:
            field_dict["IsoType"] = iso_type
        if media_type is not UNSET:
            field_dict["MediaType"] = media_type
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if locked_fields is not UNSET:
            field_dict["LockedFields"] = locked_fields
        if trailer_count is not UNSET:
            field_dict["TrailerCount"] = trailer_count
        if movie_count is not UNSET:
            field_dict["MovieCount"] = movie_count
        if series_count is not UNSET:
            field_dict["SeriesCount"] = series_count
        if program_count is not UNSET:
            field_dict["ProgramCount"] = program_count
        if episode_count is not UNSET:
            field_dict["EpisodeCount"] = episode_count
        if song_count is not UNSET:
            field_dict["SongCount"] = song_count
        if album_count is not UNSET:
            field_dict["AlbumCount"] = album_count
        if artist_count is not UNSET:
            field_dict["ArtistCount"] = artist_count
        if music_video_count is not UNSET:
            field_dict["MusicVideoCount"] = music_video_count
        if lock_data is not UNSET:
            field_dict["LockData"] = lock_data
        if width is not UNSET:
            field_dict["Width"] = width
        if height is not UNSET:
            field_dict["Height"] = height
        if camera_make is not UNSET:
            field_dict["CameraMake"] = camera_make
        if camera_model is not UNSET:
            field_dict["CameraModel"] = camera_model
        if software is not UNSET:
            field_dict["Software"] = software
        if exposure_time is not UNSET:
            field_dict["ExposureTime"] = exposure_time
        if focal_length is not UNSET:
            field_dict["FocalLength"] = focal_length
        if image_orientation is not UNSET:
            field_dict["ImageOrientation"] = image_orientation
        if aperture is not UNSET:
            field_dict["Aperture"] = aperture
        if shutter_speed is not UNSET:
            field_dict["ShutterSpeed"] = shutter_speed
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if altitude is not UNSET:
            field_dict["Altitude"] = altitude
        if iso_speed_rating is not UNSET:
            field_dict["IsoSpeedRating"] = iso_speed_rating
        if series_timer_id is not UNSET:
            field_dict["SeriesTimerId"] = series_timer_id
        if program_id is not UNSET:
            field_dict["ProgramId"] = program_id
        if channel_primary_image_tag is not UNSET:
            field_dict["ChannelPrimaryImageTag"] = channel_primary_image_tag
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if completion_percentage is not UNSET:
            field_dict["CompletionPercentage"] = completion_percentage
        if is_repeat is not UNSET:
            field_dict["IsRepeat"] = is_repeat
        if episode_title is not UNSET:
            field_dict["EpisodeTitle"] = episode_title
        if channel_type is not UNSET:
            field_dict["ChannelType"] = channel_type
        if audio is not UNSET:
            field_dict["Audio"] = audio
        if is_movie is not UNSET:
            field_dict["IsMovie"] = is_movie
        if is_sports is not UNSET:
            field_dict["IsSports"] = is_sports
        if is_series is not UNSET:
            field_dict["IsSeries"] = is_series
        if is_live is not UNSET:
            field_dict["IsLive"] = is_live
        if is_news is not UNSET:
            field_dict["IsNews"] = is_news
        if is_kids is not UNSET:
            field_dict["IsKids"] = is_kids
        if is_premiere is not UNSET:
            field_dict["IsPremiere"] = is_premiere
        if timer_id is not UNSET:
            field_dict["TimerId"] = timer_id
        if normalization_gain is not UNSET:
            field_dict["NormalizationGain"] = normalization_gain
        if current_program is not UNSET:
            field_dict["CurrentProgram"] = current_program

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chapter_info import ChapterInfo
        from ..models.media_source_info import MediaSourceInfo
        from ..models.base_item_dto_image_blur_hashes_type_0 import (
            BaseItemDtoImageBlurHashesType0,
        )
        from ..models.media_url import MediaUrl
        from ..models.base_item_person import BaseItemPerson
        from ..models.base_item_dto_trickplay_type_0 import BaseItemDtoTrickplayType0
        from ..models.name_guid_pair import NameGuidPair
        from ..models.base_item_dto_provider_ids_type_0 import (
            BaseItemDtoProviderIdsType0,
        )
        from ..models.media_stream import MediaStream
        from ..models.external_url import ExternalUrl
        from ..models.base_item_dto_image_tags_type_0 import BaseItemDtoImageTagsType0
        from ..models.user_item_data_dto import UserItemDataDto

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_original_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        original_title = _parse_original_title(d.pop("OriginalTitle", UNSET))

        def _parse_server_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        server_id = _parse_server_id(d.pop("ServerId", UNSET))

        id = d.pop("Id", UNSET)

        def _parse_etag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        etag = _parse_etag(d.pop("Etag", UNSET))

        def _parse_source_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_type = _parse_source_type(d.pop("SourceType", UNSET))

        def _parse_playlist_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        playlist_item_id = _parse_playlist_item_id(d.pop("PlaylistItemId", UNSET))

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

        def _parse_date_last_media_added(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_last_media_added_type_0 = isoparse(data)

                return date_last_media_added_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_last_media_added = _parse_date_last_media_added(
            d.pop("DateLastMediaAdded", UNSET)
        )

        _extra_type = d.pop("ExtraType", UNSET)
        extra_type: Union[Unset, BaseItemDtoExtraType]
        if isinstance(_extra_type, Unset):
            extra_type = UNSET
        else:
            extra_type = BaseItemDtoExtraType(_extra_type)

        def _parse_airs_before_season_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        airs_before_season_number = _parse_airs_before_season_number(
            d.pop("AirsBeforeSeasonNumber", UNSET)
        )

        def _parse_airs_after_season_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        airs_after_season_number = _parse_airs_after_season_number(
            d.pop("AirsAfterSeasonNumber", UNSET)
        )

        def _parse_airs_before_episode_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        airs_before_episode_number = _parse_airs_before_episode_number(
            d.pop("AirsBeforeEpisodeNumber", UNSET)
        )

        def _parse_can_delete(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        can_delete = _parse_can_delete(d.pop("CanDelete", UNSET))

        def _parse_can_download(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        can_download = _parse_can_download(d.pop("CanDownload", UNSET))

        def _parse_has_lyrics(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_lyrics = _parse_has_lyrics(d.pop("HasLyrics", UNSET))

        def _parse_has_subtitles(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_subtitles = _parse_has_subtitles(d.pop("HasSubtitles", UNSET))

        def _parse_preferred_metadata_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_metadata_language = _parse_preferred_metadata_language(
            d.pop("PreferredMetadataLanguage", UNSET)
        )

        def _parse_preferred_metadata_country_code(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_metadata_country_code = _parse_preferred_metadata_country_code(
            d.pop("PreferredMetadataCountryCode", UNSET)
        )

        def _parse_container(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        container = _parse_container(d.pop("Container", UNSET))

        def _parse_sort_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sort_name = _parse_sort_name(d.pop("SortName", UNSET))

        def _parse_forced_sort_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        forced_sort_name = _parse_forced_sort_name(d.pop("ForcedSortName", UNSET))

        _video_3d_format = d.pop("Video3DFormat", UNSET)
        video_3d_format: Union[Unset, BaseItemDtoVideo3DFormat]
        if isinstance(_video_3d_format, Unset):
            video_3d_format = UNSET
        else:
            video_3d_format = BaseItemDtoVideo3DFormat(_video_3d_format)

        def _parse_premiere_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                premiere_date_type_0 = isoparse(data)

                return premiere_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        premiere_date = _parse_premiere_date(d.pop("PremiereDate", UNSET))

        def _parse_external_urls(
            data: object,
        ) -> Union[List["ExternalUrl"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_urls_type_0 = []
                _external_urls_type_0 = data
                for external_urls_type_0_item_data in _external_urls_type_0:
                    external_urls_type_0_item = ExternalUrl.from_dict(
                        external_urls_type_0_item_data
                    )

                    external_urls_type_0.append(external_urls_type_0_item)

                return external_urls_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ExternalUrl"], None, Unset], data)

        external_urls = _parse_external_urls(d.pop("ExternalUrls", UNSET))

        def _parse_media_sources(
            data: object,
        ) -> Union[List["MediaSourceInfo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_sources_type_0 = []
                _media_sources_type_0 = data
                for media_sources_type_0_item_data in _media_sources_type_0:
                    media_sources_type_0_item = MediaSourceInfo.from_dict(
                        media_sources_type_0_item_data
                    )

                    media_sources_type_0.append(media_sources_type_0_item)

                return media_sources_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["MediaSourceInfo"], None, Unset], data)

        media_sources = _parse_media_sources(d.pop("MediaSources", UNSET))

        def _parse_critic_rating(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        critic_rating = _parse_critic_rating(d.pop("CriticRating", UNSET))

        def _parse_production_locations(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                production_locations_type_0 = cast(List[str], data)

                return production_locations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        production_locations = _parse_production_locations(
            d.pop("ProductionLocations", UNSET)
        )

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_enable_media_source_display(
            data: object,
        ) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_media_source_display = _parse_enable_media_source_display(
            d.pop("EnableMediaSourceDisplay", UNSET)
        )

        def _parse_official_rating(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        official_rating = _parse_official_rating(d.pop("OfficialRating", UNSET))

        def _parse_custom_rating(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_rating = _parse_custom_rating(d.pop("CustomRating", UNSET))

        def _parse_channel_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_id = _parse_channel_id(d.pop("ChannelId", UNSET))

        def _parse_channel_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_name = _parse_channel_name(d.pop("ChannelName", UNSET))

        def _parse_overview(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        overview = _parse_overview(d.pop("Overview", UNSET))

        def _parse_taglines(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                taglines_type_0 = cast(List[str], data)

                return taglines_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        taglines = _parse_taglines(d.pop("Taglines", UNSET))

        def _parse_genres(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genres_type_0 = cast(List[str], data)

                return genres_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        genres = _parse_genres(d.pop("Genres", UNSET))

        def _parse_community_rating(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        community_rating = _parse_community_rating(d.pop("CommunityRating", UNSET))

        def _parse_cumulative_run_time_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cumulative_run_time_ticks = _parse_cumulative_run_time_ticks(
            d.pop("CumulativeRunTimeTicks", UNSET)
        )

        def _parse_run_time_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        run_time_ticks = _parse_run_time_ticks(d.pop("RunTimeTicks", UNSET))

        _play_access = d.pop("PlayAccess", UNSET)
        play_access: Union[Unset, BaseItemDtoPlayAccess]
        if isinstance(_play_access, Unset):
            play_access = UNSET
        else:
            play_access = BaseItemDtoPlayAccess(_play_access)

        def _parse_aspect_ratio(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aspect_ratio = _parse_aspect_ratio(d.pop("AspectRatio", UNSET))

        def _parse_production_year(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        production_year = _parse_production_year(d.pop("ProductionYear", UNSET))

        def _parse_is_place_holder(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_place_holder = _parse_is_place_holder(d.pop("IsPlaceHolder", UNSET))

        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("Number", UNSET))

        def _parse_channel_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_number = _parse_channel_number(d.pop("ChannelNumber", UNSET))

        def _parse_index_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        index_number = _parse_index_number(d.pop("IndexNumber", UNSET))

        def _parse_index_number_end(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        index_number_end = _parse_index_number_end(d.pop("IndexNumberEnd", UNSET))

        def _parse_parent_index_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_index_number = _parse_parent_index_number(
            d.pop("ParentIndexNumber", UNSET)
        )

        def _parse_remote_trailers(
            data: object,
        ) -> Union[List["MediaUrl"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                remote_trailers_type_0 = []
                _remote_trailers_type_0 = data
                for remote_trailers_type_0_item_data in _remote_trailers_type_0:
                    remote_trailers_type_0_item = MediaUrl.from_dict(
                        remote_trailers_type_0_item_data
                    )

                    remote_trailers_type_0.append(remote_trailers_type_0_item)

                return remote_trailers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["MediaUrl"], None, Unset], data)

        remote_trailers = _parse_remote_trailers(d.pop("RemoteTrailers", UNSET))

        def _parse_provider_ids(
            data: object,
        ) -> Union["BaseItemDtoProviderIdsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_ids_type_0 = BaseItemDtoProviderIdsType0.from_dict(data)

                return provider_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemDtoProviderIdsType0", None, Unset], data)

        provider_ids = _parse_provider_ids(d.pop("ProviderIds", UNSET))

        def _parse_is_hd(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_hd = _parse_is_hd(d.pop("IsHD", UNSET))

        def _parse_is_folder(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_folder = _parse_is_folder(d.pop("IsFolder", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("ParentId", UNSET))

        _type = d.pop("Type", UNSET)
        type: Union[Unset, BaseItemKind]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = BaseItemKind(_type)

        def _parse_people(data: object) -> Union[List["BaseItemPerson"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                people_type_0 = []
                _people_type_0 = data
                for people_type_0_item_data in _people_type_0:
                    people_type_0_item = BaseItemPerson.from_dict(
                        people_type_0_item_data
                    )

                    people_type_0.append(people_type_0_item)

                return people_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["BaseItemPerson"], None, Unset], data)

        people = _parse_people(d.pop("People", UNSET))

        def _parse_studios(data: object) -> Union[List["NameGuidPair"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                studios_type_0 = []
                _studios_type_0 = data
                for studios_type_0_item_data in _studios_type_0:
                    studios_type_0_item = NameGuidPair.from_dict(
                        studios_type_0_item_data
                    )

                    studios_type_0.append(studios_type_0_item)

                return studios_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["NameGuidPair"], None, Unset], data)

        studios = _parse_studios(d.pop("Studios", UNSET))

        def _parse_genre_items(
            data: object,
        ) -> Union[List["NameGuidPair"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genre_items_type_0 = []
                _genre_items_type_0 = data
                for genre_items_type_0_item_data in _genre_items_type_0:
                    genre_items_type_0_item = NameGuidPair.from_dict(
                        genre_items_type_0_item_data
                    )

                    genre_items_type_0.append(genre_items_type_0_item)

                return genre_items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["NameGuidPair"], None, Unset], data)

        genre_items = _parse_genre_items(d.pop("GenreItems", UNSET))

        def _parse_parent_logo_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_logo_item_id = _parse_parent_logo_item_id(
            d.pop("ParentLogoItemId", UNSET)
        )

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

        def _parse_local_trailer_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        local_trailer_count = _parse_local_trailer_count(
            d.pop("LocalTrailerCount", UNSET)
        )

        def _parse_user_data(data: object) -> Union["UserItemDataDto", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_data_type_1 = UserItemDataDto.from_dict(data)

                return user_data_type_1
            except:  # noqa: E722
                pass
            return cast(Union["UserItemDataDto", None, Unset], data)

        user_data = _parse_user_data(d.pop("UserData", UNSET))

        def _parse_recursive_item_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        recursive_item_count = _parse_recursive_item_count(
            d.pop("RecursiveItemCount", UNSET)
        )

        def _parse_child_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        child_count = _parse_child_count(d.pop("ChildCount", UNSET))

        def _parse_series_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_name = _parse_series_name(d.pop("SeriesName", UNSET))

        def _parse_series_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_id = _parse_series_id(d.pop("SeriesId", UNSET))

        def _parse_season_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        season_id = _parse_season_id(d.pop("SeasonId", UNSET))

        def _parse_special_feature_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        special_feature_count = _parse_special_feature_count(
            d.pop("SpecialFeatureCount", UNSET)
        )

        def _parse_display_preferences_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_preferences_id = _parse_display_preferences_id(
            d.pop("DisplayPreferencesId", UNSET)
        )

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("Status", UNSET))

        def _parse_air_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        air_time = _parse_air_time(d.pop("AirTime", UNSET))

        def _parse_air_days(data: object) -> Union[List[DayOfWeek], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                air_days_type_0 = []
                _air_days_type_0 = data
                for air_days_type_0_item_data in _air_days_type_0:
                    air_days_type_0_item = DayOfWeek(air_days_type_0_item_data)

                    air_days_type_0.append(air_days_type_0_item)

                return air_days_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[DayOfWeek], None, Unset], data)

        air_days = _parse_air_days(d.pop("AirDays", UNSET))

        def _parse_tags(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(List[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        tags = _parse_tags(d.pop("Tags", UNSET))

        def _parse_primary_image_aspect_ratio(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        primary_image_aspect_ratio = _parse_primary_image_aspect_ratio(
            d.pop("PrimaryImageAspectRatio", UNSET)
        )

        def _parse_artists(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                artists_type_0 = cast(List[str], data)

                return artists_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        artists = _parse_artists(d.pop("Artists", UNSET))

        def _parse_artist_items(
            data: object,
        ) -> Union[List["NameGuidPair"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                artist_items_type_0 = []
                _artist_items_type_0 = data
                for artist_items_type_0_item_data in _artist_items_type_0:
                    artist_items_type_0_item = NameGuidPair.from_dict(
                        artist_items_type_0_item_data
                    )

                    artist_items_type_0.append(artist_items_type_0_item)

                return artist_items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["NameGuidPair"], None, Unset], data)

        artist_items = _parse_artist_items(d.pop("ArtistItems", UNSET))

        def _parse_album(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album = _parse_album(d.pop("Album", UNSET))

        _collection_type = d.pop("CollectionType", UNSET)
        collection_type: Union[Unset, BaseItemDtoCollectionType]
        if isinstance(_collection_type, Unset):
            collection_type = UNSET
        else:
            collection_type = BaseItemDtoCollectionType(_collection_type)

        def _parse_display_order(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_order = _parse_display_order(d.pop("DisplayOrder", UNSET))

        def _parse_album_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album_id = _parse_album_id(d.pop("AlbumId", UNSET))

        def _parse_album_primary_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album_primary_image_tag = _parse_album_primary_image_tag(
            d.pop("AlbumPrimaryImageTag", UNSET)
        )

        def _parse_series_primary_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_primary_image_tag = _parse_series_primary_image_tag(
            d.pop("SeriesPrimaryImageTag", UNSET)
        )

        def _parse_album_artist(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album_artist = _parse_album_artist(d.pop("AlbumArtist", UNSET))

        def _parse_album_artists(
            data: object,
        ) -> Union[List["NameGuidPair"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                album_artists_type_0 = []
                _album_artists_type_0 = data
                for album_artists_type_0_item_data in _album_artists_type_0:
                    album_artists_type_0_item = NameGuidPair.from_dict(
                        album_artists_type_0_item_data
                    )

                    album_artists_type_0.append(album_artists_type_0_item)

                return album_artists_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["NameGuidPair"], None, Unset], data)

        album_artists = _parse_album_artists(d.pop("AlbumArtists", UNSET))

        def _parse_season_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        season_name = _parse_season_name(d.pop("SeasonName", UNSET))

        def _parse_media_streams(
            data: object,
        ) -> Union[List["MediaStream"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_streams_type_0 = []
                _media_streams_type_0 = data
                for media_streams_type_0_item_data in _media_streams_type_0:
                    media_streams_type_0_item = MediaStream.from_dict(
                        media_streams_type_0_item_data
                    )

                    media_streams_type_0.append(media_streams_type_0_item)

                return media_streams_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["MediaStream"], None, Unset], data)

        media_streams = _parse_media_streams(d.pop("MediaStreams", UNSET))

        _video_type = d.pop("VideoType", UNSET)
        video_type: Union[Unset, BaseItemDtoVideoType]
        if isinstance(_video_type, Unset):
            video_type = UNSET
        else:
            video_type = BaseItemDtoVideoType(_video_type)

        def _parse_part_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        part_count = _parse_part_count(d.pop("PartCount", UNSET))

        def _parse_media_source_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        media_source_count = _parse_media_source_count(d.pop("MediaSourceCount", UNSET))

        def _parse_image_tags(
            data: object,
        ) -> Union["BaseItemDtoImageTagsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_tags_type_0 = BaseItemDtoImageTagsType0.from_dict(data)

                return image_tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemDtoImageTagsType0", None, Unset], data)

        image_tags = _parse_image_tags(d.pop("ImageTags", UNSET))

        def _parse_backdrop_image_tags(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                backdrop_image_tags_type_0 = cast(List[str], data)

                return backdrop_image_tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        backdrop_image_tags = _parse_backdrop_image_tags(
            d.pop("BackdropImageTags", UNSET)
        )

        def _parse_screenshot_image_tags(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                screenshot_image_tags_type_0 = cast(List[str], data)

                return screenshot_image_tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        screenshot_image_tags = _parse_screenshot_image_tags(
            d.pop("ScreenshotImageTags", UNSET)
        )

        def _parse_parent_logo_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_logo_image_tag = _parse_parent_logo_image_tag(
            d.pop("ParentLogoImageTag", UNSET)
        )

        def _parse_parent_art_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_art_item_id = _parse_parent_art_item_id(d.pop("ParentArtItemId", UNSET))

        def _parse_parent_art_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_art_image_tag = _parse_parent_art_image_tag(
            d.pop("ParentArtImageTag", UNSET)
        )

        def _parse_series_thumb_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_thumb_image_tag = _parse_series_thumb_image_tag(
            d.pop("SeriesThumbImageTag", UNSET)
        )

        def _parse_image_blur_hashes(
            data: object,
        ) -> Union["BaseItemDtoImageBlurHashesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_blur_hashes_type_0 = BaseItemDtoImageBlurHashesType0.from_dict(
                    data
                )

                return image_blur_hashes_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemDtoImageBlurHashesType0", None, Unset], data)

        image_blur_hashes = _parse_image_blur_hashes(d.pop("ImageBlurHashes", UNSET))

        def _parse_series_studio(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_studio = _parse_series_studio(d.pop("SeriesStudio", UNSET))

        def _parse_parent_thumb_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_thumb_item_id = _parse_parent_thumb_item_id(
            d.pop("ParentThumbItemId", UNSET)
        )

        def _parse_parent_thumb_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_thumb_image_tag = _parse_parent_thumb_image_tag(
            d.pop("ParentThumbImageTag", UNSET)
        )

        def _parse_parent_primary_image_item_id(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_primary_image_item_id = _parse_parent_primary_image_item_id(
            d.pop("ParentPrimaryImageItemId", UNSET)
        )

        def _parse_parent_primary_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_primary_image_tag = _parse_parent_primary_image_tag(
            d.pop("ParentPrimaryImageTag", UNSET)
        )

        def _parse_chapters(data: object) -> Union[List["ChapterInfo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                chapters_type_0 = []
                _chapters_type_0 = data
                for chapters_type_0_item_data in _chapters_type_0:
                    chapters_type_0_item = ChapterInfo.from_dict(
                        chapters_type_0_item_data
                    )

                    chapters_type_0.append(chapters_type_0_item)

                return chapters_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ChapterInfo"], None, Unset], data)

        chapters = _parse_chapters(d.pop("Chapters", UNSET))

        def _parse_trickplay(
            data: object,
        ) -> Union["BaseItemDtoTrickplayType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trickplay_type_0 = BaseItemDtoTrickplayType0.from_dict(data)

                return trickplay_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemDtoTrickplayType0", None, Unset], data)

        trickplay = _parse_trickplay(d.pop("Trickplay", UNSET))

        _location_type = d.pop("LocationType", UNSET)
        location_type: Union[Unset, BaseItemDtoLocationType]
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = BaseItemDtoLocationType(_location_type)

        _iso_type = d.pop("IsoType", UNSET)
        iso_type: Union[Unset, BaseItemDtoIsoType]
        if isinstance(_iso_type, Unset):
            iso_type = UNSET
        else:
            iso_type = BaseItemDtoIsoType(_iso_type)

        _media_type = d.pop("MediaType", UNSET)
        media_type: Union[Unset, MediaType]
        if isinstance(_media_type, Unset):
            media_type = UNSET
        else:
            media_type = MediaType(_media_type)

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_date = _parse_end_date(d.pop("EndDate", UNSET))

        def _parse_locked_fields(
            data: object,
        ) -> Union[List[MetadataField], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locked_fields_type_0 = []
                _locked_fields_type_0 = data
                for locked_fields_type_0_item_data in _locked_fields_type_0:
                    locked_fields_type_0_item = MetadataField(
                        locked_fields_type_0_item_data
                    )

                    locked_fields_type_0.append(locked_fields_type_0_item)

                return locked_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[MetadataField], None, Unset], data)

        locked_fields = _parse_locked_fields(d.pop("LockedFields", UNSET))

        def _parse_trailer_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        trailer_count = _parse_trailer_count(d.pop("TrailerCount", UNSET))

        def _parse_movie_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        movie_count = _parse_movie_count(d.pop("MovieCount", UNSET))

        def _parse_series_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        series_count = _parse_series_count(d.pop("SeriesCount", UNSET))

        def _parse_program_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        program_count = _parse_program_count(d.pop("ProgramCount", UNSET))

        def _parse_episode_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        episode_count = _parse_episode_count(d.pop("EpisodeCount", UNSET))

        def _parse_song_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        song_count = _parse_song_count(d.pop("SongCount", UNSET))

        def _parse_album_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        album_count = _parse_album_count(d.pop("AlbumCount", UNSET))

        def _parse_artist_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        artist_count = _parse_artist_count(d.pop("ArtistCount", UNSET))

        def _parse_music_video_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        music_video_count = _parse_music_video_count(d.pop("MusicVideoCount", UNSET))

        def _parse_lock_data(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        lock_data = _parse_lock_data(d.pop("LockData", UNSET))

        def _parse_width(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        width = _parse_width(d.pop("Width", UNSET))

        def _parse_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        height = _parse_height(d.pop("Height", UNSET))

        def _parse_camera_make(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        camera_make = _parse_camera_make(d.pop("CameraMake", UNSET))

        def _parse_camera_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        camera_model = _parse_camera_model(d.pop("CameraModel", UNSET))

        def _parse_software(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        software = _parse_software(d.pop("Software", UNSET))

        def _parse_exposure_time(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        exposure_time = _parse_exposure_time(d.pop("ExposureTime", UNSET))

        def _parse_focal_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        focal_length = _parse_focal_length(d.pop("FocalLength", UNSET))

        _image_orientation = d.pop("ImageOrientation", UNSET)
        image_orientation: Union[Unset, BaseItemDtoImageOrientation]
        if isinstance(_image_orientation, Unset):
            image_orientation = UNSET
        else:
            image_orientation = BaseItemDtoImageOrientation(_image_orientation)

        def _parse_aperture(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        aperture = _parse_aperture(d.pop("Aperture", UNSET))

        def _parse_shutter_speed(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shutter_speed = _parse_shutter_speed(d.pop("ShutterSpeed", UNSET))

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_altitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        altitude = _parse_altitude(d.pop("Altitude", UNSET))

        def _parse_iso_speed_rating(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        iso_speed_rating = _parse_iso_speed_rating(d.pop("IsoSpeedRating", UNSET))

        def _parse_series_timer_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_timer_id = _parse_series_timer_id(d.pop("SeriesTimerId", UNSET))

        def _parse_program_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        program_id = _parse_program_id(d.pop("ProgramId", UNSET))

        def _parse_channel_primary_image_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_primary_image_tag = _parse_channel_primary_image_tag(
            d.pop("ChannelPrimaryImageTag", UNSET)
        )

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_date = _parse_start_date(d.pop("StartDate", UNSET))

        def _parse_completion_percentage(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        completion_percentage = _parse_completion_percentage(
            d.pop("CompletionPercentage", UNSET)
        )

        def _parse_is_repeat(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_repeat = _parse_is_repeat(d.pop("IsRepeat", UNSET))

        def _parse_episode_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        episode_title = _parse_episode_title(d.pop("EpisodeTitle", UNSET))

        _channel_type = d.pop("ChannelType", UNSET)
        channel_type: Union[Unset, BaseItemDtoChannelType]
        if isinstance(_channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = BaseItemDtoChannelType(_channel_type)

        _audio = d.pop("Audio", UNSET)
        audio: Union[Unset, BaseItemDtoAudio]
        if isinstance(_audio, Unset):
            audio = UNSET
        else:
            audio = BaseItemDtoAudio(_audio)

        def _parse_is_movie(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_movie = _parse_is_movie(d.pop("IsMovie", UNSET))

        def _parse_is_sports(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_sports = _parse_is_sports(d.pop("IsSports", UNSET))

        def _parse_is_series(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_series = _parse_is_series(d.pop("IsSeries", UNSET))

        def _parse_is_live(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_live = _parse_is_live(d.pop("IsLive", UNSET))

        def _parse_is_news(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_news = _parse_is_news(d.pop("IsNews", UNSET))

        def _parse_is_kids(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_kids = _parse_is_kids(d.pop("IsKids", UNSET))

        def _parse_is_premiere(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_premiere = _parse_is_premiere(d.pop("IsPremiere", UNSET))

        def _parse_timer_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        timer_id = _parse_timer_id(d.pop("TimerId", UNSET))

        def _parse_normalization_gain(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        normalization_gain = _parse_normalization_gain(
            d.pop("NormalizationGain", UNSET)
        )

        def _parse_current_program(data: object) -> Union["BaseItemDto", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_program_type_1 = BaseItemDto.from_dict(data)

                return current_program_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemDto", None, Unset], data)

        current_program = _parse_current_program(d.pop("CurrentProgram", UNSET))

        base_item_dto = cls(
            name=name,
            original_title=original_title,
            server_id=server_id,
            id=id,
            etag=etag,
            source_type=source_type,
            playlist_item_id=playlist_item_id,
            date_created=date_created,
            date_last_media_added=date_last_media_added,
            extra_type=extra_type,
            airs_before_season_number=airs_before_season_number,
            airs_after_season_number=airs_after_season_number,
            airs_before_episode_number=airs_before_episode_number,
            can_delete=can_delete,
            can_download=can_download,
            has_lyrics=has_lyrics,
            has_subtitles=has_subtitles,
            preferred_metadata_language=preferred_metadata_language,
            preferred_metadata_country_code=preferred_metadata_country_code,
            container=container,
            sort_name=sort_name,
            forced_sort_name=forced_sort_name,
            video_3d_format=video_3d_format,
            premiere_date=premiere_date,
            external_urls=external_urls,
            media_sources=media_sources,
            critic_rating=critic_rating,
            production_locations=production_locations,
            path=path,
            enable_media_source_display=enable_media_source_display,
            official_rating=official_rating,
            custom_rating=custom_rating,
            channel_id=channel_id,
            channel_name=channel_name,
            overview=overview,
            taglines=taglines,
            genres=genres,
            community_rating=community_rating,
            cumulative_run_time_ticks=cumulative_run_time_ticks,
            run_time_ticks=run_time_ticks,
            play_access=play_access,
            aspect_ratio=aspect_ratio,
            production_year=production_year,
            is_place_holder=is_place_holder,
            number=number,
            channel_number=channel_number,
            index_number=index_number,
            index_number_end=index_number_end,
            parent_index_number=parent_index_number,
            remote_trailers=remote_trailers,
            provider_ids=provider_ids,
            is_hd=is_hd,
            is_folder=is_folder,
            parent_id=parent_id,
            type=type,
            people=people,
            studios=studios,
            genre_items=genre_items,
            parent_logo_item_id=parent_logo_item_id,
            parent_backdrop_item_id=parent_backdrop_item_id,
            parent_backdrop_image_tags=parent_backdrop_image_tags,
            local_trailer_count=local_trailer_count,
            user_data=user_data,
            recursive_item_count=recursive_item_count,
            child_count=child_count,
            series_name=series_name,
            series_id=series_id,
            season_id=season_id,
            special_feature_count=special_feature_count,
            display_preferences_id=display_preferences_id,
            status=status,
            air_time=air_time,
            air_days=air_days,
            tags=tags,
            primary_image_aspect_ratio=primary_image_aspect_ratio,
            artists=artists,
            artist_items=artist_items,
            album=album,
            collection_type=collection_type,
            display_order=display_order,
            album_id=album_id,
            album_primary_image_tag=album_primary_image_tag,
            series_primary_image_tag=series_primary_image_tag,
            album_artist=album_artist,
            album_artists=album_artists,
            season_name=season_name,
            media_streams=media_streams,
            video_type=video_type,
            part_count=part_count,
            media_source_count=media_source_count,
            image_tags=image_tags,
            backdrop_image_tags=backdrop_image_tags,
            screenshot_image_tags=screenshot_image_tags,
            parent_logo_image_tag=parent_logo_image_tag,
            parent_art_item_id=parent_art_item_id,
            parent_art_image_tag=parent_art_image_tag,
            series_thumb_image_tag=series_thumb_image_tag,
            image_blur_hashes=image_blur_hashes,
            series_studio=series_studio,
            parent_thumb_item_id=parent_thumb_item_id,
            parent_thumb_image_tag=parent_thumb_image_tag,
            parent_primary_image_item_id=parent_primary_image_item_id,
            parent_primary_image_tag=parent_primary_image_tag,
            chapters=chapters,
            trickplay=trickplay,
            location_type=location_type,
            iso_type=iso_type,
            media_type=media_type,
            end_date=end_date,
            locked_fields=locked_fields,
            trailer_count=trailer_count,
            movie_count=movie_count,
            series_count=series_count,
            program_count=program_count,
            episode_count=episode_count,
            song_count=song_count,
            album_count=album_count,
            artist_count=artist_count,
            music_video_count=music_video_count,
            lock_data=lock_data,
            width=width,
            height=height,
            camera_make=camera_make,
            camera_model=camera_model,
            software=software,
            exposure_time=exposure_time,
            focal_length=focal_length,
            image_orientation=image_orientation,
            aperture=aperture,
            shutter_speed=shutter_speed,
            latitude=latitude,
            longitude=longitude,
            altitude=altitude,
            iso_speed_rating=iso_speed_rating,
            series_timer_id=series_timer_id,
            program_id=program_id,
            channel_primary_image_tag=channel_primary_image_tag,
            start_date=start_date,
            completion_percentage=completion_percentage,
            is_repeat=is_repeat,
            episode_title=episode_title,
            channel_type=channel_type,
            audio=audio,
            is_movie=is_movie,
            is_sports=is_sports,
            is_series=is_series,
            is_live=is_live,
            is_news=is_news,
            is_kids=is_kids,
            is_premiere=is_premiere,
            timer_id=timer_id,
            normalization_gain=normalization_gain,
            current_program=current_program,
        )

        return base_item_dto
