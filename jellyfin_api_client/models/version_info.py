from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="VersionInfo")


@_attrs_define
class VersionInfo:
    """Defines the MediaBrowser.Model.Updates.VersionInfo class.

    Attributes:
        version (Union[Unset, str]): Gets or sets the version.
        version_number (Union[Unset, str]): Gets the version as a System.Version.
        changelog (Union[None, Unset, str]): Gets or sets the changelog for this version.
        target_abi (Union[None, Unset, str]): Gets or sets the ABI that this version was built against.
        source_url (Union[None, Unset, str]): Gets or sets the source URL.
        checksum (Union[None, Unset, str]): Gets or sets a checksum for the binary.
        timestamp (Union[None, Unset, str]): Gets or sets a timestamp of when the binary was built.
        repository_name (Union[Unset, str]): Gets or sets the repository name.
        repository_url (Union[Unset, str]): Gets or sets the repository url.
    """

    version: Union[Unset, str] = UNSET
    version_number: Union[Unset, str] = UNSET
    changelog: Union[None, Unset, str] = UNSET
    target_abi: Union[None, Unset, str] = UNSET
    source_url: Union[None, Unset, str] = UNSET
    checksum: Union[None, Unset, str] = UNSET
    timestamp: Union[None, Unset, str] = UNSET
    repository_name: Union[Unset, str] = UNSET
    repository_url: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        version = self.version

        version_number = self.version_number

        changelog: Union[None, Unset, str]
        if isinstance(self.changelog, Unset):
            changelog = UNSET
        else:
            changelog = self.changelog

        target_abi: Union[None, Unset, str]
        if isinstance(self.target_abi, Unset):
            target_abi = UNSET
        else:
            target_abi = self.target_abi

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

        timestamp: Union[None, Unset, str]
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = self.timestamp

        repository_name = self.repository_name

        repository_url = self.repository_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if version_number is not UNSET:
            field_dict["VersionNumber"] = version_number
        if changelog is not UNSET:
            field_dict["changelog"] = changelog
        if target_abi is not UNSET:
            field_dict["targetAbi"] = target_abi
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if repository_url is not UNSET:
            field_dict["repositoryUrl"] = repository_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        version_number = d.pop("VersionNumber", UNSET)

        def _parse_changelog(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        changelog = _parse_changelog(d.pop("changelog", UNSET))

        def _parse_target_abi(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        target_abi = _parse_target_abi(d.pop("targetAbi", UNSET))

        def _parse_source_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_url = _parse_source_url(d.pop("sourceUrl", UNSET))

        def _parse_checksum(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        checksum = _parse_checksum(d.pop("checksum", UNSET))

        def _parse_timestamp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        repository_name = d.pop("repositoryName", UNSET)

        repository_url = d.pop("repositoryUrl", UNSET)

        version_info = cls(
            version=version,
            version_number=version_number,
            changelog=changelog,
            target_abi=target_abi,
            source_url=source_url,
            checksum=checksum,
            timestamp=timestamp,
            repository_name=repository_name,
            repository_url=repository_url,
        )

        return version_info
