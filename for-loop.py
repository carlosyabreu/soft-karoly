
for index in range(5):
    # index works within the loop
#    if index % 2 == 0: 
#        print(f"{index} - iteration count {index + 1}")
    if index == 0: continue
    elif index % 2 == 0:
        print(f"{index} - iteration count {index + 1}")