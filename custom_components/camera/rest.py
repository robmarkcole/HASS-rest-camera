"""
Rest camera platform for use with the Home-assistant REST API.
For more details about this platform, please refer to the documentation
https://home-assistant.io/components/camera/rest/
"""
import logging
import shutil

import voluptuous as vol
import requests

from homeassistant.components.camera import Camera
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_NAME, CONF_RESOURCE)
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = 'REST camera'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_RESOURCE): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Rest camera platform."""
    add_devices([
        RestCamera(hass, config.get(CONF_RESOURCE), config.get(CONF_NAME))
    ])


class RestCamera(Camera):
    """The representation of a Demo camera."""

    def __init__(self, hass, resource, name):
        """Initialize demo camera component."""
        super().__init__()
        self._parent = hass
        self._resource = resource
        self._name = name
        self._motion_status = False

    def camera_image(self):
        """Return a still image response."""
        image_name = 'REST.jpg'
        response = requests.get(self._resource, stream=True)
        with open(image_name, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)  # Save the image.
        with open(image_name, 'rb') as file:
            return file.read()

    @property
    def name(self):
        """Return the name of this camera."""
        return self._name

    @property
    def should_poll(self):
        """Camera should poll periodically."""
        return True

    @property
    def motion_detection_enabled(self):
        """Camera Motion Detection Status."""
        return self._motion_status

    def enable_motion_detection(self):
        """Enable the Motion detection in base station (Arm)."""
        self._motion_status = True

    def disable_motion_detection(self):
        """Disable the motion detection in base station (Disarm)."""
        self._motion_status = False
