"""Data models for Miele API."""

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


class MieleTemperature:
    """A model of temperature data."""

    def __init__(self, raw_data: dict) -> None:
        """Initialize MieleTemperature."""
        self.raw_data = raw_data

    @property
    def raw(self) -> dict:
        """Return raw data."""
        return self.raw_data

    @property
    def temperature(self) -> int | None:
        """Return temperature object."""
        return self.raw_data["value_raw"]


class MieleActionTargetTemperature:
    """A model of target temperature data."""

    def __init__(self, raw_data: dict) -> None:
        """Initialize MieleActionTargetTemperature."""
        self.raw_data = raw_data

    @property
    def raw(self) -> dict:
        """Return raw data."""
        return self.raw_data

    @property
    def zone(self) -> int | None:
        """Return zone value."""
        return self.raw_data["zone"]

    @property
    def min(self) -> int | None:
        """Return min value."""
        return self.raw_data["min"]

    @property
    def max(self) -> int | None:
        """Return max value."""
        return self.raw_data["max"]


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
    def state_target_temperature(self) -> list[MieleTemperature]:
        """Return the target temperature of the device."""
        return [
            MieleTemperature(temp)
            for temp in self.raw_data["state"]["targetTemperature"]
        ]

    @property
    def state_core_target_temperature(self) -> list[dict]:
        """Return the core target temperature of the device."""
        return [
            MieleTemperature(temp)
            for temp in self.raw_data["state"]["coretargetTemperature"]
        ]

    @property
    def state_temperatures(self) -> list[MieleTemperature]:
        """Return list of all temperatures."""

        return [
            MieleTemperature(temp) for temp in self.raw_data["state"]["temperature"]
        ]

    @property
    def state_core_temperature(self) -> list[MieleTemperature]:
        """Return the core temperature of the device."""
        return [
            MieleTemperature(temp) for temp in self.raw_data["state"]["coreTemperature"]
        ]

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
    def state_ambient_light(self) -> int:
        """Return the ambient light of the device."""
        return self.raw_data["state"]["ambientLight"]

    @state_ambient_light.setter
    def state_ambient_light(self, new_value: bool) -> None:
        """Set the ambient light state."""
        self.raw_data["state"]["ambientLight"] = new_value

    @property
    def state_light(self) -> int:
        """Return the light of the device."""
        return self.raw_data["state"]["light"]

    @state_light.setter
    def state_light(self, new_value: int) -> None:
        """Set the light state."""
        self.raw_data["state"]["light"] = new_value

    @property
    def state_elapsed_time(self) -> list[int]:
        """Return the elapsed time of the device."""
        return self.raw_data["state"]["elapsedTime"]

    @property
    def state_spinning_speed(self) -> int | None:
        """Return the spinning speed of the device."""
        return self.raw_data["state"]["spinningSpeed"]["value_raw"]

    @property
    def state_drying_step(self) -> int | None:
        """Return the drying step of the device."""
        return self.raw_data["state"]["dryingStep"]["value_raw"]

    @state_drying_step.setter
    def state_drying_step(self, new_value: int) -> None:
        """Set the drying state."""
        self.raw_data["state"]["dryingStep"]["value_raw"] = new_value

    @property
    def state_ventilation_step(self) -> int | None:
        """Return the ventilation step of the device."""
        return self.raw_data["state"]["ventilationStep"]["value_raw"]

    @state_ventilation_step.setter
    def state_ventilation_step(self, new_value: int) -> None:
        """Set the ventilation state."""
        self.raw_data["state"]["ventilationStep"]["value_raw"] = new_value

    @property
    def state_plate_step(self) -> list[dict]:
        """Return the plate step of the device."""
        return self.raw_data["state"]["plateStep"]

    @property
    def state_eco_feedback(self) -> dict | None:
        """Return the eco feedback of the device."""
        return self.raw_data["state"]["ecoFeedback"]

    @property
    def current_water_consumption(self) -> float | None:
        """Return the current water consumption of the device."""
        if self.state_eco_feedback is None:
            return None
        return self.raw_data["state"]["ecoFeedback"].get("currentWaterConsumption")[
            "value"
        ]

    @property
    def current_energy_consumption(self) -> float | None:
        """Return the current energy consumption of the device."""
        if self.state_eco_feedback is None:
            return None
        return self.raw_data["state"]["ecoFeedback"]["currentEnergyConsumption"][
            "value"
        ]

    @property
    def water_forecast(self) -> float | None:
        """Return the water forecast of the device."""
        if self.state_eco_feedback is None:
            return None
        return self.raw_data["state"]["ecoFeedback"].get("waterForecast")

    @property
    def energy_forecast(self) -> float | None:
        """Return the energy forecast of the device."""
        if self.state_eco_feedback is None:
            return None
        return self.raw_data["state"]["ecoFeedback"].get("energyForecast")

    @property
    def state_battery_level(self) -> int | None:
        """Return the battery level of the device."""
        return self.raw_data["state"]["batteryLevel"]


