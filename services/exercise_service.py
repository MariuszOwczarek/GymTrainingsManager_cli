from repositories.exercise_repository import ExerciseRepository
from models.exercise import Exercise, Equipment, Difficulty, MuscleGroup, ExerciseStatus


class ExerciseService:

    def __init__(self, repository: ExerciseRepository):
        self.repository = repository

    def add_exercise(self, name, muscle_group: MuscleGroup, equipment: Equipment, difficulty: Difficulty) -> Exercise:
        exercises = self.repository.get_all()
        if not exercises:
            next_id = 1
        else:
            next_id = max([exercise.exercise_id for exercise in exercises]) + 1
            
        exercise = Exercise(exercise_id=next_id,
                        name=name,
                        muscle_group=muscle_group,
                        equipment=equipment,
                        difficulty=difficulty)

        self.repository.add(exercise)

        return exercise

    def get_exercise(self, exercise_id):
        return self.repository.get(exercise_id)

    def get_all_exercises(self):
        return self.repository.get_all()

    def update_exercise(self, exercise):
        self.repository.update(exercise)

    # so far darh deleto - to be changed
    def delete_exercise(self, exercise_id):
        self.repository.delete(exercise_id)

    def get_active_exercises(self):
        return [exercise for exercise in  self.get_all_exercises() if exercise.status == ExerciseStatus.ACTIVE]
