from enum import Enum

class MuscleGroup(Enum):
    CHEST = "Chest"
    BACK = "Back"
    SHOULDERS = "Shoulders"
    BICEPS = "Biceps"
    TRICEPS = "Triceps"
    FOREARMS = "Forearms"
    ABS = "Abs"
    GLUTES = "Glutes"
    QUADRICEPS = "Quadriceps"
    HAMSTRINGS = "Hamstrings"
    CALVES = "Calves"

class Equipment(Enum):
    BARBELL = "Barbell"
    DUMBBELL = "Dumbbell"
    KETTLEBELL = "Kettlebell"
    CABLE = "Cable"
    MACHINE = "Machine"
    BODYWEIGHT = "Bodyweight"
    RESISTANCE_BAND = "Resistance Band"
    EZ_BAR = "EZ Bar"
    SMITH_MACHINE = "Smith Machine"

class Difficulty(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"

class ExerciseStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    ARCHIVED = "Archived"

class Exercise:
    def __init__(self, 
                 exercise_id: int, 
                 name: str, 
                 muscle_group: MuscleGroup, 
                 equipment: Equipment, 
                 difficulty: Difficulty,
                 status: ExerciseStatus = ExerciseStatus.ACTIVE):
        self.exercise_id = exercise_id
        self.name = name
        self.muscle_group = muscle_group
        self.equipment = equipment
        self.difficulty = difficulty
        self.status = status

    def __str__(self):
        return (f"Exercise ID: {self.exercise_id}, Name: {self.name}, "
                f"Muscle Group: {self.muscle_group.value}, "
                f"Equipment: {self.equipment.value}, "
                f"Difficulty: {self.difficulty.value}")