class MieleAction:
    """Actions for Miele devices."""

    def __init__(self, raw_data: dict) -> None:
        """Initialize MieleAction."""
        self.raw_data = raw_data

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
        return [
            MieleActionTargetTemperature(temp)
            for temp in self.raw_data["state"]["targetTemperature"]
        ]

    @property
    def power_on_enabled(self) -> bool:
        """Return powerOn enabled."""
        return self.raw_data["powerOn"]

    @power_on_enabled.setter
    def power_on_enabled(self, value: bool) -> None:
        """Return powerOn enabled."""
        self.raw_data["powerOn"] = value

    @property
    def power_off_enabled(self) -> bool:
        """Return powerOff enabled."""
        return self.raw_data["powerOff"]

    @power_off_enabled.setter
    def power_off_enabled(self, value: bool) -> None:
        """Return powerOff enabled."""
        self.raw_data["powerOff"] = value

    @property
    def device_name_enabled(self) -> bool:
        """Return deviceName enabled."""
        return self.raw_data["deviceName"]


class MieleProgramsAvailable:
    """Model for available programs."""

    def __init__(self, raw_data: dict) -> None:
        """Initialize MieleProgramsAvailable."""
        self.raw_data = raw_data

    @property
    def programs(self) -> list[MieleProgramAvailable]:
        """Return list of all available programs."""
        return [MieleProgramAvailable(program) for program in self.raw_data]


class MieleProgramAvailable:
    """Model for available programs."""

    def __init__(self, raw_data: dict) -> None:
        """Initialize MieleProgramAvailable."""
        self.raw_data = raw_data

    @property
    def raw(self) -> dict:
        """Return raw data."""
        return self.raw_data

    @property
    def program_id(self) -> int | None:
        """Return the ID of the program."""
        return self.raw_data["programId"]

    @property
    def program_name(self) -> str | None:
        """Return the name of the program."""
        return self.raw_data["program"]

    @property
    def parameters(self) -> dict | None:
        """Return the parameters of the program."""
        return self.raw_data["parameters"]

    @property
    def temperature(self) -> dict | None:
        """Return the temperature parameter of the program."""
        return self.raw_data["parameters"].get("temperature")

    @property
    def temperature_min(self) -> int | None:
        """Return the min temperature parameter of the program."""
        return self.raw_data["parameters"]["temperature"]["min"]

    @property
    def temperature_max(self) -> int | None:
        """Return the max temperature parameter of the program."""
        return self.raw_data["parameters"]["temperature"]["max"]

    @property
    def temperature_step(self) -> int | None:
        """Return the step temperature parameter of the program."""
        return self.raw_data["parameters"]["temperature"]["step"]

    @property
    def temperature_mandatory(self) -> bool | None:
        """Return the mandatory temperature parameter of the program."""
        return self.raw_data["parameters"]["temperature"]["mandatory"]

    @property
    def duration_min(self) -> list[int] | None:
        """Return the mandatory min parameter of the program."""
        return self.raw_data["parameters"]["duration"]["min"]

    @property
    def duration_max(self) -> list[int] | None:
        """Return the duration max parameter of the program."""
        return self.raw_data["parameters"]["duration"]["max"]

    @property
    def duration_mandatory(self) -> bool | None:
        """Return the mandatory duration parameter of the program."""
        return self.raw_data["parameters"]["duration"]["mandatory"]
