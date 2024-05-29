from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import cast, Union


T = TypeVar("T", bound="GetHlsVideoSegmentStreamOptions")


@_attrs_define
class GetHlsVideoSegmentStreamOptions:
    """ """

    additional_properties: Dict[str, Union[None, str]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_hls_video_segment_stream_options = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Union[None, str]:
                if data is None:
                    return data
                return cast(Union[None, str], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        get_hls_video_segment_stream_options.additional_properties = (
            additional_properties
        )
        return get_hls_video_segment_stream_options

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union[None, str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union[None, str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
