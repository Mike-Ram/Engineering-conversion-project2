from typing import Tuple, Dict, Optional
from engineering_conversion.conversion_system.conversion import (
LengthConversion, 
AreaConversion, 
VolumeConversion, 
TimeConversion, 
MassConversion, 
AngleConversion, 
ForceConversion, 
EnergyConversion, 
PowerConversion,
DensityConversion,
PowerConversion,
ViscosityConversion,
TorqueConversion,
PowerConversion,
VelocityConversion,
PowerConversion,
AngularVelocityConversion,
AccelerationConversion,
PowerConversion,
TemperatureConversion,
AngularAccelerationConversion,
PressureConversion,
SpecificVolumeConversion,
MomentOfInertiaConversion,
MomentOfForceConversion,
ConversionStrategy
)

class UnitConverter:
    def __init__(self, conversion_strategies: Dict[str, ConversionStrategy]) -> None:
        self.conversion_strategies = conversion_strategies

    def convert_unit(self, number: float, category: str) -> (int, Optional[str]):
        strategy = self.conversion_strategies.get(category)
        if strategy:
            self.print_conversion_units(strategy.conversion_rates)
            conversion_unit = input("Enter the conversion unit: ")
            return strategy.convert(number, conversion_unit)
        else:
            print(f"Conversion category {category} not supported.")
            return False

    @staticmethod
    def print_conversion_units(conversion_rates: Dict[str, float]) -> None:
        print("Please choose a conversion unit from the following:")
        print("\n".join(conversion_rates.keys()))


def get_user_input() -> Tuple[Optional[float], Optional[str]]:
  
    """This function gather inputs from user."""
  
    try:
        input_number = float(input("Enter a number: "))
        print("Hint: Make sure the category you have chosen is spelled correctly and in lowercase.")
        input_category = str(input("Choose a category (e.g. length, area, viscosity, moment of inertia, etc.): "))
        return input_number, input_category
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None, None


def main() -> None:
    print("Welcome to the Engineering Unit Converter!")

    conversion_strategies: Dict[str, ConversionStrategy] = {
        "length": LengthConversion(LengthConversion.length_conversion_rates),
        "area": AreaConversion(AreaConversion.area_conversion_rates),
        "volume": VolumeConversion(VolumeConversion.volume_conversion_rates),
         "time": TimeConversion(TimeConversion.time_conversion_rates),
         "mass": MassConversion(MassConversion.mass_conversion_rates),
         "angle": AngleConversion(AngleConversion.angle_conversion_rates),
         "force": ForceConversion(ForceConversion.force_conversion_rates),
         "energy": EnergyConversion(EnergyConversion.energy_conversion_rates),
         "power": PowerConversion(PowerConversion.power_conversion_rates),
         "density": DensityConversion(DensityConversion.density_conversion_rates),
         "viscosity": ViscosityConversion(ViscosityConversion.viscosity_conversion_rates),
         "torque": TorqueConversion(TorqueConversion.torque_conversion_rates),
         "velocity": VelocityConversion(VelocityConversion.velocity_conversion_rates),
         "angular velocity": AngularVelocityConversion(AngularVelocityConversion.angular_velocity_conversion_rates),
         "acceleration": AccelerationConversion(AccelerationConversion.acceleration_conversion_rates),
         "temperature": TemperatureConversion(TemperatureConversion.temperature_conversion_rates),
         "angular acceleration": AngularAccelerationConversion(AngularAccelerationConversion.angular_acceleration_conversion_rates),
         "pressure": PressureConversion(PressureConversion.pressure_conversion_rates),
         "specific volume": SpecificVolumeConversion(SpecificVolumeConversion.specific_volume_conversion_rates),
         "moment of inertia": MomentOfInertiaConversion(MomentOfInertiaConversion.moment_of_inertia_conversion_rates),
         "moment of force": MomentOfForceConversion(MomentOfForceConversion.moment_of_force_conversion_rates)
    }

    try:
        input_number, input_category = get_user_input()

        if input_number is not None and input_category is not None:
            if input_category in conversion_strategies:
                converter = UnitConverter({input_category: conversion_strategies[input_category]})
                success = converter.convert_unit(input_number, input_category)
                if success:
                    print("Successfully converted! Thank you for using the converter.")
            else:
                print("Invalid conversion category. Please choose a valid category.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


