from src.classes.Node import Node
from collections import deque

class Astart():
    def __init__(self, knight):
        self.knight = knight
    
    def sort_function(self, val):
        return val[1] #get heuristic value

    def is_goal(self, node):
        return node.state == [self.knight.target_x, self.knight.target_y]
    
    def get_night_current_state(self):
        return [self.knight.x, self.knight.y]
    
    def search(self):
        states = list()
        open = deque()
        initial_node = Node(self.get_night_current_state(), None)
        open.append((initial_node, initial_node.f()))
        while len(open) > 0:
            #open.sort(key=self.sort_function, reverse=True) #lowest to highest
            current_node = open.popleft()[0]
            if (self.is_goal(current_node)):
                return current_node
            #simulate knight position
            self.knight.x = current_node.state[0]
            self.knight.y = current_node.state[1]
            for possible_move in self.knight.get_possible_moves():
                new_node = Node(possible_move, current_node)
                if (new_node.env() not in states):
                    open.append((new_node, new_node.f()))
                    states.append(new_node.env())
        print("No solution found")
        return None

