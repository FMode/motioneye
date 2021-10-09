import os
import logging
from motioneye import settings

path = os.path.join(settings.CONF_PATH, 'plugins.py')
if os.access(path, os.X_OK):
    logging.info("loading %s"%(path))
    import importlib.util
    spec = importlib.util.spec_from_file_location("motioneye_plugins", path)
    motioneye_plugins = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(motioneye_plugins)
else:
    motioneye_plugins==None