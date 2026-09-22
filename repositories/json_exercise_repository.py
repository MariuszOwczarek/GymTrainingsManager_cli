from models.exercise import Exercise, MuscleGroup, Equipment, Difficulty
from repositories.exercise_repository import ExerciseRepository
from pathlib import Path
import json
from exceptions.execrise_exceptions import ExerciseNotFoundError, InvalidExerciseError, ExerciseAlreadyExistsError

class JsonExerciseRepository(ExerciseRepository):

    def __init__(self, path: Path):
        self.file_path = path
        self.exercises: dict[int, Exercise] = {}


    def add(self, exercise: Exercise) -> None:
        if exercise is None:
            raise InvalidExerciseError ("Exercise cannot be None")

        if exercise.exercise_id is None:
            raise InvalidExerciseError("Exercise ID cannot be None")

        if exercise.exercise_id in self.exercises:
            raise ExerciseAlreadyExistsError("Exercise already exists")
        
        self.exercises[exercise.exercise_id] = exercise


    def get(self, exercise_id: int) -> Exercise:
        if exercise_id is None:
            raise InvalidExerciseError("Exercise ID cannot be None")

        if exercise_id not in self.exercises:
            raise ExerciseNotFoundError(f"Exercise with ID {exercise_id} was not found")

        return self.exercises[exercise_id]


    def get_all(self) -> list[Exercise]:
        return list(self.exercises.values())


    def update(self, exercise: Exercise) -> None:
        if exercise is None:
            raise InvalidExerciseError ("Exercise cannot be None")

        if exercise.exercise_id is None:
            raise InvalidExerciseError("Exercise ID cannot be None")

        if exercise.exercise_id not in self.exercises:
            raise ExerciseNotFoundError(f"Exercise with ID {exercise.exercise_id} was not found")

        self.exercises[exercise.exercise_id] = exercise


    def delete(self, exercise_id: int) -> None:
        if exercise_id is None:
            raise InvalidExerciseError("Exercise ID cannot be None")

        if exercise_id not in self.exercises:
            raise ExerciseNotFoundError(f"Exercise with ID {exercise_id} was not found")

        del self.exercises[exercise_id]


    def save(self) -> None:
        exercises = self.get_all()

        data_all = []
        for exercise in exercises:
            data = {
                "exercise_id" : exercise.exercise_id,
                "name": exercise.name,
                "muscle_group": str(exercise.muscle_group.value),
                "equipment": str(exercise.equipment.value),
                "difficulty": str(exercise.difficulty.value)
            }

            data_all.append(data)

        with open(self.file_path, 'w') as file:
            json.dump(data_all, file, indent = 4)

    def load(self) -> None:
        if self.file_path is None:
            raise FileNotFoundError("Exercise data file path is not set")

        with open(self.file_path, 'r') as file:
            data = json.load(file)

        for exercise_data in data:
            exercise = Exercise(
                exercise_data["exercise_id"],
                exercise_data["name"],
                MuscleGroup(exercise_data["muscle_group"]),
                Equipment(exercise_data["equipment"]),
                Difficulty(exercise_data["difficulty"])
            ) 

            self.add(exercise)

