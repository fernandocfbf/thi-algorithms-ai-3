from abc import ABC, abstractmethod
class Node(ABC):

  @abstractmethod
  def __eq__(self, other):
    pass

  @abstractmethod
  def is_the_solution(self):
    pass

  @abstractmethod
  def extend_node(self):
    pass

  @abstractmethod
  def __str__(self):
    pass
