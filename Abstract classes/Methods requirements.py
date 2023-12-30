from abc import*

class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    class SportCar(Car):
        def __init__(self):
            self.started = False

        def start_engine(self):
            if self.started:
                return False
            print("start engine")
            self.started = True
            return True

        def stop_engine(self):
            print("stop engine")
            self.started = False

            car = SportCar()
            car.start_engine()    