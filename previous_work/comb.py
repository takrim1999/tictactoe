from itertools import permutations as p
lista = ['0','1','2','3','4','5','6','7','8']
for i in p(lista):
    print(" ".join(list(i)))
