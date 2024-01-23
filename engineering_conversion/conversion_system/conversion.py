from typing import Dict
from abc import ABC, abstractmethod

class ConversionStrategy(ABC):
    @abstractmethod
    def convert(self, number: float, conversion_unit: str) -> bool:
        pass

class BaseConversion(ConversionStrategy):
    def __init__(self, conversion_rates: Dict[str, ConversionStrategy]) -> None:
        self.conversion_rates = conversion_rates

    def convert(self, number: float, conversion_unit: str) -> bool:
        rate = self.conversion_rates.get(conversion_unit)
        if rate is not None:
            result = number * rate
            print(f"{number} {conversion_unit} is equivalent {result}")
            return True
        else:
            print(f"Conversion unit {conversion_unit} not found in the converter.")
            return False

class LengthConversion(BaseConversion):
  length_conversion_rates: Dict[str, float] = {
      "inch to foot": 1/12,
      "foot to inch": 12,
      "foot to yard": 1/3,
      "yard to foot": 3,
      "foot to mile": 1/5280,
      "mile to foot": 5280
  }

class AreaConversion(BaseConversion):
  area_conversion_rates: Dict[str, float] = {
      "square–millimeter to square–centimeter": 0.01,
      "square–centimeter to square–millimeter": 100,
      "square–meter to square–centimeter": 10000,
  }

class VolumeConversion(BaseConversion):
  volume_conversion_rates: Dict[str, float] = {
    "cubic‐meter to liter": 1000,
    "liter‐cubic to meter": 1/1000
  }

class TimeConversion(BaseConversion):
  time_conversion_rates: Dict[str, float] = {
   "second to minute": 1/60,
   "minute to second": 60
  }

class MassConversion(BaseConversion):
  mass_conversion_rates: Dict[str, float] = {
    "kilogram to pound": 2.20462,
    "pound to kilogram": 1/2.20462
  }

class AngleConversion(BaseConversion):
  angle_conversion_rates: Dict[str, float] = {
    "degree to radian": 0.017453393,
    "radian to degree": 57.29577951
  }

class ForceConversion(BaseConversion):
  force_conversion_rates: Dict[str, float] = {
   "newton to dyne": 100000,
   "dyne to newton": 1/100000
  }

class EnergyConversion(BaseConversion):
  energy_conversion_rates: Dict[str, float] = {
      "joule to calorie": 1/4.184,
      "calorie to joule": 4.184
  }

class PowerConversion(BaseConversion):
  power_conversion_rates = {
    "calorie/second to watt": 4.186,
    "watt to calorie/second": 1/4.186
  }

class DensityConversion(BaseConversion):
  density_conversion_rates: Dict[str, float]  = {
    "slug/cubic–foot to kilogram/cubic–meter": 515.4,
    "kilogram/cubic–meter to slug/cubic–foot": 1/515.4
  }

class ViscosityConversion(BaseConversion):
  viscosity_conversion_rates: Dict[str, float] = {
    "pascal.second to poise": 1/0.1,
    "poise to pascal.second": 0.1
  }

class TorqueConversion(BaseConversion):
  torque_conversion_rates: Dict[str, float] = {
   "newton meter to dyne meter": 100000,
   "dyne meter to newton meter": 1/100000
 }
  
class VelocityConversion(BaseConversion):
  velocity_conversion_rates: Dict[str, float] = {
   "meter/second to knot": 1.9438444924406,
   "knot to meter/second": 1/1.9438444924406
 }

class AngularVelocityConversion(BaseConversion):
  angular_velocity_conversion_rates: Dict[str, float] = {
   "meter/second to knot": 1.9438444924406,
   "knot to meter/second": 1/1.9438444924406
 }

class AccelerationConversion(BaseConversion):
  acceleration_conversion_rates: Dict[str, float] = {
   "meter/square second to kilometer/square second": 0.001,
   "kilometer/square second to meter/square second": 1/0.001
 }

class TemperatureConversion(BaseConversion):
  temperature_conversion_rates: Dict[str, float] = {
  "celcius to fahrenheit": 33.8,
  "fahrenheit to celcius": 1/33.8
 }

class AngularAccelerationConversion(BaseConversion):
  angular_acceleration_conversion_rates: Dict[str, float] = {
   "radian/square second to revolution/minute/second": 9.549296586,
   "revolution/minute/second to radian/square second": 1/9.549296586
 }

class PressureConversion(BaseConversion):
  pressure_conversion_rates: Dict[str, float] = {
   "bar to pascal": 100000,
   "pascal to bar ": 1/100000
 }
  
class SpecificVolumeConversion(BaseConversion):
 specific_volume_conversion_rates: Dict[str, float] = {
  "cubic meter/kilogram to liter/kilogram": 1000,
  "liter/kilogram to cubic meter/kilogram": 1/1000
 }
  
class MomentOfInertiaConversion(BaseConversion):
  moment_of_inertia_conversion_rates: Dict[str, float] = {
   "gram square centimeter to kilogram square meter": 10000000,
   "kilogram square meter to gram square centimeter": 1/10000000
 }
class MomentOfForceConversion(BaseConversion):
  moment_of_force_conversion_rates: Dict[str, float] = {
   "kilonewton meter to newton meter": 1/1000,
   "newton meter to kilonewton meter": 1000
 }