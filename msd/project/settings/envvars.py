from msd.core.utils.collections import deep_update
from msd.core.utils.settings import get_settings_from_environment

# globals() is a dictionary of global variables

deep_update(globals(), get_settings_from_environment(ENV_VAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
