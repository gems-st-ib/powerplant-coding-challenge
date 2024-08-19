from app.app.exception.power_plant_challenge_exception import PowerPlantChallengeException


class InvalidPowerPlantTypeException(PowerPlantChallengeException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

