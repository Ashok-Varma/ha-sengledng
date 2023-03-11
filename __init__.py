"""A next-gen integration for Sengled lights."""
from __future__ import annotations

import logging

import voluptuous as vol

from homeassistant.const import CONF_PASSWORD, CONF_USERNAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv, discovery
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_USERNAME): cv.string,
                vol.Required(CONF_PASSWORD): cv.string,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)
PLATFORMS = [Platform.LIGHT]


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the platform API."""
    _LOGGER.warning("Setup package")
    hass.data[DOMAIN] = {}

    discovery.load_platform(hass, Platform.LIGHT, DOMAIN, {}, config)

    return True
