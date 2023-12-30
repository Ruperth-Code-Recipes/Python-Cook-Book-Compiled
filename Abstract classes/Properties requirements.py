from abc import *


class ACar(ABC):
    @property
    @abstractmethod
    def engine_volume(self):
        pass

    @engine_volume.setter
    @abstractmethod
    def engine_volume(self, val):
        pass

    class Airwave(ACar):
        def __init__(self):
            self._engineVolume = 1500

            @property
            def  engine_volume(self):
                return self._engineVolume
            

            airwave = Airwave()
            print(airwave.engine_volume)
            #printed: 1500