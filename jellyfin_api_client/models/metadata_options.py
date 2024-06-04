from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from typing import cast, List


T = TypeVar("T", bound="MetadataOptions")


@_attrs_define
class MetadataOptions:
    """Class MetadataOptions.

    Attributes:
        item_type (Union[None, Unset, str]):
        disabled_metadata_savers (Union[List[str], None, Unset]):
        local_metadata_reader_order (Union[List[str], None, Unset]):
        disabled_metadata_fetchers (Union[List[str], None, Unset]):
        metadata_fetcher_order (Union[List[str], None, Unset]):
        disabled_image_fetchers (Union[List[str], None, Unset]):
        image_fetcher_order (Union[List[str], None, Unset]):
    """

    item_type: Union[None, Unset, str] = UNSET
    disabled_metadata_savers: Union[List[str], None, Unset] = UNSET
    local_metadata_reader_order: Union[List[str], None, Unset] = UNSET
    disabled_metadata_fetchers: Union[List[str], None, Unset] = UNSET
    metadata_fetcher_order: Union[List[str], None, Unset] = UNSET
    disabled_image_fetchers: Union[List[str], None, Unset] = UNSET
    image_fetcher_order: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type: Union[None, Unset, str]
        if isinstance(self.item_type, Unset):
            item_type = UNSET
        else:
            item_type = self.item_type

        disabled_metadata_savers: Union[List[str], None, Unset]
        if isinstance(self.disabled_metadata_savers, Unset):
            disabled_metadata_savers = UNSET
        elif isinstance(self.disabled_metadata_savers, list):
            disabled_metadata_savers = self.disabled_metadata_savers

        else:
            disabled_metadata_savers = self.disabled_metadata_savers

        local_metadata_reader_order: Union[List[str], None, Unset]
        if isinstance(self.local_metadata_reader_order, Unset):
            local_metadata_reader_order = UNSET
        elif isinstance(self.local_metadata_reader_order, list):
            local_metadata_reader_order = self.local_metadata_reader_order

        else:
            local_metadata_reader_order = self.local_metadata_reader_order

        disabled_metadata_fetchers: Union[List[str], None, Unset]
        if isinstance(self.disabled_metadata_fetchers, Unset):
            disabled_metadata_fetchers = UNSET
        elif isinstance(self.disabled_metadata_fetchers, list):
            disabled_metadata_fetchers = self.disabled_metadata_fetchers

        else:
            disabled_metadata_fetchers = self.disabled_metadata_fetchers

        metadata_fetcher_order: Union[List[str], None, Unset]
        if isinstance(self.metadata_fetcher_order, Unset):
            metadata_fetcher_order = UNSET
        elif isinstance(self.metadata_fetcher_order, list):
            metadata_fetcher_order = self.metadata_fetcher_order

        else:
            metadata_fetcher_order = self.metadata_fetcher_order

        disabled_image_fetchers: Union[List[str], None, Unset]
        if isinstance(self.disabled_image_fetchers, Unset):
            disabled_image_fetchers = UNSET
        elif isinstance(self.disabled_image_fetchers, list):
            disabled_image_fetchers = self.disabled_image_fetchers

        else:
            disabled_image_fetchers = self.disabled_image_fetchers

        image_fetcher_order: Union[List[str], None, Unset]
        if isinstance(self.image_fetcher_order, Unset):
            image_fetcher_order = UNSET
        elif isinstance(self.image_fetcher_order, list):
            image_fetcher_order = self.image_fetcher_order

        else:
            image_fetcher_order = self.image_fetcher_order

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if disabled_metadata_savers is not UNSET:
            field_dict["DisabledMetadataSavers"] = disabled_metadata_savers
        if local_metadata_reader_order is not UNSET:
            field_dict["LocalMetadataReaderOrder"] = local_metadata_reader_order
        if disabled_metadata_fetchers is not UNSET:
            field_dict["DisabledMetadataFetchers"] = disabled_metadata_fetchers
        if metadata_fetcher_order is not UNSET:
            field_dict["MetadataFetcherOrder"] = metadata_fetcher_order
        if disabled_image_fetchers is not UNSET:
            field_dict["DisabledImageFetchers"] = disabled_image_fetchers
        if image_fetcher_order is not UNSET:
            field_dict["ImageFetcherOrder"] = image_fetcher_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_item_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_type = _parse_item_type(d.pop("ItemType", UNSET))

        def _parse_disabled_metadata_savers(
            data: object,
        ) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disabled_metadata_savers_type_0 = cast(List[str], data)

                return disabled_metadata_savers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        disabled_metadata_savers = _parse_disabled_metadata_savers(
            d.pop("DisabledMetadataSavers", UNSET)
        )

        def _parse_local_metadata_reader_order(
            data: object,
        ) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                local_metadata_reader_order_type_0 = cast(List[str], data)

                return local_metadata_reader_order_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        local_metadata_reader_order = _parse_local_metadata_reader_order(
            d.pop("LocalMetadataReaderOrder", UNSET)
        )

        def _parse_disabled_metadata_fetchers(
            data: object,
        ) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disabled_metadata_fetchers_type_0 = cast(List[str], data)

                return disabled_metadata_fetchers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        disabled_metadata_fetchers = _parse_disabled_metadata_fetchers(
            d.pop("DisabledMetadataFetchers", UNSET)
        )

        def _parse_metadata_fetcher_order(
            data: object,
        ) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_fetcher_order_type_0 = cast(List[str], data)

                return metadata_fetcher_order_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        metadata_fetcher_order = _parse_metadata_fetcher_order(
            d.pop("MetadataFetcherOrder", UNSET)
        )

        def _parse_disabled_image_fetchers(
            data: object,
        ) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disabled_image_fetchers_type_0 = cast(List[str], data)

                return disabled_image_fetchers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        disabled_image_fetchers = _parse_disabled_image_fetchers(
            d.pop("DisabledImageFetchers", UNSET)
        )

        def _parse_image_fetcher_order(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_fetcher_order_type_0 = cast(List[str], data)

                return image_fetcher_order_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        image_fetcher_order = _parse_image_fetcher_order(
            d.pop("ImageFetcherOrder", UNSET)
        )

        metadata_options = cls(
            item_type=item_type,
            disabled_metadata_savers=disabled_metadata_savers,
            local_metadata_reader_order=local_metadata_reader_order,
            disabled_metadata_fetchers=disabled_metadata_fetchers,
            metadata_fetcher_order=metadata_fetcher_order,
            disabled_image_fetchers=disabled_image_fetchers,
            image_fetcher_order=image_fetcher_order,
        )

        return metadata_options
