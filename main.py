from pathlib import Path
from models.exercise import Exercise, MuscleGroup, Equipment, Difficulty
from repositories.json_exercise_repository import JsonExerciseRepository

exercise_1 = Exercise(
    exercise_id=4,
    name="Barbell Bench Press",
    muscle_group=MuscleGroup.CHEST,
    equipment=Equipment.BARBELL,
    difficulty=Difficulty.INTERMEDIATE
)

exercise_2 = Exercise(
    exercise_id=5,
    name="Trying Biceps",
    muscle_group=MuscleGroup.BICEPS,
    equipment=Equipment.DUMBBELL,
    difficulty=Difficulty.BEGINNER
)

exercise_3 = Exercise(
    exercise_id=6,
    name="Trying Biceps",
    muscle_group=MuscleGroup.BICEPS,
    equipment=Equipment.DUMBBELL,
    difficulty=Difficulty.BEGINNER
)

file_path = Path("test.json")
repository = JsonExerciseRepository(file_path)
repository.load()
repository.add(exercise_1)
repository.add(exercise_2)
repository.add(exercise_3)
repository.save()