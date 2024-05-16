from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="MediaAttachment")


@_attrs_define
class MediaAttachment:
    """Class MediaAttachment.

    Attributes:
        codec (Union[None, Unset, str]): Gets or sets the codec.
        codec_tag (Union[None, Unset, str]): Gets or sets the codec tag.
        comment (Union[None, Unset, str]): Gets or sets the comment.
        index (Union[Unset, int]): Gets or sets the index.
        file_name (Union[None, Unset, str]): Gets or sets the filename.
        mime_type (Union[None, Unset, str]): Gets or sets the MIME type.
        delivery_url (Union[None, Unset, str]): Gets or sets the delivery URL.
    """

    codec: Union[None, Unset, str] = UNSET
    codec_tag: Union[None, Unset, str] = UNSET
    comment: Union[None, Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    file_name: Union[None, Unset, str] = UNSET
    mime_type: Union[None, Unset, str] = UNSET
    delivery_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        codec: Union[None, Unset, str]
        if isinstance(self.codec, Unset):
            codec = UNSET
        else:
            codec = self.codec

        codec_tag: Union[None, Unset, str]
        if isinstance(self.codec_tag, Unset):
            codec_tag = UNSET
        else:
            codec_tag = self.codec_tag

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        index = self.index

        file_name: Union[None, Unset, str]
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        mime_type: Union[None, Unset, str]
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        delivery_url: Union[None, Unset, str]
        if isinstance(self.delivery_url, Unset):
            delivery_url = UNSET
        else:
            delivery_url = self.delivery_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if codec is not UNSET:
            field_dict["Codec"] = codec
        if codec_tag is not UNSET:
            field_dict["CodecTag"] = codec_tag
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if index is not UNSET:
            field_dict["Index"] = index
        if file_name is not UNSET:
            field_dict["FileName"] = file_name
        if mime_type is not UNSET:
            field_dict["MimeType"] = mime_type
        if delivery_url is not UNSET:
            field_dict["DeliveryUrl"] = delivery_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        codec = _parse_codec(d.pop("Codec", UNSET))

        def _parse_codec_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        codec_tag = _parse_codec_tag(d.pop("CodecTag", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("Comment", UNSET))

        index = d.pop("Index", UNSET)

        def _parse_file_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_name = _parse_file_name(d.pop("FileName", UNSET))

        def _parse_mime_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mime_type = _parse_mime_type(d.pop("MimeType", UNSET))

        def _parse_delivery_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_url = _parse_delivery_url(d.pop("DeliveryUrl", UNSET))

        media_attachment = cls(
            codec=codec,
            codec_tag=codec_tag,
            comment=comment,
            index=index,
            file_name=file_name,
            mime_type=mime_type,
            delivery_url=delivery_url,
        )

        return media_attachment
