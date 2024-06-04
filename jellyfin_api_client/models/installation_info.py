from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union

if TYPE_CHECKING:
    from ..models.package_info import PackageInfo


T = TypeVar("T", bound="InstallationInfo")


@_attrs_define
class InstallationInfo:
    """Class InstallationInfo.

    Attributes:
        guid (Union[Unset, str]): Gets or sets the Id.
        name (Union[None, Unset, str]): Gets or sets the name.
        version (Union[None, Unset, str]): Gets or sets the version.
        changelog (Union[None, Unset, str]): Gets or sets the changelog for this version.
        source_url (Union[None, Unset, str]): Gets or sets the source URL.
        checksum (Union[None, Unset, str]): Gets or sets a checksum for the binary.
        package_info (Union['PackageInfo', None, Unset]): Gets or sets package information for the installation.
    """

    guid: Union[Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    changelog: Union[None, Unset, str] = UNSET
    source_url: Union[None, Unset, str] = UNSET
    checksum: Union[None, Unset, str] = UNSET
    package_info: Union["PackageInfo", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.package_info import PackageInfo

        guid = self.guid

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        changelog: Union[None, Unset, str]
        if isinstance(self.changelog, Unset):
            changelog = UNSET
        else:
            changelog = self.changelog

        source_url: Union[None, Unset, str]
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        checksum: Union[None, Unset, str]
        if isinstance(self.checksum, Unset):
            checksum = UNSET
        else:
            checksum = self.checksum

        package_info: Union[Dict[str, Any], None, Unset]
        if isinstance(self.package_info, Unset):
            package_info = UNSET
        elif isinstance(self.package_info, PackageInfo):
            package_info = self.package_info.to_dict()
        else:
            package_info = self.package_info

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if name is not UNSET:
            field_dict["Name"] = name
        if version is not UNSET:
            field_dict["Version"] = version
        if changelog is not UNSET:
            field_dict["Changelog"] = changelog
        if source_url is not UNSET:
            field_dict["SourceUrl"] = source_url
        if checksum is not UNSET:
            field_dict["Checksum"] = checksum
        if package_info is not UNSET:
            field_dict["PackageInfo"] = package_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_info import PackageInfo

        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("Version", UNSET))

        def _parse_changelog(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        changelog = _parse_changelog(d.pop("Changelog", UNSET))

        def _parse_source_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_url = _parse_source_url(d.pop("SourceUrl", UNSET))

        def _parse_checksum(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        checksum = _parse_checksum(d.pop("Checksum", UNSET))

        def _parse_package_info(data: object) -> Union["PackageInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                package_info_type_1 = PackageInfo.from_dict(data)

                return package_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["PackageInfo", None, Unset], data)

        package_info = _parse_package_info(d.pop("PackageInfo", UNSET))

        installation_info = cls(
            guid=guid,
            name=name,
            version=version,
            changelog=changelog,
            source_url=source_url,
            checksum=checksum,
            package_info=package_info,
        )

        return installation_info
