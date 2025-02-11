import math

from unum import Unum

from utils.units import rad


def bounded_angle_diff(theta_from: float, theta_too: float) -> float:
    """
    Finds the bounded (from -π to π) angle difference between two unbounded angles
    """
    res = math.fmod(theta_too - theta_from, 6.283185307179586)
    if res > math.pi:
        res -= 6.283185307179586
    if res < -math.pi:
        res += 6.283185307179586
    return res


def rotate_vector(x: float, y: float, theta: float) -> tuple[float, float]:
    return (
        x * math.cos(theta) - y * math.sin(theta),
        x * math.sin(theta) + y * math.cos(theta)
    )


def clamp(val: float, _min: float, _max: float):
    """
    Clamps a value between a min and max

    Args:
        val (float): value to clamp
        _min (float): min value
        _max (float): max value

    Returns:
        float: clamped value
    """
    if val < _min:
        return _min
    if val > _max:
        return _max
    return val


def ft_to_m(ft: float):
    """
    Converts feet to meters

    Args:
        ft (float): feet (float)

    Returns:
        float: meters (float)
    """
    return ft * 0.3048


def talon_sensor_units_to_inches(sensor_units: float, low_gear: bool) -> float:
    """
    Converts sensor units to inches

    Args:
        sensor_units (float): sensor units as a float
        low_gear (bool): low gear as a bool

    Returns:
        inches as a float
    """
    motor_rotations = sensor_units / 2048.0

    if low_gear:
        wheelbase_rotations = motor_rotations / 15.45  # Low gear
    else:
        wheelbase_rotations = motor_rotations / 8.21  # High gear

    inches = wheelbase_rotations * (6 * math.pi)

    return inches


def talon_sensor_units_to_meters(sensor_units: float, low_gear: bool) -> float:
    """
    Converts sensor units to meters

    Args:
        sensor_units (float):  sensor units as a float
        low_gear (bool): low gear as a bool

    Returns:
        meters as a float
    """
    return talon_sensor_units_to_inches(sensor_units, low_gear) * 0.0254


def meters_to_talon_sensor_units(meters: float, low_gear: bool) -> float:
    """
    Converts meters to sensor units

    Args:
        meters (float): meters as a float
        low_gear (float): low gear as a bool

    Returns:
        sensor units as a float
    """
    return inches_to_talon_sensor_units(meters / 0.0254, low_gear)


def inches_to_talon_sensor_units(inches: float, low_gear: bool) -> float:
    """
    Converts inches to sensor units

    Args:
        inches (float): inches as a float
        low_gear (float): low gear as a bool

    Returns:
        sensor units as a float
    """
    wheelbase_rotations = inches / (6 * math.pi)

    if low_gear:
        motor_rotations = wheelbase_rotations * 15.45  # Low gear
    else:
        motor_rotations = wheelbase_rotations * 8.21  # High gear

    sensor_units = motor_rotations * 2048.0

    return sensor_units
