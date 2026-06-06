from backend.workout import Workout

class WorkoutTracker:

    def __init__(self):
        self.workouts = []

    #Show_Workouts
    def get_workouts(self):
        return self.workouts

    def has_workouts(self):
        return len(self.workouts) > 0

    #Add_Workout
    def add_workout(self, name, reps):
        workout = Workout(name, reps)

        self.workouts.append(workout)
        return True

    #Remove_Workout
    def has_valid_index(self, index):
        if index < 0:
            return False

        if index >= len(self.workouts):
            return False

        return True

    def remove_workout(self, index):
        if not self.has_valid_index(index):
            return False

        self.workouts.pop(index)
        return True

    #Update_Workout
    def update_workout(self, index, reps):
        if not self.has_valid_index(index):
            return False

        self.workouts[index].reps = reps
        return True
