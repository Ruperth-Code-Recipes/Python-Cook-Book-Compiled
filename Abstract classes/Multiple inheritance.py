from abc import *


class PId(ABC):
    @property
    @abstractmethod
    def id(self):
        pass

    class Priced(ABC):
        @property
        @abstractmethod
        def price(self):
            pass

        class Goods(PId, Priced):
            def _init_(self,p_id,p_price):
                self._id = p_id
                self._price = p_price

                @property
                def id(self):
                    return self._id
                
                @property
                def price (self):
                    return self._price
                
                def show_id_and_price(info):
                    print(F"ID = {info.id}, Price = {info.price}")

                    bread = Goods(1,5)
                    show_id_and_price(bread)
                    #printed: id = 1,price = 5
