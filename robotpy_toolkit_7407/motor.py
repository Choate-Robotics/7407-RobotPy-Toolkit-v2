class Motor:
    def init(self): ...
    def set_raw_output(self, x: float): ...


class EncoderMotor(Motor):
    def get_sensor_position(self) -> float: ...
    def get_sensor_velocity(self) -> float: ...


class PIDMotor(EncoderMotor):
    def set_target_position(self, pos: float): ...
    def set_target_velocity(self, vel: float): ...
