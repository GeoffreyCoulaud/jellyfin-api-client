from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
from ...models.location_type import LocationType
from ...models.series_status import SeriesStatus
from ...models.video_type import VideoType
from ...models.item_fields import ItemFields
from ...models.image_type import ImageType
import datetime
from ...models.sort_order import SortOrder
from ...models.base_item_kind import BaseItemKind
from ...models.media_type import MediaType
from ...models.item_filter import ItemFilter
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_sort_by import ItemSortBy


def _get_kwargs(
    *,
    user_id: Union[Unset, str] = UNSET,
    max_official_rating: Union[Unset, str] = UNSET,
    has_theme_song: Union[Unset, bool] = UNSET,
    has_theme_video: Union[Unset, bool] = UNSET,
    has_subtitles: Union[Unset, bool] = UNSET,
    has_special_feature: Union[Unset, bool] = UNSET,
    has_trailer: Union[Unset, bool] = UNSET,
    adjacent_to: Union[Unset, str] = UNSET,
    parent_index_number: Union[Unset, int] = UNSET,
    has_parental_rating: Union[Unset, bool] = UNSET,
    is_hd: Union[Unset, bool] = UNSET,
    is_4k: Union[Unset, bool] = UNSET,
    location_types: Union[Unset, List[LocationType]] = UNSET,
    exclude_location_types: Union[Unset, List[LocationType]] = UNSET,
    is_missing: Union[Unset, bool] = UNSET,
    is_unaired: Union[Unset, bool] = UNSET,
    min_community_rating: Union[Unset, float] = UNSET,
    min_critic_rating: Union[Unset, float] = UNSET,
    min_premiere_date: Union[Unset, datetime.datetime] = UNSET,
    min_date_last_saved: Union[Unset, datetime.datetime] = UNSET,
    min_date_last_saved_for_user: Union[Unset, datetime.datetime] = UNSET,
    max_premiere_date: Union[Unset, datetime.datetime] = UNSET,
    has_overview: Union[Unset, bool] = UNSET,
    has_imdb_id: Union[Unset, bool] = UNSET,
    has_tmdb_id: Union[Unset, bool] = UNSET,
    has_tvdb_id: Union[Unset, bool] = UNSET,
    is_movie: Union[Unset, bool] = UNSET,
    is_series: Union[Unset, bool] = UNSET,
    is_news: Union[Unset, bool] = UNSET,
    is_kids: Union[Unset, bool] = UNSET,
    is_sports: Union[Unset, bool] = UNSET,
    exclude_item_ids: Union[Unset, List[str]] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, List[SortOrder]] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    media_types: Union[Unset, List[MediaType]] = UNSET,
    image_types: Union[Unset, List[ImageType]] = UNSET,
    sort_by: Union[Unset, List[ItemSortBy]] = UNSET,
    is_played: Union[Unset, bool] = UNSET,
    genres: Union[Unset, List[str]] = UNSET,
    official_ratings: Union[Unset, List[str]] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    years: Union[Unset, List[int]] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    person: Union[Unset, str] = UNSET,
    person_ids: Union[Unset, List[str]] = UNSET,
    person_types: Union[Unset, List[str]] = UNSET,
    studios: Union[Unset, List[str]] = UNSET,
    artists: Union[Unset, List[str]] = UNSET,
    exclude_artist_ids: Union[Unset, List[str]] = UNSET,
    artist_ids: Union[Unset, List[str]] = UNSET,
    album_artist_ids: Union[Unset, List[str]] = UNSET,
    contributing_artist_ids: Union[Unset, List[str]] = UNSET,
    albums: Union[Unset, List[str]] = UNSET,
    album_ids: Union[Unset, List[str]] = UNSET,
    ids: Union[Unset, List[str]] = UNSET,
    video_types: Union[Unset, List[VideoType]] = UNSET,
    min_official_rating: Union[Unset, str] = UNSET,
    is_locked: Union[Unset, bool] = UNSET,
    is_place_holder: Union[Unset, bool] = UNSET,
    has_official_rating: Union[Unset, bool] = UNSET,
    collapse_box_set_items: Union[Unset, bool] = UNSET,
    min_width: Union[Unset, int] = UNSET,
    min_height: Union[Unset, int] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    is_3d: Union[Unset, bool] = UNSET,
    series_status: Union[Unset, List[SeriesStatus]] = UNSET,
    name_starts_with_or_greater: Union[Unset, str] = UNSET,
    name_starts_with: Union[Unset, str] = UNSET,
    name_less_than: Union[Unset, str] = UNSET,
    studio_ids: Union[Unset, List[str]] = UNSET,
    genre_ids: Union[Unset, List[str]] = UNSET,
    enable_total_record_count: Union[Unset, bool] = True,
    enable_images: Union[Unset, bool] = True,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["userId"] = user_id

    params["maxOfficialRating"] = max_official_rating

    params["hasThemeSong"] = has_theme_song

    params["hasThemeVideo"] = has_theme_video

    params["hasSubtitles"] = has_subtitles

    params["hasSpecialFeature"] = has_special_feature

    params["hasTrailer"] = has_trailer

    params["adjacentTo"] = adjacent_to

    params["parentIndexNumber"] = parent_index_number

    params["hasParentalRating"] = has_parental_rating

    params["isHd"] = is_hd

    params["is4K"] = is_4k

    json_location_types: Union[Unset, List[str]] = UNSET
    if not isinstance(location_types, Unset):
        json_location_types = []
        for location_types_item_data in location_types:
            location_types_item = location_types_item_data.value
            json_location_types.append(location_types_item)

    params["locationTypes"] = json_location_types

    json_exclude_location_types: Union[Unset, List[str]] = UNSET
    if not isinstance(exclude_location_types, Unset):
        json_exclude_location_types = []
        for exclude_location_types_item_data in exclude_location_types:
            exclude_location_types_item = exclude_location_types_item_data.value
            json_exclude_location_types.append(exclude_location_types_item)

    params["excludeLocationTypes"] = json_exclude_location_types

    params["isMissing"] = is_missing

    params["isUnaired"] = is_unaired

    params["minCommunityRating"] = min_community_rating

    params["minCriticRating"] = min_critic_rating

    json_min_premiere_date: Union[Unset, str] = UNSET
    if not isinstance(min_premiere_date, Unset):
        json_min_premiere_date = min_premiere_date.isoformat()
    params["minPremiereDate"] = json_min_premiere_date

    json_min_date_last_saved: Union[Unset, str] = UNSET
    if not isinstance(min_date_last_saved, Unset):
        json_min_date_last_saved = min_date_last_saved.isoformat()
    params["minDateLastSaved"] = json_min_date_last_saved

    json_min_date_last_saved_for_user: Union[Unset, str] = UNSET
    if not isinstance(min_date_last_saved_for_user, Unset):
        json_min_date_last_saved_for_user = min_date_last_saved_for_user.isoformat()
    params["minDateLastSavedForUser"] = json_min_date_last_saved_for_user

    json_max_premiere_date: Union[Unset, str] = UNSET
    if not isinstance(max_premiere_date, Unset):
        json_max_premiere_date = max_premiere_date.isoformat()
    params["maxPremiereDate"] = json_max_premiere_date

    params["hasOverview"] = has_overview

    params["hasImdbId"] = has_imdb_id

    params["hasTmdbId"] = has_tmdb_id

    params["hasTvdbId"] = has_tvdb_id

    params["isMovie"] = is_movie

    params["isSeries"] = is_series

    params["isNews"] = is_news

    params["isKids"] = is_kids

    params["isSports"] = is_sports

    json_exclude_item_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(exclude_item_ids, Unset):
        json_exclude_item_ids = exclude_item_ids

    params["excludeItemIds"] = json_exclude_item_ids

    params["startIndex"] = start_index

    params["limit"] = limit

    params["recursive"] = recursive

    params["searchTerm"] = search_term

    json_sort_order: Union[Unset, List[str]] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = []
        for sort_order_item_data in sort_order:
            sort_order_item = sort_order_item_data.value
            json_sort_order.append(sort_order_item)

    params["sortOrder"] = json_sort_order

    params["parentId"] = parent_id

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    json_exclude_item_types: Union[Unset, List[str]] = UNSET
    if not isinstance(exclude_item_types, Unset):
        json_exclude_item_types = []
        for exclude_item_types_item_data in exclude_item_types:
            exclude_item_types_item = exclude_item_types_item_data.value
            json_exclude_item_types.append(exclude_item_types_item)

    params["excludeItemTypes"] = json_exclude_item_types

    json_filters: Union[Unset, List[str]] = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.value
            json_filters.append(filters_item)

    params["filters"] = json_filters

    params["isFavorite"] = is_favorite

    json_media_types: Union[Unset, List[str]] = UNSET
    if not isinstance(media_types, Unset):
        json_media_types = []
        for media_types_item_data in media_types:
            media_types_item = media_types_item_data.value
            json_media_types.append(media_types_item)

    params["mediaTypes"] = json_media_types

    json_image_types: Union[Unset, List[str]] = UNSET
    if not isinstance(image_types, Unset):
        json_image_types = []
        for image_types_item_data in image_types:
            image_types_item = image_types_item_data.value
            json_image_types.append(image_types_item)

    params["imageTypes"] = json_image_types

    json_sort_by: Union[Unset, List[str]] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = []
        for sort_by_item_data in sort_by:
            sort_by_item = sort_by_item_data.value
            json_sort_by.append(sort_by_item)

    params["sortBy"] = json_sort_by

    params["isPlayed"] = is_played

    json_genres: Union[Unset, List[str]] = UNSET
    if not isinstance(genres, Unset):
        json_genres = genres

    params["genres"] = json_genres

    json_official_ratings: Union[Unset, List[str]] = UNSET
    if not isinstance(official_ratings, Unset):
        json_official_ratings = official_ratings

    params["officialRatings"] = json_official_ratings

    json_tags: Union[Unset, List[str]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_years: Union[Unset, List[int]] = UNSET
    if not isinstance(years, Unset):
        json_years = years

    params["years"] = json_years

    params["enableUserData"] = enable_user_data

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: Union[Unset, List[str]] = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params["person"] = person

    json_person_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(person_ids, Unset):
        json_person_ids = person_ids

    params["personIds"] = json_person_ids

    json_person_types: Union[Unset, List[str]] = UNSET
    if not isinstance(person_types, Unset):
        json_person_types = person_types

    params["personTypes"] = json_person_types

    json_studios: Union[Unset, List[str]] = UNSET
    if not isinstance(studios, Unset):
        json_studios = studios

    params["studios"] = json_studios

    json_artists: Union[Unset, List[str]] = UNSET
    if not isinstance(artists, Unset):
        json_artists = artists

    params["artists"] = json_artists

    json_exclude_artist_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(exclude_artist_ids, Unset):
        json_exclude_artist_ids = exclude_artist_ids

    params["excludeArtistIds"] = json_exclude_artist_ids

    json_artist_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(artist_ids, Unset):
        json_artist_ids = artist_ids

    params["artistIds"] = json_artist_ids

    json_album_artist_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(album_artist_ids, Unset):
        json_album_artist_ids = album_artist_ids

    params["albumArtistIds"] = json_album_artist_ids

    json_contributing_artist_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(contributing_artist_ids, Unset):
        json_contributing_artist_ids = contributing_artist_ids

    params["contributingArtistIds"] = json_contributing_artist_ids

    json_albums: Union[Unset, List[str]] = UNSET
    if not isinstance(albums, Unset):
        json_albums = albums

    params["albums"] = json_albums

    json_album_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(album_ids, Unset):
        json_album_ids = album_ids

    params["albumIds"] = json_album_ids

    json_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids"] = json_ids

    json_video_types: Union[Unset, List[str]] = UNSET
    if not isinstance(video_types, Unset):
        json_video_types = []
        for video_types_item_data in video_types:
            video_types_item = video_types_item_data.value
            json_video_types.append(video_types_item)

    params["videoTypes"] = json_video_types

    params["minOfficialRating"] = min_official_rating

    params["isLocked"] = is_locked

    params["isPlaceHolder"] = is_place_holder

    params["hasOfficialRating"] = has_official_rating

    params["collapseBoxSetItems"] = collapse_box_set_items

    params["minWidth"] = min_width

    params["minHeight"] = min_height

    params["maxWidth"] = max_width

    params["maxHeight"] = max_height

    params["is3D"] = is_3d

    json_series_status: Union[Unset, List[str]] = UNSET
    if not isinstance(series_status, Unset):
        json_series_status = []
        for series_status_item_data in series_status:
            series_status_item = series_status_item_data.value
            json_series_status.append(series_status_item)

    params["seriesStatus"] = json_series_status

    params["nameStartsWithOrGreater"] = name_starts_with_or_greater

    params["nameStartsWith"] = name_starts_with

    params["nameLessThan"] = name_less_than

    json_studio_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(studio_ids, Unset):
        json_studio_ids = studio_ids

    params["studioIds"] = json_studio_ids

    json_genre_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(genre_ids, Unset):
        json_genre_ids = genre_ids

    params["genreIds"] = json_genre_ids

    params["enableTotalRecordCount"] = enable_total_record_count

    params["enableImages"] = enable_images

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/Trailers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    max_official_rating: Union[Unset, str] = UNSET,
    has_theme_song: Union[Unset, bool] = UNSET,
    has_theme_video: Union[Unset, bool] = UNSET,
    has_subtitles: Union[Unset, bool] = UNSET,
    has_special_feature: Union[Unset, bool] = UNSET,
    has_trailer: Union[Unset, bool] = UNSET,
    adjacent_to: Union[Unset, str] = UNSET,
    parent_index_number: Union[Unset, int] = UNSET,
    has_parental_rating: Union[Unset, bool] = UNSET,
    is_hd: Union[Unset, bool] = UNSET,
    is_4k: Union[Unset, bool] = UNSET,
    location_types: Union[Unset, List[LocationType]] = UNSET,
    exclude_location_types: Union[Unset, List[LocationType]] = UNSET,
    is_missing: Union[Unset, bool] = UNSET,
    is_unaired: Union[Unset, bool] = UNSET,
    min_community_rating: Union[Unset, float] = UNSET,
    min_critic_rating: Union[Unset, float] = UNSET,
    min_premiere_date: Union[Unset, datetime.datetime] = UNSET,
    min_date_last_saved: Union[Unset, datetime.datetime] = UNSET,
    min_date_last_saved_for_user: Union[Unset, datetime.datetime] = UNSET,
    max_premiere_date: Union[Unset, datetime.datetime] = UNSET,
    has_overview: Union[Unset, bool] = UNSET,
    has_imdb_id: Union[Unset, bool] = UNSET,
    has_tmdb_id: Union[Unset, bool] = UNSET,
    has_tvdb_id: Union[Unset, bool] = UNSET,
    is_movie: Union[Unset, bool] = UNSET,
    is_series: Union[Unset, bool] = UNSET,
    is_news: Union[Unset, bool] = UNSET,
    is_kids: Union[Unset, bool] = UNSET,
    is_sports: Union[Unset, bool] = UNSET,
    exclude_item_ids: Union[Unset, List[str]] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, List[SortOrder]] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    media_types: Union[Unset, List[MediaType]] = UNSET,
    image_types: Union[Unset, List[ImageType]] = UNSET,
    sort_by: Union[Unset, List[ItemSortBy]] = UNSET,
    is_played: Union[Unset, bool] = UNSET,
    genres: Union[Unset, List[str]] = UNSET,
    official_ratings: Union[Unset, List[str]] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    years: Union[Unset, List[int]] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    person: Union[Unset, str] = UNSET,
    person_ids: Union[Unset, List[str]] = UNSET,
    person_types: Union[Unset, List[str]] = UNSET,
    studios: Union[Unset, List[str]] = UNSET,
    artists: Union[Unset, List[str]] = UNSET,
    exclude_artist_ids: Union[Unset, List[str]] = UNSET,
    artist_ids: Union[Unset, List[str]] = UNSET,
    album_artist_ids: Union[Unset, List[str]] = UNSET,
    contributing_artist_ids: Union[Unset, List[str]] = UNSET,
    albums: Union[Unset, List[str]] = UNSET,
    album_ids: Union[Unset, List[str]] = UNSET,
    ids: Union[Unset, List[str]] = UNSET,
    video_types: Union[Unset, List[VideoType]] = UNSET,
    min_official_rating: Union[Unset, str] = UNSET,
    is_locked: Union[Unset, bool] = UNSET,
    is_place_holder: Union[Unset, bool] = UNSET,
    has_official_rating: Union[Unset, bool] = UNSET,
    collapse_box_set_items: Union[Unset, bool] = UNSET,
    min_width: Union[Unset, int] = UNSET,
    min_height: Union[Unset, int] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    is_3d: Union[Unset, bool] = UNSET,
    series_status: Union[Unset, List[SeriesStatus]] = UNSET,
    name_starts_with_or_greater: Union[Unset, str] = UNSET,
    name_starts_with: Union[Unset, str] = UNSET,
    name_less_than: Union[Unset, str] = UNSET,
    studio_ids: Union[Unset, List[str]] = UNSET,
    genre_ids: Union[Unset, List[str]] = UNSET,
    enable_total_record_count: Union[Unset, bool] = True,
    enable_images: Union[Unset, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Finds movies and trailers similar to a given trailer.

    Args:
        user_id (Union[Unset, str]):
        max_official_rating (Union[Unset, str]):
        has_theme_song (Union[Unset, bool]):
        has_theme_video (Union[Unset, bool]):
        has_subtitles (Union[Unset, bool]):
        has_special_feature (Union[Unset, bool]):
        has_trailer (Union[Unset, bool]):
        adjacent_to (Union[Unset, str]):
        parent_index_number (Union[Unset, int]):
        has_parental_rating (Union[Unset, bool]):
        is_hd (Union[Unset, bool]):
        is_4k (Union[Unset, bool]):
        location_types (Union[Unset, List[LocationType]]):
        exclude_location_types (Union[Unset, List[LocationType]]):
        is_missing (Union[Unset, bool]):
        is_unaired (Union[Unset, bool]):
        min_community_rating (Union[Unset, float]):
        min_critic_rating (Union[Unset, float]):
        min_premiere_date (Union[Unset, datetime.datetime]):
        min_date_last_saved (Union[Unset, datetime.datetime]):
        min_date_last_saved_for_user (Union[Unset, datetime.datetime]):
        max_premiere_date (Union[Unset, datetime.datetime]):
        has_overview (Union[Unset, bool]):
        has_imdb_id (Union[Unset, bool]):
        has_tmdb_id (Union[Unset, bool]):
        has_tvdb_id (Union[Unset, bool]):
        is_movie (Union[Unset, bool]):
        is_series (Union[Unset, bool]):
        is_news (Union[Unset, bool]):
        is_kids (Union[Unset, bool]):
        is_sports (Union[Unset, bool]):
        exclude_item_ids (Union[Unset, List[str]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        recursive (Union[Unset, bool]):
        search_term (Union[Unset, str]):
        sort_order (Union[Unset, List[SortOrder]]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        exclude_item_types (Union[Unset, List[BaseItemKind]]):
        filters (Union[Unset, List[ItemFilter]]):
        is_favorite (Union[Unset, bool]):
        media_types (Union[Unset, List[MediaType]]):
        image_types (Union[Unset, List[ImageType]]):
        sort_by (Union[Unset, List[ItemSortBy]]):
        is_played (Union[Unset, bool]):
        genres (Union[Unset, List[str]]):
        official_ratings (Union[Unset, List[str]]):
        tags (Union[Unset, List[str]]):
        years (Union[Unset, List[int]]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        person (Union[Unset, str]):
        person_ids (Union[Unset, List[str]]):
        person_types (Union[Unset, List[str]]):
        studios (Union[Unset, List[str]]):
        artists (Union[Unset, List[str]]):
        exclude_artist_ids (Union[Unset, List[str]]):
        artist_ids (Union[Unset, List[str]]):
        album_artist_ids (Union[Unset, List[str]]):
        contributing_artist_ids (Union[Unset, List[str]]):
        albums (Union[Unset, List[str]]):
        album_ids (Union[Unset, List[str]]):
        ids (Union[Unset, List[str]]):
        video_types (Union[Unset, List[VideoType]]):
        min_official_rating (Union[Unset, str]):
        is_locked (Union[Unset, bool]):
        is_place_holder (Union[Unset, bool]):
        has_official_rating (Union[Unset, bool]):
        collapse_box_set_items (Union[Unset, bool]):
        min_width (Union[Unset, int]):
        min_height (Union[Unset, int]):
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        is_3d (Union[Unset, bool]):
        series_status (Union[Unset, List[SeriesStatus]]):
        name_starts_with_or_greater (Union[Unset, str]):
        name_starts_with (Union[Unset, str]):
        name_less_than (Union[Unset, str]):
        studio_ids (Union[Unset, List[str]]):
        genre_ids (Union[Unset, List[str]]):
        enable_total_record_count (Union[Unset, bool]):  Default: True.
        enable_images (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_official_rating=max_official_rating,
        has_theme_song=has_theme_song,
        has_theme_video=has_theme_video,
        has_subtitles=has_subtitles,
        has_special_feature=has_special_feature,
        has_trailer=has_trailer,
        adjacent_to=adjacent_to,
        parent_index_number=parent_index_number,
        has_parental_rating=has_parental_rating,
        is_hd=is_hd,
        is_4k=is_4k,
        location_types=location_types,
        exclude_location_types=exclude_location_types,
        is_missing=is_missing,
        is_unaired=is_unaired,
        min_community_rating=min_community_rating,
        min_critic_rating=min_critic_rating,
        min_premiere_date=min_premiere_date,
        min_date_last_saved=min_date_last_saved,
        min_date_last_saved_for_user=min_date_last_saved_for_user,
        max_premiere_date=max_premiere_date,
        has_overview=has_overview,
        has_imdb_id=has_imdb_id,
        has_tmdb_id=has_tmdb_id,
        has_tvdb_id=has_tvdb_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        exclude_item_ids=exclude_item_ids,
        start_index=start_index,
        limit=limit,
        recursive=recursive,
        search_term=search_term,
        sort_order=sort_order,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        image_types=image_types,
        sort_by=sort_by,
        is_played=is_played,
        genres=genres,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        artists=artists,
        exclude_artist_ids=exclude_artist_ids,
        artist_ids=artist_ids,
        album_artist_ids=album_artist_ids,
        contributing_artist_ids=contributing_artist_ids,
        albums=albums,
        album_ids=album_ids,
        ids=ids,
        video_types=video_types,
        min_official_rating=min_official_rating,
        is_locked=is_locked,
        is_place_holder=is_place_holder,
        has_official_rating=has_official_rating,
        collapse_box_set_items=collapse_box_set_items,
        min_width=min_width,
        min_height=min_height,
        max_width=max_width,
        max_height=max_height,
        is_3d=is_3d,
        series_status=series_status,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        studio_ids=studio_ids,
        genre_ids=genre_ids,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    max_official_rating: Union[Unset, str] = UNSET,
    has_theme_song: Union[Unset, bool] = UNSET,
    has_theme_video: Union[Unset, bool] = UNSET,
    has_subtitles: Union[Unset, bool] = UNSET,
    has_special_feature: Union[Unset, bool] = UNSET,
    has_trailer: Union[Unset, bool] = UNSET,
    adjacent_to: Union[Unset, str] = UNSET,
    parent_index_number: Union[Unset, int] = UNSET,
    has_parental_rating: Union[Unset, bool] = UNSET,
    is_hd: Union[Unset, bool] = UNSET,
    is_4k: Union[Unset, bool] = UNSET,
    location_types: Union[Unset, List[LocationType]] = UNSET,
    exclude_location_types: Union[Unset, List[LocationType]] = UNSET,
    is_missing: Union[Unset, bool] = UNSET,
    is_unaired: Union[Unset, bool] = UNSET,
    min_community_rating: Union[Unset, float] = UNSET,
    min_critic_rating: Union[Unset, float] = UNSET,
    min_premiere_date: Union[Unset, datetime.datetime] = UNSET,
    min_date_last_saved: Union[Unset, datetime.datetime] = UNSET,
    min_date_last_saved_for_user: Union[Unset, datetime.datetime] = UNSET,
    max_premiere_date: Union[Unset, datetime.datetime] = UNSET,
    has_overview: Union[Unset, bool] = UNSET,
    has_imdb_id: Union[Unset, bool] = UNSET,
    has_tmdb_id: Union[Unset, bool] = UNSET,
    has_tvdb_id: Union[Unset, bool] = UNSET,
    is_movie: Union[Unset, bool] = UNSET,
    is_series: Union[Unset, bool] = UNSET,
    is_news: Union[Unset, bool] = UNSET,
    is_kids: Union[Unset, bool] = UNSET,
    is_sports: Union[Unset, bool] = UNSET,
    exclude_item_ids: Union[Unset, List[str]] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, List[SortOrder]] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    media_types: Union[Unset, List[MediaType]] = UNSET,
    image_types: Union[Unset, List[ImageType]] = UNSET,
    sort_by: Union[Unset, List[ItemSortBy]] = UNSET,
    is_played: Union[Unset, bool] = UNSET,
    genres: Union[Unset, List[str]] = UNSET,
    official_ratings: Union[Unset, List[str]] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    years: Union[Unset, List[int]] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    person: Union[Unset, str] = UNSET,
    person_ids: Union[Unset, List[str]] = UNSET,
    person_types: Union[Unset, List[str]] = UNSET,
    studios: Union[Unset, List[str]] = UNSET,
    artists: Union[Unset, List[str]] = UNSET,
    exclude_artist_ids: Union[Unset, List[str]] = UNSET,
    artist_ids: Union[Unset, List[str]] = UNSET,
    album_artist_ids: Union[Unset, List[str]] = UNSET,
    contributing_artist_ids: Union[Unset, List[str]] = UNSET,
    albums: Union[Unset, List[str]] = UNSET,
    album_ids: Union[Unset, List[str]] = UNSET,
    ids: Union[Unset, List[str]] = UNSET,
    video_types: Union[Unset, List[VideoType]] = UNSET,
    min_official_rating: Union[Unset, str] = UNSET,
    is_locked: Union[Unset, bool] = UNSET,
    is_place_holder: Union[Unset, bool] = UNSET,
    has_official_rating: Union[Unset, bool] = UNSET,
    collapse_box_set_items: Union[Unset, bool] = UNSET,
    min_width: Union[Unset, int] = UNSET,
    min_height: Union[Unset, int] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    is_3d: Union[Unset, bool] = UNSET,
    series_status: Union[Unset, List[SeriesStatus]] = UNSET,
    name_starts_with_or_greater: Union[Unset, str] = UNSET,
    name_starts_with: Union[Unset, str] = UNSET,
    name_less_than: Union[Unset, str] = UNSET,
    studio_ids: Union[Unset, List[str]] = UNSET,
    genre_ids: Union[Unset, List[str]] = UNSET,
    enable_total_record_count: Union[Unset, bool] = True,
    enable_images: Union[Unset, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Finds movies and trailers similar to a given trailer.

    Args:
        user_id (Union[Unset, str]):
        max_official_rating (Union[Unset, str]):
        has_theme_song (Union[Unset, bool]):
        has_theme_video (Union[Unset, bool]):
        has_subtitles (Union[Unset, bool]):
        has_special_feature (Union[Unset, bool]):
        has_trailer (Union[Unset, bool]):
        adjacent_to (Union[Unset, str]):
        parent_index_number (Union[Unset, int]):
        has_parental_rating (Union[Unset, bool]):
        is_hd (Union[Unset, bool]):
        is_4k (Union[Unset, bool]):
        location_types (Union[Unset, List[LocationType]]):
        exclude_location_types (Union[Unset, List[LocationType]]):
        is_missing (Union[Unset, bool]):
        is_unaired (Union[Unset, bool]):
        min_community_rating (Union[Unset, float]):
        min_critic_rating (Union[Unset, float]):
        min_premiere_date (Union[Unset, datetime.datetime]):
        min_date_last_saved (Union[Unset, datetime.datetime]):
        min_date_last_saved_for_user (Union[Unset, datetime.datetime]):
        max_premiere_date (Union[Unset, datetime.datetime]):
        has_overview (Union[Unset, bool]):
        has_imdb_id (Union[Unset, bool]):
        has_tmdb_id (Union[Unset, bool]):
        has_tvdb_id (Union[Unset, bool]):
        is_movie (Union[Unset, bool]):
        is_series (Union[Unset, bool]):
        is_news (Union[Unset, bool]):
        is_kids (Union[Unset, bool]):
        is_sports (Union[Unset, bool]):
        exclude_item_ids (Union[Unset, List[str]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        recursive (Union[Unset, bool]):
        search_term (Union[Unset, str]):
        sort_order (Union[Unset, List[SortOrder]]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        exclude_item_types (Union[Unset, List[BaseItemKind]]):
        filters (Union[Unset, List[ItemFilter]]):
        is_favorite (Union[Unset, bool]):
        media_types (Union[Unset, List[MediaType]]):
        image_types (Union[Unset, List[ImageType]]):
        sort_by (Union[Unset, List[ItemSortBy]]):
        is_played (Union[Unset, bool]):
        genres (Union[Unset, List[str]]):
        official_ratings (Union[Unset, List[str]]):
        tags (Union[Unset, List[str]]):
        years (Union[Unset, List[int]]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        person (Union[Unset, str]):
        person_ids (Union[Unset, List[str]]):
        person_types (Union[Unset, List[str]]):
        studios (Union[Unset, List[str]]):
        artists (Union[Unset, List[str]]):
        exclude_artist_ids (Union[Unset, List[str]]):
        artist_ids (Union[Unset, List[str]]):
        album_artist_ids (Union[Unset, List[str]]):
        contributing_artist_ids (Union[Unset, List[str]]):
        albums (Union[Unset, List[str]]):
        album_ids (Union[Unset, List[str]]):
        ids (Union[Unset, List[str]]):
        video_types (Union[Unset, List[VideoType]]):
        min_official_rating (Union[Unset, str]):
        is_locked (Union[Unset, bool]):
        is_place_holder (Union[Unset, bool]):
        has_official_rating (Union[Unset, bool]):
        collapse_box_set_items (Union[Unset, bool]):
        min_width (Union[Unset, int]):
        min_height (Union[Unset, int]):
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        is_3d (Union[Unset, bool]):
        series_status (Union[Unset, List[SeriesStatus]]):
        name_starts_with_or_greater (Union[Unset, str]):
        name_starts_with (Union[Unset, str]):
        name_less_than (Union[Unset, str]):
        studio_ids (Union[Unset, List[str]]):
        genre_ids (Union[Unset, List[str]]):
        enable_total_record_count (Union[Unset, bool]):  Default: True.
        enable_images (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        max_official_rating=max_official_rating,
        has_theme_song=has_theme_song,
        has_theme_video=has_theme_video,
        has_subtitles=has_subtitles,
        has_special_feature=has_special_feature,
        has_trailer=has_trailer,
        adjacent_to=adjacent_to,
        parent_index_number=parent_index_number,
        has_parental_rating=has_parental_rating,
        is_hd=is_hd,
        is_4k=is_4k,
        location_types=location_types,
        exclude_location_types=exclude_location_types,
        is_missing=is_missing,
        is_unaired=is_unaired,
        min_community_rating=min_community_rating,
        min_critic_rating=min_critic_rating,
        min_premiere_date=min_premiere_date,
        min_date_last_saved=min_date_last_saved,
        min_date_last_saved_for_user=min_date_last_saved_for_user,
        max_premiere_date=max_premiere_date,
        has_overview=has_overview,
        has_imdb_id=has_imdb_id,
        has_tmdb_id=has_tmdb_id,
        has_tvdb_id=has_tvdb_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        exclude_item_ids=exclude_item_ids,
        start_index=start_index,
        limit=limit,
        recursive=recursive,
        search_term=search_term,
        sort_order=sort_order,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        image_types=image_types,
        sort_by=sort_by,
        is_played=is_played,
        genres=genres,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        artists=artists,
        exclude_artist_ids=exclude_artist_ids,
        artist_ids=artist_ids,
        album_artist_ids=album_artist_ids,
        contributing_artist_ids=contributing_artist_ids,
        albums=albums,
        album_ids=album_ids,
        ids=ids,
        video_types=video_types,
        min_official_rating=min_official_rating,
        is_locked=is_locked,
        is_place_holder=is_place_holder,
        has_official_rating=has_official_rating,
        collapse_box_set_items=collapse_box_set_items,
        min_width=min_width,
        min_height=min_height,
        max_width=max_width,
        max_height=max_height,
        is_3d=is_3d,
        series_status=series_status,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        studio_ids=studio_ids,
        genre_ids=genre_ids,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    max_official_rating: Union[Unset, str] = UNSET,
    has_theme_song: Union[Unset, bool] = UNSET,
    has_theme_video: Union[Unset, bool] = UNSET,
    has_subtitles: Union[Unset, bool] = UNSET,
    has_special_feature: Union[Unset, bool] = UNSET,
    has_trailer: Union[Unset, bool] = UNSET,
    adjacent_to: Union[Unset, str] = UNSET,
    parent_index_number: Union[Unset, int] = UNSET,
    has_parental_rating: Union[Unset, bool] = UNSET,
    is_hd: Union[Unset, bool] = UNSET,
    is_4k: Union[Unset, bool] = UNSET,
    location_types: Union[Unset, List[LocationType]] = UNSET,
    exclude_location_types: Union[Unset, List[LocationType]] = UNSET,
    is_missing: Union[Unset, bool] = UNSET,
    is_unaired: Union[Unset, bool] = UNSET,
    min_community_rating: Union[Unset, float] = UNSET,
    min_critic_rating: Union[Unset, float] = UNSET,
    min_premiere_date: Union[Unset, datetime.datetime] = UNSET,
    min_date_last_saved: Union[Unset, datetime.datetime] = UNSET,
    min_date_last_saved_for_user: Union[Unset, datetime.datetime] = UNSET,
    max_premiere_date: Union[Unset, datetime.datetime] = UNSET,
    has_overview: Union[Unset, bool] = UNSET,
    has_imdb_id: Union[Unset, bool] = UNSET,
    has_tmdb_id: Union[Unset, bool] = UNSET,
    has_tvdb_id: Union[Unset, bool] = UNSET,
    is_movie: Union[Unset, bool] = UNSET,
    is_series: Union[Unset, bool] = UNSET,
    is_news: Union[Unset, bool] = UNSET,
    is_kids: Union[Unset, bool] = UNSET,
    is_sports: Union[Unset, bool] = UNSET,
    exclude_item_ids: Union[Unset, List[str]] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, List[SortOrder]] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    media_types: Union[Unset, List[MediaType]] = UNSET,
    image_types: Union[Unset, List[ImageType]] = UNSET,
    sort_by: Union[Unset, List[ItemSortBy]] = UNSET,
    is_played: Union[Unset, bool] = UNSET,
    genres: Union[Unset, List[str]] = UNSET,
    official_ratings: Union[Unset, List[str]] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    years: Union[Unset, List[int]] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    person: Union[Unset, str] = UNSET,
    person_ids: Union[Unset, List[str]] = UNSET,
    person_types: Union[Unset, List[str]] = UNSET,
    studios: Union[Unset, List[str]] = UNSET,
    artists: Union[Unset, List[str]] = UNSET,
    exclude_artist_ids: Union[Unset, List[str]] = UNSET,
    artist_ids: Union[Unset, List[str]] = UNSET,
    album_artist_ids: Union[Unset, List[str]] = UNSET,
    contributing_artist_ids: Union[Unset, List[str]] = UNSET,
    albums: Union[Unset, List[str]] = UNSET,
    album_ids: Union[Unset, List[str]] = UNSET,
    ids: Union[Unset, List[str]] = UNSET,
    video_types: Union[Unset, List[VideoType]] = UNSET,
    min_official_rating: Union[Unset, str] = UNSET,
    is_locked: Union[Unset, bool] = UNSET,
    is_place_holder: Union[Unset, bool] = UNSET,
    has_official_rating: Union[Unset, bool] = UNSET,
    collapse_box_set_items: Union[Unset, bool] = UNSET,
    min_width: Union[Unset, int] = UNSET,
    min_height: Union[Unset, int] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    is_3d: Union[Unset, bool] = UNSET,
    series_status: Union[Unset, List[SeriesStatus]] = UNSET,
    name_starts_with_or_greater: Union[Unset, str] = UNSET,
    name_starts_with: Union[Unset, str] = UNSET,
    name_less_than: Union[Unset, str] = UNSET,
    studio_ids: Union[Unset, List[str]] = UNSET,
    genre_ids: Union[Unset, List[str]] = UNSET,
    enable_total_record_count: Union[Unset, bool] = True,
    enable_images: Union[Unset, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Finds movies and trailers similar to a given trailer.

    Args:
        user_id (Union[Unset, str]):
        max_official_rating (Union[Unset, str]):
        has_theme_song (Union[Unset, bool]):
        has_theme_video (Union[Unset, bool]):
        has_subtitles (Union[Unset, bool]):
        has_special_feature (Union[Unset, bool]):
        has_trailer (Union[Unset, bool]):
        adjacent_to (Union[Unset, str]):
        parent_index_number (Union[Unset, int]):
        has_parental_rating (Union[Unset, bool]):
        is_hd (Union[Unset, bool]):
        is_4k (Union[Unset, bool]):
        location_types (Union[Unset, List[LocationType]]):
        exclude_location_types (Union[Unset, List[LocationType]]):
        is_missing (Union[Unset, bool]):
        is_unaired (Union[Unset, bool]):
        min_community_rating (Union[Unset, float]):
        min_critic_rating (Union[Unset, float]):
        min_premiere_date (Union[Unset, datetime.datetime]):
        min_date_last_saved (Union[Unset, datetime.datetime]):
        min_date_last_saved_for_user (Union[Unset, datetime.datetime]):
        max_premiere_date (Union[Unset, datetime.datetime]):
        has_overview (Union[Unset, bool]):
        has_imdb_id (Union[Unset, bool]):
        has_tmdb_id (Union[Unset, bool]):
        has_tvdb_id (Union[Unset, bool]):
        is_movie (Union[Unset, bool]):
        is_series (Union[Unset, bool]):
        is_news (Union[Unset, bool]):
        is_kids (Union[Unset, bool]):
        is_sports (Union[Unset, bool]):
        exclude_item_ids (Union[Unset, List[str]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        recursive (Union[Unset, bool]):
        search_term (Union[Unset, str]):
        sort_order (Union[Unset, List[SortOrder]]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        exclude_item_types (Union[Unset, List[BaseItemKind]]):
        filters (Union[Unset, List[ItemFilter]]):
        is_favorite (Union[Unset, bool]):
        media_types (Union[Unset, List[MediaType]]):
        image_types (Union[Unset, List[ImageType]]):
        sort_by (Union[Unset, List[ItemSortBy]]):
        is_played (Union[Unset, bool]):
        genres (Union[Unset, List[str]]):
        official_ratings (Union[Unset, List[str]]):
        tags (Union[Unset, List[str]]):
        years (Union[Unset, List[int]]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        person (Union[Unset, str]):
        person_ids (Union[Unset, List[str]]):
        person_types (Union[Unset, List[str]]):
        studios (Union[Unset, List[str]]):
        artists (Union[Unset, List[str]]):
        exclude_artist_ids (Union[Unset, List[str]]):
        artist_ids (Union[Unset, List[str]]):
        album_artist_ids (Union[Unset, List[str]]):
        contributing_artist_ids (Union[Unset, List[str]]):
        albums (Union[Unset, List[str]]):
        album_ids (Union[Unset, List[str]]):
        ids (Union[Unset, List[str]]):
        video_types (Union[Unset, List[VideoType]]):
        min_official_rating (Union[Unset, str]):
        is_locked (Union[Unset, bool]):
        is_place_holder (Union[Unset, bool]):
        has_official_rating (Union[Unset, bool]):
        collapse_box_set_items (Union[Unset, bool]):
        min_width (Union[Unset, int]):
        min_height (Union[Unset, int]):
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        is_3d (Union[Unset, bool]):
        series_status (Union[Unset, List[SeriesStatus]]):
        name_starts_with_or_greater (Union[Unset, str]):
        name_starts_with (Union[Unset, str]):
        name_less_than (Union[Unset, str]):
        studio_ids (Union[Unset, List[str]]):
        genre_ids (Union[Unset, List[str]]):
        enable_total_record_count (Union[Unset, bool]):  Default: True.
        enable_images (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_official_rating=max_official_rating,
        has_theme_song=has_theme_song,
        has_theme_video=has_theme_video,
        has_subtitles=has_subtitles,
        has_special_feature=has_special_feature,
        has_trailer=has_trailer,
        adjacent_to=adjacent_to,
        parent_index_number=parent_index_number,
        has_parental_rating=has_parental_rating,
        is_hd=is_hd,
        is_4k=is_4k,
        location_types=location_types,
        exclude_location_types=exclude_location_types,
        is_missing=is_missing,
        is_unaired=is_unaired,
        min_community_rating=min_community_rating,
        min_critic_rating=min_critic_rating,
        min_premiere_date=min_premiere_date,
        min_date_last_saved=min_date_last_saved,
        min_date_last_saved_for_user=min_date_last_saved_for_user,
        max_premiere_date=max_premiere_date,
        has_overview=has_overview,
        has_imdb_id=has_imdb_id,
        has_tmdb_id=has_tmdb_id,
        has_tvdb_id=has_tvdb_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        exclude_item_ids=exclude_item_ids,
        start_index=start_index,
        limit=limit,
        recursive=recursive,
        search_term=search_term,
        sort_order=sort_order,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        image_types=image_types,
        sort_by=sort_by,
        is_played=is_played,
        genres=genres,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        artists=artists,
        exclude_artist_ids=exclude_artist_ids,
        artist_ids=artist_ids,
        album_artist_ids=album_artist_ids,
        contributing_artist_ids=contributing_artist_ids,
        albums=albums,
        album_ids=album_ids,
        ids=ids,
        video_types=video_types,
        min_official_rating=min_official_rating,
        is_locked=is_locked,
        is_place_holder=is_place_holder,
        has_official_rating=has_official_rating,
        collapse_box_set_items=collapse_box_set_items,
        min_width=min_width,
        min_height=min_height,
        max_width=max_width,
        max_height=max_height,
        is_3d=is_3d,
        series_status=series_status,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        studio_ids=studio_ids,
        genre_ids=genre_ids,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    max_official_rating: Union[Unset, str] = UNSET,
    has_theme_song: Union[Unset, bool] = UNSET,
    has_theme_video: Union[Unset, bool] = UNSET,
    has_subtitles: Union[Unset, bool] = UNSET,
    has_special_feature: Union[Unset, bool] = UNSET,
    has_trailer: Union[Unset, bool] = UNSET,
    adjacent_to: Union[Unset, str] = UNSET,
    parent_index_number: Union[Unset, int] = UNSET,
    has_parental_rating: Union[Unset, bool] = UNSET,
    is_hd: Union[Unset, bool] = UNSET,
    is_4k: Union[Unset, bool] = UNSET,
    location_types: Union[Unset, List[LocationType]] = UNSET,
    exclude_location_types: Union[Unset, List[LocationType]] = UNSET,
    is_missing: Union[Unset, bool] = UNSET,
    is_unaired: Union[Unset, bool] = UNSET,
    min_community_rating: Union[Unset, float] = UNSET,
    min_critic_rating: Union[Unset, float] = UNSET,
    min_premiere_date: Union[Unset, datetime.datetime] = UNSET,
    min_date_last_saved: Union[Unset, datetime.datetime] = UNSET,
    min_date_last_saved_for_user: Union[Unset, datetime.datetime] = UNSET,
    max_premiere_date: Union[Unset, datetime.datetime] = UNSET,
    has_overview: Union[Unset, bool] = UNSET,
    has_imdb_id: Union[Unset, bool] = UNSET,
    has_tmdb_id: Union[Unset, bool] = UNSET,
    has_tvdb_id: Union[Unset, bool] = UNSET,
    is_movie: Union[Unset, bool] = UNSET,
    is_series: Union[Unset, bool] = UNSET,
    is_news: Union[Unset, bool] = UNSET,
    is_kids: Union[Unset, bool] = UNSET,
    is_sports: Union[Unset, bool] = UNSET,
    exclude_item_ids: Union[Unset, List[str]] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, List[SortOrder]] = UNSET,
    parent_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    media_types: Union[Unset, List[MediaType]] = UNSET,
    image_types: Union[Unset, List[ImageType]] = UNSET,
    sort_by: Union[Unset, List[ItemSortBy]] = UNSET,
    is_played: Union[Unset, bool] = UNSET,
    genres: Union[Unset, List[str]] = UNSET,
    official_ratings: Union[Unset, List[str]] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    years: Union[Unset, List[int]] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, List[ImageType]] = UNSET,
    person: Union[Unset, str] = UNSET,
    person_ids: Union[Unset, List[str]] = UNSET,
    person_types: Union[Unset, List[str]] = UNSET,
    studios: Union[Unset, List[str]] = UNSET,
    artists: Union[Unset, List[str]] = UNSET,
    exclude_artist_ids: Union[Unset, List[str]] = UNSET,
    artist_ids: Union[Unset, List[str]] = UNSET,
    album_artist_ids: Union[Unset, List[str]] = UNSET,
    contributing_artist_ids: Union[Unset, List[str]] = UNSET,
    albums: Union[Unset, List[str]] = UNSET,
    album_ids: Union[Unset, List[str]] = UNSET,
    ids: Union[Unset, List[str]] = UNSET,
    video_types: Union[Unset, List[VideoType]] = UNSET,
    min_official_rating: Union[Unset, str] = UNSET,
    is_locked: Union[Unset, bool] = UNSET,
    is_place_holder: Union[Unset, bool] = UNSET,
    has_official_rating: Union[Unset, bool] = UNSET,
    collapse_box_set_items: Union[Unset, bool] = UNSET,
    min_width: Union[Unset, int] = UNSET,
    min_height: Union[Unset, int] = UNSET,
    max_width: Union[Unset, int] = UNSET,
    max_height: Union[Unset, int] = UNSET,
    is_3d: Union[Unset, bool] = UNSET,
    series_status: Union[Unset, List[SeriesStatus]] = UNSET,
    name_starts_with_or_greater: Union[Unset, str] = UNSET,
    name_starts_with: Union[Unset, str] = UNSET,
    name_less_than: Union[Unset, str] = UNSET,
    studio_ids: Union[Unset, List[str]] = UNSET,
    genre_ids: Union[Unset, List[str]] = UNSET,
    enable_total_record_count: Union[Unset, bool] = True,
    enable_images: Union[Unset, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Finds movies and trailers similar to a given trailer.

    Args:
        user_id (Union[Unset, str]):
        max_official_rating (Union[Unset, str]):
        has_theme_song (Union[Unset, bool]):
        has_theme_video (Union[Unset, bool]):
        has_subtitles (Union[Unset, bool]):
        has_special_feature (Union[Unset, bool]):
        has_trailer (Union[Unset, bool]):
        adjacent_to (Union[Unset, str]):
        parent_index_number (Union[Unset, int]):
        has_parental_rating (Union[Unset, bool]):
        is_hd (Union[Unset, bool]):
        is_4k (Union[Unset, bool]):
        location_types (Union[Unset, List[LocationType]]):
        exclude_location_types (Union[Unset, List[LocationType]]):
        is_missing (Union[Unset, bool]):
        is_unaired (Union[Unset, bool]):
        min_community_rating (Union[Unset, float]):
        min_critic_rating (Union[Unset, float]):
        min_premiere_date (Union[Unset, datetime.datetime]):
        min_date_last_saved (Union[Unset, datetime.datetime]):
        min_date_last_saved_for_user (Union[Unset, datetime.datetime]):
        max_premiere_date (Union[Unset, datetime.datetime]):
        has_overview (Union[Unset, bool]):
        has_imdb_id (Union[Unset, bool]):
        has_tmdb_id (Union[Unset, bool]):
        has_tvdb_id (Union[Unset, bool]):
        is_movie (Union[Unset, bool]):
        is_series (Union[Unset, bool]):
        is_news (Union[Unset, bool]):
        is_kids (Union[Unset, bool]):
        is_sports (Union[Unset, bool]):
        exclude_item_ids (Union[Unset, List[str]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        recursive (Union[Unset, bool]):
        search_term (Union[Unset, str]):
        sort_order (Union[Unset, List[SortOrder]]):
        parent_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        exclude_item_types (Union[Unset, List[BaseItemKind]]):
        filters (Union[Unset, List[ItemFilter]]):
        is_favorite (Union[Unset, bool]):
        media_types (Union[Unset, List[MediaType]]):
        image_types (Union[Unset, List[ImageType]]):
        sort_by (Union[Unset, List[ItemSortBy]]):
        is_played (Union[Unset, bool]):
        genres (Union[Unset, List[str]]):
        official_ratings (Union[Unset, List[str]]):
        tags (Union[Unset, List[str]]):
        years (Union[Unset, List[int]]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        person (Union[Unset, str]):
        person_ids (Union[Unset, List[str]]):
        person_types (Union[Unset, List[str]]):
        studios (Union[Unset, List[str]]):
        artists (Union[Unset, List[str]]):
        exclude_artist_ids (Union[Unset, List[str]]):
        artist_ids (Union[Unset, List[str]]):
        album_artist_ids (Union[Unset, List[str]]):
        contributing_artist_ids (Union[Unset, List[str]]):
        albums (Union[Unset, List[str]]):
        album_ids (Union[Unset, List[str]]):
        ids (Union[Unset, List[str]]):
        video_types (Union[Unset, List[VideoType]]):
        min_official_rating (Union[Unset, str]):
        is_locked (Union[Unset, bool]):
        is_place_holder (Union[Unset, bool]):
        has_official_rating (Union[Unset, bool]):
        collapse_box_set_items (Union[Unset, bool]):
        min_width (Union[Unset, int]):
        min_height (Union[Unset, int]):
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        is_3d (Union[Unset, bool]):
        series_status (Union[Unset, List[SeriesStatus]]):
        name_starts_with_or_greater (Union[Unset, str]):
        name_starts_with (Union[Unset, str]):
        name_less_than (Union[Unset, str]):
        studio_ids (Union[Unset, List[str]]):
        genre_ids (Union[Unset, List[str]]):
        enable_total_record_count (Union[Unset, bool]):  Default: True.
        enable_images (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            max_official_rating=max_official_rating,
            has_theme_song=has_theme_song,
            has_theme_video=has_theme_video,
            has_subtitles=has_subtitles,
            has_special_feature=has_special_feature,
            has_trailer=has_trailer,
            adjacent_to=adjacent_to,
            parent_index_number=parent_index_number,
            has_parental_rating=has_parental_rating,
            is_hd=is_hd,
            is_4k=is_4k,
            location_types=location_types,
            exclude_location_types=exclude_location_types,
            is_missing=is_missing,
            is_unaired=is_unaired,
            min_community_rating=min_community_rating,
            min_critic_rating=min_critic_rating,
            min_premiere_date=min_premiere_date,
            min_date_last_saved=min_date_last_saved,
            min_date_last_saved_for_user=min_date_last_saved_for_user,
            max_premiere_date=max_premiere_date,
            has_overview=has_overview,
            has_imdb_id=has_imdb_id,
            has_tmdb_id=has_tmdb_id,
            has_tvdb_id=has_tvdb_id,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            exclude_item_ids=exclude_item_ids,
            start_index=start_index,
            limit=limit,
            recursive=recursive,
            search_term=search_term,
            sort_order=sort_order,
            parent_id=parent_id,
            fields=fields,
            exclude_item_types=exclude_item_types,
            filters=filters,
            is_favorite=is_favorite,
            media_types=media_types,
            image_types=image_types,
            sort_by=sort_by,
            is_played=is_played,
            genres=genres,
            official_ratings=official_ratings,
            tags=tags,
            years=years,
            enable_user_data=enable_user_data,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            person=person,
            person_ids=person_ids,
            person_types=person_types,
            studios=studios,
            artists=artists,
            exclude_artist_ids=exclude_artist_ids,
            artist_ids=artist_ids,
            album_artist_ids=album_artist_ids,
            contributing_artist_ids=contributing_artist_ids,
            albums=albums,
            album_ids=album_ids,
            ids=ids,
            video_types=video_types,
            min_official_rating=min_official_rating,
            is_locked=is_locked,
            is_place_holder=is_place_holder,
            has_official_rating=has_official_rating,
            collapse_box_set_items=collapse_box_set_items,
            min_width=min_width,
            min_height=min_height,
            max_width=max_width,
            max_height=max_height,
            is_3d=is_3d,
            series_status=series_status,
            name_starts_with_or_greater=name_starts_with_or_greater,
            name_starts_with=name_starts_with,
            name_less_than=name_less_than,
            studio_ids=studio_ids,
            genre_ids=genre_ids,
            enable_total_record_count=enable_total_record_count,
            enable_images=enable_images,
        )
    ).parsed
