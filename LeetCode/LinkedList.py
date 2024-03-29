class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes[0])
            self.head = node
            for i in range(1,len(nodes)):
                node.next = Node(nodes[i])
                node = node.next

    def __repr__(self): = 
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data);
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    


    

