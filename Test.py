from json.encoder import INFINITY
vaeee = 0
dade = 1
while dade == 1:
    print(f"Loading: {vaeee}%") 
    vaeee += 1
    if vaeee > INFINITY:
        print("Loading ERROR:", vaeee,"%" ) 
        break
