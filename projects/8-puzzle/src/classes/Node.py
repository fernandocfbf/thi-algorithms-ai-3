class Node:
    def __init__(self,state,father_node):
        self.state = state
        self.father_node = father_node
        if self.father_node == None:
            self.depth = 0
            self.g = 0
        else:
            self.depth = father_node.depth + 1
            self.g = 1 + self.father_node.g

    def show_path(self):
        if self.father_node != None:
            return self.father_node.show_path()  + " -> " + self.state.last_moviment 
        else:
            return self.state.last_moviment
    
    def h(self):
        return self.state.h()

    def f(self):
        #f(n) = g(n) + h(n)
        return self.g + self.h()
    
    def best_nextState(self, neighbours):
        best = neighbours[0]

        for i in neighbours:
            if i < best:
                best = i

        return best