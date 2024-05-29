from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import cast, Union


T = TypeVar("T", bound="ConfigurationPageInfo")


@_attrs_define
class ConfigurationPageInfo:
    """The configuration page info.

    Attributes:
        name (Union[Unset, str]): Gets or sets the name.
        enable_in_main_menu (Union[Unset, bool]): Gets or sets a value indicating whether the configurations page is
            enabled in the main menu.
        menu_section (Union[None, Unset, str]): Gets or sets the menu section.
        menu_icon (Union[None, Unset, str]): Gets or sets the menu icon.
        display_name (Union[None, Unset, str]): Gets or sets the display name.
        plugin_id (Union[None, Unset, str]): Gets or sets the plugin id.
    """

    name: Union[Unset, str] = UNSET
    enable_in_main_menu: Union[Unset, bool] = UNSET
    menu_section: Union[None, Unset, str] = UNSET
    menu_icon: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    plugin_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        enable_in_main_menu = self.enable_in_main_menu

        menu_section: Union[None, Unset, str]
        if isinstance(self.menu_section, Unset):
            menu_section = UNSET
        else:
            menu_section = self.menu_section

        menu_icon: Union[None, Unset, str]
        if isinstance(self.menu_icon, Unset):
            menu_icon = UNSET
        else:
            menu_icon = self.menu_icon

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        plugin_id: Union[None, Unset, str]
        if isinstance(self.plugin_id, Unset):
            plugin_id = UNSET
        else:
            plugin_id = self.plugin_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if enable_in_main_menu is not UNSET:
            field_dict["EnableInMainMenu"] = enable_in_main_menu
        if menu_section is not UNSET:
            field_dict["MenuSection"] = menu_section
        if menu_icon is not UNSET:
            field_dict["MenuIcon"] = menu_icon
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if plugin_id is not UNSET:
            field_dict["PluginId"] = plugin_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        enable_in_main_menu = d.pop("EnableInMainMenu", UNSET)

        def _parse_menu_section(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        menu_section = _parse_menu_section(d.pop("MenuSection", UNSET))

        def _parse_menu_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        menu_icon = _parse_menu_icon(d.pop("MenuIcon", UNSET))

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("DisplayName", UNSET))

        def _parse_plugin_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        plugin_id = _parse_plugin_id(d.pop("PluginId", UNSET))

        configuration_page_info = cls(
            name=name,
            enable_in_main_menu=enable_in_main_menu,
            menu_section=menu_section,
            menu_icon=menu_icon,
            display_name=display_name,
            plugin_id=plugin_id,
        )

        return configuration_page_info
