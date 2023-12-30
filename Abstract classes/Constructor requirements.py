from abc import*

class List(ABC):
    @abstractmethod
    def _init_(self, item_count):
        self.itemCount = item_count

        class SortedList(List):
            def _init_ (self, item_count):
                super(). _init_ (item_count)
                #implementation
                print(item_count)


                lst = SortedList(10)
                print(lst.itemCount)