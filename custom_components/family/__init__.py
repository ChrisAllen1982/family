from homeassistant import core

from homeassistant.const import (
    ATTR_EDITABLE,
    ATTR_GPS_ACCURACY,
    ATTR_ID,
    ATTR_LATITUDE,
    ATTR_LONGITUDE,
)

from homeassistant.helpers import collection

from homeassistant.helpers.restore_state import RestoreEntity

from collections.abc import Callable
import logging
from typing import Any

from homeassistant.core import callback

async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Family component."""
    # @TODO: Add setup code.
    return True

ATTR_SOURCE = "source"
ATTR_TEST = "test"
ATTR_USER_ID = "user_id"
ATTR_DEVICE_TRACKERS = "device_trackers"

CONF_DEVICE_TRACKERS = "device_trackers"
CONF_USER_ID = "user_id"
CONF_PICTURE = "picture"


class Person(
    collection.CollectionEntity,
    RestoreEntity,
):

    @callback
    def _update_extra_state_attributes(self) -> None:
        """Update extra state attributes."""
        data: dict[str, Any] = {
            ATTR_EDITABLE: self.editable,
            ATTR_ID: self.unique_id,
            ATTR_DEVICE_TRACKERS: self.device_trackers,
        }

        if self._latitude is not None:
            data[ATTR_LATITUDE] = self._latitude
        if self._longitude is not None:
            data[ATTR_LONGITUDE] = self._longitude
        if self._gps_accuracy is not None:
            data[ATTR_GPS_ACCURACY] = self._gps_accuracy
        if self._source is not None:
            data[ATTR_SOURCE] = self._source
        if (user_id := self._config.get(CONF_USER_ID)) is not None:
            data[ATTR_USER_ID] = user_id

            data[ATTR_TEST] = "TEST"

        self._attr_extra_state_attributes = data