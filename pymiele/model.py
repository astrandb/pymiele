"""Data models for Miele API."""
# Todo: Move to pymiele when complete and stable

from __future__ import annotations


class MieleDevices:
    """Data for all devices from API."""

    def __init__(self, raw_data: dict) -> None:
        """Initialize MieleDevices."""
        self.raw_data = raw_data

    @property
    def devices(self) -> list[str]:
        """Return list of all devices."""

        return list(self.raw_data.keys())


class MieleDevice:
    """Data for a single device from API."""

    def __init__(self, raw_data: dict) -> None:
        """Initialize MieleDevice."""
        self.raw_data = raw_data

    @property
    def raw(self) -> dict:
        """Return raw data."""
        return self.raw_data

    @property
    def fab_number(self) -> str:
        """Return the ID of the device."""
        return str(self.raw_data["ident"]["deviceIdentLabel"]["fabNumber"])

    @property
    def device_type(self) -> int:
        """Return the type of the device."""
        return self.raw_data["ident"]["type"]["value_raw"]

    @property
    def device_type_localized(self) -> str:
        """Return the type of the device."""
        return self.raw_data["ident"]["type"]["value_localized"]

    @property
    def device_name(self) -> str:
        """Return the name of the device."""
        return self.raw_data["ident"]["deviceName"]

    @property
    def tech_type(self) -> str:
        """Return the tech type of the device."""
        return self.raw_data["ident"]["deviceIdentLabel"]["techType"]

    @property
    def xkm_tech_type(self) -> str:
        """Return the xkm tech type of the device."""
        return self.raw_data["ident"]["xkmIdentLabel"]["techType"]

    @property
    def xkm_release_version(self) -> str:
        """Return the xkm release version of the device."""
        return self.raw_data["ident"]["xkmIdentLabel"]["releaseVersion"]

    @property
    def state_program_id(self) -> int:
        """Return the program ID of the device."""
        return self.raw_data["state"]["ProgramID"]["value_raw"]

    @property
    def state_status(self) -> int:
        """Return the status of the device."""
        return self.raw_data["state"]["status"]["value_raw"]

    @property
    def state_program_type(self) -> int:
        """Return the program type of the device."""
        return self.raw_data["state"]["programType"]["value_raw"]

    @property
    def state_program_phase(self) -> int:
        """Return the program phase of the device."""
        return self.raw_data["state"]["programPhase"]["value_raw"]

    @property
    def state_remaining_time(self) -> list[int]:
        """Return the remaining time of the device."""
        return self.raw_data["state"]["remainingTime"]

    @property
    def state_start_time(self) -> list[int]:
        """Return the start time of the device."""
        return self.raw_data["state"]["startTime"]

    @property
    def state_target_temperature(self) -> list[dict]:
        """Return the target temperature of the device."""
        return self.raw_data["state"]["targetTemperature"]

    @property
    def state_core_target_temperature(self) -> list[dict]:
        """Return the core target temperature of the device."""
        return self.raw_data["state"]["coreTargetTemperature"]

    @property
    def state_temperature(self) -> list[int]:
        """Return the temperature of the device."""
        return [temp["value_raw"] for temp in self.raw_data["state"]["temperature"]]

    @property
    def state_temperature_1(self) -> int:
        """Return the temperature in zone 1 of the device."""
        return self.raw_data["state"]["temperature"][0]["value_raw"]

    @property
    def state_temperature_2(self) -> int:
        """Return the temperature in zone 2 of the device."""
        return self.raw_data["state"]["temperature"][1]["value_raw"]

    @property
    def state_temperature_3(self) -> int:
        """Return the temperature in zone 3 of the device."""
        return self.raw_data["state"]["temperature"][2]["value_raw"]

    @property
    def state_core_temperature(self) -> list[dict]:
        """Return the core temperature of the device."""
        return self.raw_data["state"]["coreTemperature"]

    @property
    def state_core_temperature_1(self) -> list[dict]:
        """Return the core temperature in zone 1 of the device."""
        return self.raw_data["state"]["coreTemperature"][0]["value_raw"]

    @property
    def state_core_temperature_2(self) -> list[dict]:
        """Return the core temperature in zone 2 of the device."""
        return self.raw_data["state"]["coreTemperature"][1]["value_raw"]

    @property
    def state_signal_info(self) -> bool:
        """Return the signal info of the device."""
        return self.raw_data["state"]["signalInfo"]

    @property
    def state_signal_failure(self) -> bool:
        """Return the signal failure of the device."""
        return self.raw_data["state"]["signalFailure"]

    @property
    def state_signal_door(self) -> bool:
        """Return the signal door of the device."""
        return self.raw_data["state"]["signalDoor"]

    @property
    def state_full_remote_control(self) -> bool:
        """Return the remote control enable of the device."""
        return self.raw_data["state"]["remoteEnable"]["fullRemoteControl"]

    @property
    def state_smart_grid(self) -> bool:
        """Return the smart grid of the device."""
        return self.raw_data["state"]["remoteEnable"]["smartGrid"]

    @property
    def state_mobile_start(self) -> bool:
        """Return the mobile start of the device."""
        return self.raw_data["state"]["remoteEnable"]["mobileStart"]

    @property
    def state_ambient_light(self) -> bool:
        """Return the ambient light of the device."""
        return self.raw_data["state"]["ambientLight"]

    @property
    def state_light(self) -> bool:
        """Return the light of the device."""
        return self.raw_data["state"]["light"]

    @property
    def state_elapsed_time(self) -> list[int]:
        """Return the elapsed time of the device."""
        return self.raw_data["state"]["elapsedTime"]

    @property
    def state_spinning_speed(self) -> int | None:
        """Return the spinning speed of the device."""
        return self.raw_data["state"]["spinningSpeed"]

    @property
    def state_drying_step(self) -> int | None:
        """Return the drying step of the device."""
        return self.raw_data["state"]["dryingStep"]

    @property
    def state_ventilation_step(self) -> int | None:
        """Return the ventilation step of the device."""
        return self.raw_data["state"]["ventilationStep"]

    @property
    def state_plate_step(self) -> list[dict]:
        """Return the plate step of the device."""
        return self.raw_data["state"]["plateStep"]

    @property
    def state_eco_feedback(self) -> dict | None:
        """Return the eco feedback of the device."""
        return self.raw_data["state"]["ecoFeedback"]

    @property
    def state_battery_level(self) -> int | None:
        """Return the battery level of the device."""
        return self.raw_data["state"]["batteryLevel"]


