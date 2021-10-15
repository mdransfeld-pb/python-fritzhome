# -*- coding: utf-8 -*-

import logging

from .fritzhomedevicebase import FritzhomeDeviceBase
from .fritzhomedevicefeatures import FritzhomeDeviceFeatures

_LOGGER = logging.getLogger(__name__)


class FritzhomeDeviceBlind(FritzhomeDeviceBase):
    """The Fritzhome Device class."""

    level = None
    level_percentage = None
    alert_state = None

    def _update_from_node(self, node):
        super()._update_from_node(node)
        if self.present is False:
            return

        if self.has_blind:
            self._update_blind_from_node(node)

    # Blind
    @property
    def has_blind(self):
        """Check if the device has blind function."""
        return self._has_feature(FritzhomeDeviceFeatures.BLIND)

    def _update_blind_from_node(self, node):
        level_element = node.find("levelcontrol")
        try:
            self.level = self.get_node_value_as_int(level_element, "level")
            self.level_percentage = self.get_node_value_as_int(level_element, "levelpercentage")
        except ValueError:
            pass

        alert_element = node.find("alert")
        try:
            self.alert_state = self.get_node_value_as_int(level_element, "state")
        except ValueError:
            pass

    def set_blind_open(self):
        """Set the blind to open state."""
        return self._fritz.set_blind_open(self.ain)

    def set_blind_close(self):
        """"Set the blind to close state."""
        return self._fritz.set_blind_close(self.ain)

    def set_blind_stop(self):
        """Set the blind to stop state."""
        return self._fritz.set_blind_stop(self.ain)

    def set_level_percentage(self, level):
        """Set height in interval [0,100]."""
        return self._fritz.set_level_percentage(self.ain, level)
