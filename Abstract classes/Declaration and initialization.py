from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self,color):
        pass


    shape = Printable() #<-error