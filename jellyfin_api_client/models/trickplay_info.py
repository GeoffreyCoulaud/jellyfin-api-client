from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union


T = TypeVar("T", bound="TrickplayInfo")


@_attrs_define
class TrickplayInfo:
    """An entity representing the metadata for a group of trickplay tiles.

    Attributes:
        width (Union[Unset, int]): Gets or sets width of an individual thumbnail.
        height (Union[Unset, int]): Gets or sets height of an individual thumbnail.
        tile_width (Union[Unset, int]): Gets or sets amount of thumbnails per row.
        tile_height (Union[Unset, int]): Gets or sets amount of thumbnails per column.
        thumbnail_count (Union[Unset, int]): Gets or sets total amount of non-black thumbnails.
        interval (Union[Unset, int]): Gets or sets interval in milliseconds between each trickplay thumbnail.
        bandwidth (Union[Unset, int]): Gets or sets peak bandwith usage in bits per second.
    """

    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    tile_width: Union[Unset, int] = UNSET
    tile_height: Union[Unset, int] = UNSET
    thumbnail_count: Union[Unset, int] = UNSET
    interval: Union[Unset, int] = UNSET
    bandwidth: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        width = self.width

        height = self.height

        tile_width = self.tile_width

        tile_height = self.tile_height

        thumbnail_count = self.thumbnail_count

        interval = self.interval

        bandwidth = self.bandwidth

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if width is not UNSET:
            field_dict["Width"] = width
        if height is not UNSET:
            field_dict["Height"] = height
        if tile_width is not UNSET:
            field_dict["TileWidth"] = tile_width
        if tile_height is not UNSET:
            field_dict["TileHeight"] = tile_height
        if thumbnail_count is not UNSET:
            field_dict["ThumbnailCount"] = thumbnail_count
        if interval is not UNSET:
            field_dict["Interval"] = interval
        if bandwidth is not UNSET:
            field_dict["Bandwidth"] = bandwidth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        width = d.pop("Width", UNSET)

        height = d.pop("Height", UNSET)

        tile_width = d.pop("TileWidth", UNSET)

        tile_height = d.pop("TileHeight", UNSET)

        thumbnail_count = d.pop("ThumbnailCount", UNSET)

        interval = d.pop("Interval", UNSET)

        bandwidth = d.pop("Bandwidth", UNSET)

        trickplay_info = cls(
            width=width,
            height=height,
            tile_width=tile_width,
            tile_height=tile_height,
            thumbnail_count=thumbnail_count,
            interval=interval,
            bandwidth=bandwidth,
        )

        return trickplay_info
