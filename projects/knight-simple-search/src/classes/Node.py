class Node():
    def __init__(self, state, father_node):
        self.state = state
        self.father_node = father_node
        if self.father_node == None:
            self.depth = 0
        else:
            self.depth = father_node.depth + 1

    def show_path(self):
        if self.father_node != None:
            return self.father_node.show_path()  + " ; " + self.state.operator 
        else:
            return self.state.operator
    
    def get_all_parents(self, node):
        if node.father_node == None:
            print(node.state)
            return
        self.get_all_parents(node.father_node)
        print(node.state)
    
    def env(self):
        return f"{str(self.state)} | {str(self.father_node.state)}"

    def f(self):
        return 1 #without heuristic
    
    def best_nextState(self, neighbours):
        best = neighbours[0]

        for i in neighbours:
            if i < best:
                best = i

        return best 