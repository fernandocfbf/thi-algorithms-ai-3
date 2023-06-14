from src.classes.Node import Node

class Astar ():

    def sort_function(self, val):
        return val[1]

    def search (self, initialState):
        states = []
        open = []
        new_n = Node(initialState, None)
        open.append((new_n, new_n.f()))
        while (len(open) > 0):
            open.sort(key = self.sort_function, reverse=True)
            n = open.pop()[0]
            if (n.state.is_goal()):
                return n
            for i in n.state.sucessors():
                new_n = Node(i,n)
                if (new_n.state.env() not in states):
                    open.append((new_n,new_n.f()))
                    states.append(new_n.state.env())
        return None