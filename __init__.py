# __init__.py

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = DataStoragePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
