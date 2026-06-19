#here's all the shortcuts of CDOS
from logging import critical

from CDOS_start import error_print, safetymode, last_command

try:
    import logging
except ImportError:
    error_print(0,"","")
else:
    LOGGER: logging.Logger = logging.getLogger(__name__)
    LOGGER.addHandler(logging.StreamHandler())
    LOGGER.setLevel(logging.INFO)
from logging import critical
try :
    import keyboard
except ImportError:
    error_print(1,"keyboard","start")
    LOGGER.critical("shortcuts are not available due to an import error, please restart CDOS and retry")
while True:
    keyboard.add_hotkey("arrow up",last_command)