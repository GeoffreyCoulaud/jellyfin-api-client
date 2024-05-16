from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union
from typing import cast, List
from ..types import UNSET, Unset
from typing import Union
from ..models.down_mix_stereo_algorithms import DownMixStereoAlgorithms


T = TypeVar("T", bound="EncodingOptions")


@_attrs_define
class EncodingOptions:
    """Class EncodingOptions.

    Attributes:
        encoding_thread_count (Union[Unset, int]): Gets or sets the thread count used for encoding.
        transcoding_temp_path (Union[None, Unset, str]): Gets or sets the temporary transcoding path.
        fallback_font_path (Union[None, Unset, str]): Gets or sets the path to the fallback font.
        enable_fallback_font (Union[Unset, bool]): Gets or sets a value indicating whether to use the fallback font.
        enable_audio_vbr (Union[Unset, bool]): Gets or sets a value indicating whether audio VBR is enabled.
        down_mix_audio_boost (Union[Unset, float]): Gets or sets the audio boost applied when downmixing audio.
        down_mix_stereo_algorithm (Union[Unset, DownMixStereoAlgorithms]): An enum representing an algorithm to downmix
            6ch+ to stereo.
            Algorithms sourced from https://superuser.com/questions/852400/properly-downmix-5-1-to-stereo-using-
            ffmpeg/1410620#1410620.
        max_muxing_queue_size (Union[Unset, int]): Gets or sets the maximum size of the muxing queue.
        enable_throttling (Union[Unset, bool]): Gets or sets a value indicating whether throttling is enabled.
        throttle_delay_seconds (Union[Unset, int]): Gets or sets the delay after which throttling happens.
        enable_segment_deletion (Union[Unset, bool]): Gets or sets a value indicating whether segment deletion is
            enabled.
        segment_keep_seconds (Union[Unset, int]): Gets or sets seconds for which segments should be kept before being
            deleted.
        hardware_acceleration_type (Union[None, Unset, str]): Gets or sets the hardware acceleration type.
        encoder_app_path (Union[None, Unset, str]): Gets or sets the FFmpeg path as set by the user via the UI.
        encoder_app_path_display (Union[None, Unset, str]): Gets or sets the current FFmpeg path being used by the
            system and displayed on the transcode page.
        vaapi_device (Union[None, Unset, str]): Gets or sets the VA-API device.
        enable_tonemapping (Union[Unset, bool]): Gets or sets a value indicating whether tonemapping is enabled.
        enable_vpp_tonemapping (Union[Unset, bool]): Gets or sets a value indicating whether VPP tonemapping is enabled.
        enable_video_toolbox_tonemapping (Union[Unset, bool]): Gets or sets a value indicating whether videotoolbox
            tonemapping is enabled.
        tonemapping_algorithm (Union[None, Unset, str]): Gets or sets the tone-mapping algorithm.
        tonemapping_mode (Union[None, Unset, str]): Gets or sets the tone-mapping mode.
        tonemapping_range (Union[None, Unset, str]): Gets or sets the tone-mapping range.
        tonemapping_desat (Union[Unset, float]): Gets or sets the tone-mapping desaturation.
        tonemapping_peak (Union[Unset, float]): Gets or sets the tone-mapping peak.
        tonemapping_param (Union[Unset, float]): Gets or sets the tone-mapping parameters.
        vpp_tonemapping_brightness (Union[Unset, float]): Gets or sets the VPP tone-mapping brightness.
        vpp_tonemapping_contrast (Union[Unset, float]): Gets or sets the VPP tone-mapping contrast.
        h264_crf (Union[Unset, int]): Gets or sets the H264 CRF.
        h265_crf (Union[Unset, int]): Gets or sets the H265 CRF.
        encoder_preset (Union[None, Unset, str]): Gets or sets the encoder preset.
        deinterlace_double_rate (Union[Unset, bool]): Gets or sets a value indicating whether the framerate is doubled
            when deinterlacing.
        deinterlace_method (Union[None, Unset, str]): Gets or sets the deinterlace method.
        enable_decoding_color_depth_10_hevc (Union[Unset, bool]): Gets or sets a value indicating whether 10bit HEVC
            decoding is enabled.
        enable_decoding_color_depth_10_vp_9 (Union[Unset, bool]): Gets or sets a value indicating whether 10bit VP9
            decoding is enabled.
        enable_enhanced_nvdec_decoder (Union[Unset, bool]): Gets or sets a value indicating whether the enhanced NVDEC
            is enabled.
        prefer_system_native_hw_decoder (Union[Unset, bool]): Gets or sets a value indicating whether the system native
            hardware decoder should be used.
        enable_intel_low_power_h264_hw_encoder (Union[Unset, bool]): Gets or sets a value indicating whether the Intel
            H264 low-power hardware encoder should be used.
        enable_intel_low_power_hevc_hw_encoder (Union[Unset, bool]): Gets or sets a value indicating whether the Intel
            HEVC low-power hardware encoder should be used.
        enable_hardware_encoding (Union[Unset, bool]): Gets or sets a value indicating whether hardware encoding is
            enabled.
        allow_hevc_encoding (Union[Unset, bool]): Gets or sets a value indicating whether HEVC encoding is enabled.
        allow_av_1_encoding (Union[Unset, bool]): Gets or sets a value indicating whether AV1 encoding is enabled.
        enable_subtitle_extraction (Union[Unset, bool]): Gets or sets a value indicating whether subtitle extraction is
            enabled.
        hardware_decoding_codecs (Union[List[str], None, Unset]): Gets or sets the codecs hardware encoding is used for.
        allow_on_demand_metadata_based_keyframe_extraction_for_extensions (Union[List[str], None, Unset]): Gets or sets
            the file extensions on-demand metadata based keyframe extraction is enabled for.
    """

    encoding_thread_count: Union[Unset, int] = UNSET
    transcoding_temp_path: Union[None, Unset, str] = UNSET
    fallback_font_path: Union[None, Unset, str] = UNSET
    enable_fallback_font: Union[Unset, bool] = UNSET
    enable_audio_vbr: Union[Unset, bool] = UNSET
    down_mix_audio_boost: Union[Unset, float] = UNSET
    down_mix_stereo_algorithm: Union[Unset, DownMixStereoAlgorithms] = UNSET
    max_muxing_queue_size: Union[Unset, int] = UNSET
    enable_throttling: Union[Unset, bool] = UNSET
    throttle_delay_seconds: Union[Unset, int] = UNSET
    enable_segment_deletion: Union[Unset, bool] = UNSET
    segment_keep_seconds: Union[Unset, int] = UNSET
    hardware_acceleration_type: Union[None, Unset, str] = UNSET
    encoder_app_path: Union[None, Unset, str] = UNSET
    encoder_app_path_display: Union[None, Unset, str] = UNSET
    vaapi_device: Union[None, Unset, str] = UNSET
    enable_tonemapping: Union[Unset, bool] = UNSET
    enable_vpp_tonemapping: Union[Unset, bool] = UNSET
    enable_video_toolbox_tonemapping: Union[Unset, bool] = UNSET
    tonemapping_algorithm: Union[None, Unset, str] = UNSET
    tonemapping_mode: Union[None, Unset, str] = UNSET
    tonemapping_range: Union[None, Unset, str] = UNSET
    tonemapping_desat: Union[Unset, float] = UNSET
    tonemapping_peak: Union[Unset, float] = UNSET
    tonemapping_param: Union[Unset, float] = UNSET
    vpp_tonemapping_brightness: Union[Unset, float] = UNSET
    vpp_tonemapping_contrast: Union[Unset, float] = UNSET
    h264_crf: Union[Unset, int] = UNSET
    h265_crf: Union[Unset, int] = UNSET
    encoder_preset: Union[None, Unset, str] = UNSET
    deinterlace_double_rate: Union[Unset, bool] = UNSET
    deinterlace_method: Union[None, Unset, str] = UNSET
    enable_decoding_color_depth_10_hevc: Union[Unset, bool] = UNSET
    enable_decoding_color_depth_10_vp_9: Union[Unset, bool] = UNSET
    enable_enhanced_nvdec_decoder: Union[Unset, bool] = UNSET
    prefer_system_native_hw_decoder: Union[Unset, bool] = UNSET
    enable_intel_low_power_h264_hw_encoder: Union[Unset, bool] = UNSET
    enable_intel_low_power_hevc_hw_encoder: Union[Unset, bool] = UNSET
    enable_hardware_encoding: Union[Unset, bool] = UNSET
    allow_hevc_encoding: Union[Unset, bool] = UNSET
    allow_av_1_encoding: Union[Unset, bool] = UNSET
    enable_subtitle_extraction: Union[Unset, bool] = UNSET
    hardware_decoding_codecs: Union[List[str], None, Unset] = UNSET
    allow_on_demand_metadata_based_keyframe_extraction_for_extensions: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        encoding_thread_count = self.encoding_thread_count

        transcoding_temp_path: Union[None, Unset, str]
        if isinstance(self.transcoding_temp_path, Unset):
            transcoding_temp_path = UNSET
        else:
            transcoding_temp_path = self.transcoding_temp_path

        fallback_font_path: Union[None, Unset, str]
        if isinstance(self.fallback_font_path, Unset):
            fallback_font_path = UNSET
        else:
            fallback_font_path = self.fallback_font_path

        enable_fallback_font = self.enable_fallback_font

        enable_audio_vbr = self.enable_audio_vbr

        down_mix_audio_boost = self.down_mix_audio_boost

        down_mix_stereo_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.down_mix_stereo_algorithm, Unset):
            down_mix_stereo_algorithm = self.down_mix_stereo_algorithm.value

        max_muxing_queue_size = self.max_muxing_queue_size

        enable_throttling = self.enable_throttling

        throttle_delay_seconds = self.throttle_delay_seconds

        enable_segment_deletion = self.enable_segment_deletion

        segment_keep_seconds = self.segment_keep_seconds

        hardware_acceleration_type: Union[None, Unset, str]
        if isinstance(self.hardware_acceleration_type, Unset):
            hardware_acceleration_type = UNSET
        else:
            hardware_acceleration_type = self.hardware_acceleration_type

        encoder_app_path: Union[None, Unset, str]
        if isinstance(self.encoder_app_path, Unset):
            encoder_app_path = UNSET
        else:
            encoder_app_path = self.encoder_app_path

        encoder_app_path_display: Union[None, Unset, str]
        if isinstance(self.encoder_app_path_display, Unset):
            encoder_app_path_display = UNSET
        else:
            encoder_app_path_display = self.encoder_app_path_display

        vaapi_device: Union[None, Unset, str]
        if isinstance(self.vaapi_device, Unset):
            vaapi_device = UNSET
        else:
            vaapi_device = self.vaapi_device

        enable_tonemapping = self.enable_tonemapping

        enable_vpp_tonemapping = self.enable_vpp_tonemapping

        enable_video_toolbox_tonemapping = self.enable_video_toolbox_tonemapping

        tonemapping_algorithm: Union[None, Unset, str]
        if isinstance(self.tonemapping_algorithm, Unset):
            tonemapping_algorithm = UNSET
        else:
            tonemapping_algorithm = self.tonemapping_algorithm

        tonemapping_mode: Union[None, Unset, str]
        if isinstance(self.tonemapping_mode, Unset):
            tonemapping_mode = UNSET
        else:
            tonemapping_mode = self.tonemapping_mode

        tonemapping_range: Union[None, Unset, str]
        if isinstance(self.tonemapping_range, Unset):
            tonemapping_range = UNSET
        else:
            tonemapping_range = self.tonemapping_range

        tonemapping_desat = self.tonemapping_desat

        tonemapping_peak = self.tonemapping_peak

        tonemapping_param = self.tonemapping_param

        vpp_tonemapping_brightness = self.vpp_tonemapping_brightness

        vpp_tonemapping_contrast = self.vpp_tonemapping_contrast

        h264_crf = self.h264_crf

        h265_crf = self.h265_crf

        encoder_preset: Union[None, Unset, str]
        if isinstance(self.encoder_preset, Unset):
            encoder_preset = UNSET
        else:
            encoder_preset = self.encoder_preset

        deinterlace_double_rate = self.deinterlace_double_rate

        deinterlace_method: Union[None, Unset, str]
        if isinstance(self.deinterlace_method, Unset):
            deinterlace_method = UNSET
        else:
            deinterlace_method = self.deinterlace_method

        enable_decoding_color_depth_10_hevc = self.enable_decoding_color_depth_10_hevc

        enable_decoding_color_depth_10_vp_9 = self.enable_decoding_color_depth_10_vp_9

        enable_enhanced_nvdec_decoder = self.enable_enhanced_nvdec_decoder

        prefer_system_native_hw_decoder = self.prefer_system_native_hw_decoder

        enable_intel_low_power_h264_hw_encoder = self.enable_intel_low_power_h264_hw_encoder

        enable_intel_low_power_hevc_hw_encoder = self.enable_intel_low_power_hevc_hw_encoder

        enable_hardware_encoding = self.enable_hardware_encoding

        allow_hevc_encoding = self.allow_hevc_encoding

        allow_av_1_encoding = self.allow_av_1_encoding

        enable_subtitle_extraction = self.enable_subtitle_extraction

        hardware_decoding_codecs: Union[List[str], None, Unset]
        if isinstance(self.hardware_decoding_codecs, Unset):
            hardware_decoding_codecs = UNSET
        elif isinstance(self.hardware_decoding_codecs, list):
            hardware_decoding_codecs = self.hardware_decoding_codecs

        else:
            hardware_decoding_codecs = self.hardware_decoding_codecs

        allow_on_demand_metadata_based_keyframe_extraction_for_extensions: Union[List[str], None, Unset]
        if isinstance(self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions, Unset):
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions = UNSET
        elif isinstance(self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions, list):
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions = (
                self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions
            )

        else:
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions = (
                self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if encoding_thread_count is not UNSET:
            field_dict["EncodingThreadCount"] = encoding_thread_count
        if transcoding_temp_path is not UNSET:
            field_dict["TranscodingTempPath"] = transcoding_temp_path
        if fallback_font_path is not UNSET:
            field_dict["FallbackFontPath"] = fallback_font_path
        if enable_fallback_font is not UNSET:
            field_dict["EnableFallbackFont"] = enable_fallback_font
        if enable_audio_vbr is not UNSET:
            field_dict["EnableAudioVbr"] = enable_audio_vbr
        if down_mix_audio_boost is not UNSET:
            field_dict["DownMixAudioBoost"] = down_mix_audio_boost
        if down_mix_stereo_algorithm is not UNSET:
            field_dict["DownMixStereoAlgorithm"] = down_mix_stereo_algorithm
        if max_muxing_queue_size is not UNSET:
            field_dict["MaxMuxingQueueSize"] = max_muxing_queue_size
        if enable_throttling is not UNSET:
            field_dict["EnableThrottling"] = enable_throttling
        if throttle_delay_seconds is not UNSET:
            field_dict["ThrottleDelaySeconds"] = throttle_delay_seconds
        if enable_segment_deletion is not UNSET:
            field_dict["EnableSegmentDeletion"] = enable_segment_deletion
        if segment_keep_seconds is not UNSET:
            field_dict["SegmentKeepSeconds"] = segment_keep_seconds
        if hardware_acceleration_type is not UNSET:
            field_dict["HardwareAccelerationType"] = hardware_acceleration_type
        if encoder_app_path is not UNSET:
            field_dict["EncoderAppPath"] = encoder_app_path
        if encoder_app_path_display is not UNSET:
            field_dict["EncoderAppPathDisplay"] = encoder_app_path_display
        if vaapi_device is not UNSET:
            field_dict["VaapiDevice"] = vaapi_device
        if enable_tonemapping is not UNSET:
            field_dict["EnableTonemapping"] = enable_tonemapping
        if enable_vpp_tonemapping is not UNSET:
            field_dict["EnableVppTonemapping"] = enable_vpp_tonemapping
        if enable_video_toolbox_tonemapping is not UNSET:
            field_dict["EnableVideoToolboxTonemapping"] = enable_video_toolbox_tonemapping
        if tonemapping_algorithm is not UNSET:
            field_dict["TonemappingAlgorithm"] = tonemapping_algorithm
        if tonemapping_mode is not UNSET:
            field_dict["TonemappingMode"] = tonemapping_mode
        if tonemapping_range is not UNSET:
            field_dict["TonemappingRange"] = tonemapping_range
        if tonemapping_desat is not UNSET:
            field_dict["TonemappingDesat"] = tonemapping_desat
        if tonemapping_peak is not UNSET:
            field_dict["TonemappingPeak"] = tonemapping_peak
        if tonemapping_param is not UNSET:
            field_dict["TonemappingParam"] = tonemapping_param
        if vpp_tonemapping_brightness is not UNSET:
            field_dict["VppTonemappingBrightness"] = vpp_tonemapping_brightness
        if vpp_tonemapping_contrast is not UNSET:
            field_dict["VppTonemappingContrast"] = vpp_tonemapping_contrast
        if h264_crf is not UNSET:
            field_dict["H264Crf"] = h264_crf
        if h265_crf is not UNSET:
            field_dict["H265Crf"] = h265_crf
        if encoder_preset is not UNSET:
            field_dict["EncoderPreset"] = encoder_preset
        if deinterlace_double_rate is not UNSET:
            field_dict["DeinterlaceDoubleRate"] = deinterlace_double_rate
        if deinterlace_method is not UNSET:
            field_dict["DeinterlaceMethod"] = deinterlace_method
        if enable_decoding_color_depth_10_hevc is not UNSET:
            field_dict["EnableDecodingColorDepth10Hevc"] = enable_decoding_color_depth_10_hevc
        if enable_decoding_color_depth_10_vp_9 is not UNSET:
            field_dict["EnableDecodingColorDepth10Vp9"] = enable_decoding_color_depth_10_vp_9
        if enable_enhanced_nvdec_decoder is not UNSET:
            field_dict["EnableEnhancedNvdecDecoder"] = enable_enhanced_nvdec_decoder
        if prefer_system_native_hw_decoder is not UNSET:
            field_dict["PreferSystemNativeHwDecoder"] = prefer_system_native_hw_decoder
        if enable_intel_low_power_h264_hw_encoder is not UNSET:
            field_dict["EnableIntelLowPowerH264HwEncoder"] = enable_intel_low_power_h264_hw_encoder
        if enable_intel_low_power_hevc_hw_encoder is not UNSET:
            field_dict["EnableIntelLowPowerHevcHwEncoder"] = enable_intel_low_power_hevc_hw_encoder
        if enable_hardware_encoding is not UNSET:
            field_dict["EnableHardwareEncoding"] = enable_hardware_encoding
        if allow_hevc_encoding is not UNSET:
            field_dict["AllowHevcEncoding"] = allow_hevc_encoding
        if allow_av_1_encoding is not UNSET:
            field_dict["AllowAv1Encoding"] = allow_av_1_encoding
        if enable_subtitle_extraction is not UNSET:
            field_dict["EnableSubtitleExtraction"] = enable_subtitle_extraction
        if hardware_decoding_codecs is not UNSET:
            field_dict["HardwareDecodingCodecs"] = hardware_decoding_codecs
        if allow_on_demand_metadata_based_keyframe_extraction_for_extensions is not UNSET:
            field_dict[
                "AllowOnDemandMetadataBasedKeyframeExtractionForExtensions"
            ] = allow_on_demand_metadata_based_keyframe_extraction_for_extensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encoding_thread_count = d.pop("EncodingThreadCount", UNSET)

        def _parse_transcoding_temp_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        transcoding_temp_path = _parse_transcoding_temp_path(d.pop("TranscodingTempPath", UNSET))

        def _parse_fallback_font_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fallback_font_path = _parse_fallback_font_path(d.pop("FallbackFontPath", UNSET))

        enable_fallback_font = d.pop("EnableFallbackFont", UNSET)

        enable_audio_vbr = d.pop("EnableAudioVbr", UNSET)

        down_mix_audio_boost = d.pop("DownMixAudioBoost", UNSET)

        _down_mix_stereo_algorithm = d.pop("DownMixStereoAlgorithm", UNSET)
        down_mix_stereo_algorithm: Union[Unset, DownMixStereoAlgorithms]
        if isinstance(_down_mix_stereo_algorithm, Unset):
            down_mix_stereo_algorithm = UNSET
        else:
            down_mix_stereo_algorithm = DownMixStereoAlgorithms(_down_mix_stereo_algorithm)

        max_muxing_queue_size = d.pop("MaxMuxingQueueSize", UNSET)

        enable_throttling = d.pop("EnableThrottling", UNSET)

        throttle_delay_seconds = d.pop("ThrottleDelaySeconds", UNSET)

        enable_segment_deletion = d.pop("EnableSegmentDeletion", UNSET)

        segment_keep_seconds = d.pop("SegmentKeepSeconds", UNSET)

        def _parse_hardware_acceleration_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hardware_acceleration_type = _parse_hardware_acceleration_type(d.pop("HardwareAccelerationType", UNSET))

        def _parse_encoder_app_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        encoder_app_path = _parse_encoder_app_path(d.pop("EncoderAppPath", UNSET))

        def _parse_encoder_app_path_display(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        encoder_app_path_display = _parse_encoder_app_path_display(d.pop("EncoderAppPathDisplay", UNSET))

        def _parse_vaapi_device(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vaapi_device = _parse_vaapi_device(d.pop("VaapiDevice", UNSET))

        enable_tonemapping = d.pop("EnableTonemapping", UNSET)

        enable_vpp_tonemapping = d.pop("EnableVppTonemapping", UNSET)

        enable_video_toolbox_tonemapping = d.pop("EnableVideoToolboxTonemapping", UNSET)

        def _parse_tonemapping_algorithm(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tonemapping_algorithm = _parse_tonemapping_algorithm(d.pop("TonemappingAlgorithm", UNSET))

        def _parse_tonemapping_mode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tonemapping_mode = _parse_tonemapping_mode(d.pop("TonemappingMode", UNSET))

        def _parse_tonemapping_range(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tonemapping_range = _parse_tonemapping_range(d.pop("TonemappingRange", UNSET))

        tonemapping_desat = d.pop("TonemappingDesat", UNSET)

        tonemapping_peak = d.pop("TonemappingPeak", UNSET)

        tonemapping_param = d.pop("TonemappingParam", UNSET)

        vpp_tonemapping_brightness = d.pop("VppTonemappingBrightness", UNSET)

        vpp_tonemapping_contrast = d.pop("VppTonemappingContrast", UNSET)

        h264_crf = d.pop("H264Crf", UNSET)

        h265_crf = d.pop("H265Crf", UNSET)

        def _parse_encoder_preset(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        encoder_preset = _parse_encoder_preset(d.pop("EncoderPreset", UNSET))

        deinterlace_double_rate = d.pop("DeinterlaceDoubleRate", UNSET)

        def _parse_deinterlace_method(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deinterlace_method = _parse_deinterlace_method(d.pop("DeinterlaceMethod", UNSET))

        enable_decoding_color_depth_10_hevc = d.pop("EnableDecodingColorDepth10Hevc", UNSET)

        enable_decoding_color_depth_10_vp_9 = d.pop("EnableDecodingColorDepth10Vp9", UNSET)

        enable_enhanced_nvdec_decoder = d.pop("EnableEnhancedNvdecDecoder", UNSET)

        prefer_system_native_hw_decoder = d.pop("PreferSystemNativeHwDecoder", UNSET)

        enable_intel_low_power_h264_hw_encoder = d.pop("EnableIntelLowPowerH264HwEncoder", UNSET)

        enable_intel_low_power_hevc_hw_encoder = d.pop("EnableIntelLowPowerHevcHwEncoder", UNSET)

        enable_hardware_encoding = d.pop("EnableHardwareEncoding", UNSET)

        allow_hevc_encoding = d.pop("AllowHevcEncoding", UNSET)

        allow_av_1_encoding = d.pop("AllowAv1Encoding", UNSET)

        enable_subtitle_extraction = d.pop("EnableSubtitleExtraction", UNSET)

        def _parse_hardware_decoding_codecs(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hardware_decoding_codecs_type_0 = cast(List[str], data)

                return hardware_decoding_codecs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        hardware_decoding_codecs = _parse_hardware_decoding_codecs(d.pop("HardwareDecodingCodecs", UNSET))

        def _parse_allow_on_demand_metadata_based_keyframe_extraction_for_extensions(
            data: object,
        ) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allow_on_demand_metadata_based_keyframe_extraction_for_extensions_type_0 = cast(List[str], data)

                return allow_on_demand_metadata_based_keyframe_extraction_for_extensions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        allow_on_demand_metadata_based_keyframe_extraction_for_extensions = (
            _parse_allow_on_demand_metadata_based_keyframe_extraction_for_extensions(
                d.pop("AllowOnDemandMetadataBasedKeyframeExtractionForExtensions", UNSET)
            )
        )

        encoding_options = cls(
            encoding_thread_count=encoding_thread_count,
            transcoding_temp_path=transcoding_temp_path,
            fallback_font_path=fallback_font_path,
            enable_fallback_font=enable_fallback_font,
            enable_audio_vbr=enable_audio_vbr,
            down_mix_audio_boost=down_mix_audio_boost,
            down_mix_stereo_algorithm=down_mix_stereo_algorithm,
            max_muxing_queue_size=max_muxing_queue_size,
            enable_throttling=enable_throttling,
            throttle_delay_seconds=throttle_delay_seconds,
            enable_segment_deletion=enable_segment_deletion,
            segment_keep_seconds=segment_keep_seconds,
            hardware_acceleration_type=hardware_acceleration_type,
            encoder_app_path=encoder_app_path,
            encoder_app_path_display=encoder_app_path_display,
            vaapi_device=vaapi_device,
            enable_tonemapping=enable_tonemapping,
            enable_vpp_tonemapping=enable_vpp_tonemapping,
            enable_video_toolbox_tonemapping=enable_video_toolbox_tonemapping,
            tonemapping_algorithm=tonemapping_algorithm,
            tonemapping_mode=tonemapping_mode,
            tonemapping_range=tonemapping_range,
            tonemapping_desat=tonemapping_desat,
            tonemapping_peak=tonemapping_peak,
            tonemapping_param=tonemapping_param,
            vpp_tonemapping_brightness=vpp_tonemapping_brightness,
            vpp_tonemapping_contrast=vpp_tonemapping_contrast,
            h264_crf=h264_crf,
            h265_crf=h265_crf,
            encoder_preset=encoder_preset,
            deinterlace_double_rate=deinterlace_double_rate,
            deinterlace_method=deinterlace_method,
            enable_decoding_color_depth_10_hevc=enable_decoding_color_depth_10_hevc,
            enable_decoding_color_depth_10_vp_9=enable_decoding_color_depth_10_vp_9,
            enable_enhanced_nvdec_decoder=enable_enhanced_nvdec_decoder,
            prefer_system_native_hw_decoder=prefer_system_native_hw_decoder,
            enable_intel_low_power_h264_hw_encoder=enable_intel_low_power_h264_hw_encoder,
            enable_intel_low_power_hevc_hw_encoder=enable_intel_low_power_hevc_hw_encoder,
            enable_hardware_encoding=enable_hardware_encoding,
            allow_hevc_encoding=allow_hevc_encoding,
            allow_av_1_encoding=allow_av_1_encoding,
            enable_subtitle_extraction=enable_subtitle_extraction,
            hardware_decoding_codecs=hardware_decoding_codecs,
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions=allow_on_demand_metadata_based_keyframe_extraction_for_extensions,
        )

        return encoding_options
