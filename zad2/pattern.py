print("x y z w")
for x in range(2): #range(2) 0..2-1
    for y in range(2):
        for z in range(2):
            for w in range(2):
                func = ((x and (not(y))) or (x==z) or w)
                if func == 0:
                    print(x,y,z,w)
