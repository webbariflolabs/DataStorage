# data_storage.py
import octoprint.plugin

class DataStoragePlugin(octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.ProgressPlugin):

    def __init__(self):
        self._complete_data = []

    def on_print_progress(self, storage, path, progress):
        data = dict(location=storage,
                    path=path,
                    progress=progress)
        self._complete_data.append(data)

        # Write data to file in append mode
        with open("print_progress.txt", "a"):
            f.write(str(self._complete_data) + "\n")

        # Print the data for verification
        self._logger.info("Print Progress Data: {}".format(self._complete_data))

    
__plugin_name__ = "DataStorage"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    plugin = DataStoragePlugin()
    global __plugin_implementation__
    __plugin_implementation__ = plugin
