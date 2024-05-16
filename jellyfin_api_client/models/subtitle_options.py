from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, List
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="SubtitleOptions")


@_attrs_define
class SubtitleOptions:
    """
    Attributes:
        skip_if_embedded_subtitles_present (Union[Unset, bool]):
        skip_if_audio_track_matches (Union[Unset, bool]):
        download_languages (Union[List[str], None, Unset]):
        download_movie_subtitles (Union[Unset, bool]):
        download_episode_subtitles (Union[Unset, bool]):
        open_subtitles_username (Union[None, Unset, str]):
        open_subtitles_password_hash (Union[None, Unset, str]):
        is_open_subtitle_vip_account (Union[Unset, bool]):
        require_perfect_match (Union[Unset, bool]):
    """

    skip_if_embedded_subtitles_present: Union[Unset, bool] = UNSET
    skip_if_audio_track_matches: Union[Unset, bool] = UNSET
    download_languages: Union[List[str], None, Unset] = UNSET
    download_movie_subtitles: Union[Unset, bool] = UNSET
    download_episode_subtitles: Union[Unset, bool] = UNSET
    open_subtitles_username: Union[None, Unset, str] = UNSET
    open_subtitles_password_hash: Union[None, Unset, str] = UNSET
    is_open_subtitle_vip_account: Union[Unset, bool] = UNSET
    require_perfect_match: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        skip_if_embedded_subtitles_present = self.skip_if_embedded_subtitles_present

        skip_if_audio_track_matches = self.skip_if_audio_track_matches

        download_languages: Union[List[str], None, Unset]
        if isinstance(self.download_languages, Unset):
            download_languages = UNSET
        elif isinstance(self.download_languages, list):
            download_languages = self.download_languages

        else:
            download_languages = self.download_languages

        download_movie_subtitles = self.download_movie_subtitles

        download_episode_subtitles = self.download_episode_subtitles

        open_subtitles_username: Union[None, Unset, str]
        if isinstance(self.open_subtitles_username, Unset):
            open_subtitles_username = UNSET
        else:
            open_subtitles_username = self.open_subtitles_username

        open_subtitles_password_hash: Union[None, Unset, str]
        if isinstance(self.open_subtitles_password_hash, Unset):
            open_subtitles_password_hash = UNSET
        else:
            open_subtitles_password_hash = self.open_subtitles_password_hash

        is_open_subtitle_vip_account = self.is_open_subtitle_vip_account

        require_perfect_match = self.require_perfect_match

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if skip_if_embedded_subtitles_present is not UNSET:
            field_dict["SkipIfEmbeddedSubtitlesPresent"] = skip_if_embedded_subtitles_present
        if skip_if_audio_track_matches is not UNSET:
            field_dict["SkipIfAudioTrackMatches"] = skip_if_audio_track_matches
        if download_languages is not UNSET:
            field_dict["DownloadLanguages"] = download_languages
        if download_movie_subtitles is not UNSET:
            field_dict["DownloadMovieSubtitles"] = download_movie_subtitles
        if download_episode_subtitles is not UNSET:
            field_dict["DownloadEpisodeSubtitles"] = download_episode_subtitles
        if open_subtitles_username is not UNSET:
            field_dict["OpenSubtitlesUsername"] = open_subtitles_username
        if open_subtitles_password_hash is not UNSET:
            field_dict["OpenSubtitlesPasswordHash"] = open_subtitles_password_hash
        if is_open_subtitle_vip_account is not UNSET:
            field_dict["IsOpenSubtitleVipAccount"] = is_open_subtitle_vip_account
        if require_perfect_match is not UNSET:
            field_dict["RequirePerfectMatch"] = require_perfect_match

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        skip_if_embedded_subtitles_present = d.pop("SkipIfEmbeddedSubtitlesPresent", UNSET)

        skip_if_audio_track_matches = d.pop("SkipIfAudioTrackMatches", UNSET)

        def _parse_download_languages(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                download_languages_type_0 = cast(List[str], data)

                return download_languages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        download_languages = _parse_download_languages(d.pop("DownloadLanguages", UNSET))

        download_movie_subtitles = d.pop("DownloadMovieSubtitles", UNSET)

        download_episode_subtitles = d.pop("DownloadEpisodeSubtitles", UNSET)

        def _parse_open_subtitles_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        open_subtitles_username = _parse_open_subtitles_username(d.pop("OpenSubtitlesUsername", UNSET))

        def _parse_open_subtitles_password_hash(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        open_subtitles_password_hash = _parse_open_subtitles_password_hash(d.pop("OpenSubtitlesPasswordHash", UNSET))

        is_open_subtitle_vip_account = d.pop("IsOpenSubtitleVipAccount", UNSET)

        require_perfect_match = d.pop("RequirePerfectMatch", UNSET)

        subtitle_options = cls(
            skip_if_embedded_subtitles_present=skip_if_embedded_subtitles_present,
            skip_if_audio_track_matches=skip_if_audio_track_matches,
            download_languages=download_languages,
            download_movie_subtitles=download_movie_subtitles,
            download_episode_subtitles=download_episode_subtitles,
            open_subtitles_username=open_subtitles_username,
            open_subtitles_password_hash=open_subtitles_password_hash,
            is_open_subtitle_vip_account=is_open_subtitle_vip_account,
            require_perfect_match=require_perfect_match,
        )

        return subtitle_options
