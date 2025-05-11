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
        return self.raw_data.get("value_raw")

    @temperature.setter
    def temperature(self, new_value: int) -> None:
        """Write the temperature."""
        self.raw_data["value_raw"] = new_value


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
        return self.raw_data.get("zone")

    @property
    def min(self) -> int | None:
        """Return min value."""
        return self.raw_data.get("min")

    @property
    def max(self) -> int | None:
        """Return max value."""
        return self.raw_data.get("max")


class MielePlateStep:
    """Model of plate step."""

    def __init__(self, raw_data: dict) -> None:
        """Initialize MielePlateStep."""
        self.raw_data = raw_data

    @property
    def raw(self) -> dict:
        """Return raw data."""
        return self.raw_data

    @property
    def value_raw(self) -> int | None:
        """Return raw value data."""
        return self.raw_data.get("value_raw")

    @property
    def value_localized(self) -> str | None:
        """Return localized value."""
        return self.raw_data.get("value_localized")


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
        try:
            ret_val = str(self.raw_data["ident"]["deviceIdentLabel"]["fabNumber"])
        except KeyError:
            ret_val = ""
        return ret_val

    @property
    def device_type(self) -> int:
        """Return the type of the device."""
        try:
            ret_val = self.raw_data["ident"]["type"]["value_raw"]
        except KeyError:
            ret_val = 0
        return ret_val

    @property
    def device_type_localized(self) -> str:
        """Return the type of the device."""
        try:
            ret_val = self.raw_data["ident"]["type"]["value_localized"]
        except KeyError:
            ret_val = ""
        return ret_val

    @property
    def device_name(self) -> str:
        """Return the name of the device."""
        try:
            ret_val = self.raw_data["ident"]["deviceName"]
        except KeyError:
            ret_val = ""
        return ret_val

    @property
    def tech_type(self) -> str:
        """Return the tech type of the device."""
        try:
            ret_val = self.raw_data["ident"]["deviceIdentLabel"]["techType"]
        except KeyError:
            ret_val = ""
        return ret_val

    @property
    def xkm_tech_type(self) -> str:
        """Return the xkm tech type of the device."""
        try:
            ret_val = self.raw_data["ident"]["xkmIdentLabel"]["techType"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def xkm_release_version(self) -> str:
        """Return the xkm release version of the device."""
        try:
            ret_val = self.raw_data["ident"]["xkmIdentLabel"]["releaseVersion"]
        except KeyError:
            ret_val = ""
        return ret_val

    @property
    def state_program_id(self) -> int:
        """Return the program ID of the device."""
        try:
            # Note that ProgramID is spelled this way in API data
            ret_val = self.raw_data["state"]["ProgramID"]["value_raw"]
        except KeyError:
            ret_val = 0
        return ret_val

    @property
    def state_program_id_localized(self) -> str:
        """Return the program ID of the device."""
        try:
            ret_val = self.raw_data["state"]["ProgramID"]["value_localized"]
        except KeyError:
            ret_val = ""
        return ret_val

    @property
    def state_status(self) -> int:
        """Return the status of the device."""
        try:
            ret_val = self.raw_data["state"]["status"]["value_raw"]
        except KeyError:
            ret_val = 0
        return ret_val

    @property
    def state_status_localized(self) -> str:
        """Return the status of the device."""
        try:
            ret_val = self.raw_data["state"]["status"]["value_localized"]
        except KeyError:
            ret_val = ""
        return ret_val

    @property
    def state_program_type(self) -> int:
        """Return the program type of the device."""
        try:
            ret_val = self.raw_data["state"]["programType"]["value_raw"]
        except KeyError:
            ret_val = 0
        return ret_val

    @property
    def state_program_type_localized(self) -> str:
        """Return the program type of the device."""
        try:
            ret_val = self.raw_data["state"]["programType"]["value_localized"]
        except KeyError:
            ret_val = ""
        return ret_val

    @property
    def state_program_phase(self) -> int:
        """Return the program phase of the device."""
        try:
            ret_val = self.raw_data["state"]["programPhase"]["value_raw"]
        except KeyError:
            ret_val = 0
        return ret_val

    @property
    def state_program_phase_localized(self) -> str:
        """Return the program phase of the device."""
        try:
            ret_val = self.raw_data["state"]["programPhase"]["value_localized"]
        except KeyError:
            ret_val = ""
        return ret_val

    @property
    def state_remaining_time(self) -> list[int]:
        """Return the remaining time of the device."""
        try:
            ret_val = self.raw_data["state"]["remainingTime"]
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def state_start_time(self) -> list[int]:
        """Return the start time of the device."""
        try:
            ret_val = self.raw_data["state"]["startTime"]
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def state_target_temperature(self) -> list[MieleTemperature]:
        """Return the target temperature of the device."""
        try:
            ret_val = [
                MieleTemperature(temp)
                for temp in self.raw_data["state"]["targetTemperature"]
            ]
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def state_core_target_temperature(self) -> list[MieleTemperature]:
        """Return the core target temperature of the device."""
        try:
            ret_val = [
                MieleTemperature(temp)
                for temp in self.raw_data["state"]["coreTargetTemperature"]
            ]
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def state_temperatures(self) -> list[MieleTemperature]:
        """Return list of all temperatures."""
        try:
            ret_val = [
                MieleTemperature(temp) for temp in self.raw_data["state"]["temperature"]
            ]
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def state_core_temperature(self) -> list[MieleTemperature]:
        """Return the core temperature of the device."""
        try:
            ret_val = [
                MieleTemperature(temp)
                for temp in self.raw_data["state"]["coreTemperature"]
            ]
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def state_signal_info(self) -> bool | None:
        """Return the signal info of the device."""
        try:
            ret_val = self.raw_data["state"]["signalInfo"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def state_signal_failure(self) -> bool | None:
        """Return the signal failure of the device."""
        try:
            ret_val = self.raw_data["state"]["signalFailure"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def state_signal_door(self) -> bool | None:
        """Return the signal door of the device."""
        try:
            ret_val = self.raw_data["state"]["signalDoor"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def state_full_remote_control(self) -> bool | None:
        """Return the remote control enable of the device."""
        try:
            ret_val = self.raw_data["state"]["remoteEnable"]["fullRemoteControl"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def state_smart_grid(self) -> bool | None:
        """Return the smart grid of the device."""
        try:
            ret_val = self.raw_data["state"]["remoteEnable"]["smartGrid"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def state_mobile_start(self) -> bool | None:
        """Return the mobile start of the device."""
        try:
            ret_val = self.raw_data["state"]["remoteEnable"]["mobileStart"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def state_ambient_light(self) -> int | None:
        """Return the ambient light of the device."""
        try:
            ret_val = self.raw_data["state"]["ambientLight"]
        except KeyError:
            ret_val = None
        return ret_val

    @state_ambient_light.setter
    def state_ambient_light(self, new_value: bool) -> None:
        """Set the ambient light state."""
        self.raw_data["state"]["ambientLight"] = new_value

    @property
    def state_light(self) -> int | None:
        """Return the light of the device."""
        try:
            ret_val = self.raw_data["state"]["light"]
        except KeyError:
            ret_val = None
        return ret_val

    @state_light.setter
    def state_light(self, new_value: int) -> None:
        """Set the light state."""
        self.raw_data["state"]["light"] = new_value

    @property
    def state_elapsed_time(self) -> list[int]:
        """Return the elapsed time of the device."""
        try:
            ret_val = self.raw_data["state"]["elapsedTime"]
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def state_spinning_speed(self) -> int | None:
        """Return the spinning speed of the device."""
        try:
            ret_val = self.raw_data["state"]["spinningSpeed"]["value_raw"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def state_drying_step(self) -> int | None:
        """Return the drying step of the device."""
        try:
            ret_val = self.raw_data["state"]["dryingStep"]["value_raw"]
        except KeyError:
            ret_val = None
        return ret_val

    @state_drying_step.setter
    def state_drying_step(self, new_value: int) -> None:
        """Set the drying state."""
        self.raw_data["state"]["dryingStep"]["value_raw"] = new_value

    @property
    def state_ventilation_step(self) -> int | None:
        """Return the ventilation step of the device."""
        try:
            ret_val = self.raw_data["state"]["ventilationStep"]["value_raw"]
        except KeyError:
            ret_val = None
        return ret_val

    @state_ventilation_step.setter
    def state_ventilation_step(self, new_value: int) -> None:
        """Set the ventilation state."""
        self.raw_data["state"]["ventilationStep"]["value_raw"] = new_value

    @property
    def state_plate_step(self) -> list[MielePlateStep]:
        """Return the plate step of the device."""
        try:
            ret_val = [
                MielePlateStep(plate) for plate in self.raw_data["state"]["plateStep"]
            ]
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def state_eco_feedback(self) -> dict | None:
        """Return the eco feedback of the device."""
        try:
            ret_val = self.raw_data["state"]["ecoFeedback"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def current_water_consumption(self) -> float | None:
        """Return the current water consumption of the device."""
        if self.state_eco_feedback is None:
            return None
        try:
            ret_val = self.raw_data["state"]["ecoFeedback"].get(
                "currentWaterConsumption"
            )["value"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def current_energy_consumption(self) -> float | None:
        """Return the current energy consumption of the device."""
        if self.state_eco_feedback is None:
            return None
        try:
            ret_val = self.raw_data["state"]["ecoFeedback"].get(
                "currentEnergyConsumption"
            )["value"]
        except KeyError:
            ret_val = None
        return ret_val

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
        try:
            ret_val = self.raw_data["state"]["batteryLevel"]
        except KeyError:
            ret_val = None
        return ret_val


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
        try:
            ret_val = list(self.raw_data["modes"])
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def process_actions(self) -> list[int]:
        """Return list of process actions."""
        try:
            ret_val = list(self.raw_data["processAction"])
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def light(self) -> list[int]:
        """Return list of light actions."""
        try:
            ret_val = list(self.raw_data["light"])
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def ambient_light(self) -> list[int]:
        """Return list of ambient light actions."""
        try:
            ret_val = list(self.raw_data["ambientLight"])
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def start_time(self) -> list[int]:
        """Return list of start time actions."""
        try:
            ret_val = list(self.raw_data["start_time"])
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def ventilation_setp(self) -> list[int]:
        """Return list of ventilation step actions."""
        try:
            ret_val = list(self.raw_data["ventilationStep"])
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def program_id(self) -> list[int]:
        """Return list of program id actions."""
        try:
            ret_val = list(self.raw_data["programId"])
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def run_on_time(self) -> list[int]:
        """Return list of run on time actions."""
        try:
            ret_val = list(self.raw_data["runOnTime"])
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def target_temperature(self) -> list[MieleActionTargetTemperature]:
        """Return list of target temperature actions."""
        try:
            ret_val = [
                MieleActionTargetTemperature(temp)
                for temp in self.raw_data["targetTemperature"]
            ]
        except KeyError:
            ret_val = []
        return ret_val

    @property
    def power_on_enabled(self) -> bool:
        """Return powerOn enabled."""
        return self.raw_data.get("powerOn", False)

    @power_on_enabled.setter
    def power_on_enabled(self, value: bool) -> None:
        """Return powerOn enabled."""
        self.raw_data["powerOn"] = value

    @property
    def power_off_enabled(self) -> bool:
        """Return powerOff enabled."""
        return self.raw_data.get("powerOff", False)

    @power_off_enabled.setter
    def power_off_enabled(self, value: bool) -> None:
        """Return powerOff enabled."""
        self.raw_data["powerOff"] = value

    @property
    def device_name_enabled(self) -> bool:
        """Return deviceName enabled."""
        return self.raw_data.get("deviceName", False)


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
        return self.raw_data.get("programId")

    @property
    def program_name(self) -> str | None:
        """Return the name of the program."""
        return self.raw_data.get("program")

    @property
    def parameters(self) -> dict | None:
        """Return the parameters of the program."""
        return self.raw_data.get("parameters")

    @property
    def temperature(self) -> dict | None:
        """Return the temperature parameter of the program."""
        try:
            ret_val = self.raw_data["parameters"].get("temperature")
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def temperature_min(self) -> int | None:
        """Return the min temperature parameter of the program."""
        return self.raw_data["parameters"]["temperature"]["min"]

    @property
    def temperature_max(self) -> int | None:
        """Return the max temperature parameter of the program."""
        try:
            ret_val = self.raw_data["parameters"]["temperature"]["max"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def temperature_step(self) -> int | None:
        """Return the step temperature parameter of the program."""
        try:
            ret_val = self.raw_data["parameters"]["temperature"]["step"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def temperature_mandatory(self) -> bool | None:
        """Return the mandatory temperature parameter of the program."""
        try:
            ret_val = self.raw_data["parameters"]["temperature"]["mandatory"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def duration_min(self) -> list[int] | None:
        """Return the mandatory min parameter of the program."""
        try:
            ret_val = self.raw_data["parameters"]["duration"]["min"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def duration_max(self) -> list[int] | None:
        """Return the duration max parameter of the program."""
        try:
            ret_val = self.raw_data["parameters"]["duration"]["max"]
        except KeyError:
            ret_val = None
        return ret_val

    @property
    def duration_mandatory(self) -> bool | None:
        """Return the mandatory duration parameter of the program."""
        try:
            ret_val = self.raw_data["parameters"]["duration"]["mandatory"]
        except KeyError:
            ret_val = None
        return ret_val
