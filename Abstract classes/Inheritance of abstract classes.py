from abc import *

class AVehicle(ABC):
    @property
    @abstractmethod
    def max_speed (self):
        pass

    class ATruck(AVehicle):
        @property
        @abstractmethod
        def capacity(self):
            pass

        class Kamaz5320(ATruck):
            @property
            def max_speed(self):
                return 85
            

            @property
            def capacity(self):
                return 8000
            

            kamaz = Kamaz5320()
            maxSpeed = kamaz.max_speed
            #maxSpeed is 85


            print(maxSpeed)