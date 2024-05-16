from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from ..models.trickplay_scan_behavior import TrickplayScanBehavior
from ..types import UNSET, Unset
from typing import Union
from ..models.process_priority_class import ProcessPriorityClass


T = TypeVar("T", bound="TrickplayOptions")


@_attrs_define
class TrickplayOptions:
    """Class TrickplayOptions.

    Attributes:
        enable_hw_acceleration (Union[Unset, bool]): Gets or sets a value indicating whether or not to use HW
            acceleration.
        enable_hw_encoding (Union[Unset, bool]): Gets or sets a value indicating whether or not to use HW accelerated
            MJPEG encoding.
        scan_behavior (Union[Unset, TrickplayScanBehavior]): Enum TrickplayScanBehavior.
        process_priority (Union[Unset, ProcessPriorityClass]):
        interval (Union[Unset, int]): Gets or sets the interval, in ms, between each new trickplay image.
        width_resolutions (Union[Unset, List[int]]): Gets or sets the target width resolutions, in px, to generates
            preview images for.
        tile_width (Union[Unset, int]): Gets or sets number of tile images to allow in X dimension.
        tile_height (Union[Unset, int]): Gets or sets number of tile images to allow in Y dimension.
        qscale (Union[Unset, int]): Gets or sets the ffmpeg output quality level.
        jpeg_quality (Union[Unset, int]): Gets or sets the jpeg quality to use for image tiles.
        process_threads (Union[Unset, int]): Gets or sets the number of threads to be used by ffmpeg.
    """

    enable_hw_acceleration: Union[Unset, bool] = UNSET
    enable_hw_encoding: Union[Unset, bool] = UNSET
    scan_behavior: Union[Unset, TrickplayScanBehavior] = UNSET
    process_priority: Union[Unset, ProcessPriorityClass] = UNSET
    interval: Union[Unset, int] = UNSET
    width_resolutions: Union[Unset, List[int]] = UNSET
    tile_width: Union[Unset, int] = UNSET
    tile_height: Union[Unset, int] = UNSET
    qscale: Union[Unset, int] = UNSET
    jpeg_quality: Union[Unset, int] = UNSET
    process_threads: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enable_hw_acceleration = self.enable_hw_acceleration

        enable_hw_encoding = self.enable_hw_encoding

        scan_behavior: Union[Unset, str] = UNSET
        if not isinstance(self.scan_behavior, Unset):
            scan_behavior = self.scan_behavior.value

        process_priority: Union[Unset, str] = UNSET
        if not isinstance(self.process_priority, Unset):
            process_priority = self.process_priority.value

        interval = self.interval

        width_resolutions: Union[Unset, List[int]] = UNSET
        if not isinstance(self.width_resolutions, Unset):
            width_resolutions = self.width_resolutions

        tile_width = self.tile_width

        tile_height = self.tile_height

        qscale = self.qscale

        jpeg_quality = self.jpeg_quality

        process_threads = self.process_threads

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if enable_hw_acceleration is not UNSET:
            field_dict["EnableHwAcceleration"] = enable_hw_acceleration
        if enable_hw_encoding is not UNSET:
            field_dict["EnableHwEncoding"] = enable_hw_encoding
        if scan_behavior is not UNSET:
            field_dict["ScanBehavior"] = scan_behavior
        if process_priority is not UNSET:
            field_dict["ProcessPriority"] = process_priority
        if interval is not UNSET:
            field_dict["Interval"] = interval
        if width_resolutions is not UNSET:
            field_dict["WidthResolutions"] = width_resolutions
        if tile_width is not UNSET:
            field_dict["TileWidth"] = tile_width
        if tile_height is not UNSET:
            field_dict["TileHeight"] = tile_height
        if qscale is not UNSET:
            field_dict["Qscale"] = qscale
        if jpeg_quality is not UNSET:
            field_dict["JpegQuality"] = jpeg_quality
        if process_threads is not UNSET:
            field_dict["ProcessThreads"] = process_threads

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable_hw_acceleration = d.pop("EnableHwAcceleration", UNSET)

        enable_hw_encoding = d.pop("EnableHwEncoding", UNSET)

        _scan_behavior = d.pop("ScanBehavior", UNSET)
        scan_behavior: Union[Unset, TrickplayScanBehavior]
        if isinstance(_scan_behavior, Unset):
            scan_behavior = UNSET
        else:
            scan_behavior = TrickplayScanBehavior(_scan_behavior)

        _process_priority = d.pop("ProcessPriority", UNSET)
        process_priority: Union[Unset, ProcessPriorityClass]
        if isinstance(_process_priority, Unset):
            process_priority = UNSET
        else:
            process_priority = ProcessPriorityClass(_process_priority)

        interval = d.pop("Interval", UNSET)

        width_resolutions = cast(List[int], d.pop("WidthResolutions", UNSET))

        tile_width = d.pop("TileWidth", UNSET)

        tile_height = d.pop("TileHeight", UNSET)

        qscale = d.pop("Qscale", UNSET)

        jpeg_quality = d.pop("JpegQuality", UNSET)

        process_threads = d.pop("ProcessThreads", UNSET)

        trickplay_options = cls(
            enable_hw_acceleration=enable_hw_acceleration,
            enable_hw_encoding=enable_hw_encoding,
            scan_behavior=scan_behavior,
            process_priority=process_priority,
            interval=interval,
            width_resolutions=width_resolutions,
            tile_width=tile_width,
            tile_height=tile_height,
            qscale=qscale,
            jpeg_quality=jpeg_quality,
            process_threads=process_threads,
        )

        return trickplay_options
