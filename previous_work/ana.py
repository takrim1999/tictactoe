with open("work.txt","r") as f:
    array = [i for i in f.read().strip().split("\n")]

# quering present move from all moves
def find_next_step(semi_array,full_array):
    for i in full_array:
        if semi_array == i.split()[:len(semi_array)]:
            element = i
            break
    return element

# sending present move to 
element = find_next_step(['1','2','3'],array)

print(element)
array.remove(element)
element = find_next_step(['1','2','3'],array)
print(element)

with open("work.txt","w") as f:
    for i in array:
        f.write(i+"\n")