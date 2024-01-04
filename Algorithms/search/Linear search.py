from datetime import datetime

def linear_search(lst, x):
    n = 0 
    length = len(lst)
    while n < length:
        if lst[n] == x:
            return n
        
        n += 1
        
        
        items = [2,3,5,7,11,13,17]
        print(linear_search(items, 1)) # None
        print(linear_search(items, 7)) # 3
        print(linear_search(items, 19)) # None
        
        print (items)
        
        # *** simplified speed test ***
        
        items = list(range(0, 1000000))
        count = 100
        
        start = datetime.now()
        
        for i in range (1,count):
            linear_search(items, 777777)
            
            delta = datetime.now() - start
            totalMicroseconds = delta.seconds * 1000000 + delta.microseconds
            
            print(totalMicroseconds / count)
            # about 317368.22 microseconds