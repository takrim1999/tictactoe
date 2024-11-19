NumList = [1,2,3,4]
class Node:
    def __init__(self,value,childs):
        self.value = value
        self.childs = childs
    def __str__(self):
        return str((self.value,self.childs))
connection_list = []

for i in NumList:
    a = Node(i,[j for j in NumList if j != i])
    print(a)