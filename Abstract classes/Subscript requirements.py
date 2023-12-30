from abc import*


class Alterable(ABC):
    @abstractmethod
    def _getitem_(self, i):
        pass

    class PowerOfTwo(Alterable):
        pass

    def _getitem_(self, i):
        return pow(2, i)
    

    power = PowerOfTwo()
    p8 = power[8]
    #p8 is 256

    p16 = power[16]
    #p16 is 65536

    print(p8)
    print(p16)