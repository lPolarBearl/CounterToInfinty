import time
vaeee = 0
dade = 1
while dade == 1:
    print("Loading: ", vaeee ," %" ) 
    vaeee += 1
    if vaeee > INFINITY:
        print("Loading:", vaeee,"%" ) 
        print("W-wait. Infinty?")
        time.sleep(2)
        print("Is it greater than infinity?")
        time.sleep(2)
        print("Yes.")
        break
