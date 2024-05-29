from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast
from typing import Union

if TYPE_CHECKING:
    from ..models.theme_media_result import ThemeMediaResult


T = TypeVar("T", bound="AllThemeMediaResult")


@_attrs_define
class AllThemeMediaResult:
    """
    Attributes:
        theme_videos_result (Union['ThemeMediaResult', None, Unset]): Class ThemeMediaResult.
        theme_songs_result (Union['ThemeMediaResult', None, Unset]): Class ThemeMediaResult.
        soundtrack_songs_result (Union['ThemeMediaResult', None, Unset]): Class ThemeMediaResult.
    """

    theme_videos_result: Union["ThemeMediaResult", None, Unset] = UNSET
    theme_songs_result: Union["ThemeMediaResult", None, Unset] = UNSET
    soundtrack_songs_result: Union["ThemeMediaResult", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.theme_media_result import ThemeMediaResult

        theme_videos_result: Union[Dict[str, Any], None, Unset]
        if isinstance(self.theme_videos_result, Unset):
            theme_videos_result = UNSET
        elif isinstance(self.theme_videos_result, ThemeMediaResult):
            theme_videos_result = self.theme_videos_result.to_dict()
        else:
            theme_videos_result = self.theme_videos_result

        theme_songs_result: Union[Dict[str, Any], None, Unset]
        if isinstance(self.theme_songs_result, Unset):
            theme_songs_result = UNSET
        elif isinstance(self.theme_songs_result, ThemeMediaResult):
            theme_songs_result = self.theme_songs_result.to_dict()
        else:
            theme_songs_result = self.theme_songs_result

        soundtrack_songs_result: Union[Dict[str, Any], None, Unset]
        if isinstance(self.soundtrack_songs_result, Unset):
            soundtrack_songs_result = UNSET
        elif isinstance(self.soundtrack_songs_result, ThemeMediaResult):
            soundtrack_songs_result = self.soundtrack_songs_result.to_dict()
        else:
            soundtrack_songs_result = self.soundtrack_songs_result

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if theme_videos_result is not UNSET:
            field_dict["ThemeVideosResult"] = theme_videos_result
        if theme_songs_result is not UNSET:
            field_dict["ThemeSongsResult"] = theme_songs_result
        if soundtrack_songs_result is not UNSET:
            field_dict["SoundtrackSongsResult"] = soundtrack_songs_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.theme_media_result import ThemeMediaResult

        d = src_dict.copy()

        def _parse_theme_videos_result(
            data: object,
        ) -> Union["ThemeMediaResult", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                theme_videos_result_type_1 = ThemeMediaResult.from_dict(data)

                return theme_videos_result_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ThemeMediaResult", None, Unset], data)

        theme_videos_result = _parse_theme_videos_result(
            d.pop("ThemeVideosResult", UNSET)
        )

        def _parse_theme_songs_result(
            data: object,
        ) -> Union["ThemeMediaResult", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                theme_songs_result_type_1 = ThemeMediaResult.from_dict(data)

                return theme_songs_result_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ThemeMediaResult", None, Unset], data)

        theme_songs_result = _parse_theme_songs_result(d.pop("ThemeSongsResult", UNSET))

        def _parse_soundtrack_songs_result(
            data: object,
        ) -> Union["ThemeMediaResult", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                soundtrack_songs_result_type_1 = ThemeMediaResult.from_dict(data)

                return soundtrack_songs_result_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ThemeMediaResult", None, Unset], data)

        soundtrack_songs_result = _parse_soundtrack_songs_result(
            d.pop("SoundtrackSongsResult", UNSET)
        )

        all_theme_media_result = cls(
            theme_videos_result=theme_videos_result,
            theme_songs_result=theme_songs_result,
            soundtrack_songs_result=soundtrack_songs_result,
        )

        return all_theme_media_result
