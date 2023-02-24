vaeee = 0
dade = 1
while dade == 1:
    print(f"Loading: {vaeee}%") 
    vaeee += 1
    if vaeee > float('inf'):
        print(f"Loading ERROR: {vaeee}%") 
        break
