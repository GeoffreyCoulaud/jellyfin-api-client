from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union

if TYPE_CHECKING:
    from ..models.person_lookup_info import PersonLookupInfo


T = TypeVar("T", bound="PersonLookupInfoRemoteSearchQuery")


@_attrs_define
class PersonLookupInfoRemoteSearchQuery:
    """
    Attributes:
        search_info (Union['PersonLookupInfo', None, Unset]):
        item_id (Union[Unset, str]):
        search_provider_name (Union[None, Unset, str]): Gets or sets the provider name to search within if set.
        include_disabled_providers (Union[Unset, bool]): Gets or sets a value indicating whether disabled providers
            should be included.
    """

    search_info: Union["PersonLookupInfo", None, Unset] = UNSET
    item_id: Union[Unset, str] = UNSET
    search_provider_name: Union[None, Unset, str] = UNSET
    include_disabled_providers: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.person_lookup_info import PersonLookupInfo

        search_info: Union[Dict[str, Any], None, Unset]
        if isinstance(self.search_info, Unset):
            search_info = UNSET
        elif isinstance(self.search_info, PersonLookupInfo):
            search_info = self.search_info.to_dict()
        else:
            search_info = self.search_info

        item_id = self.item_id

        search_provider_name: Union[None, Unset, str]
        if isinstance(self.search_provider_name, Unset):
            search_provider_name = UNSET
        else:
            search_provider_name = self.search_provider_name

        include_disabled_providers = self.include_disabled_providers

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if search_info is not UNSET:
            field_dict["SearchInfo"] = search_info
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if search_provider_name is not UNSET:
            field_dict["SearchProviderName"] = search_provider_name
        if include_disabled_providers is not UNSET:
            field_dict["IncludeDisabledProviders"] = include_disabled_providers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.person_lookup_info import PersonLookupInfo

        d = src_dict.copy()

        def _parse_search_info(data: object) -> Union["PersonLookupInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_info_type_1 = PersonLookupInfo.from_dict(data)

                return search_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["PersonLookupInfo", None, Unset], data)

        search_info = _parse_search_info(d.pop("SearchInfo", UNSET))

        item_id = d.pop("ItemId", UNSET)

        def _parse_search_provider_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        search_provider_name = _parse_search_provider_name(
            d.pop("SearchProviderName", UNSET)
        )

        include_disabled_providers = d.pop("IncludeDisabledProviders", UNSET)

        person_lookup_info_remote_search_query = cls(
            search_info=search_info,
            item_id=item_id,
            search_provider_name=search_provider_name,
            include_disabled_providers=include_disabled_providers,
        )

        return person_lookup_info_remote_search_query
