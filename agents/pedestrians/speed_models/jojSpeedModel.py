from .SpeedModel import SpeedModel

class jojSpeedModel(SpeedModel):
    
    def initialize(self):
        self._desiredSpeed = self.internalFactors["desired_speed"] * 3
        self._minSpeed = self.internalFactors["min_crossing_speed"] * 3
        self._maxSpeed = self.internalFactors["max_crossing_speed"] * 3
        self._relaxationTime = self.internalFactors["relaxation_time"]
        pass