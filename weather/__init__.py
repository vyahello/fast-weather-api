"""Package contains a set of interfaces to operate `weather` application."""
from pathlib import Path

__author__: str = 'Vladimir Yahello'
__email__: str = 'vyahello@gmail.com'
__license__: str = 'MIT'
__copyright__: str = f'Copyright 2021, {__author__}'
__version__: str = '0.0.0'


TEMPLATES_PATH: str = 'weather/templates/'
STATIC_FILES_PATH: str = 'weather/static/'
SETTINGS_PATH: Path = Path('settings.json')
