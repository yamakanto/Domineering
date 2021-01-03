from abc import ABC, abstractmethod


class EvaluationFunction(ABC):
    @abstractmethod
    def __call__(self, board):
        pass
