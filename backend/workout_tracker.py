from backend.workout import Workout

class WorkoutTracker:

    def __init__(self):
        self.workouts = []

    #Add_Workout

    def add_workout(self, name, reps):
        workout = Workout(name, reps)
        self.workouts.append(workout)
        return True

    def get_workouts(self):
        return self.workouts
