from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from ..models.plugin_status import PluginStatus
from typing import cast


T = TypeVar("T", bound="PluginInfo")


@_attrs_define
class PluginInfo:
    """This is a serializable stub class that is used by the api to provide information about installed plugins.

    Attributes:
        name (Union[Unset, str]): Gets or sets the name.
        version (Union[Unset, str]): Gets or sets the version.
        configuration_file_name (Union[None, Unset, str]): Gets or sets the name of the configuration file.
        description (Union[Unset, str]): Gets or sets the description.
        id (Union[Unset, str]): Gets or sets the unique id.
        can_uninstall (Union[Unset, bool]): Gets or sets a value indicating whether the plugin can be uninstalled.
        has_image (Union[Unset, bool]): Gets or sets a value indicating whether this plugin has a valid image.
        status (Union[Unset, PluginStatus]): Plugin load status.
    """

    name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    configuration_file_name: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    can_uninstall: Union[Unset, bool] = UNSET
    has_image: Union[Unset, bool] = UNSET
    status: Union[Unset, PluginStatus] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        version = self.version

        configuration_file_name: Union[None, Unset, str]
        if isinstance(self.configuration_file_name, Unset):
            configuration_file_name = UNSET
        else:
            configuration_file_name = self.configuration_file_name

        description = self.description

        id = self.id

        can_uninstall = self.can_uninstall

        has_image = self.has_image

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if version is not UNSET:
            field_dict["Version"] = version
        if configuration_file_name is not UNSET:
            field_dict["ConfigurationFileName"] = configuration_file_name
        if description is not UNSET:
            field_dict["Description"] = description
        if id is not UNSET:
            field_dict["Id"] = id
        if can_uninstall is not UNSET:
            field_dict["CanUninstall"] = can_uninstall
        if has_image is not UNSET:
            field_dict["HasImage"] = has_image
        if status is not UNSET:
            field_dict["Status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        version = d.pop("Version", UNSET)

        def _parse_configuration_file_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        configuration_file_name = _parse_configuration_file_name(
            d.pop("ConfigurationFileName", UNSET)
        )

        description = d.pop("Description", UNSET)

        id = d.pop("Id", UNSET)

        can_uninstall = d.pop("CanUninstall", UNSET)

        has_image = d.pop("HasImage", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, PluginStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PluginStatus(_status)

        plugin_info = cls(
            name=name,
            version=version,
            configuration_file_name=configuration_file_name,
            description=description,
            id=id,
            can_uninstall=can_uninstall,
            has_image=has_image,
            status=status,
        )

        return plugin_info
