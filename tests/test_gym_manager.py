from models.exercise import Exercise, MuscleGroup, Equipment, Difficulty
import pytest
import json
from repositories.json_exercise_repository import JsonExerciseRepository
from exceptions.execrise_exceptions import InvalidExerciseError, ExerciseAlreadyExistsError, ExerciseNotFoundError

# =========================================================
# EXERCISE TESTS 
# =========================================================

@pytest.fixture
def exercise_1():
    exercise_1 = Exercise(
            exercise_id=1,
            name="Barbell Bench Press",
            muscle_group=MuscleGroup.CHEST,
            equipment=Equipment.BARBELL,
            difficulty=Difficulty.INTERMEDIATE
        )
    return exercise_1

@pytest.fixture
def exercise_2():
    exercise_2 = Exercise(
            exercise_id=2,
            name="Trying Biceps",
            muscle_group=MuscleGroup.BICEPS,
            equipment=Equipment.DUMBBELL,
            difficulty=Difficulty.BEGINNER
        )
    return exercise_2

def test_create_exercise(exercise_1):
    assert exercise_1.exercise_id == 1
    assert exercise_1.name == "Barbell Bench Press"
    assert exercise_1.muscle_group == MuscleGroup.CHEST
    assert exercise_1.equipment == Equipment.BARBELL
    assert exercise_1.difficulty == Difficulty.INTERMEDIATE


def test_str_exercise(exercise_1):
    assert str(exercise_1) == "Exercise ID: 1, Name: Barbell Bench Press, Muscle Group: Chest, Equipment: Barbell, Difficulty: Intermediate"


def test_exercise_save_to_file(tmp_path, exercise_1):
    file_path = tmp_path / "test.json"
    json_file = JsonExerciseRepository(file_path)
    json_file.add(exercise_1)
    json_file.save()

    assert file_path.exists()

    with open(file_path, 'r') as file:
        data = json.load(file)

    file_dict = {
                    "exercise_id" : exercise_1.exercise_id,
                    "name": exercise_1.name,
                    "muscle_group": str(exercise_1.muscle_group.value),
                    "equipment": str(exercise_1.equipment.value),
                    "difficulty": str(exercise_1.difficulty.value)
                }

    assert data == [file_dict]


def test_two_exercises_save_to_file(tmp_path, exercise_1, exercise_2):
    file_path = tmp_path / "test.json"
    json_file = JsonExerciseRepository(file_path)
    json_file.add(exercise_1)
    json_file.add(exercise_2)
    json_file.save()

    assert file_path.exists()

    with open(file_path, 'r') as file:
        data = json.load(file)

    exercise_1_data= {
                    "exercise_id" : exercise_1.exercise_id,
                    "name": exercise_1.name,
                    "muscle_group": str(exercise_1.muscle_group.value),
                    "equipment": str(exercise_1.equipment.value),
                    "difficulty": str(exercise_1.difficulty.value)
                }
                
    exercise_2_data = {
                    "exercise_id" : exercise_2.exercise_id,
                    "name": exercise_2.name,
                    "muscle_group": str(exercise_2.muscle_group.value),
                    "equipment": str(exercise_2.equipment.value),
                    "difficulty": str(exercise_2.difficulty.value)
                }

    assert data == [exercise_1_data, exercise_2_data]


def test_exercises_load_from_repo(tmp_path, exercise_1):
    file_path = tmp_path / "test.json"
    repo_1 = JsonExerciseRepository(file_path)
    repo_1.add(exercise_1)
    repo_1.save()

    repo_2 = JsonExerciseRepository(file_path)
    repo_2.load()

    loaded_exercise = repo_2.get(1)

    assert loaded_exercise.exercise_id == exercise_1.exercise_id
    assert loaded_exercise.name == exercise_1.name
    assert loaded_exercise.muscle_group == exercise_1.muscle_group
    assert loaded_exercise.equipment == exercise_1.equipment
    assert loaded_exercise.difficulty == exercise_1.difficulty


def test_add_None(tmp_path):
    file_path = tmp_path / "test.json"
    repository = JsonExerciseRepository(file_path)

    with pytest.raises(InvalidExerciseError):
        repository.add(None)


def test_add_exercise_id_is_None(tmp_path, exercise_1):
    file_path = tmp_path / "test.json"
    repository = JsonExerciseRepository(file_path)
    exercise_1.exercise_id = None


    with pytest.raises(InvalidExerciseError):
        repository.add(exercise_1)


def test_add_the_same_exercise_id(tmp_path, exercise_1):
    file_path = tmp_path / "test.json"
    repository = JsonExerciseRepository(file_path)
    repository.add(exercise_1)

    with pytest.raises(ExerciseAlreadyExistsError):
        repository.add(exercise_1)


def test_get_None(tmp_path):
    file_path = tmp_path / "test.json"
    repository = JsonExerciseRepository(file_path)

    with pytest.raises(InvalidExerciseError):
        repository.get(None)


def test_get_id_not_in_repository(tmp_path, exercise_1, exercise_2):
        file_path = tmp_path / "test.json"
        repository = JsonExerciseRepository(file_path)
        repository.add(exercise_1)

        with pytest.raises(ExerciseNotFoundError):
            repository.get(exercise_2.exercise_id)


def test_update_exercise_None(tmp_path):
    file_path = tmp_path / "test.json"
    repository = JsonExerciseRepository(file_path)

    with pytest.raises(InvalidExerciseError):
        repository.update(None)


def test_update_id_not_in_repository(tmp_path, exercise_1, exercise_2):
        file_path = tmp_path / "test.json"
        repository = JsonExerciseRepository(file_path)
        repository.add(exercise_1)

        with pytest.raises(ExerciseNotFoundError):
            repository.update(exercise_2)


def test_delete_exercise_None(tmp_path):
    file_path = tmp_path / "test.json"
    repository = JsonExerciseRepository(file_path)

    with pytest.raises(InvalidExerciseError):
        repository.delete(None)


def test_delete_id_not_in_repository(tmp_path, exercise_1, exercise_2):
        file_path = tmp_path / "test.json"
        repository = JsonExerciseRepository(file_path)
        repository.add(exercise_1)

        with pytest.raises(ExerciseNotFoundError):
            repository.delete(exercise_2.exercise_id)