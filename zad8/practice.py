from itertools import product
k=0
for i in product ("012345678", repeat=5):
    w = "".join(i)
    if w.count ("3")==1:
        if "53" not in w and "35" not in w and "63" not in w and "36" not in w and "73" not in w and "37" not in w and "83" not in w and "38" not in w:
            k+=1
            print(k,w)
'''
Вычитаем из конца списка начало+1
'''
