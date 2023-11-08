from pluggy import PluginManager

# singleton class 

class MetaPluginManager(type):
    _plugin_manager: PluginManager = None

    @staticmethod
    def get_plugin_manager():
        if not MetaPluginManager._plugin_manager:
            MetaPluginManager._plugin_manager = PluginManager('demo')
            # MetaPluginManager._plugin_manager.add_hookspecs(_hooks)
           

        return MetaPluginManager._plugin_manager

    def __getattr__(cls, attr):
        pm = MetaPluginManager.get_plugin_manager()
        return getattr(pm, attr)


class plugin_manager(metaclass=MetaPluginManager):
    pass

# source: allure 
