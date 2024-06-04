from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union
from typing import List

if TYPE_CHECKING:
    from ..models.tuner_host_info import TunerHostInfo
    from ..models.listings_provider_info import ListingsProviderInfo


T = TypeVar("T", bound="LiveTvOptions")


@_attrs_define
class LiveTvOptions:
    """
    Attributes:
        guide_days (Union[None, Unset, int]):
        recording_path (Union[None, Unset, str]):
        movie_recording_path (Union[None, Unset, str]):
        series_recording_path (Union[None, Unset, str]):
        enable_recording_subfolders (Union[Unset, bool]):
        enable_original_audio_with_encoded_recordings (Union[Unset, bool]):
        tuner_hosts (Union[List['TunerHostInfo'], None, Unset]):
        listing_providers (Union[List['ListingsProviderInfo'], None, Unset]):
        pre_padding_seconds (Union[Unset, int]):
        post_padding_seconds (Union[Unset, int]):
        media_locations_created (Union[List[str], None, Unset]):
        recording_post_processor (Union[None, Unset, str]):
        recording_post_processor_arguments (Union[None, Unset, str]):
        save_recording_nfo (Union[Unset, bool]):
        save_recording_images (Union[Unset, bool]):
    """

    guide_days: Union[None, Unset, int] = UNSET
    recording_path: Union[None, Unset, str] = UNSET
    movie_recording_path: Union[None, Unset, str] = UNSET
    series_recording_path: Union[None, Unset, str] = UNSET
    enable_recording_subfolders: Union[Unset, bool] = UNSET
    enable_original_audio_with_encoded_recordings: Union[Unset, bool] = UNSET
    tuner_hosts: Union[List["TunerHostInfo"], None, Unset] = UNSET
    listing_providers: Union[List["ListingsProviderInfo"], None, Unset] = UNSET
    pre_padding_seconds: Union[Unset, int] = UNSET
    post_padding_seconds: Union[Unset, int] = UNSET
    media_locations_created: Union[List[str], None, Unset] = UNSET
    recording_post_processor: Union[None, Unset, str] = UNSET
    recording_post_processor_arguments: Union[None, Unset, str] = UNSET
    save_recording_nfo: Union[Unset, bool] = UNSET
    save_recording_images: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guide_days: Union[None, Unset, int]
        if isinstance(self.guide_days, Unset):
            guide_days = UNSET
        else:
            guide_days = self.guide_days

        recording_path: Union[None, Unset, str]
        if isinstance(self.recording_path, Unset):
            recording_path = UNSET
        else:
            recording_path = self.recording_path

        movie_recording_path: Union[None, Unset, str]
        if isinstance(self.movie_recording_path, Unset):
            movie_recording_path = UNSET
        else:
            movie_recording_path = self.movie_recording_path

        series_recording_path: Union[None, Unset, str]
        if isinstance(self.series_recording_path, Unset):
            series_recording_path = UNSET
        else:
            series_recording_path = self.series_recording_path

        enable_recording_subfolders = self.enable_recording_subfolders

        enable_original_audio_with_encoded_recordings = (
            self.enable_original_audio_with_encoded_recordings
        )

        tuner_hosts: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.tuner_hosts, Unset):
            tuner_hosts = UNSET
        elif isinstance(self.tuner_hosts, list):
            tuner_hosts = []
            for tuner_hosts_type_0_item_data in self.tuner_hosts:
                tuner_hosts_type_0_item = tuner_hosts_type_0_item_data.to_dict()
                tuner_hosts.append(tuner_hosts_type_0_item)

        else:
            tuner_hosts = self.tuner_hosts

        listing_providers: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.listing_providers, Unset):
            listing_providers = UNSET
        elif isinstance(self.listing_providers, list):
            listing_providers = []
            for listing_providers_type_0_item_data in self.listing_providers:
                listing_providers_type_0_item = (
                    listing_providers_type_0_item_data.to_dict()
                )
                listing_providers.append(listing_providers_type_0_item)

        else:
            listing_providers = self.listing_providers

        pre_padding_seconds = self.pre_padding_seconds

        post_padding_seconds = self.post_padding_seconds

        media_locations_created: Union[List[str], None, Unset]
        if isinstance(self.media_locations_created, Unset):
            media_locations_created = UNSET
        elif isinstance(self.media_locations_created, list):
            media_locations_created = self.media_locations_created

        else:
            media_locations_created = self.media_locations_created

        recording_post_processor: Union[None, Unset, str]
        if isinstance(self.recording_post_processor, Unset):
            recording_post_processor = UNSET
        else:
            recording_post_processor = self.recording_post_processor

        recording_post_processor_arguments: Union[None, Unset, str]
        if isinstance(self.recording_post_processor_arguments, Unset):
            recording_post_processor_arguments = UNSET
        else:
            recording_post_processor_arguments = self.recording_post_processor_arguments

        save_recording_nfo = self.save_recording_nfo

        save_recording_images = self.save_recording_images

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guide_days is not UNSET:
            field_dict["GuideDays"] = guide_days
        if recording_path is not UNSET:
            field_dict["RecordingPath"] = recording_path
        if movie_recording_path is not UNSET:
            field_dict["MovieRecordingPath"] = movie_recording_path
        if series_recording_path is not UNSET:
            field_dict["SeriesRecordingPath"] = series_recording_path
        if enable_recording_subfolders is not UNSET:
            field_dict["EnableRecordingSubfolders"] = enable_recording_subfolders
        if enable_original_audio_with_encoded_recordings is not UNSET:
            field_dict["EnableOriginalAudioWithEncodedRecordings"] = (
                enable_original_audio_with_encoded_recordings
            )
        if tuner_hosts is not UNSET:
            field_dict["TunerHosts"] = tuner_hosts
        if listing_providers is not UNSET:
            field_dict["ListingProviders"] = listing_providers
        if pre_padding_seconds is not UNSET:
            field_dict["PrePaddingSeconds"] = pre_padding_seconds
        if post_padding_seconds is not UNSET:
            field_dict["PostPaddingSeconds"] = post_padding_seconds
        if media_locations_created is not UNSET:
            field_dict["MediaLocationsCreated"] = media_locations_created
        if recording_post_processor is not UNSET:
            field_dict["RecordingPostProcessor"] = recording_post_processor
        if recording_post_processor_arguments is not UNSET:
            field_dict["RecordingPostProcessorArguments"] = (
                recording_post_processor_arguments
            )
        if save_recording_nfo is not UNSET:
            field_dict["SaveRecordingNFO"] = save_recording_nfo
        if save_recording_images is not UNSET:
            field_dict["SaveRecordingImages"] = save_recording_images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tuner_host_info import TunerHostInfo
        from ..models.listings_provider_info import ListingsProviderInfo

        d = src_dict.copy()

        def _parse_guide_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        guide_days = _parse_guide_days(d.pop("GuideDays", UNSET))

        def _parse_recording_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recording_path = _parse_recording_path(d.pop("RecordingPath", UNSET))

        def _parse_movie_recording_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        movie_recording_path = _parse_movie_recording_path(
            d.pop("MovieRecordingPath", UNSET)
        )

        def _parse_series_recording_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_recording_path = _parse_series_recording_path(
            d.pop("SeriesRecordingPath", UNSET)
        )

        enable_recording_subfolders = d.pop("EnableRecordingSubfolders", UNSET)

        enable_original_audio_with_encoded_recordings = d.pop(
            "EnableOriginalAudioWithEncodedRecordings", UNSET
        )

        def _parse_tuner_hosts(
            data: object,
        ) -> Union[List["TunerHostInfo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tuner_hosts_type_0 = []
                _tuner_hosts_type_0 = data
                for tuner_hosts_type_0_item_data in _tuner_hosts_type_0:
                    tuner_hosts_type_0_item = TunerHostInfo.from_dict(
                        tuner_hosts_type_0_item_data
                    )

                    tuner_hosts_type_0.append(tuner_hosts_type_0_item)

                return tuner_hosts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["TunerHostInfo"], None, Unset], data)

        tuner_hosts = _parse_tuner_hosts(d.pop("TunerHosts", UNSET))

        def _parse_listing_providers(
            data: object,
        ) -> Union[List["ListingsProviderInfo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                listing_providers_type_0 = []
                _listing_providers_type_0 = data
                for listing_providers_type_0_item_data in _listing_providers_type_0:
                    listing_providers_type_0_item = ListingsProviderInfo.from_dict(
                        listing_providers_type_0_item_data
                    )

                    listing_providers_type_0.append(listing_providers_type_0_item)

                return listing_providers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ListingsProviderInfo"], None, Unset], data)

        listing_providers = _parse_listing_providers(d.pop("ListingProviders", UNSET))

        pre_padding_seconds = d.pop("PrePaddingSeconds", UNSET)

        post_padding_seconds = d.pop("PostPaddingSeconds", UNSET)

        def _parse_media_locations_created(
            data: object,
        ) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_locations_created_type_0 = cast(List[str], data)

                return media_locations_created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        media_locations_created = _parse_media_locations_created(
            d.pop("MediaLocationsCreated", UNSET)
        )

        def _parse_recording_post_processor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recording_post_processor = _parse_recording_post_processor(
            d.pop("RecordingPostProcessor", UNSET)
        )

        def _parse_recording_post_processor_arguments(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recording_post_processor_arguments = _parse_recording_post_processor_arguments(
            d.pop("RecordingPostProcessorArguments", UNSET)
        )

        save_recording_nfo = d.pop("SaveRecordingNFO", UNSET)

        save_recording_images = d.pop("SaveRecordingImages", UNSET)

        live_tv_options = cls(
            guide_days=guide_days,
            recording_path=recording_path,
            movie_recording_path=movie_recording_path,
            series_recording_path=series_recording_path,
            enable_recording_subfolders=enable_recording_subfolders,
            enable_original_audio_with_encoded_recordings=enable_original_audio_with_encoded_recordings,
            tuner_hosts=tuner_hosts,
            listing_providers=listing_providers,
            pre_padding_seconds=pre_padding_seconds,
            post_padding_seconds=post_padding_seconds,
            media_locations_created=media_locations_created,
            recording_post_processor=recording_post_processor,
            recording_post_processor_arguments=recording_post_processor_arguments,
            save_recording_nfo=save_recording_nfo,
            save_recording_images=save_recording_images,
        )

        return live_tv_options
