from  typing import Protocol
from models.exercise import Exercise

class ExerciseRepository(Protocol):

    def add(self, exercise: Exercise) -> None:
        ...

    def get(self, exercise_id: int) -> Exercise:
        ...

    def get_all(self) -> list[Exercise]:
        ...

    def update(self, exercise: Exercise) -> None:
        ...

    def delete(self, exercise_id: int) -> None:
        ...

    def save(self) -> None:
        ...

    def load(self) -> None:
        ...
