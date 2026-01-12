"""Sensor platform for PanaVista Calendar integration."""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, SENSOR_PREFIX
from . import PanaVistaCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up PanaVista sensors from a config entry."""
    coordinator: PanaVistaCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[SensorEntity] = [
        PanaVistaConfigSensor(coordinator, entry),
        PanaVistaUpcomingEventsSensor(coordinator, entry),
    ]

    async_add_entities(entities)


class PanaVistaConfigSensor(CoordinatorEntity, SensorEntity):
    """Sensor that exposes the PanaVista configuration."""

    def __init__(self, coordinator: PanaVistaCoordinator, entry: ConfigEntry) -> None:
        """Initialize the config sensor."""
        super().__init__(coordinator)
        self._entry = entry
        self._attr_name = f"{SENSOR_PREFIX}_config"
        self._attr_unique_id = f"{entry.entry_id}_config"
        self._attr_icon = "mdi:calendar-multiple"

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        return "configured"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        data = self.coordinator.data or {}
        return {
            "calendars": data.get("calendars", []),
            "events": data.get("events", []),
            "display": self.coordinator.display_config,
            "version": self._entry.version,
        }


class PanaVistaUpcomingEventsSensor(CoordinatorEntity, SensorEntity):
    """Sensor that shows upcoming events count."""

    def __init__(self, coordinator: PanaVistaCoordinator, entry: ConfigEntry) -> None:
        """Initialize the upcoming events sensor."""
        super().__init__(coordinator)
        self._entry = entry
        self._attr_name = f"{SENSOR_PREFIX}_upcoming_events"
        self._attr_unique_id = f"{entry.entry_id}_upcoming_events"
        self._attr_icon = "mdi:calendar-clock"

    @property
    def state(self) -> int:
        """Return the count of upcoming events."""
        if not self.coordinator.data:
            return 0
        return len(self.coordinator.data.get("upcoming_events", []))

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        if not self.coordinator.data:
            return {"events": [], "last_updated": datetime.now().isoformat()}

        upcoming = self.coordinator.data.get("upcoming_events", [])
        return {
            "events": upcoming,
            "last_updated": datetime.now().isoformat(),
        }
