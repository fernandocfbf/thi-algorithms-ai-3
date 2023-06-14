class DFS():
    def __init__(self, start):
        self.start_state = start
        self.frontier = [self.start_state]
        self.checked_nodes = []
        self.number_of_steps = 0
    
    def insert_to_frontier(self, node):
        self.frontier.insert(0, node)
    
    def remove_from_frontier(self):
        first_node = self.frontier.pop(0)
        self.checked_nodes.append(first_node)
        return first_node

    def frontier_is_empty(self):
        return len(self.frontier) == 0

    def search(self):
        while True:
            self.number_of_steps += 1
            if self.frontier_is_empty():
                print(f"No solution found after {self.number_of_steps} steps.")
                break
            selected_node = self.remove_from_frontier()
            if selected_node.is_solution():
                print(f"Solution found in {self.number_of_steps} steps")
                print(selected_node.to_string())
                break
            new_nodes = selected_node.extend_node()
            if len(new_nodes) > 0:
                for new_node in new_nodes:
                    if new_node not in self.frontier and new_node not in self.checked_nodes:
                        self.insert_to_frontier(new_node)