class MieleAction:
    """Actions for Miele devices."""

    def __init__(self, raw_data: dict) -> None:
        """Initialize MieleAction."""
        self.raw_data = raw_data

    # Todo : Add process actions
    @property
    def raw(self) -> dict:
        """Return raw data."""
        return self.raw_data

    @property
    def actions(self) -> list[str]:
        """Return list of all actions."""
        return list(self.raw_data.keys())

    @property
    def modes(self) -> list[int]:
        """Return list of modes."""
        return list(self.raw_data["modes"])

    @property
    def process_actions(self) -> list[int]:
        """Return list of process actions."""
        return list(self.raw_data["processAction"])

    @property
    def light(self) -> list[int]:
        """Return list of light actions."""
        return list(self.raw_data["light"])

    @property
    def ambient_light(self) -> list[int]:
        """Return list of ambient light actions."""
        return list(self.raw_data["ambientLight"])

    @property
    def start_time(self) -> list[int]:
        """Return list of start time actions."""
        return list(self.raw_data["start_time"])

    @property
    def ventilation_setp(self) -> list[int]:
        """Return list of ventilation step actions."""
        return list(self.raw_data["ventilationStep"])

    @property
    def program_id(self) -> list[int]:
        """Return list of program id actions."""
        return list(self.raw_data["programId"])

    @property
    def runOnTime(self) -> list[int]:
        """Return list of run on time actions."""
        return list(self.raw_data["runOnTime"])

    @property
    def target_temperature(self) -> list[dict]:
        """Return list of target temperature actions."""
        return list(self.raw_data["targetTemperature"])

    @property
    def power_on_enabled(self) -> bool:
        """Return powerOn enabled."""
        return self.raw_data["powerOn"]

    @property
    def power_off_enabled(self) -> bool:
        """Return powerOff enabled."""
        return self.raw_data["powerOff"]

    @property
    def device_name_enabled(self) -> bool:
        """Return deviceName enabled."""
        return self.raw_data["deviceName"]
